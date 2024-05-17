import pytest

from scripts.chp2.video7 import data_processor_end as data_processor


def test_csv_reader_malformed_data_contents():
    """
    Sad Path Test
    """
    city_list_location_malformed = "tests/resources/cities/malformed_map.csv"
    with pytest.raises(ValueError) as exp:
        data_processor.csv_reader(city_list_location_malformed)
    assert str(exp.value) == "Invalid input: could not convert string to float: 'not_an_altitude'"
