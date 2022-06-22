from typing import TypedDict

import pytermgui as ptg


class PageWindows(TypedDict):
    window: ptg.Window
    assign: str


class Page(TypedDict):
    layout: ptg.Layout | None
    windows: list[PageWindows]
