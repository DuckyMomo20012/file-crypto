import pytermgui as ptg

from src.helpers.page_manager import drawPage, goToPrevPage


def Settings():

    window = ptg.Window(
        "",
        ptg.Button(
            "Your information",
            lambda *_: drawPage(
                window.manager,
                window.manager.routes["dashboard/settings/your_information"](),
            ),
        ),
        ptg.Button(
            "Change password",
            lambda *_: drawPage(
                window.manager,
                window.manager.routes["dashboard/settings/change_password"](),
            ),
        ),
        ptg.Button(
            "Logout",
            lambda *_: drawPage(window.manager, window.manager.routes["auth/logout"]()),
        ),
        "",
        # NOTE: We don't use window.close() because we want to keep track of
        # navigation and this is a page not a modal or an alert. We use goToPrevPage to
        # pop this page from the navigation stack.
        ptg.Button("Close", lambda *_: goToPrevPage(window.manager)),
    )

    window.center()
    window.is_modal = True
    window.is_noresize = True
    window.set_title(title="Settings")

    return {
        "layout": None,
        "windows": [
            {"window": window, "assign": ""},
        ],
    }
