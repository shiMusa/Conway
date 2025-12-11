import numpy as np
import pyray as pr
from raylib import FLAG_WINDOW_RESIZABLE
from .core import GameOfLife


def run_with_raylib(game: GameOfLife) -> None:
    width, height = 800, 800

    pr.set_config_flags(FLAG_WINDOW_RESIZABLE)
    pr.init_window(width, height, "Conway's Game of Life")

    iter = 0
    while not pr.window_should_close():
        iter += 1
        width = pr.get_screen_width()
        height = pr.get_screen_height()
        grid_size = (width / game.state.shape[1], height / game.state.shape[0])

        pr.begin_drawing()
        pr.clear_background(pr.WHITE)

        game.step()
        (life_cells_row, life_cell_col) = np.where(game.state == 1)
        for r, c in zip(life_cells_row, life_cell_col):
            pr.draw_rectangle_v(
                (c * grid_size[0], r * grid_size[1]), grid_size, pr.BLACK
            )

        pr.end_drawing()

    pr.close_window()
