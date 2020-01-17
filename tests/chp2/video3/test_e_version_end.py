import pytest

from scripts.chp2.video3.mapmaker_exceptions_end import Point


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Senegal", 99.6937, -189.44406)
    # breakpoint()

    assert str(exp.value) == "Invalid latitude, longitude combination."
