# List Analysis Utility

A Python utility to analyze and identify duplicate and similar lists in SQL Server databases.

## Features

- Identifies duplicate lists (lists with exactly the same members)
- Identifies similar lists using a robust similarity algorithm
- Works with SQL Server databases
- Configurable similarity threshold
- Command-line interface for easy use

## Requirements

- Python 3.6+
- SQL Server database
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/python_utils.git
cd python_utils
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with your database connection string and attribute_id:

```bash
python list_analyzer.py --connection-string "mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server" --attribute-id 123
```

### Arguments

- `--connection-string`: SQL Server connection string (required)
- `--attribute-id`: The attribute_id to analyze (required)
- `--similarity-threshold`: Optional threshold for considering lists similar (default: 0.8)

## Database Schema

The utility works with the following tables:

### list
- list_id: int
- version_id: int
- attribute_id: int
- name: varchar
- status: char

### list_member
- list_id: int
- version_id: int
- value: varchar

## License

MIT License 