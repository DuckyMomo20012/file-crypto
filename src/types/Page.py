from typing import TypedDict, Union

import pytermgui as ptg


class PageWindows(TypedDict):
    window: ptg.Window
    assign: str


class Page(TypedDict):
    layout: Union[ptg.Layout, None]
    windows: list[PageWindows]
