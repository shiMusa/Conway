# Conway
Simulate Conway's Game of Live in Python.

## Setup

### Using `uv` package manager
Install dependencies via 
```bash
uv sync
```
Install the project itself as a module via
```bash
uv pip install --editable .
```

Run code via
```bash
uv run experiments.py
```

### Using [Docker](https://www.docker.com/)

Build Docker image via
```bash
docker build -t conway .
```

Run Docker image and access bash shell
```bash
docker run -it conway /bin/bash
```

You can now run the code via
```bash
uv run experiments.py
```

## Development

...todo...