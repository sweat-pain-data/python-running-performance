import pytest

# Predictions were done with https://tools.runnerspace.com/gprofile.php?do=title&title_id=801&mgroup_id=45577
# causing some subtle differences. Trying to get the diff below 0.5% in the tests.

PERFORMANCES = [
    {
        'distance': 5000,
        'time': 24 * 60 + 14,
        'purdy': 229.24,
        'VO2Max': 39.75,
        'purdy_times': (
            (5000, 24 * 60 + 14),
            (10000, 51 * 60 + 18),
            (21100, 1 * 60**2 + 55 * 60 + 7),
        ),
        'VO2Max_times': (
            (5000, 24 * 60 + 14),
            (10000, 50 * 60 + 17),
            (21100, 1 * 60**2 + 51 * 60 + 30),
        ),
        'cameron_times': (
            (5000, 24 * 60 + 14),
            (10000, 50 * 60 + 29),
            (21100, 1 * 60**2 + 51 * 60 + 18),
        ),
        'riegel_times': (
            (5000, 24 * 60 + 14),
            (10000, 50 * 60 + 32),
            (21100, 1 * 60**2 + 51 * 60 + 29),
        ),
    },
    {
        'distance': 10000,
        'time': 52 * 60 + 22,
        'purdy': 209.81,
        'VO2Max': 37.90,
        'purdy_times': (
            (5000, 24 * 60 + 43),
            (10000, 52 * 60 + 18),
            (21100, 1 * 60**2 + 57 * 60 + 34),
        ),
        'VO2Max_times': (
            (5000, 25 * 60 + 14),
            (10000, 52 * 60 + 22),
            (21100, 1 * 60**2 + 56 * 60 + 7),
        ),
        'cameron_times': (
            (5000, 25 * 60 + 8),
            (10000, 52 * 60 + 22),
            (21100, 1 * 60**2 + 55 * 60 + 27),
        ),
        'riegel_times': (
            (5000, 25 * 60 + 7),
            (10000, 52 * 60 + 22),
            (21100, 1 * 60**2 + 55 * 60 + 33),
        ),
    },
    {
        'distance': 21100,
        'time': 2 * 60**2 + 38,
        'purdy': 186.79,
        'VO2Max': 36.24,
        'purdy_times': (
            (5000, 25 * 60 + 20),
            (10000, 53 * 60 + 41),
            (21100, 2 * 60**2 + 37),
        ),
        'VO2Max_times': (
            (5000, 26 * 60 + 12),
            (10000, 54 * 60 + 24),
            (21100, 2 * 60**2 + 37),
        ),
        'cameron_times': (
            (5000, 26 * 60 + 15),
            (10000, 54 * 60 + 42),
            (21100, 2 * 60**2 + 37),
        ),
        'riegel_times': (
            (5000, 26 * 60 + 13),
            (10000, 54 * 60 + 40),
            (21100, 2 * 60**2 + 37),
        ),
    },
    {
        'distance': 2010,
        'time': 9 * 60 + 49,
        'purdy': 123.06,
        'VO2Max': 36.64,
        'purdy_times': (
            (5000, 27 * 60 + 11),
            (10000, 57 * 60 + 43),
            (21100, 2 * 60**2 + 9 * 60 + 55),
        ),
        'VO2Max_times': (
            (5000, 25 * 60 + 57),
            (10000, 53 * 60 + 54),
            (21100, 1 * 60**2 + 59 * 60 + 30),
        ),
        'cameron_times': (
            (5000, 26 * 60 + 22),
            (10000, 54 * 60 + 55),
            (21100, 2 * 60**2 + 1 * 60 + 5),
        ),
        'riegel_times': (
            (5000, 25 * 60 + 48),
            (10000, 53 * 60 + 47),
            (21100, 1 * 60**2 + 58 * 60 + 39),
        ),
    },
]


@pytest.fixture(params=PERFORMANCES)
def performance(request):
    yield request.param


def _flatten_times(key):
    times = []
    for performance in PERFORMANCES:
        for time in performance['{}_times'.format(key)]:
            times.append({
                'distance': performance['distance'],
                'time': performance['time'],
                'predicted_distance': time[0],
                'predicted_time': time[1],
            })
    return times


@pytest.fixture(params=_flatten_times('purdy'))
def purdy_time(request):
    yield request.param


@pytest.fixture(params=_flatten_times('VO2Max'))
def VO2Max_time(request):
    yield request.param


@pytest.fixture(params=_flatten_times('cameron'))
def cameron_time(request):
    yield request.param


@pytest.fixture(params=_flatten_times('riegel'))
def riegel_time(request):
    yield request.param
