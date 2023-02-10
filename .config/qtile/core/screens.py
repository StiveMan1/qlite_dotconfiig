from libqtile.config import Screen

from core.bar import bar, bottom_bar
from utils import config

screens = [
  Screen(
    wallpaper = config['wallpaper'],
    wallpaper_mode = 'fill',
    top = bar,
    bottom = bottom_bar,

    x=0,
    y=0,
    width=1980,
    height=1080
  ),

  Screen(
    wallpaper = config['wallpaper'],
    wallpaper_mode = 'fill',
    
    x=0,
    y=0,
    width=600,
    height=480
  ),
]
