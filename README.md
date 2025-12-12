# Conway
Simulate Conway's Game of Live in Python.

[Repository by Felix Fehse (shiMusa)](https://github.com/shiMusa/Conway)

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

The game can either be printed in the console/terminal, or rendered to a native window using [pyray/raylib](https://electronstudio.github.io/raylib-python-cffi/README.html).

Example use is given below, the [interactive html documentation](https://shimusa.github.io/Conway/) can be found under `docs/index.html`.

## Setup

### Using uv package manager
If not already installed, [install uv](https://github.com/astral-sh/uv#installation) for your system.

Install dependencies via 
```bash
uv sync
```
Install the project itself as a module via
```bash
uv pip install --editable .
```

### Using [Docker](https://www.docker.com/)

> [!WARNING] 
> You might not be able to use the raylib native window renderin using Docker!

Build Docker image via
```bash
docker build -t conway .
```

Run Docker image and access bash shell
```bash
docker run -it conway /bin/bash
```

## Example

The provided `main.py` program will randomly generate an initial state of the game and simulate it's evolution.

For the first time, it's suggested to run with the following arguments:
```bash
uv run main.py --grid 64 32 --sleep-ms 500 --max-iter 10
```
It will
- `-g 64 321`: generate a game with 64x32 cells,
- `-s 500`: sleep between iteration for 500 ms,
- `-i 10`: run for 10 iterations and then stop.

You can get help on the commands via
```bash
uv run main.py --help
```

You can use the Raylib rendering with the flag `--raylib`, e.g.
```bash
uv run main.py --grid 256 256 --sleep-ms 32 --max-iter 1000 --raylib
```

## Development

The module `conway` can be fund under `src/conway/`, the tests are under `tests/`.

These are the typical development commands used:

**black**: python source code formatter, run via  
```bash
uv run black .
```
or on windows from `scripts/` via the `bat`-script `black`.

**mypy**: python typing tests, run via  
```bash 
uv run uv run mypy -p conway -p tests
uv run mypy main.py
```
or on windows from `scripts/` via the `bat`-script `mypy`.

**pytest**: python testing harness, run via
```bash 
uv run pytest
```
or on windows from `scripts/` via the `bat`-script `test`.

**pdoc**: python documentation tool, rendering the project and it's docstrings into interactive `html` documents. Run with auto updates via
```bash 
uv run pdoc src/conway --docformat google
```
or on windows from `scripts/` via the `bat`-script `doc`. 

To build the documentation to the `docs/` folder, run via
```bash
uv run pdoc src/conway --docformat google -o ./docs  
```