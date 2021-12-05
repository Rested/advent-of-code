from day_1 import number_of_increases, sliding_window

def test_gets_number_of_increases():
    assert number_of_increases([
        1,
        2,
        3
    ]) == 2

    assert number_of_increases([
        1,
        2,
        2,
        1,
        2
    ]) == 2


def test_sliding_window_increases():
    assert sliding_window([1,2,3,4]) == 1
    assert sliding_window([1,2,3,4,5]) == 2
    assert sliding_window([1,2,3,4,4]) == 2
    assert sliding_window([1,2,3,4,2]) == 1