from scripts.chp2.video4.mapmaker_challenge import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp1:
        Point("Senegal", 99.6937, -189.44406)
    assert str(exp1.value) == "Invalid latitude, longitude combination."

    """
    Your solution here! You will need to edit the following source code
    file to get your test running:

        File path:
        scripts/chp2/video4/mapmaker_challenge import

    It has already been imported for you on the first line of this file
    """
    with pytest.raises(Exception) as exp2:
        Point(20, 49.6937, 89.44406)
    assert str(exp2.value) == "name should be a string"
