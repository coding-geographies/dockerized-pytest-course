import pytest

from scripts.chp2.video7 import data_processor_end as data_processor


@pytest.fixture(scope="function")
def city_list_location_malformed():
    return 'tests/resources/cities/malformed_map.csv'


def test_csv_reader_malformed_data_contents(city_list_location_malformed):
    """
    Sad Path Test
    """
    with pytest.raises(ValueError) as exp:
        data_processor.csv_reader(city_list_location_malformed)
    assert str(exp.value) == "Invalid input: could not convert string to float: 'not_an_altitude'"
