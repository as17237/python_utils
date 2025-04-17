import pandas as pd
from sqlalchemy import create_engine, text
from difflib import SequenceMatcher
from collections import defaultdict
import argparse
from typing import List, Dict, Tuple

def get_db_connection(connection_string: str):
    """Create a database connection using SQLAlchemy."""
    return create_engine(connection_string)

def get_lists_for_attribute(engine, attribute_id: int) -> pd.DataFrame:
    """Get all active lists for a given attribute_id."""
    query = text("""
        SELECT l.list_id, l.version_id, l.attribute_id, l.name, l.status
        FROM list l
        WHERE l.attribute_id = :attribute_id AND l.status = 'A'
    """)
    return pd.read_sql(query, engine, params={'attribute_id': attribute_id})

def get_list_members(engine, list_ids: List[int]) -> pd.DataFrame:
    """Get all members for the given list_ids."""
    query = text("""
        SELECT list_id, version_id, value
        FROM list_member
        WHERE list_id IN :list_ids
    """)
    return pd.read_sql(query, engine, params={'list_ids': tuple(list_ids)})

def calculate_similarity(list1: List[str], list2: List[str]) -> float:
    """Calculate similarity between two lists using SequenceMatcher."""
    # Convert lists to strings for comparison
    str1 = ' '.join(sorted(list1))
    str2 = ' '.join(sorted(list2))
    return SequenceMatcher(None, str1, str2).ratio()

def find_duplicate_lists(lists_df: pd.DataFrame, members_df: pd.DataFrame) -> List[Tuple[int, int]]:
    """Find lists that have exactly the same members."""
    # Group members by list_id
    list_members = defaultdict(set)
    for _, row in members_df.iterrows():
        list_members[row['list_id']].add(row['value'])
    
    # Find duplicates
    duplicates = []
    processed = set()
    
    for list_id1, members1 in list_members.items():
        if list_id1 in processed:
            continue
            
        for list_id2, members2 in list_members.items():
            if list_id1 != list_id2 and list_id2 not in processed:
                if members1 == members2:
                    duplicates.append((list_id1, list_id2))
                    processed.add(list_id2)
        
        processed.add(list_id1)
    
    return duplicates

def find_similar_lists(lists_df: pd.DataFrame, members_df: pd.DataFrame, threshold: float = 0.8) -> List[Tuple[int, int, float]]:
    """Find lists that are similar based on their members."""
    # Group members by list_id
    list_members = defaultdict(list)
    for _, row in members_df.iterrows():
        list_members[row['list_id']].append(row['value'])
    
    # Find similar lists
    similar_lists = []
    processed = set()
    
    for list_id1, members1 in list_members.items():
        if list_id1 in processed:
            continue
            
        for list_id2, members2 in list_members.items():
            if list_id1 != list_id2 and list_id2 not in processed:
                similarity = calculate_similarity(members1, members2)
                if similarity >= threshold:
                    similar_lists.append((list_id1, list_id2, similarity))
        
        processed.add(list_id1)
    
    return similar_lists

def main():
    parser = argparse.ArgumentParser(description='Analyze lists for duplicates and similarities')
    parser.add_argument('--connection-string', required=True, help='SQL Server connection string')
    parser.add_argument('--attribute-id', type=int, required=True, help='Attribute ID to analyze')
    parser.add_argument('--similarity-threshold', type=float, default=0.8, 
                       help='Similarity threshold (0-1) for considering lists similar')
    
    args = parser.parse_args()
    
    # Create database connection
    engine = get_db_connection(args.connection_string)
    
    # Get lists for the attribute
    lists_df = get_lists_for_attribute(engine, args.attribute_id)
    
    if lists_df.empty:
        print(f"No active lists found for attribute_id {args.attribute_id}")
        return
    
    # Get list members
    list_ids = lists_df['list_id'].tolist()
    members_df = get_list_members(engine, list_ids)
    
    # Find duplicates
    duplicates = find_duplicate_lists(lists_df, members_df)
    print("\nDuplicate Lists:")
    for list_id1, list_id2 in duplicates:
        list1_name = lists_df[lists_df['list_id'] == list_id1]['name'].iloc[0]
        list2_name = lists_df[lists_df['list_id'] == list_id2]['name'].iloc[0]
        print(f"List {list_id1} ('{list1_name}') is identical to List {list_id2} ('{list2_name}')")
    
    # Find similar lists
    similar_lists = find_similar_lists(lists_df, members_df, args.similarity_threshold)
    print("\nSimilar Lists:")
    for list_id1, list_id2, similarity in similar_lists:
        list1_name = lists_df[lists_df['list_id'] == list_id1]['name'].iloc[0]
        list2_name = lists_df[lists_df['list_id'] == list_id2]['name'].iloc[0]
        print(f"List {list_id1} ('{list1_name}') is {similarity:.2%} similar to List {list_id2} ('{list2_name}')")

if __name__ == "__main__":
    main() 