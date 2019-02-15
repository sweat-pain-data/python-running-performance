from .cameron import cameron_prediction
from .exceptions import DistanceOutOfBoundsError
from .purdy import purdy, purdy_prediction
from .riegel import riegel_prediction
from .vo2max import VO2Max, VO2Max_prediction

name = 'running_performance'

__all__ = [
    cameron_prediction,
    DistanceOutOfBoundsError,
    name,
    purdy_prediction,
    purdy,
    riegel_prediction,
    VO2Max_prediction,
    VO2Max,
]
