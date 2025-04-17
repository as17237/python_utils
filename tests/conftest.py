import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@pytest.fixture
def test_engine():
    """Create a test SQLite in-memory database engine."""
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    return engine

@pytest.fixture
def test_session(test_engine):
    """Create a test database session."""
    Session = sessionmaker(bind=test_engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture
def cli_formatter():
    """Create a CLI formatter instance."""
    from python_utils.cli_utils.formatter import CLIFormatter
    return CLIFormatter() 