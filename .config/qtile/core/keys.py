from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from extras import float_to_front
from utils import config

keys, mod, alt = [ ], 'mod4', 'mod1'
terminal = config['terminal'].copy()

if not terminal['main']:
  terminal['main'] = guess_terminal()

for key in [
  # Switch between windows
  ([mod], 'left', lazy.layout.left()),
  ([mod], 'right', lazy.layout.right()),
  ([mod], 'down', lazy.layout.down()),
  ([mod], 'up', lazy.layout.up()),

  # Move windows between columns
  ([mod, 'shift'], 'left', lazy.layout.shuffle_left()),
  ([mod, 'shift'], 'right', lazy.layout.shuffle_right()),
  ([mod, 'shift'], 'down', lazy.layout.shuffle_down()),
  ([mod, 'shift'], 'up', lazy.layout.shuffle_up()),

  # Increase/decrease window size
  #([alt, 'Tab'], 'o', lazy.layout.grow()),
  #([alt, 'Tab'], 'p', lazy.layout.shrink()),

  # Window management
  ([mod, 'shift'], 'space', lazy.layout.flip()),
  #([mod], 'o', lazy.layout.maximize()),
  #([mod], 'n', lazy.layout.normalize()),
  ([mod], 'BackSpace', lazy.window.kill()),
  ([ ], 'F11', lazy.window.toggle_fullscreen()),

  # Floating window management
  ([mod], 'space', lazy.window.toggle_floating()),
  ([mod], 'c', lazy.window.center()),
  ([mod], 'f', lazy.function(float_to_front)),

  # Toggle between layouts
  ([mod], 'Tab', lazy.next_layout()),

  # Qtile management
  ([alt, 'shift'], 'b', lazy.hide_show_bar()),
  ([alt, 'shift'], 's', lazy.shutdown()),
  ([alt, 'shift'], 'r', lazy.reload_config()),
  ([mod, 'shift'], 'r', lazy.restart()),

  # Kill X11 session
  ([mod, alt], 's', lazy.spawn('kill -9 -1')),

  (['control', alt], 'left',  lazy.screen.prev_group()),
  (['control', alt], 'right', lazy.screen.next_group()),

  # Terminal
  ([alt], 'Return', lazy.spawn(terminal['main'])),
  ([alt, 'shift'], 'Return', lazy.spawn(terminal['floating'])),

  # Application Launcher
  ([mod, 'shift'], 'Return', lazy.spawn('rofi -show window')),
  ([mod], 'Return', lazy.spawn('rofi -show drun')),

  # Web Browser
  ([mod], 'b', lazy.spawn(config['browser'])),

  # Screenshot Tool
  ([ ], 'Print', lazy.spawn('gnome-screenshot -i')),

  # Backlight
  ([mod], 'XF86AudioLowerVolume', lazy.spawn('brightnessctl set 5%-')),
  ([mod], 'XF86AudioRaiseVolume', lazy.spawn('brightnessctl set +5%')),

  # Volume
  ([ ], 'XF86AudioMute', lazy.spawn('pamixer --toggle-mute')),
  ([ ], 'XF86AudioLowerVolume', lazy.spawn('pamixer --decrease 5')),
  ([ ], 'XF86AudioRaiseVolume', lazy.spawn('pamixer --increase 5')),

  # Player
  ([ ], 'XF86AudioPlay', lazy.spawn('playerctl play-pause')),
  ([ ], 'XF86AudioPrev', lazy.spawn('playerctl previous')),
  ([ ], 'XF86AudioNext', lazy.spawn('playerctl next')),
]: keys.append(Key(*key)) # type: ignore
