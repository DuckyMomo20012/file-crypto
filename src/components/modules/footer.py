import pytermgui as ptg

from src.helpers.macros import getCPUPercent, getRAMPercent


def Footer() -> ptg.Window:

    ptg.tim.define("!cpu", getCPUPercent)
    ptg.tim.define("!ram", getRAMPercent)

    footer = ptg.Window(
        ptg.Splitter(
            ptg.Label(
                "[!cpu]CPU: {cpu}%",
                parent_align=0,
            ),
            ptg.Label(
                "[!ram]RAM: {ram}%",
                parent_align=2,
            ),
        ),
        box="EMPTY",
    )

    return footer
