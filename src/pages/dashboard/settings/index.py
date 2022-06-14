import pytermgui as ptg
from src.helpers.index import drawWindow, goToPrevPage


def Settings():

    window = ptg.Window(
        "",
        ptg.Button(
            "Change password",
            lambda *_: drawWindow(
                window.manager,
                window.manager.routes["dashboard/settings/change_password"](),
            ),
        ),
        ptg.Button(
            "Logout",
            lambda *_: drawWindow(
                window.manager, window.manager.routes["auth/logout"]()
            ),
        ),
        "",
        # NOTE: We don't use window.close() because we want to keep track of
        # navigation and this is a page not a modal or an alert. We use goToPrevPage to
        # pop this page from the navigation stack.
        ptg.Button("Close", lambda *_: goToPrevPage(window.manager)),
    )

    window.set_title(title="Settings")
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [
            {"window": window, "assign": ""},
        ],
    }
