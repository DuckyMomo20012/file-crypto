from typing import Optional

import pytermgui as ptg

from src.helpers.macros import (
    getCPUPercent,
    getCursor,
    getRAMPercent,
    getSelectionLength,
)


def Footer(inputField: Optional[ptg.InputField]) -> ptg.Window:

    ptg.tim.define("!cpu", getCPUPercent)
    ptg.tim.define("!ram", getRAMPercent)

    windowWidgets = [
        # ptg.Label(
        #     "[!cpu]CPU: {cpu}%",
        #     parent_align=ptg.HorizontalAlignment.LEFT,
        # ),
        # ptg.Label(
        #     "[!ram]RAM: {ram}%",
        #     parent_align=ptg.HorizontalAlignment.RIGHT,
        # ),
    ]

    if inputField:
        ptg.tim.define("!cursor", getCursor(inputField))
        ptg.tim.define("!select_len", getSelectionLength(inputField))

        windowWidgets.append(
            ptg.Label(
                "[!cursor]Cursor: {row}:{col}[/!cursor] // [!select_len]{select_len}",
                parent_align=ptg.HorizontalAlignment.RIGHT,
            ),
        )

    footer = ptg.Window(
        ptg.Splitter(*windowWidgets),
        box="EMPTY",
    )

    return footer
