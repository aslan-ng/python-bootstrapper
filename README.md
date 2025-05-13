# python-bootstrapper
A minimal Python package showing how to bootstrap and auto-discover local plugin modules at runtime using a two-phase binding approach

## Features

- **Zero-boilerplate plugins** — just drop a `<plugin_name>.py` next to your script.
- **Bootstrapped imports** — automatically binds plugin without path hacks.
- **Configurable filename** — pick any `<plugin_name>.py`.
- **Pure stdlib** — no extra dependencies.

## Installation

Clone and install in editable mode:

```bash
git clone https://github.com/<your-username>/python-bootstrapper.git
cd python-bootstrapper
pip install -e .
```

## How It Works

### 1. Early binding
Without defining this initial part, the code will face circular import error during runtime. This works as the default so that from bootstrapper import Math never fails—even while plugins are still loading.

```python
from .main import Math as _BasePackage
Math = _BasePackage
```

### 2. Dynamic discovery

Later, it calls:

```python
Math = _discover_local(plugin_name="customize")
```

which:
* Finds the directory of the running script.
* Builds the filename `<plugin_name>.py`.
* If present, imports that file as a module.
* Scans for any subclass of _BasePackage.
* Returns that subclass—or falls back to _BasePackage.


## Adapting to Your Own Project
1. Change the package name (bootstrapper) to match your own module.
2. Change package files and the base class name (Math) in `main.py` to your own.
3. In `__init__.py`, change `plugin_name` in `_discover_local` function.
4. Write `<plugin_name>.py` next to your script, subclassing your base class.
5. Start using your customized package! In your entry-point, simply import your base class. The bootstrapper will swap in your subclass automatically.