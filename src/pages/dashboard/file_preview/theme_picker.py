from functools import partial

import pytermgui as ptg
from pygments.styles import STYLE_MAP  # type: ignore

import routes
from src.helpers.page_manager import goToPrevPage, switchCurrPageWindowSlot


def ThemePicker(
    fileName: str,
    passphrase: str,
    preview: str,
    currTheme: str,
):
    def handleThemeClick(
        _button, fileName: str, passphrase: str, preview: str, theme: str
    ):
        # Close the theme picker window
        goToPrevPage(window.manager)
        # Then swap the theme
        switchCurrPageWindowSlot(
            manager=window.manager,
            targetAssign=("body"),
            newWindow=routes.routes["dashboard/file_preview"](
                fileName, passphrase, preview, theme
            ),
        )

    # Some themes cause error on printing the content, so we have blacklist them
    themes = [
        theme
        for theme in list(STYLE_MAP.keys())
        if theme not in ("borland", "lilypond", "trac", "bw", "algol", "algol_nu")
    ]

    themes.insert(0, "no theme")

    # NOTE: We CAN'T pass function correctly when we are in loop. Instead, we
    # use partial to "bind" the arguments to the function.
    themeButtons = [
        ptg.Button(
            f'{"[nord12 italic]" if theme == currTheme else ""}{theme}',
            partial(
                handleThemeClick,
                fileName=fileName,
                passphrase=passphrase,
                preview=preview,
                theme=theme,
            ),
        )
        for theme in themes
    ]

    window = ptg.Window(
        "",
        *themeButtons,
    )

    window.height = 10
    window.is_modal = True
    window.overflow = ptg.Overflow.SCROLL
    window.set_title("Theme picker")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
