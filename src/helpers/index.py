from typing import Any
import pytermgui as ptg


def switchPage(manager, newPage: Any) -> None:
    goToPrevPage(manager)
    drawPage(manager, newPage)


def switchCurrPageWindowSlot(
    manager: ptg.WindowManager,
    currAssign: str,
    newWindow: ptg.Window | Any,
    clear=True,
):

    if len(manager.navigation) > 0:
        # We build new page based on previous page, then we remove assigned slots
        # which are match with currAssign
        newPage = manager.navigation[-1]

        # Loop to find the "slot" to replace, maybe many windows are
        # assigned to the same slot
        swapSlots = [
            slot for slot in newPage["windows"] if str(slot["assign"]) == currAssign
        ]

        # Then we remove all windows assigned to the this slot if clear is True
        if clear == True:
            for slot in swapSlots:
                # Close window
                manager.remove(window=slot["window"], autostop=False)
                newPage["windows"].remove(slot)

        else:
            # If clear is False, we just remove the last window in the list
            manager.remove(window=swapSlots[-1]["window"], autostop=False)
            newPage["windows"].remove(swapSlots[-1])

        # Then we add the new window to the slot
        if isinstance(newWindow, ptg.Window):
            newPage["windows"].append(newWindow)
        else:
            newPage["windows"].extend(newWindow["windows"])

        # NOTE: manager won't redraw the same window instance, so only the
        # newWindow is drawn
        drawPage(manager, newPage)


def drawPage(manager: ptg.WindowManager, newPage) -> None:

    # Append new page to navigation stack
    manager.navigation.append(newPage)

    if newPage["layout"] is not None:
        manager.layout = newPage["layout"]
    for window in newPage["windows"]:
        manager.add(window=window["window"], assign=window["assign"])


def goToPrevPage(manager: ptg.WindowManager) -> None:

    if len(manager.navigation) > 0:
        # Remove last page from navigation stack
        currWindow = manager.navigation.pop()

        if currWindow["layout"] is not None:
            manager.layout = currWindow["layout"]
        for window in currWindow["windows"]:
            manager.remove(window=window["window"], autostop=False)


def clearNavigation(manager: ptg.WindowManager):

    for _ in range(len(manager.navigation)):
        goToPrevPage(manager)


def exitApp(manager: ptg.WindowManager):

    manager.stop()
