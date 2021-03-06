from typing import Optional, Union

import pytermgui as ptg

import session
from src.constants import WINDOW_ANIMATE
from src.helpers.file import getSettingField
from src.types.Page import Page


def switchPage(
    manager: Optional[ptg.WindowManager], newPage: Union[Page, None]
) -> None:
    goToPrevPage(manager)
    drawPage(manager, newPage)


# NOTE: Temporary set "clear" default to True and isAdd to False due to bug
# in pytermgui
# BUG: pytermgui doesn't close window completely. Need more research
def switchCurrPageWindowSlot(
    manager: Optional[ptg.WindowManager],
    targetAssign: str,
    newWindow: Union[ptg.Window, Page, None] = None,
    clear=True,
    isAdd=False,
):

    animate = getSettingField("workbench.animation", WINDOW_ANIMATE)

    if manager and len(session.navigation) > 0:
        # We build new page based on previous page, then we remove assigned slots
        # which are match with currAssign
        newPage = session.navigation[-1]

        # Loop to find the "slot" to replace, maybe many windows are
        # assigned to the same slot
        swapSlots = [
            slot for slot in newPage["windows"] if str(slot["assign"]) == targetAssign
        ]

        # Then we remove all windows assigned to the this slot if clear is True
        if clear is True:
            for slot in swapSlots:
                # Close window
                manager.remove(window=slot["window"], autostop=False, animate=animate)
                newPage["windows"].remove(slot)

        elif isAdd is False:
            # If clear is False, we just remove the last window in the list
            manager.remove(
                window=swapSlots[-1]["window"], autostop=False, animate=animate
            )
            newPage["windows"].remove(swapSlots[-1])

        # Then we add the new window to the slot
        if isinstance(newWindow, ptg.Window):
            newPage["windows"].append({"window": newWindow, "assign": targetAssign})

            manager.add(window=newWindow, assign=targetAssign, animate=animate)
        elif newWindow is not None:
            newPage["windows"].extend(newWindow["windows"])

            for window in newWindow["windows"]:
                manager.add(
                    window=window["window"], assign=window["assign"], animate=animate
                )

        session.navigation[-1] = newPage


def drawPage(manager: Optional[ptg.WindowManager], newPage: Union[Page, None]) -> None:

    animate = getSettingField("workbench.animation", WINDOW_ANIMATE)

    if manager and newPage is not None:
        # Append new page to navigation stack
        session.navigation.append(newPage)

        if newPage["layout"] is not None:
            manager.layout = newPage["layout"]
        for window in newPage["windows"]:
            manager.add(
                window=window["window"], assign=window["assign"], animate=animate
            )


def goToPrevPage(manager: Optional[ptg.WindowManager]) -> None:

    animate = getSettingField("workbench.animation", WINDOW_ANIMATE)

    if manager and len(session.navigation) > 0:
        # Remove last page from navigation stack
        currWindow = session.navigation.pop()

        if currWindow["layout"] is not None:
            manager.layout = currWindow["layout"]
        for window in currWindow["windows"]:
            manager.remove(window=window["window"], autostop=False, animate=animate)


def clearNavigation(manager: Optional[ptg.WindowManager]):

    if manager is not None:
        for _ in range(len(session.navigation)):
            goToPrevPage(manager)


def exitApp(manager: Optional[ptg.WindowManager]):

    if manager is not None:
        manager.stop()
