import os
from pathlib import Path
from pyspark.dbutils import DBUtils
from pyspark.sql import SparkSession


class PathResolver:
    _instance = None

    def __new__(cls):
        """
        Singleton pattern implementation for PathResolver class
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._root = Path(__file__).parent.parent
        return cls._instance

    @property
    def resources(self):
        """
        Define properties to resolve paths for resources, config, and tests directories
        """

        return self._root / "resources"

    @property
    def tests(self):
        """
        Property to resolve the path for the tests directory
        """
        return self._root / "tests"

    @property
    def common_framework(self):
        """
        Property to resolve the path for the common_framework directory
        """
        return self._root.parent / "common_framework"
