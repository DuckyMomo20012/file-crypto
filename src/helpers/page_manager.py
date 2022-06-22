from typing import Any

import pytermgui as ptg

import session


def switchPage(manager, newPage: Any) -> None:
    goToPrevPage(manager)
    drawPage(manager, newPage)


def switchCurrPageWindowSlot(
    manager: ptg.WindowManager,
    targetAssign: str,
    newWindow: ptg.Window | Any | None = None,
    clear=True,
    isAdd=False,
):
    # NOTE: Temporary set "clear" default to True and isAdd to False due to bug
    # in pytermgui
    # BUG: pytermgui doesn't close window completely. Need more research

    if len(session.navigation) > 0:
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
                manager.remove(window=slot["window"], autostop=False)
                newPage["windows"].remove(slot)

        elif isAdd is False:
            # If clear is False, we just remove the last window in the list
            manager.remove(window=swapSlots[-1]["window"], autostop=False)
            newPage["windows"].remove(swapSlots[-1])

        # Then we add the new window to the slot
        if isinstance(newWindow, ptg.Window):
            newPage["windows"].append({"window": newWindow, "assign": targetAssign})

            manager.add(window=newWindow, assign=targetAssign)
        elif newWindow is not None:
            newPage["windows"].extend(newWindow["windows"])

            for window in newWindow["windows"]:
                manager.add(window=window["window"], assign=window["assign"])

        session.navigation[-1] = newPage


def drawPage(manager: ptg.WindowManager, newPage: Any | None) -> None:

    if newPage is not None:
        # Append new page to navigation stack
        session.navigation.append(newPage)

        if newPage["layout"] is not None:
            manager.layout = newPage["layout"]
        for window in newPage["windows"]:
            manager.add(window=window["window"], assign=window["assign"])


def goToPrevPage(manager: ptg.WindowManager) -> None:

    if len(session.navigation) > 0:
        # Remove last page from navigation stack
        currWindow = session.navigation.pop()

        if currWindow["layout"] is not None:
            manager.layout = currWindow["layout"]
        for window in currWindow["windows"]:
            manager.remove(window=window["window"], autostop=False)


def clearNavigation(manager: ptg.WindowManager):

    for _ in range(len(session.navigation)):
        goToPrevPage(manager)


def exitApp(manager: ptg.WindowManager):

    manager.stop()
