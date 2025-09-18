from __future__ import annotations

import pytest

from chispa.formatting import FormattingConfig
from pyspark.sql import SparkSession


@pytest.fixture()
def my_formats():
    return FormattingConfig(
        mismatched_rows={"color": "light_yellow"},
        matched_rows={"color": "cyan", "style": "bold"},
        mismatched_cells={"color": "purple"},
        matched_cells={"color": "blue"},
    )


@pytest.fixture()
def my_chispa():
    return FormattingConfig(
        mismatched_rows={"color": "light_yellow"},
        matched_rows={"color": "cyan", "style": "bold"},
        mismatched_cells={"color": "purple"},
        matched_cells={"color": "blue"},
    )

@pytest.fixture()
def spark() -> SparkSession:
    # Create a new Databricks Connect session. If this fails,
    # check that you have configured Databricks Connect correctly.
    # See https://docs.databricks.com/dev-tools/databricks-connect.html.
    try:
        from databricks.connect import DatabricksSession

        return DatabricksSession.builder.getOrCreate()
    except ImportError:
        return SparkSession.builder.getOrCreate()
