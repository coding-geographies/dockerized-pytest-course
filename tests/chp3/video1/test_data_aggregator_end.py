import pytest
from scripts import data_processor, map_population_update


@pytest.fixture(scope="module")
def map_data_location():
    return 'tests/resources/cities/clean_map.csv'


@pytest.fixture(scope="function")
def prep_transform_data(map_data_location):
    population_dict = {
            'Andorra': 77142,
            'Argentina': 44780677,
            'Cape Verde': 546388,
            'Germany': 83670653,
            'Greece': 10473455,
            'India': 1366417754,
            'Japan': 128860301,
            'Morocco': 36471769,
            'Senegal': 16296364,
            'United States': 329064917
    }
    data = data_processor.csv_reader(map_data_location)
    data_to_transform = map_population_update.MapData(data, False)
    yield data_to_transform, population_dict


def test_data_population_update(prep_transform_data):
    """
    Happy Path test
    """

    data_to_transform, population_dict = prep_transform_data
    data_to_transform.add_population(population_dict)   # transform object in place

    for row in data_to_transform.get_data():
        assert 'Population' in row
        assert 'Updated' in row


def test_data_population_no_update(prep_transform_data):
    """
    Sad Path test: We don't want the data transformed twice

    We've kept the `prep_transform_data`'s scope one a per
    function basis so that the preceding happy path test
    is not coupled to this test.
    """

    data_to_transform, population_dict = prep_transform_data
    data_to_transform.add_population(population_dict)   # transform object in place

    # Try calling the function again
    with pytest.raises(Exception) as e:
        data_to_transform.add_population(population_dict)
    assert str(e.value) == 'You cannot transform the data twice'
