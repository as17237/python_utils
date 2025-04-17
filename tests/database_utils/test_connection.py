import pytest
from python_utils.database_utils.connection import DatabaseConnection

def test_database_connection_initialization():
    """Test database connection initialization."""
    conn = DatabaseConnection("sqlite:///:memory:")
    assert conn.connection_string == "sqlite:///:memory:"
    assert conn._engine is None

def test_engine_creation():
    """Test that engine is created on first access."""
    conn = DatabaseConnection("sqlite:///:memory:")
    engine = conn.engine
    assert engine is not None
    assert str(engine.url) == "sqlite:///:memory:"

def test_engine_reuse():
    """Test that engine is reused on subsequent accesses."""
    conn = DatabaseConnection("sqlite:///:memory:")
    engine1 = conn.engine
    engine2 = conn.engine
    assert engine1 is engine2

def test_execute_query(test_engine):
    """Test query execution."""
    # Create a test table
    test_engine.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
    
    # Insert some test data
    test_engine.execute("""
        INSERT INTO test (id, name) VALUES
        (1, 'test1'),
        (2, 'test2')
    """)
    
    conn = DatabaseConnection("sqlite:///:memory:")
    conn._engine = test_engine  # Use our test engine
    
    # Execute a query
    results = conn.execute_query("SELECT * FROM test")
    assert len(results) == 2
    assert results[0] == (1, 'test1')
    assert results[1] == (2, 'test2')

def test_execute_query_with_params(test_engine):
    """Test query execution with parameters."""
    # Create a test table
    test_engine.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
    
    # Insert some test data
    test_engine.execute("""
        INSERT INTO test (id, name) VALUES
        (1, 'test1'),
        (2, 'test2')
    """)
    
    conn = DatabaseConnection("sqlite:///:memory:")
    conn._engine = test_engine  # Use our test engine
    
    # Execute a query with parameters
    results = conn.execute_query(
        "SELECT * FROM test WHERE name = :name",
        {"name": "test1"}
    )
    assert len(results) == 1
    assert results[0] == (1, 'test1')

def test_close_connection():
    """Test closing the database connection."""
    conn = DatabaseConnection("sqlite:///:memory:")
    conn.engine  # Create the engine
    assert conn._engine is not None
    
    conn.close()
    assert conn._engine is None 