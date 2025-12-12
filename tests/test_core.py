"""
Test fore the core module of the `conway` module.

The following unittests will check still lifes and oscillators
as given in the wikipedia article about [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns).
"""

import numpy as np
import pytest
from conway.core import GameOfLife
from tests.conftest import check_all_shifts


def test_exception_on_wrong_dimensions():
    with pytest.raises(ValueError) as info:
        start = np.zeros((5))
        GameOfLife(start)
    print(f"\nException message: \n{info.value}")

    with pytest.raises(ValueError) as info:
        start = np.zeros((5, 6, 7))
        GameOfLife(start)
    print(f"\nException message: \n{info.value}")


def test_exception_on_wrong_values():
    with pytest.raises(ValueError) as info:
        start = np.array([[0, 1], [1, 2]])
        GameOfLife(start)
    print(f"\nException message: \n{info.value}")

    with pytest.raises(ValueError) as info:
        start = np.array([[0, 1], [1, -1]])
        GameOfLife(start)
    print(f"\nException message: \n{info.value}")

    with pytest.raises(ValueError) as info:
        start = np.array([[0, 1], [1, 0.25]])
        GameOfLife(start)
    print(f"\nException message: \n{info.value}")


@pytest.mark.parametrize(
    "start",
    [
        # block
        np.array(
            [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
            ]
        ),
        # beehive
        np.array(
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ]
        ),
        # loaf
        np.array(
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ]
        ),
        # boat
        np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        ),
        # tub
        np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        ),
    ],
)  # type: ignore
def test_still_life(start: np.ndarray) -> None:
    check_all_shifts(start, start.copy(), 1)


@pytest.mark.parametrize(
    "period,start",
    [
        # blinker
        (
            2,
            np.array(
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                ]
            ),
        ),
        # toad
        (
            2,
            np.array(
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                ]
            ),
        ),
        # beacon
        (
            2,
            np.array(
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                ]
            ),
        ),
    ],
)  # type: ignore
def test_oscillator(period: int, start: np.ndarray) -> None:
    check_all_shifts(start, start.copy(), period)
