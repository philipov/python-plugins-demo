# python-plugins-demo
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
