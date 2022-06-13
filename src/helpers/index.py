def switchPage(currWindow, newWindow) -> None:
    manager = currWindow.manager
    currWindow.close()
    drawWindow(manager, newWindow)


def drawWindow(manager, newWindow):
    if newWindow["layout"] is not None:
        manager.layout = newWindow["layout"]
    for window in newWindow["windows"]:
        manager.add(window=window["window"], assign=window["assign"])
