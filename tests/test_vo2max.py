from running_performance import VO2Max


def test_VO2Max(performance):
    assert VO2Max(performance['distance'], performance['time']) == performance['VO2Max']
