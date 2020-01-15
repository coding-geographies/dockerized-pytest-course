from scripts.chp2.video5.mapmaker_solution import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Senegal", 99.6937, -189.44406)
    assert str(exp.value) == "Invalid latitude, longitude combination."

    with pytest.raises(ValueError) as exp:
        Point(5, 12.11386, -55.08269)
    assert str(exp.value) == 'City name provided must be a string'
