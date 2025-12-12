import argparse
from time import sleep
import numpy as np
from conway import GameOfLife
from conway import run_with_raylib


def main(
    size: tuple[int, int],
    use_raylib: bool = False,
    max_iterations: int | None = None,
    sleep_ms: int | None = None,
) -> None:
    start = np.random.random(size)
    start = np.array(start > 0.5, dtype=np.uint8)
    game = GameOfLife(start)
    if use_raylib:
        run_with_raylib(game, max_iterations=max_iterations, sleep_ms=sleep_ms)
    else:
        print("0")
        print(game)
        iter = 1
        while game.step():
            if sleep_ms:
                sleep(0.001 * sleep_ms)

            print(f"{iter}")
            print(game)

            if max_iterations and iter == max_iterations:
                return
            iter += 1

        print(f"{iter}")
        print(game)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument(
        "-g",
        "--grid",
        nargs=2,
        type=int,
        default=[64, 64],
        metavar=("w", "h"),
        help="size of the game grid",
    )
    parser.add_argument(
        "-rl",
        "--raylib",
        action="store_true",
        help="display the GoL using Raylib in a window",
    )
    parser.add_argument(
        "-i",
        "--max-iter",
        type=int,
        default=None,
        metavar="n",
        help="maximum number of simulation steps",
    )
    parser.add_argument(
        "-s",
        "--sleep-ms",
        type=int,
        default=None,
        metavar="n",
        help="number of milliseconds pause between iterations",
    )
    args = parser.parse_args()
    print(f"Arguments passed : {args}")
    main(
        size=(args.grid[1], args.grid[0]),
        use_raylib=args.raylib,
        max_iterations=args.max_iter,
        sleep_ms=args.sleep_ms,
    )
