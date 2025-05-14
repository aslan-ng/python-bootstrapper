<h1 align="center">
    python-bootstrapper
</h1>

<h3 align="center">
    A minimal Python package showing how to bootstrap and auto-discover local plugin modules at runtime using a two-phase binding approach
</h3>

<div align="center">
    <img src="https://raw.githubusercontent.com/aslan-ng/python-bootstrapper/refs/heads/main/assets/bootstrap-1.png" alt="python-bootstrapper" width="500">
</div>

## Features

- **Zero-boilerplate plugins** — just drop a `<plugin_name>.py` next to your script.
- **Bootstrapped imports** — automatically binds plugin without path hacks.
- **Configurable filename** — pick any `<plugin_name>.py`.
- **Pure stdlib** — no extra dependencies.

## Why Bootstrap Plugins?

The **bootstrapper** pattern solves these pain‑points by:

* Giving you a **single drop‑in file** (`<plugin_name>.py`) that overrides behaviour—no need to touch the upstream package.
* Avoiding path juggling by locating the plugin **relative to the script you actually run**, not the working directory.
* Preventing **circular‑import errors** via an early, provisional binding.
* Staying **dependency‑free**—everything is done with the Python standard library.

## When is this useful?

- Needing a simple plugin capability in your Python project.
- Small tools or projects where simplicity is key.
- Educational, prototyping, or single-user tools.
- Scenarios where you want users to customize behavior by simply editing or replacing a file.

| Scenario | Benefit |
|----------|---------|
| Custom math/physics kernels in a simulation repo | Collaborators can add their own formulas without editing core code |
| Data‑processing pipelines (ETL) | Drop a new `transform.py` to adjust business logic per deployment |
| Classroom assignments | Instructors ship a locked framework; students implement only `solution.py` |
| CLI tools with pluggable commands | Users add commands merely by shipping an extra file |
| Rapid prototyping | Swap algorithms by switching which plugin file sits next to the script |

If you ever find yourself telling users “clone the repo, then modify `some_module.py`,” consider adopting this lightweight bootstrapper instead.

## Installation

Clone it first using your preferred method:

```bash
# HTTPS
git clone https://github.com/aslan-ng/python-bootstrapper.git

# SSH
git clone git@github.com:aslan-ng/python-bootstrapper.git

# GitHub CLI
gh repo clone aslan-ng/python-bootstrapper
```

Then, install in editable mode:
```bash
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

Typical approaches to extensibility often require users to:

1. **Fork the library** and edit core code.
2. Change the package name (bootstrapper) to match your own module.
3. Change package files and the base class name (Math) in `main.py` to your own.
4. In `__init__.py`, change `plugin_name` in `_discover_local` function.
5. Write `<plugin_name>.py` next to your script, subclassing your base class.
6. Start using your customized package! In your entry-point, simply import your base class. The bootstrapper will swap in your subclass automatically.

## Limitations
This is a minimalistic, intentionally simple approach to enable plugin capability by local file discovery. The bootstrapper expects a **single plugin file** (`<plugin_name>.py`) placed next to your script. All plugin classes inside the file must inherit from the base class, and they will be **merged automatically into a single class at runtime**. No error reporting is provided if multiple classes define conflicting methods: the last class in the inheritance chain takes precedence silently. Finally, It does not support more advanced plugin lifecycle management (e.g., enabling/disabling plugins dynamically, multiple isolated plugins, or plugin priorities).