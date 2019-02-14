from .exceptions import DistanceOutOfBoundsError
from .purdy import purdy, purdy_prediction
from .vo2max import VO2Max, VO2Max_prediction

name = 'running_performance'
VERSION = '0.1.0'

__all__ = [
    DistanceOutOfBoundsError,
    name,
    purdy_prediction,
    purdy,
    VERSION,
    VO2Max_prediction,
    VO2Max,
]
