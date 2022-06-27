import io

from climage.__main__ import _get_color_type, _toAnsi
from PIL import Image


def convert_frombytes(
    fileContent: bytes,
    is_unicode=False,
    is_truecolor=False,
    is_256color=True,
    is_16color=False,
    is_8color=False,
    width=80,
    palette="default",
):
    """
    Convert an image, and return the resulting string.
    Arguments:
    infile          -- The name of the input file to load. Example:
    '/home/user/image.png'
    Keyword Arguments:
    is_unicode      -- whether to use unicode in generating output (default
    False, ASCII will be used)
    is_truecolor    -- whether to use RGB colors in generation (few terminals
    support this). Exactly one color option must only be selected. Default
    False.
    is_256color     -- whether to use 256 colors (16 system colors, 6x6x6 color
    cube, and 24 grayscale colors) for generating the output. This is the
    default color setting. Please run colortest-256 for a demonstration of
    colors. Default True.
    is_16color      -- Whether to use only the 16 System colors. Default False
    is_8color       -- Whether to use only the first 8 of the System colors.
    Default False.
    width           -- Number of columns the output will use
    palette         -- Determines which RGB colors the System colors map to.
    This only is relevant when using 8/16/256 color modes. This may be one of
    ["default", "xterm", "linuxconsole", "solarized", "rxvt", "tango",
    "gruvbox", "gruvboxdark"]
    """
    # open the img, but convert to rgb because this fails if grayscale
    # (assumes pixels are at least triplets)
    stream = io.BytesIO(fileContent)
    im = Image.open(stream).convert("RGB")
    ctype = _get_color_type(
        is_truecolor=is_truecolor,
        is_256color=is_256color,
        is_16color=is_16color,
        is_8color=is_8color,
    )
    return _toAnsi(
        im, oWidth=width, is_unicode=is_unicode, color_type=ctype, palette=palette
    )
