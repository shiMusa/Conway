"""
# Conway's Game of Life

A python implementation using numpy.

The repository can be found here: [Conway](https://github.com/shiMusa/Conway)

The game state can either be printed to the console
```
┌────────────────────────────────────────────────────────────────┐
│  ▄▀ ██▀   ▄   ▄█▀▄█▀▄      █▀ ▄▀▄      ▄▄        ▀ ▀▀ ▀  █  ▀ █│
│      ▀  ▄█▀   ▄ ▄▄ ▀ █     █  ▀█▀      ▀▀               ▄▀█▄   │
│▄ ▄ ▀█▄▀   ▀    ▀▀ ▀█▄▀     ▀▄ ▄        ▄         ▄▄▄▄▄██▀█   ▄▀│
│   ▄▄▀       ▄█▄ ██ ▀▀   ▄▄   ▀▀      ▀▀▄ ███      ▀█   ▄▄█  ▀▄ │
│▀▀█     ▄█▀▀▀ ▀ █▄▀█     ▀▀             ▀▀ ▀▀        ▄ ▄ ▀ ▄  ▀█│
│█▀      ▀█   ▀▀ ▄▄▀      ▄ ▀▄     ▄ ▄     ▀▄▄        ▀▄█▄▀█▀ ▄▄▀│
│         ▀▄▄█  █▀       ▄█▄  ▀▄  █  ▀       ▄  █▄ ▄▄  ▀▀▄▄   █▀▀│
│   ▄▄█▄     ▀▄         ▀▄█▄▄▀   █▀ █   ▄█   ▀  ▀▄█▀█   ▄█▄ ▀█   │
│ ▀█ ██ ▄     ▄▀          ▀▀ ▀  ▀▄▀     ▀█▄    ▀▀    ▄▄██▀▀▀▀ ▀▄ │
│   ▀               ▄▀▄     █             ▀ ▄▀▀█     ▀      ▀▄▄▄▀│
│                 ▄ █  █▄          ▄ ▄      ▀   ▄                │
│ ▄ ▄ ▄          ▀▄▄  █▀▀           ▀███▄     ▄ ▄                │
│ ▀  ▀▀▄          ▀        ▄ ▄       █ ▄▀▀         ▄▄          ██│
│██▀▀▀█▄          █ ▀▄   ██   ▀▄      ██▄        ▄█ ▄█         ▀▀│
│▀▀ ▄▄▀▄          █      ▄    ▀▄████▄   ▀█▄▄     ▀█ █▄▄▄▄▄▄▄▄ █▀▀│
│ █ █▄██        ▄▀▀ ▄    ▀ █  ▀▄▄   ▀     ▀▀      ▀▄   ▄ █ █ ▀█▄ │
└────────────────────────────────────────────────────────────────┘
```
or be rendered do a native window via [pyray/raylib](https://electronstudio.github.io/raylib-python-cffi/README.html):
<img src="images/game_raylib.png" width="500" alt="Screenshot of the native raylib window showing the game state.">

There are two sub modules:
- The .core module contains the .core.GameOfLife class used to run the simulation.
- The .raylib module offers the `run_with_raylib` function that opens a native window and renders the game in real time.

"""

from .core import GameOfLife
from .raylib import run_with_raylib
