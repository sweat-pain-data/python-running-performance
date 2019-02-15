import math
from running_performance import cameron_prediction


def test_cameron_time(cameron_time):
    prediction = cameron_prediction(cameron_time['distance'], cameron_time['time'], cameron_time['predicted_distance'])
    difference = prediction - cameron_time['predicted_time']
    assert math.fabs(difference) / cameron_time['predicted_time'] < 0.005
