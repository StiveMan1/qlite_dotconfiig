from libqtile.bar import CALCULATED
from libqtile.lazy import lazy

from core.bar.utils import base, decoration, iconFont, powerline
from extras import Clock, GroupBox, modify, TextBox, Volume, widget
from utils import color

tags = [
  '•', '•', '•', '•', '•', '•',
]

bar = {
  'background': color['bg']+'.9',
  'border_color': color['bg']+'.0',
  'border_width': 4,
  'margin': [5, 5, 0, 5],
  'opacity': 1.0,
  'size': 18,
}
bottom_bar = {
  'background': color['bg']+'.0',
  'margin': [5, 5, 5, 0],
  'opacity': 1.0,
  'size': 24,
}

def sep(fg: str, offset = 0, padding = 8) -> TextBox:
  return TextBox(
    **base(None, fg),
    **iconFont(),
    offset = offset,
    padding = padding,
    text = '|',
  )

def logo(bg: str, fg: str) -> TextBox:
  return modify(
    TextBox,
    **base(bg, fg),
    **decoration(),
    **iconFont(),
    mouse_callbacks = { 'Button1': lazy.restart() },
    offset = 4,
    padding = 17,
    text = '',
  )

def groups(bg: str, fg: str) -> GroupBox:
  return GroupBox(
    **base(bg, fg),
    **iconFont(),
    **decoration(),
    borderwidth = 1,
    colors = [color['blue']] * 6,
    highlight_color = bg,
    highlight_method = 'line',
    inactive = color['black'],
    invert = True,
    padding = 8,
    rainbow = True,
  )

def volume(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **decoration('left'),
      **iconFont(),
      text = '',
      x = 4,
    ),
    modify(
      Volume,
      **base(bg, fg),
      **powerline('arrow_right'),
      commands = {
        'decrease': 'pamixer --decrease 5',
        'increase': 'pamixer --increase 5',
        'get': 'pamixer --get-volume-human',
        'mute': 'pamixer --toggle-mute',
      },
      update_interval = 0.1,
    ),
  ]

def updates(bg: str, fg: str) -> list:
  return [
    TextBox(
      **base(bg, fg),
      **iconFont(),
      offset = -1,
      text = '',
      x = -5,
    ),
    widget.CheckUpdates(
      **base(bg, fg),
      **decoration('right'),
      colour_have_updates = fg,
      colour_no_updates = fg,
      display_format = '{updates} updates  ',
      distro = 'Arch_checkupdates',
      initial_text = 'No updates  ',
      no_update_string = 'No updates  ',
      padding = 0,
      update_interval = 3600,
    ),
  ]

def window_name(bg: str, fg: str) -> object:
  return widget.WindowName(
    **base(bg, fg),
    format = '{name}',
    max_chars = 60,
    width = CALCULATED,
  )

def cpu(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **decoration('left'),
      **iconFont(),
      offset = 3,
      text = '',
      x = 5,
    ),
    widget.CPU(
      **base(bg, fg),
      **powerline('arrow_right'),
      format = '{load_percent:.0f}%',
    )
  ]

def ram(bg: str, fg: str) -> list:
  return [
    TextBox(
      **base(bg, fg),
      **iconFont(),
      offset = -2,
      padding = 5,
      text = '﬙',
      x = -2,
    ),
    widget.Memory(
      **base(bg, fg),
      **powerline('arrow_right'),
      format = '{MemUsed: .0f}{mm} ',
      padding = -1,
    ),
  ]

def disk(bg: str, fg: str) -> list:
  return [
    TextBox(
      **base(bg, fg),
      **iconFont(),
      offset = -1,
      text = '',
      x = -5,
    ),
    widget.DF(
      **base(bg, fg),
      **decoration('right'),
      format = '{f} GB  ',
      padding = 0,
      partition = '/',
      visible_on_warn = False,
      warn_color = fg,
    ),
  ]

def clock(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **decoration('left'),
      **iconFont(),
      offset = 2,
      text = '',
      x = 4,
    ),
    modify(
      Clock,
      **base(bg, fg),
      **decoration('right'),
      format = '%A - %I:%M %p ',
      long_format = '%B %-d, %Y ',
      padding = 6,
    ),
  ]
def lol():
    pass


widgets = [
  widget.Spacer(length = 2),
  logo(color['blue'], color['bg']),
  sep(color['black'], offset = 4, padding = 4),
  *volume(color['magenta'], color['bg']),
  *updates(color['red'], color['bg']),

  widget.Spacer(),
  window_name(None, color['fg']),
  widget.Spacer(),

  *cpu(color['green'], color['bg']),
  *ram(color['yellow'], color['bg']),
  *disk(color['cyan'], color['bg']),
  
  sep(color['black']),
  
  sep(color['black']),
  *clock(color['magenta'], color['bg']),
  widget.Spacer(length = 2),
]

bottom_widgets = [
  widget.Spacer(),
  modify(
    TextBox,
    **base(color['bg']+'.9', color['black']),
    **decoration('left', 12),
    **iconFont(),
    offset = -12,
  ),
    
  groups(color['bg']+'.9', color['black']),
  
  modify(
    TextBox,
    **base(color['bg']+'.9', color['black']),
    **decoration('right', 12),
    **iconFont(),
    offset = -12,
  ),
  widget.Spacer(),
]
