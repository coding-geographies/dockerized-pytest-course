import os
import pytest

from scripts import data_processor


@pytest.fixture(scope="module")
def process_data(city_list_location):
    """
    This fixture serves as a factory fixture
    Instead of directly returning a  reader for the file we'd
    like to access for a test, it will return a function that
    takes arguments.

    Those arguments will determine what the fixture ultimately
    provides to the test functions that reference it.
    """
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
