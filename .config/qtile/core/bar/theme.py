from importlib import import_module
from libqtile.bar import Bar

from utils import config

themes = [
  'decorated'
]

if config['bar'] in themes:
  module = import_module(f"core.bar.{config['bar']}")
  module.bar.update(
    { 'widgets': module.widgets }
  )
  module.bottom_bar.update(
    { 'widgets': module.bottom_widgets }
  )

  bar: tuple[Bar | None, list] = (
    Bar(**module.bar),
    Bar(**module.bottom_bar),
    module.tags,
  )
else:
  bar = (None, None, [None] * 10 )
