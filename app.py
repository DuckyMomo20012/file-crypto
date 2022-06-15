import pytermgui as ptg

from src.pages.routes import routes

from src.helpers.index import drawPage

with ptg.WindowManager() as manager:
    ptg.boxes.ROUNDED.set_chars_of(ptg.Container)
    ptg.boxes.ROUNDED.set_chars_of(ptg.Window)

    manager.routes = routes

    # Add navigation history stack
    manager.navigation = []

    # drawPage(manager, manager.routes["dashboard"]())
    drawPage(manager, manager.routes["auth/login"]())

    manager.run()
