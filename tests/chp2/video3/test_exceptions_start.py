from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest

def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():  # TO DO
    # with pytest.raises(Exception) as exp:
    #     Point("Buenes Aires", 12.11, -555.34)
    #     #raise(Exception)
    # breakpoint()
    with pytest.raises(ValueError) as exp:
        Point("Buenes Aires", 12.11, -555.34)
    assert str(exp.value) == "Invalid latitude or longitude"

def test_invalid_city_name():
    with pytest.raises(TypeError) as exp:
        Point(123, 12.11, 12.11)
        raise(Exception)
    assert str(exp.value) == "Invalid type for city name, must be string"
    #breakpoint()