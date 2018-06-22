# python-plugins-demo
Dependencies are imported by downstream packages. Plugins allow dependencies to import their children. This is usually used when the dependency is an application and libraries that depend on it provide extensions that should be used within the application. It can also be exploited to structure user-created configuration profiles as python packages. 

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
