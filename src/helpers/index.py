import pytermgui as ptg


def switchPage(currWindow: ptg.Window, newWindow: ptg.Window) -> None:
    manager = currWindow.manager
    goToPrevPage(manager)
    drawWindow(manager, newWindow)


def drawWindow(manager: ptg.WindowManager, newWindow) -> None:
    # Append new page to navigation stack
    manager.navigation.append(newWindow)

    if newWindow["layout"] is not None:
        manager.layout = newWindow["layout"]
    for window in newWindow["windows"]:
        manager.add(window=window["window"], assign=window["assign"])


def goToPrevPage(manager: ptg.WindowManager) -> None:

    if len(manager.navigation) > 0:
        # Remove last page from navigation stack
        currWindow = manager.navigation.pop()

        if currWindow["layout"] is not None:
            manager.layout = currWindow["layout"]
        for window in currWindow["windows"]:
            manager.remove(window=window["window"], autostop=False)


def clearNavigation(manager):
    for _ in range(len(manager.navigation)):
        goToPrevPage(manager)
