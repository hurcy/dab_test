# dab_demo

A comprehensive Databricks Asset Bundle (DAB) project demonstrating CI/CD patterns, Python module management, and testing strategies for Databricks environments. This project showcases best practices for developing, testing, and deploying data applications in Databricks.

> 📖 **한국어 문서**: [README-KR.md](./README-KR.md)

## 🏗️ Project Structure

```
dab_demo/
├── src/                         # Source code
│   ├── foo/                     # Example module package
│   │   ├── __init__.py          # Package initialization
│   │   └── bar.py               # YAML config reader utility
│   ├── path_manager.py          # Path management utility (Singleton)
│   ├── demo.ipynb               # Demonstration notebook
│   └── set_notebook_paths.ipynb # Path configuration helper
├── resources/                   # Resource files
│   └── dab_demo.job.yml         # Databricks Job definition
├── tests/                       # Test suite
│   ├── foo/                     # Module tests
│   │   └── test_read_resource.py # Resource reading tests
│   ├── test_path_manager.py     # Path manager tests
│   └── pytest_runner.ipynb     # Databricks pytest runner
├── scratch/                     # Development workspace
│   ├── exploration.ipynb        # Data exploration notebook
│   └── README.md                # Scratch area documentation
├── fixtures/                    # Test fixtures directory
├── databricks.yml              # DAB configuration
├── setup.py                    # Python package setup
├── pytest.ini                  # pytest configuration
├── requirements-dev.txt         # Development dependencies
└── README.md                    # This file
```

## 🚀 Key Features

### 1. **Path Management System (PathResolver)**
- **Singleton Pattern**: Ensures consistent path resolution across the application
- **Cross-Environment Support**: Works in both local development and Databricks Bundle environments
- **Multiple Path Types**: Provides access to `resources`, `tests`, and `common_framework` directories

```python
from path_manager import PathResolver

paths = PathResolver()
print(paths.resources)       # Project resources directory
print(paths.tests)          # Test files directory  
print(paths.common_framework) # Shared common_framework directory
```

### 2. **Smart Notebook Path Configuration**
- **`set_notebook_paths.ipynb`**: Automatically detects and configures `sys.path` for module imports
- **Bundle-Aware**: Intelligently handles both Bundle and non-Bundle environments
- **Error-Resilient**: Includes fallback strategies for path resolution

### 3. **Configuration Management**
- **YAML Config Reading**: Safe and robust configuration file handling
- **PathResolver Integration**: Uses centralized path management for file access
- **Error Handling**: Graceful handling of missing or corrupted config files

```python
from foo.bar import parse_bar

# Reads configuration from common_framework/config/bar.yml
config_data = parse_bar()
print(config_data)  # {'bar_test': {'foo_test': 'zoo'}}
```

### 4. **Comprehensive Testing Framework**
- **pytest Integration**: Full pytest support with custom configuration
- **Databricks-Native Testing**: `pytest_runner.ipynb` for running tests in Databricks
- **Path Manager Tests**: Validates path resolution across environments
- **Resource Tests**: Ensures configuration files are accessible and valid

### 5. **Monorepo Support**
- **Multi-Project Structure**: Supports both `dab_demo` and `common_framework` projects
- **Shared Dependencies**: Seamless integration between related projects
- **Synchronized Deployment**: Bundle configuration includes both projects

## 🚀 Getting Started

### 1. **Prerequisites**

Install required tools:
```bash
# Install Databricks CLI
pip install databricks-cli

# Install development dependencies
pip install -r requirements-dev.txt
```

Authenticate to your Databricks workspace:
```bash
databricks configure
```

To enable serverless compute in your IDE, use the DEFAULT configuration profile, which is selected by the DatabricksSession.builder when no parameters are specified:

1. Create a configuration profile named DEFAULT using the instructions from step 1.
2. Use a text editor to open the .databrickscfg file, which is found in:
  - Your $HOME user home folder on Unix, Linux, or macOS: ~/.databrickscfg, or
  - Your %USERPROFILE% (your user home) folder on Windows. For example, for macOS:

```
nano ~/.databrickscfg
```

3. Add serverless_compute_id = auto to the DEFAULT profile:

```
[DEFAULT]
host                  = https://my-workspace.cloud.databricks.com
auth_type             = databricks-cli
serverless_compute_id = auto
```

4. Save the changes and exit your editor.


### 2. **Local Development**

