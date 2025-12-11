import numpy as np
import pyray as pr
from raylib import FLAG_WINDOW_RESIZABLE
from .core import GameOfLife


def _state_to_img(state: np.ndarray, img: pr.Image):
    pr.image_clear_background(img, pr.WHITE)
    (life_cells_row, life_cell_col) = np.where(state == 1)
    for r, c in zip(life_cells_row, life_cell_col):
        pr.image_draw_pixel(img, c, r, pr.BLACK)


def run_with_raylib(game: GameOfLife) -> None:
    width, height = 800, 800
    (cells_y, cells_x) = game.state.shape

    pr.set_config_flags(FLAG_WINDOW_RESIZABLE)
    pr.init_window(width, height, "Conway's Game of Life")

    img = pr.gen_image_color(cells_x, cells_y, pr.WHITE)
    tex = pr.load_texture_from_image(img)

    iter = 0
    while not pr.window_should_close():
        iter += 1
        width = pr.get_screen_width()
        height = pr.get_screen_height()

        game.step()
        _state_to_img(game.state, img)
        pr.update_texture(tex, img.data)

        pr.begin_drawing()
        pr.clear_background(pr.WHITE)
        pr.draw_texture_pro(
            tex, (0, 0, cells_x, cells_y), (0, 0, width, height), (0, 0), 0, pr.WHITE
        )
        pr.end_drawing()

    pr.close_window()
