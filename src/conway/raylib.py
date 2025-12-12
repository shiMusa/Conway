from time import sleep
import numpy as np
import pyray as pr
from raylib import FLAG_WINDOW_RESIZABLE, PIXELFORMAT_UNCOMPRESSED_R8G8B8A8
from .core import GameOfLife


def run_with_raylib(
    game: GameOfLife,
    max_iterations: int | None = None,
    sleep_ms: int | None = None,
) -> None:
    """
    This function simulates the .core.GameOfLife and displays it in a native window using [pyray/raylib](https://electronstudio.github.io/raylib-python-cffi/README.html).

    Args:
        game (`.core.GameOfLife`):The initialized game.
        max_iterations (`int | None`): If given, the maximum number of iterations to run the simulation for. In any case, the simulation will stop when no life cells remain.
        sleep_ms (`int | None`): The number of milliseconds to sleep between iterations.
    """
    (rows, cols) = game.state.shape

    height = 800
    width = int(height / rows * cols)

    pr.set_config_flags(FLAG_WINDOW_RESIZABLE)
    pr.init_window(width, height, "Conway's Game of Life")

    img = pr.gen_image_color(cols, rows, pr.WHITE)
    pr.image_format(img, PIXELFORMAT_UNCOMPRESSED_R8G8B8A8)

    tex = pr.load_texture_from_image(img)

    CHANNELS = 4
    num_bytes = cols * rows * CHANNELS
    byte_buffer = pr.ffi.buffer(img.data, num_bytes)
    np_pixels = np.frombuffer(byte_buffer, dtype=np.uint8).reshape(
        (rows, cols, CHANNELS)
    )

    iter = 0
    while not pr.window_should_close():
        iter += 1
        width = pr.get_screen_width()
        height = pr.get_screen_height()

        if not max_iterations or (max_iterations and iter < max_iterations):
            game.step()

            np_pixels[:, :, :] = [255, 255, 255, 255]
            np_pixels[game.state == 1] = [0, 0, 0, 255]
            pr.update_texture(tex, img.data)

            if sleep_ms:
                sleep(0.001 * sleep_ms)

        pr.begin_drawing()
        pr.clear_background(pr.WHITE)
        pr.draw_texture_pro(
            tex, (0, 0, cols, rows), (0, 0, width, height), (0, 0), 0, pr.WHITE
        )
        pr.end_drawing()

    pr.close_window()
