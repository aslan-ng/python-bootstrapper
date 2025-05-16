"""
__init__.py for python-bootstrapper package.

Sets up a bootstrap mechanism for discovering a local plugin (<plugin_name>.py)
next to the user's entry-point script. Falls back to the base <BaseClass> if
no local plugin is found.

Example:
    # Put a file named `<plugin_name>.py` next to your script defining:
    # >>> class MyPlugin(<BaseClass>):
    # >>> ...
    #
    # Then in your script:
    # >>> import <MyPackage>
    # >>> ...
    # 
    # It is will automatically load the plugin and use it to customzie the package

Refer to the README for more details on how to use it.
"""

# Standard library imports for filesystem operations, reflection, and dynamic loading
import os, inspect, importlib.util, sys

# Import the core Math class from the main module as the fallback base implementation
"""
Change this import to the actual class you want to use as the base
from .main import <ClassName> as _BasePackage
"""
from .main import Shape as _BasePackage

# Provisional binding: make the base <BaseClass> class immediately available
# so that user plugins can import it without causing a circular import
"""
Change this import to the actual class you want to use as the base
<ClassName> = _BasePackage
"""
Shape = _BasePackage

# plugin_name: the filename (without .py) of the local plugin to load
# Function to locate and load a user-defined '*.py' plugin module
# living alongside the entry-point script, and return its subclass
def _discover_local(plugin_name: str):
    # Determine the directory of the running script (or use cwd as fallback)
    main_mod = sys.modules.get("__main__")
    if hasattr(main_mod, "__file__"):
        script_dir = os.path.dirname(os.path.abspath(main_mod.__file__))
    else:
        script_dir = os.getcwd()
    # Construct the expected path to the plugin file: "<plugin_name>.py"
    plugin_filename = f"{plugin_name}.py"
    path = os.path.join(script_dir, plugin_filename)
    # If the plugin file is not found, fall back to the base <BaseClass>
    if not os.path.isfile(path):
        return _BasePackage
    # Dynamically load the plugin module under the name "<plugin_name>"
    spec = importlib.util.spec_from_file_location(plugin_name, path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # Inspect loaded module for a subclass of the base class
    for obj in vars(mod).values():
        if inspect.isclass(obj) and issubclass(obj, _BasePackage) and obj is not _BasePackage:
            return obj
    return _BasePackage

"""
Override the Plugin name in this package with the discovered subclass
Change this to the actual class you want to use as the base and the plugin filename
"""
Shape = _discover_local(plugin_name="customize")
