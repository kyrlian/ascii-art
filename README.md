# Simple tool to explore packaging

Pacakged with [uv](https://docs.astral.sh/uv/)

## Run

Run the project script directly with uv:
```sh
uv run ascii_art\app.py
```

Run the project script without installation with uvx:
```sh
uvx --from . ascii
```

## Install

Install with
```sh
uv tool install .
```

Then run with `ascii`

Uninstall with:
```sh
uv tool uninstall ascii_art
```