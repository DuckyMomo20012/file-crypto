import pytermgui as ptg

import routes
import session
from src.helpers.page_manager import clearNavigation, drawPage, goToPrevPage
from src.types.Page import Page


def Logout() -> Page:
    def handleLogoutClick():
        window.manager.toast("Logging out...")
        # DONE: Implement logout logic

        # We simply reset the current session and go back to the login page
        session.user = None

        clearNavigation(window.manager)
        drawPage(window.manager, routes.routes["auth/login"]())

    window = ptg.Window(
        "",
        "Do you really want to logout?",
        "",
        ptg.Splitter(
            # NOTE: We don't use window.close() because we want to keep track of
            # navigation and this is a page not a modal or an alert. We use
            # goToPrevPage to pop this page from the navigation stack.
            ptg.Button("Yes", lambda *_: handleLogoutClick()),
            ptg.Button("No", lambda *_: goToPrevPage(window.manager)),
        ),
    )

    window.center()
    window.is_modal = True
    window.is_noresize = True
    window.set_title(title="Logout")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
