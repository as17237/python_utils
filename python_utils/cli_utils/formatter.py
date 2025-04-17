from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from typing import List, Any

class CLIFormatter:
    """A utility class for formatting CLI output."""
    
    def __init__(self):
        """Initialize the CLI formatter."""
        self.console = Console()
    
    def print_table(self, headers: List[str], rows: List[List[Any]], title: str = None):
        """Print data in a table format.
        
        Args:
            headers: List of column headers
            rows: List of rows, where each row is a list of values
            title: Optional table title
        """
        table = Table(title=title)
        
        for header in headers:
            table.add_column(header)
        
        for row in rows:
            table.add_row(*[str(item) for item in row])
        
        self.console.print(table)
    
    def print_panel(self, content: str, title: str = None):
        """Print content in a panel.
        
        Args:
            content: The content to display
            title: Optional panel title
        """
        panel = Panel(content, title=title)
        self.console.print(panel)
    
    def print_error(self, message: str):
        """Print an error message.
        
        Args:
            message: The error message to display
        """
        self.console.print(f"[red]Error:[/red] {message}")
    
    def print_success(self, message: str):
        """Print a success message.
        
        Args:
            message: The success message to display
        """
        self.console.print(f"[green]Success:[/green] {message}") 