Clone and set up the project:
```bash
# Navigate to project directory
cd dab_demo

# Install in development mode
pip install -e .

# Run local tests
pytest
```

### 3. **Databricks Bundle Deployment**

Deploy to development environment:
```bash
# Deploy both dab_demo and common_framework
databricks bundle deploy --target dev
```

Deploy to production environment:
```bash
databricks bundle deploy --target prod
```

### 4. **Running Jobs**

Execute the deployed job:
```bash
# Run the main job
databricks bundle run dab_demo_job --target dev
```

### 5. **Notebook Development**

In Databricks notebooks, use the path configuration helper:
```python
# In any notebook, run this first:
%run ./set_notebook_paths

# Now you can import project modules:
from foo.bar import parse_bar
from path_manager import PathResolver
```

## 🧪 Testing Strategy

### **Local Testing**
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test modules
pytest tests/test_path_manager.py
pytest tests/foo/test_read_resource.py

# Run tests with coverage
pytest --cov=src tests/
```

### **Databricks Testing**
Use the provided `pytest_runner.ipynb` notebook:
1. Open `tests/pytest_runner.ipynb` in Databricks
2. Run all cells to execute the full test suite
3. View test results and coverage reports

### **Test Structure**
- **Path Manager Tests** (`test_path_manager.py`): 
  - Validates PathResolver singleton behavior
  - Tests path resolution in different environments
  - Ensures proper directory access

- **Resource Tests** (`test_read_resource.py`):
  - Validates YAML configuration file reading
  - Tests error handling for missing files
  - Ensures proper integration with PathResolver

### **Test Configuration**
The `pytest.ini` file configures:
```ini
[pytest]
testpaths = tests        # Test discovery path
pythonpath = src         # Add src to Python path
```

## 🛠️ Development Tools & Best Practices

### **Recommended IDE Setup**
- **Databricks Extension for VS Code**: Full integration with Databricks workspace
- **Python Language Server**: Enhanced code completion and error detection
- **pytest Integration**: Run tests directly from IDE

### **Development Workflow**
1. **Local Development**: Write and test code locally using pytest
2. **Bundle Validation**: Use `databricks bundle validate` before deployment
3. **Incremental Deployment**: Deploy to dev environment for integration testing
4. **Production Release**: Deploy to prod environment after validation

### **Code Organization**
- **Modular Design**: Separate concerns into focused modules
- **Path Management**: Use PathResolver for all file system operations
- **Configuration Management**: Centralize config in YAML files
- **Error Handling**: Implement robust error handling and logging

## 🔄 CI/CD & Deployment

### **Bundle Configuration Features**
```yaml
# databricks.yml highlights
bundle:
  name: dab_demo

# Monorepo support - deploys both projects
sync:
  paths:
    - ../common_framework
    - ./src

# Multi-environment targets
targets:
  dev:    # Development environment
  prod:   # Production environment
```

### **Deployment Strategy**
- **Environment Separation**: Clear dev/prod environment boundaries
- **Shared Resources**: Common framework deployed alongside main project
- **Job Orchestration**: Databricks Workflows for complex data pipelines
- **Resource Management**: Bundle manages compute clusters, jobs, and permissions

### **Monitoring & Observability**
- **Job Monitoring**: Built-in Databricks job monitoring and alerting
- **Error Tracking**: Comprehensive error logging and notification
- **Performance Metrics**: Job execution time and resource utilization tracking

## 📚 Additional Resources

### **Documentation**
- [Databricks Asset Bundles Documentation](https://docs.databricks.com/dev-tools/bundles/index.html)
- [Databricks Connect Guide](https://docs.databricks.com/dev-tools/databricks-connect.html)
- [Python Testing in Databricks](https://docs.databricks.com/notebooks/testing.html)

### **Project Dependencies**
- **Core**: `setuptools`, `wheel`
- **Testing**: `pytest`, `databricks-dlt`
- **Development**: `databricks-connect` (optional)
- **Configuration**: `PyYAML` (included in Databricks Runtime)

### **Common Issues & Solutions**
- **Import Errors**: Use `set_notebook_paths.ipynb` for proper path configuration
- **Bundle Path Issues**: Prefer original source paths over `.bundle` paths
- **File Encoding**: Handle encoding issues with explicit UTF-8 specification
- **Permission Errors**: Ensure proper workspace permissions for Bundle deployment

