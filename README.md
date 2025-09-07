# DAB Test Project

A comprehensive monorepo demonstrating Databricks Asset Bundle (DAB) patterns, featuring shared utilities, configuration management, and CI/CD best practices for Databricks environments. This project showcases enterprise-grade development workflows for data applications.

## 🏗️ Repository Structure

```
dab_test/
├── common_framework/           # Shared utility framework
│   ├── config/                 # Configuration files
│   │   ├── bar.yml            # YAML configuration
│   │   └── data.json          # JSON data
│   ├── src/zoo/               # Utility modules
│   ├── tests/                 # Framework tests
│   ├── pytest.ini            # Pytest configuration
│   └── README.md              # Framework documentation
├── dab_demo/                  # Main DAB demonstration project
│   ├── src/                   # Application source code
│   │   ├── foo/               # Example modules
│   │   ├── helpers/           # PySpark utility functions
│   │   ├── path_manager.py    # Path management utility
│   │   ├── session_manager.py # Spark session management
│   │   └── *.ipynb           # Demonstration notebooks
│   ├── tests/                 # Application tests
│   │   ├── helpers/           # Helper function tests
│   │   ├── conftest.py        # Pytest configuration
│   │   └── test_*.py         # Test modules
│   ├── resources/             # DAB resources
│   ├── scratch/               # Development workspace
│   ├── fixtures/              # Test fixtures
│   ├── databricks.yml        # DAB configuration
│   ├── requirements-dev.txt   # Development dependencies
│   └── README.md              # Project documentation
├── LICENSE                    # Project license
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🚀 Project Overview

### **Common Framework**
A shared library providing:
- **Configuration Management**: YAML/JSON configuration handling with validation
- **Utility Functions**: Reusable mathematical and data processing utilities
- **Data Pipelines**: Delta Live Tables integration for data processing
- **Testing Infrastructure**: Comprehensive pytest-based testing framework

### **DAB Demo**
A production-ready Databricks Asset Bundle showcasing:
- **Path Management**: Singleton-based path resolution across environments
- **Session Management**: Optimized Spark session configuration with logging control
- **PySpark Utilities**: Helper functions for DataFrame operations and column manipulation
- **Testing Framework**: Comprehensive testing with chispa integration and pytest fixtures
- **Smart Configuration**: Environment-aware setup for notebooks and modules
- **CI/CD Patterns**: Multi-environment deployment with Bundle configuration

## 🎯 Key Features

### **Monorepo Architecture**
- **Shared Dependencies**: Common framework used across multiple projects
- **Synchronized Deployment**: Bundle configuration deploys both projects together
- **Cross-Project Integration**: Seamless module sharing and path resolution

### **Environment Management**
- **Multi-Environment Support**: Development and production configurations
- **Path Resolution**: Intelligent handling of local vs. Bundle environments
- **Configuration Validation**: Automated testing of configuration integrity

### **Testing Excellence**
- **Comprehensive Coverage**: Unit tests for all modules and configurations
- **PySpark Testing**: Advanced DataFrame testing with chispa library
- **Pytest Integration**: Custom fixtures and configuration for Spark testing
- **Helper Function Testing**: Validation of column operations and DataFrame utilities
- **Databricks Integration**: Native testing within Databricks notebooks
- **CI/CD Ready**: Automated testing in deployment pipelines

### **Developer Experience**
- **Smart Path Setup**: Automatic `sys.path` configuration for notebooks
- **Error Resilience**: Robust error handling and fallback strategies
- **Documentation**: Comprehensive guides in both English and Korean

## 🚀 Quick Start

### **Prerequisites**
```bash
# Install Databricks CLI
pip install databricks-cli

# Authenticate to workspace
databricks configure
```

### **Local Development**
```bash
# Clone and setup
git clone <repository-url>
cd dab_test

# Install dependencies
pip install -r dab_demo/requirements-dev.txt

# Run tests
cd common_framework && pytest
cd ../dab_demo && pytest
```

### **Databricks Deployment**
```bash
# Deploy to development
cd dab_demo
databricks bundle deploy --target dev

# Run jobs
databricks bundle run dab_demo_job --target dev

# Deploy to production
databricks bundle deploy --target prod
```

## 🧪 Testing Strategy

### **Local Testing**
```bash
# Test common framework
cd common_framework
pytest tests/ -v

