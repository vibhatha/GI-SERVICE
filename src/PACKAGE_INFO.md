# OpenData Python Package

## Package Structure

The `opendata` Python package is located in the `src/` directory with the following structure:

```
GI-SERVICE/
├── LICENSE                   # License file
├── Procfile                  # Deployment config
├── chartFactory/             # Chart utilities
├── venv/                     # Virtual environment
│
└── src/                      # 🎯 ALL PROJECT FILES HERE
    ├── main.py               # FastAPI application entry point
    ├── README.md             # Project README
    ├── requirements.txt      # Project dependencies
    ├── test.py               # Test script
    ├── pyproject.toml        # Package configuration (PEP 621)
    ├── setup.py              # Setup script for backward compatibility
    ├── MANIFEST.in           # Package manifest
    ├── test_package.py       # Package test script
    ├── PACKAGE_INFO.md       # This file
    │
    └── opendata/             # Main Python package
        ├── __init__.py       # Package exports
        ├── py.typed          # Type hints marker
        ├── models/           # Pydantic models
        ├── services/         # Business logic
        ├── routers/          # FastAPI routers
        └── dependencies/     # Dependency injection
```

## Installation

### From Source (Development Mode)

```bash
cd src
pip install -e .
```

### With Development Dependencies

```bash
cd src
pip install -e ".[dev]"
```

### With Test Dependencies

```bash
cd src
pip install -e ".[test]"
```

## Building the Package

```bash
cd src
pip install build
python -m build
```

This creates:
- `dist/opendata-0.1.0.tar.gz` (source distribution)
- `dist/opendata-0.1.0-py3-none-any.whl` (wheel distribution)

## Testing the Package

```bash
cd src
python test_package.py
```

## Usage

After installation, import the package:

```python
from opendata import (
    IncomingServiceAttributes,
    IncomingServiceOrgchart,
    WriteAttributes,
    ENTITY_PAYLOAD,
    ATTRIBUTE_PAYLOAD,
    WRITE_PAYLOAD,
)
```

## Running the FastAPI Application

From the `src/` directory:

```bash
cd src
uvicorn main:app --reload
```

The application imports the package using:
```python
from opendata.routers import payload_incoming_router
```

## Installing Dependencies

```bash
cd src
pip install -r requirements.txt
```

## Notes

- The `src/` directory contains **everything**: application code, package source, and build configuration
- The root directory only contains deployment files (LICENSE, Procfile) and utilities (chartFactory)
- The package name is `opendata` and can be installed and imported system-wide
- Package version: 0.1.0
- All development and deployment should be done from the `src/` directory

## Quick Start

```bash
# 1. Navigate to src directory
cd src

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install the package in development mode
pip install -e .

# 4. Run the FastAPI application
uvicorn main:app --reload

# 5. Test the package
python test_package.py
```

