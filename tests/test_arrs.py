from utils import arrs


def test_get():
    assert arrs.get([], -2, "test") == "test"
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([12], 0, "test") == 12
    assert arrs.get([], 0) == None


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
