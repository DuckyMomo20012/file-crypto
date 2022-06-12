import pytermgui as ptg

from src.pages.auth.login import Login


with ptg.WindowManager() as manager:
    ptg.boxes.ROUNDED.set_chars_of(ptg.Container)
    ptg.boxes.ROUNDED.set_chars_of(ptg.Window)

    # manager.layout = AppShell()
    manager.add(Login(manager))

    manager.run()
