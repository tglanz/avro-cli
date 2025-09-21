# Avro CLI

A command-line tool for interacting with Apache Avro files.

## Features

- **inspect**: Display schema, metadata, and record count of Avro files
- **head**: Show the first N records from Avro files
- **diff**: Diff the schema or the data between to given avro files

## Installation

```bash
pip install -e .
```

## Usage

Use `--help` to see available commands and options:

```bash
avro-cli --help
avro-cli inspect --help
avro-cli head --help
```

## Development

### Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black .
```
