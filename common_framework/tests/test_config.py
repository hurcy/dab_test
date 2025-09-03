import os
import json
import yaml
import pytest
from pathlib import Path


# Module-level fixtures that can be used by all test classes
@pytest.fixture
def config_dir():
    """Fixture to get the config directory path"""
    return Path(__file__).parent.parent / "config"


@pytest.fixture
def bar_yml_path(config_dir):
    """Fixture to get bar.yml file path"""
    return config_dir / "bar.yml"


@pytest.fixture
def data_json_path(config_dir):
    """Fixture to get data.json file path"""
    return config_dir / "data.json"


class TestBarYml:
    """Tests for bar.yml configuration file"""
    
    def test_bar_yml_file_exists(self, bar_yml_path):
        """Test that bar.yml file exists"""
        assert bar_yml_path.exists(), f"bar.yml file not found at {bar_yml_path}"
    
    def test_bar_yml_is_valid_yaml(self, bar_yml_path):
        """Test that bar.yml contains valid YAML syntax"""
        with open(bar_yml_path, 'r') as file:
            try:
                yaml.safe_load(file)
            except yaml.YAMLError as e:
                pytest.fail(f"bar.yml contains invalid YAML syntax: {e}")
    
    def test_bar_yml_structure(self, bar_yml_path):
        """Test that bar.yml has expected structure"""
        with open(bar_yml_path, 'r') as file:
            config = yaml.safe_load(file)
        
        # Test that config is a dictionary
        assert isinstance(config, dict), "bar.yml should contain a dictionary at root level"
        
        # Test that bar_test key exists
        assert 'bar_test' in config, "bar.yml should contain 'bar_test' key"
        
        # Test that bar_test is a dictionary
        assert isinstance(config['bar_test'], dict), "'bar_test' should be a dictionary"
    
    def test_bar_yml_content(self, bar_yml_path):
        """Test specific content expectations in bar.yml"""
        with open(bar_yml_path, 'r') as file:
            config = yaml.safe_load(file)
        
        # Test that foo_test key exists under bar_test
        assert 'foo_test' in config['bar_test'], "'foo_test' key should exist under 'bar_test'"
        
        # Test that foo_test has expected value
        assert config['bar_test']['foo_test'] == "zoo", "'foo_test' should have value 'zoo'"
    
    def test_bar_yml_file_not_empty(self, bar_yml_path):
        """Test that bar.yml file is not empty"""
        assert bar_yml_path.stat().st_size > 0, "bar.yml file should not be empty"


class TestDataJson:
    """Tests for data.json configuration file"""
    
    def test_data_json_file_exists(self, data_json_path):
        """Test that data.json file exists"""
        assert data_json_path.exists(), f"data.json file not found at {data_json_path}"
    
    def test_data_json_is_valid_json(self, data_json_path):
        """Test that data.json contains valid JSON syntax"""
        with open(data_json_path, 'r') as file:
            try:
                json.load(file)
            except json.JSONDecodeError as e:
                pytest.fail(f"data.json contains invalid JSON syntax: {e}")
    
    def test_data_json_structure(self, data_json_path):
        """Test that data.json has expected structure"""
        with open(data_json_path, 'r') as file:
            data = json.load(file)
        
        # Test that data is a list
        assert isinstance(data, list), "data.json should contain a list at root level"
    
    def test_data_json_content(self, data_json_path):
        """Test specific content expectations in data.json"""
        with open(data_json_path, 'r') as file:
            data = json.load(file)
        
        expected_content = ["Lorem", "Ipsum", "Dolor", "Sit", "Amet"]
        assert data == expected_content, f"data.json should contain {expected_content}"
    
    def test_data_json_list_length(self, data_json_path):
        """Test that data.json list has expected length"""
        with open(data_json_path, 'r') as file:
            data = json.load(file)
        
        assert len(data) == 5, "data.json should contain exactly 5 elements"
    
    def test_data_json_all_strings(self, data_json_path):
        """Test that all elements in data.json are strings"""
        with open(data_json_path, 'r') as file:
            data = json.load(file)
        
        for item in data:
            assert isinstance(item, str), f"All items in data.json should be strings, but found {type(item)}: {item}"
    
    def test_data_json_file_not_empty(self, data_json_path):
        """Test that data.json file is not empty"""
        assert data_json_path.stat().st_size > 0, "data.json file should not be empty"


class TestConfigFilesIntegration:
    """Integration tests for both configuration files"""
    
    def test_both_config_files_exist(self, config_dir):
        """Test that both configuration files exist"""
        bar_yml = config_dir / "bar.yml"
        data_json = config_dir / "data.json"
        
        assert bar_yml.exists(), "bar.yml file should exist"
        assert data_json.exists(), "data.json file should exist"
    
    def test_config_directory_readable(self, config_dir):
        """Test that config directory is readable"""
        assert config_dir.exists(), "Config directory should exist"
        assert config_dir.is_dir(), "Config path should be a directory"
        assert os.access(config_dir, os.R_OK), "Config directory should be readable"
