from src.drift import mean_shift
def test_flags_shift():
    assert mean_shift([0, 0.1, -0.1], [2, 2.1, 1.9])["drift"] is True
    assert mean_shift([0, 0.1], [0.05, 0.0], threshold=0.5)["drift"] is False
