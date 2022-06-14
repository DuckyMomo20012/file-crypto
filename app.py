import pytermgui as ptg

from src.pages.routes import routes

from src.helpers.index import drawWindow


with ptg.WindowManager() as manager:
    ptg.boxes.ROUNDED.set_chars_of(ptg.Container)
    ptg.boxes.ROUNDED.set_chars_of(ptg.Window)

    manager.routes = routes

    # Add navigation history stack
    manager.navigation = []

    # drawWindow(manager, manager.routes["dashboard"]())
    drawWindow(manager, manager.routes["auth/login"]())

    manager.run()
