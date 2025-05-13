# python-bootstrapper
A minimal Python package showing how to bootstrap and auto-discover local plugin modules at runtime using a two-phase binding approach

## Features

- **Zero-boilerplate plugins** — just drop a `<plugin_name>.py` next to your script.
- **Bootstrapped imports** — automatically binds plugin without path hacks.
- **Configurable filename** — pick any `<plugin_name>.py`.
- **Pure stdlib** — no extra dependencies.

## Why Bootstrap Plugins?

Typical approaches to extensibility often require users to:

1. **Fork the library** and edit core code.
2. Sprinkle **`sys.path` hacks** or environment variables to point at their own modules.
3. Add a heavy plugin framework with extra dependencies.

The **bootstrapper** pattern solves these pain‑points by:

* Giving you a **single drop‑in file** (`<plugin_name>.py`) that overrides behaviour—no need to touch the upstream package.
* Avoiding path juggling by locating the plugin **relative to the script you actually run**, not the working directory.
* Preventing **circular‑import errors** via an early, provisional binding.
* Staying **dependency‑free**—everything is done with the Python standard library.

## When is this useful?

| Scenario | Benefit |
|----------|---------|
| Custom math/physics kernels in a simulation repo | Collaborators can add their own formulas without editing core code |
| Data‑processing pipelines (ETL) | Drop a new `transform.py` to adjust business logic per deployment |
| Classroom assignments | Instructors ship a locked framework; students implement only `solution.py` |
| CLI tools with pluggable commands | Users add commands merely by shipping an extra file |
| Rapid prototyping | Swap algorithms by switching which plugin file sits next to the script |

If you ever find yourself telling users “clone the repo, then modify `some_module.py`,” consider adopting this lightweight bootstrapper instead.

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