# Test main application
cd dab_demo
pytest tests/ -v --cov=src
```

### **Databricks Testing**
- Use `dab_demo/tests/pytest_runner.ipynb` for in-platform testing
- Automated test execution within Databricks environment
- Integration testing with actual Databricks resources

## 📋 Configuration Management

### **Common Framework Config**
- `common_framework/config/bar.yml`: Structured YAML configuration
- `common_framework/config/data.json`: JSON data arrays
- Automated validation through pytest

### **DAB Configuration**
- `dab_demo/databricks.yml`: Multi-environment Bundle configuration
- Resource definitions and job orchestration
- Monorepo synchronization settings

## 🛠️ Development Workflow

### **1. Local Development**
- Write and test code locally using pytest
- Use PathResolver for consistent file access
- Validate configurations before deployment

### **2. Bundle Deployment**
- Deploy to development environment for integration testing
- Run comprehensive test suites in Databricks
- Validate job execution and resource access

### **3. Production Release**
- Deploy to production after thorough validation
- Monitor job execution and performance
- Maintain configuration integrity

## 📚 Project Components

### **Common Framework Components**
- **Zoo Utilities** (`src/zoo/`): Mathematical and data processing functions
- **Configuration System**: YAML/JSON handling with validation
- **DLT Pipeline**: Delta Live Tables integration
- **Test Suite**: Comprehensive validation framework

### **DAB Demo Components**
- **Path Manager**: Singleton pattern for environment-aware path resolution
- **Configuration Reader**: YAML configuration integration with common framework
- **Notebook Utilities**: Smart path setup and module import helpers
- **Job Definitions**: Databricks Workflows and resource management

## 🔧 Advanced Features

### **Cross-Project Integration**
```python
# In dab_demo, access common_framework resources
from path_manager import PathResolver
from foo.bar import parse_bar

paths = PathResolver()
config_data = parse_bar()  # Reads from common_framework/config/bar.yml
```

### **Environment Detection**
```python
# Smart environment handling
%run ./set_notebook_paths  # In Databricks notebooks

# Automatic path configuration based on environment
# - Local development
# - Databricks Bundle
# - User workspace
```

### **Robust Error Handling**
- File encoding detection and handling
- Bundle vs. source path resolution
- Graceful fallback strategies

## 📖 Documentation

- **[Common Framework](./common_framework/README.md)**: Detailed framework documentation
- **[DAB Demo](./dab_demo/README.md)**: Complete project guide
- **[Databricks Asset Bundles](https://docs.databricks.com/dev-tools/bundles/index.html)**: Official DAB documentation

## 🤝 Contributing

1. **Fork the repository** and create a feature branch
2. **Develop locally** with comprehensive testing
3. **Test in both projects** (common_framework and dab_demo)
4. **Validate Bundle deployment** in development environment
5. **Submit pull request** with clear documentation

## 🔍 Common Issues & Solutions

### **Import Errors**
```python
# Solution: Use notebook path setup
%run ./set_notebook_paths
```

### **Bundle Path Issues**
- Prefer original source paths over `.bundle` paths
- Use PathResolver for consistent path handling

### **Configuration Problems**
- Validate YAML/JSON syntax with pytest
- Check file permissions and encoding

### **Deployment Failures**
```bash
# Validate configuration
databricks bundle validate

# Check authentication
databricks auth profiles
```

## 📊 Project Metrics

- **2 Main Projects**: common_framework + dab_demo
- **Comprehensive Testing**: 100% configuration validation coverage
- **Multi-Environment**: Development and production ready
- **Cross-Platform**: Local development + Databricks deployment
- **Documentation**: English + Korean language support

## 🎯 Use Cases

### **Data Engineering Teams**
- Shared utility libraries across multiple projects
- Standardized configuration management
- Consistent deployment patterns

### **MLOps Workflows**
- Model training and deployment pipelines
- Environment-specific configuration handling
- Automated testing and validation

### **Enterprise Development**
- Multi-project monorepo management
- CI/CD pipeline integration
- Cross-team collaboration patterns

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🏷️ Tags

`databricks` `asset-bundles` `python` `pytest` `monorepo` `ci-cd` `data-engineering` `mlops` `configuration-management` `path-resolution`
