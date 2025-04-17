from unittest.mock import patch
from python_utils.cli_utils.formatter import CLIFormatter

def test_cli_formatter_initialization():
    """Test CLI formatter initialization."""
    formatter = CLIFormatter()
    assert formatter.console is not None

@patch('rich.console.Console.print')
def test_print_table(mock_print):
    """Test printing a table."""
    formatter = CLIFormatter()
    headers = ["ID", "Name"]
    rows = [[1, "Test1"], [2, "Test2"]]
    
    formatter.print_table(headers, rows, "Test Table")
    
    # Verify that print was called
    assert mock_print.called
    
    # Get the table that was printed
    table = mock_print.call_args[0][0]
    assert table.title == "Test Table"
    assert len(table.columns) == 2
    assert table.columns[0].header == "ID"
    assert table.columns[1].header == "Name"

@patch('rich.console.Console.print')
def test_print_panel(mock_print):
    """Test printing a panel."""
    formatter = CLIFormatter()
    content = "Test content"
    title = "Test Panel"
    
    formatter.print_panel(content, title)
    
    # Verify that print was called
    assert mock_print.called
    
    # Get the panel that was printed
    panel = mock_print.call_args[0][0]
    assert panel.title == title
    assert panel.renderable == content

@patch('rich.console.Console.print')
def test_print_error(mock_print):
    """Test printing an error message."""
    formatter = CLIFormatter()
    message = "Test error"
    
    formatter.print_error(message)
    
    # Verify that print was called with the correct format
    assert mock_print.called
    assert "[red]Error:[/red] Test error" in mock_print.call_args[0][0]

@patch('rich.console.Console.print')
def test_print_success(mock_print):
    """Test printing a success message."""
    formatter = CLIFormatter()
    message = "Test success"
    
    formatter.print_success(message)
    
    # Verify that print was called with the correct format
    assert mock_print.called
    assert "[green]Success:[/green] Test success" in mock_print.call_args[0][0] 