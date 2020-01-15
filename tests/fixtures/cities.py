import pytest


@pytest.fixture(scope="module")
def city_list_location():
    return 'tests/resources/cities/'
