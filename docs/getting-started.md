# Getting Started

This project ships runnable demos and lightweight docs. Use minimal dependencies for fast setup.

## Prerequisites
- Python 3.11
- Pip

## Install minimal dependencies
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements-min.txt
```

## Run the full demo
```bash
python glasssphere_infrared_demo.py
```

## Run tests
```bash
pip install -r requirements-dev.txt
pytest -q
```

## Docs site
Docs are published via GitHub Pages. CI builds MkDocs on main and deploys to the `gh-pages` branch.

