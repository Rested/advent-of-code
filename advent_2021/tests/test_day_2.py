
from typing import List

from day_2 import navigate_aim_course, navigate_course


def test_navigate_course():
    assert navigate_course([
        "forward 2",
        "down 5",
        "up 2"
    ]) == (2, 3)


def test_navigate_aim_course():
    assert navigate_aim_course([
        "forward 2",
        "down 5",
        "up 2"
    ]) == (2, 0)

    assert navigate_aim_course([
        "forward 2",
        "down 5",
        "up 2",
        "forward 1"
    ]) == (3, 3)

    assert navigate_aim_course([
        "forward 2",
        "down 5",
        "up 2",
        "forward 2"
    ]) == (4, 6)