from session_manager import get_spark


def test_get_spark():
    spark = get_spark()
    df = spark.read.table("samples.nyctaxi.trips")
    assert df.count() > 5
