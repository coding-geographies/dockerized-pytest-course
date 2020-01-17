import pytest
from scripts import data_processor


@pytest.fixture(scope="module")
def city_list_location():
    return 'tests/resources/cities/clean_map.csv'


@pytest.fixture(scope="module")
def process_data(city_list_location):
    yield data_processor.csv_reader(city_list_location)


@pytest.fixture(scope="function")
def city_list_location_malformed():
    return 'tests/resources/cities/malformed_map.csv'


def test_csv_reader_header_fields(process_data):
    """
    Happy Path test to make sure the processed data
    contains the right header fields
    """
    data = process_data
    header_fields = list(data[0].keys())
    assert header_fields == [
            'Country',
            'City',
            'State_Or_Province',
            'Lat',
            'Long',
            'Altitude'
            ]


def test_csv_reader_data_contents(process_data):
    """
    Happy Path Test to examine that each row
    had the appropriate data type per field
    """
    data = process_data

    # Check row types
    for row in data:
        assert(isinstance(row['Country'], str))
        assert(isinstance(row['City'], str))
        assert(isinstance(row['State_Or_Province'], str))
        assert(isinstance(row['Lat'], float))
        assert(isinstance(row['Long'], float))
        assert(isinstance(row['Altitude'], float))

    # Basic data checks
    assert len(data) == 180  # We have collected 180 rows
    assert data[0]['Country'] == 'Andorra'
    assert data[106]['Country'] == 'Japan'


def test_csv_reader_malformed_data_contents(city_list_location_malformed):
    """
    Sad Path Test
    """
    with pytest.raises(ValueError) as exp:
        data_processor.csv_reader(city_list_location_malformed)
    assert str(exp.value) == "could not convert string to float: 'not_an_altitude'"
