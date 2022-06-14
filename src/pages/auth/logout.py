import pytermgui as ptg

from src.helpers.index import clearNavigation, drawWindow, goToPrevPage


def Logout():
    def handleLogoutClick():
        window.manager.toast("Logging out...")
        # TODO: Implement logout logic

        clearNavigation(window.manager)
        drawWindow(window.manager, window.manager.routes["auth/login"]())

    window = ptg.Window(
        "",
        "Do you really want to logout?",
        "",
        ptg.Splitter(
            # NOTE: We don't use window.close() because we want to keep track of
            # navigation and this is a page not a modal or an alert. We use goToPrevPage to
            # pop this page from the navigation stack.
            ptg.Button("Yes", lambda *_: handleLogoutClick()),
            ptg.Button("No", lambda *_: goToPrevPage(window.manager)),
        ),
    )

    window.set_title(title="Logout")
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
