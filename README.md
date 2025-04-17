# Python Utilities

A collection of useful Python utilities for various tasks.

## Project Structure

```
python_utils/
├── list_analyzer/         # List analysis and comparison utilities
├── database_utils/        # Database related utilities
├── file_utils/           # File and directory operations
├── text_utils/           # Text processing and analysis
├── cli_utils/            # Command-line interface utilities
└── tests/                # Test files for all utilities
```

## Available Utilities

### List Analyzer
- Identifies duplicate and similar lists in SQL Server databases
- Configurable similarity threshold
- Command-line interface

### Database Utilities
- SQL Server connection management
- Query execution helpers
- Data export/import tools

### File Utilities
- File system operations
- File format conversion
- Directory management

### Text Utilities
- Text processing
- String manipulation
- Pattern matching

### CLI Utilities
- Command-line interface helpers
- Argument parsing
- Output formatting

## Installation

1. Clone the repository:
```bash
git clone https://github.com/as17237/python_utils.git
cd python_utils
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Each utility module can be used independently. Refer to the specific module's documentation for usage instructions.

### List Analyzer Example
```bash
python -m python_utils.list_analyzer.main --connection-string "mssql+pyodbc://..." --attribute-id 123
```

## Contributing

1. Fork the repository
2. Create a new branch for your utility
3. Add your utility in the appropriate module
4. Add tests
5. Submit a pull request

## License

MIT License 