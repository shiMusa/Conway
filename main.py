import argparse
import numpy as np
from conway import GameOfLife
from conway import run_with_raylib


def main(use_raylib: bool = False) -> None:
    N = 128 * 2
    start = np.random.random((N, N))
    start = np.array(start > 0.5, dtype=np.uint8)
    game = GameOfLife(start)
    if use_raylib:
        run_with_raylib(game)
    else:
        print(game)
        iter = 0
        while game.step():
            iter += 1
            print(f"{iter}" + 40 * "-")
            print(game)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument(
        "-rl",
        "--raylib",
        action="store_true",
        help="Display the GoL using Raylib in a window.",
    )
    args = parser.parse_args()
    print(f"args : {args}")
    print(f"raylib {args.raylib}")
    main(use_raylib=args.raylib)
