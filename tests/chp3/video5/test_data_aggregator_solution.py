from io import StringIO
import os
import pytest

from scripts import data_processor, data_aggregator


@pytest.fixture(scope="module")
def city_list_location():
    return 'tests/resources/cities/'


@pytest.fixture(scope="module")
def process_data(city_list_location):
    files = os.listdir(city_list_location)

    def _specify_type(file_name_or_type):
        for f in files:
            if file_name_or_type in f:
                if file_name_or_type != '.json':
                    data = data_processor.csv_reader(city_list_location + f)
                else:
                    data = data_processor.json_reader(city_list_location + f)
        return data

    yield _specify_type


@pytest.mark.parametrize("country,stat,expected", [
    ('Andorra', 'Mean', 1641.42),
    ('Andorra', 'Median', 1538.02),
    ('Argentina', 'Median', 125.0),
    ])
def test_csv_writer(process_data, country, stat, expected):
    data = process_data(file_name_or_type="clean_map.csv")
    result = data_aggregator.atitude_stat_per_country(data, country, stat)
    output_location = StringIO()
    data_aggregator.csv_writer(result, output_location)

    res = output_location.getvalue().strip('\r\n')
    assert res == f'Country,{stat}\r\n{country},{expected}'
