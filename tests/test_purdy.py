import math
import pytest
from running_performance import DistanceOutOfBoundsError, purdy, purdy_prediction
from running_performance.purdy import PORTUGESE_TABLE, _fraction_on_turns


@pytest.mark.parametrize('distance,fraction', (
    (109, 0),
    (449, 0.44543429844098),
    (149, 0.6644295302013423),
    (249, 0.40160642570281124),
    (349, 0.5702005730659025),
    (399, 0.5012531328320802),
))
def test_fraction_on_turns(distance, fraction):
    assert _fraction_on_turns(distance) == fraction


def test_purdy_points(performance):
    assert purdy(performance['distance'], performance['time']) == performance['purdy']


def test_purdy_points_low_distance():
    low_distance, low_velocity = PORTUGESE_TABLE[0]
    low_time = low_distance / low_velocity

    assert purdy(low_distance, low_time) == 1631.93


def test_purdy_points_distance_too_short():
    low_distance, _ = PORTUGESE_TABLE[0]
    with pytest.raises(DistanceOutOfBoundsError):
        purdy(low_distance - 1, 60)


def test_purdy_points_high_distance():
    high_distance, high_velocity = PORTUGESE_TABLE[-1]
    high_time = high_distance / high_velocity

    assert purdy(high_distance, high_time) == 950.05


def test_purdy_points_distance_too_long():
    high_distance, _ = PORTUGESE_TABLE[-1]
    with pytest.raises(DistanceOutOfBoundsError):
        purdy(high_distance + 1, 60)


def test_purdy_time(purdy_time):
    prediction = purdy_prediction(purdy_time['distance'], purdy_time['time'], purdy_time['predicted_distance'])
    difference = prediction - purdy_time['predicted_time']
    assert math.fabs(difference) / purdy_time['predicted_time'] < 0.005
