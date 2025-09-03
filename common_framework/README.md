# Common Framework

A shared framework library containing utilities, configurations, and data processing pipelines for the DAB (Databricks Asset Bundles) test project.

## 📁 Project Structure

```
common_framework/
├── config/                 # Configuration files
│   ├── bar.yml            # YAML configuration with bar_test settings
│   └── data.json          # JSON data file with Lorem Ipsum content
├── src/                   # Source code
│   └── zoo/               # Zoo utility module
│       ├── __init__.py    # Python package initialization
│       └── util.py        # Utility functions (math operations)
├── tests/                 # Test suite
│   ├── test_config.py     # Configuration file validation tests
│   └── zoo/               # Zoo module tests
│       └── test_util.py   # Unit tests for utility functions
├── dlt_pipeline.ipynb     # Delta Live Tables pipeline notebook
├── pytest.ini            # Pytest configuration
└── README.md              # This file
```

## 🚀 Features

### Configuration Management
- **YAML Configuration**: `config/bar.yml` contains structured configuration data
- **JSON Data**: `config/data.json` stores array data for processing
- **Validation**: Comprehensive pytest suite validates configuration integrity

### Utility Library
- **Math Operations**: Basic arithmetic functions in `src/zoo/util.py`
- **Extensible Design**: Modular structure for adding new utilities
- **Type Safety**: Clean function interfaces with proper testing

### Data Pipeline
- **Delta Live Tables**: `dlt_pipeline.ipynb` provides DLT pipeline definitions
- **Databricks Integration**: Compatible with Databricks Asset Bundles (DAB)
- **Spark Processing**: Uses PySpark for data transformations

## 🧪 Testing

The framework includes comprehensive test coverage:

### Configuration Tests (`tests/test_config.py`)
- **File Existence**: Validates that configuration files exist
- **Format Validation**: Ensures YAML and JSON syntax correctness
- **Content Validation**: Verifies expected data structures and values
- **Integration Tests**: Cross-file validation and directory accessibility

### Utility Tests (`tests/zoo/test_util.py`)
- **Function Testing**: Unit tests for utility functions
- **Edge Cases**: Comprehensive test coverage for all scenarios

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_config.py

# Run with verbose output
pytest -v

# Run specific test class
pytest tests/test_config.py::TestBarYml
```

## 📋 Configuration Files

### `config/bar.yml`
Contains hierarchical configuration data:
```yaml
bar_test:
  foo_test: "zoo"
```

### `config/data.json`
Contains array data for processing:
```json
["Lorem", "Ipsum", "Dolor", "Sit", "Amet"]
```

## 🔧 Development Setup

### Prerequisites
- Python 3.7+
- pytest for testing
- PyYAML for YAML processing
- Databricks environment (for DLT pipeline)

### Installation
```bash
# Install dependencies
pip install pytest pyyaml

# Run tests to verify setup
pytest
```

### Project Configuration
The `pytest.ini` file configures:
- Test discovery paths: `tests/`
- Python path: `src/` (for importing modules)

## 📊 Usage Examples

### Using Utility Functions
```python
from zoo.util import add

result = add(5, 3)  # Returns 8
```

### Loading Configuration
```python
import yaml
import json
from pathlib import Path

# Load YAML config
with open('config/bar.yml', 'r') as f:
    config = yaml.safe_load(f)
    print(config['bar_test']['foo_test'])  # "zoo"

# Load JSON data
with open('config/data.json', 'r') as f:
    data = json.load(f)
    print(data)  # ["Lorem", "Ipsum", "Dolor", "Sit", "Amet"]
```

## 🏗️ Architecture

The common_framework follows a modular architecture:

1. **Configuration Layer**: Centralized config management in `config/`
2. **Utility Layer**: Reusable functions in `src/zoo/`
3. **Pipeline Layer**: Data processing in `dlt_pipeline.ipynb`
4. **Test Layer**: Comprehensive validation in `tests/`


## 📝 Notes

- This framework is part of a larger DAB (Databricks Asset Bundles) test project
- The Delta Live Tables pipeline integrates with Databricks workflows
- Configuration files are validated automatically via pytest
- All utilities should include corresponding unit tests
