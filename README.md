# python-plugins-demo
---

Dependencies are imported by downstream packages. A plugin system enables dependencies to import their children, creating upstream coupling between packages. Python provides a way of implementing plugin systems using the packaging tools. Inside the `setup.py` configuration for a plugin package, one may specify an `entry-points` parameter that registers modules with a namespace that may be searched by other packages installed in the same python environment. 

Plugins are usually used when the dependency is an application and libraries that depend on it contribute extension code that may be used within the application. The `master` module implements a `Thing` class that downstream plugins can extend and register for use by the `master` application.

It can also be exploited to structure user-created configuration profiles as python packages. The `master` application can take a parameter to select a plugin and use its attributes to supply configuration parameters. This approach can be convenient for straight-through processes where the configuration is only allowed to change between invocations of the command.

---
install:
- `pip install -e master`
- `pip install -e plugin1`
- `pip install -e plugin2`

run:
- show installed plugins and registered Thing subclasses:
  - `python -m master -v`
- show some attributes of plugin1 module
  - `python -m master plugin1`

---
