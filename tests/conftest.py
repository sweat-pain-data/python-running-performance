import pytest


PERFORMANCES = [
    {
        'distance': 5000,
        'time': 24 * 60 + 14,
        'purdy': 229.24,
        'VO2Max': 39.75,
    },
    {
        'distance': 10000,
        'time': 52 * 60 + 22,
        'purdy': 209.81,
        'VO2Max': 37.90,
    },
    {
        'distance': 21100,
        'time': 2 * 60**2 + 38,
        'purdy': 186.79,
        'VO2Max': 36.24,
    },
    {
        'distance': 2010,
        'time': 9 * 60 + 49,
        'purdy': 123.06,
        'VO2Max': 36.64,
    },
]


@pytest.fixture(params=PERFORMANCES)
def performance(request):
    yield request.param
