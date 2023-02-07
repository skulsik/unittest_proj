from utils import arrs


def test_get_1():
    assert arrs.get([1, 2, 3], -2) == None


def test_get_2():
    assert arrs.get([1, 2, 3], 1, "test") == 2


def test_get_3():
    assert arrs.get([], 0, "test") == "test"


def test_slice_1():
    assert arrs.my_slice([]) == []


def test_slice_2():
    assert arrs.my_slice([1, 2, 3], 1, 2) == [2]


def test_slice_3():
    assert arrs.my_slice([1, 2, 3, 4, 5], -6, 3) == [1, 2, 3]



def test_slice_4():
    assert arrs.my_slice([1, 2, 3], -1) == [3]


def test_slice_5():
    assert arrs.my_slice([1, 2, 3], -1, -5) == []
