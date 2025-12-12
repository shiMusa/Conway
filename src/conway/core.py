import numpy as np


class GameOfLife:
    """
    This class represents [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#).
    """

    def __init__(self, start: np.ndarray):
        """
        Initializes the game from a given initial state.

        Args:
            start (`np.ndarray`): A 2d-array of the initial state, where `0` is a dead cell and `1` a live cell.

        Raises:
            ValueError: If the input state `start` is not 2-dimensional.
            ValueError: If the input state has other values than `0` and `1` for dead/live cells.
        """
        if start.ndim != 2:
            raise ValueError(
                f"Input 'start' must be a 2-dim numpy array, but it has {start.ndim} dimensions."
            )
        if not ((start == 0) | (start == 1)).all():
            (rows, cols) = np.where(~((start == 0) | (start == 1)))
            invalid_vals = {(int(r), int(c)): start[r, c] for r, c in zip(rows, cols)}
            raise ValueError(
                f"Input state must only have values 0/1 for dead/live cells, but the following invalid entries were found: {invalid_vals}"
            )

        self.state: np.ndarray = np.array(start.copy(), dtype=np.uint8)
        """The current state of the game as a 2d array. Entries with value `0` are dead cells and `1` are live cells."""
        self._neighbors = np.zeros_like(self.state)
        self._flop = np.zeros_like(self.state)

    def step(self) -> bool:
        """
        Calculates one simulation step of the game.

        Returns:
            bool: `True` if there are still some cells alive, `False` if all are dead.
        """
        self._neighbors.fill(0)

        self._neighbors += np.roll(self.state, -1, axis=0)  # bottom neighbors
        self._neighbors += np.roll(self.state, 1, axis=0)  # top neighbors
        self._neighbors += np.roll(self.state, -1, axis=1)  # right neighbors
        self._neighbors += np.roll(self.state, 1, axis=1)  # left neighbors

        self._neighbors += np.roll(
            self.state, (-1, -1), axis=(0, 1)
        )  # bottom right neighbors
        self._neighbors += np.roll(
            self.state, (-1, 1), axis=(0, 1)
        )  # bottom left neighbors
        self._neighbors += np.roll(
            self.state, (1, 1), axis=(0, 1)
        )  # top left  neighbors
        self._neighbors += np.roll(
            self.state, (1, -1), axis=(0, 1)
        )  # top right neighbors

        # each cell in `flop` now containes the number of neighbors at that site.
        # Conway's Game of Life rules are the following:
        # 1. Live cell with #neighbors < 2 dies
        # 2. Live cell with #neighbors == 2, 3 survives
        # 3. Live cell with #neighbors > 3 dies
        # 4. Dead cell with #neighbors == 3 comes to life

        alive = self.state > 0

        self._flop.fill(0)
        self._flop[(self._neighbors < 2) & alive] = 0
        self._flop[((self._neighbors == 2) | (self._neighbors == 3)) & alive] = 1
        self._flop[(self._neighbors > 3) & alive] = 0
        self._flop[(self._neighbors == 3) & ~alive] = 1

        self.state, self._flop = self._flop, self.state

        return self.state.sum().sum() != 0

    def simulate(self, max_iterations: int | None = None) -> None:
        """
        Simulates the game until the given maximum number of iterations, or all cells are dead.

        Args:
            max_iterations (int | None): If given, the maximum number of simulation steps to calculate. Otherwise, run indefinitely, or until all cells are dead.
        """
        if max_iterations is not None:
            for _ in range(max_iterations):
                if not self.step():
                    return
        else:
            while self.step():
                ...

    def __str__(self) -> str:
        """
        Generates a multi-line string representation of the game state.
        Useful for printing in the console/terminal.

        Returns:
            str: A multi-line string representation of the game.
        """
        (rows, cols) = self.state.shape

        symbols = [" ", "▀", "▄", "█"]
        game_str: str = "┌" + cols * "─" + "┐\n"

        for r in range(rows // 2):
            game_str += "│"
            for c in range(cols):
                index = int(self.state[r * 2, c] + 2 * self.state[r * 2 + 1, c])
                game_str += symbols[index]
            game_str += "│\n"

        if rows % 2 == 1:
            game_str += "│"
            for c in range(cols):
                index = int(self.state[-1, c])
                game_str += symbols[index]
            game_str += "│\n"

        game_str += "└" + cols * "─" + "┘\n"
        return game_str
