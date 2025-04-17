from sqlalchemy import create_engine
from typing import Optional

class DatabaseConnection:
    """A utility class for managing database connections."""
    
    def __init__(self, connection_string: str):
        """Initialize the database connection.
        
        Args:
            connection_string: The SQLAlchemy connection string
        """
        self.connection_string = connection_string
        self._engine = None
    
    @property
    def engine(self):
        """Get the SQLAlchemy engine, creating it if necessary."""
        if self._engine is None:
            self._engine = create_engine(self.connection_string)
        return self._engine
    
    def execute_query(self, query: str, params: Optional[dict] = None):
        """Execute a SQL query and return the results.
        
        Args:
            query: The SQL query to execute
            params: Optional parameters for the query
            
        Returns:
            The query results
        """
        with self.engine.connect() as connection:
            result = connection.execute(query, params or {})
            return result.fetchall()
    
    def close(self):
        """Close the database connection."""
        if self._engine is not None:
            self._engine.dispose()
            self._engine = None 