import pytermgui as ptg

from src.helpers.page_manager import drawPage, goToPrevPage


def Tools():

    window = ptg.Window(
        "",
        ptg.Button(
            "Sign file",
            lambda *_: drawPage(
                window.manager, window.manager.routes["dashboard/tools/sign_file"]()
            ),
            parent_align=ptg.HorizontalAlignment.CENTER,
        ),
        ptg.Button(
            "Verify signed file",
            lambda *_: drawPage(
                window.manager,
                window.manager.routes["dashboard/tools/verify_signed_file"](),
            ),
            parent_align=ptg.HorizontalAlignment.CENTER,
        ),
        ptg.Button(
            "Encrypt file",
            lambda *_: drawPage(
                window.manager, window.manager.routes["dashboard/tools/encrypt_file"]()
            ),
            parent_align=ptg.HorizontalAlignment.CENTER,
        ),
        ptg.Button(
            "Decrypt file",
            lambda *_: drawPage(
                window.manager,
                window.manager.routes["dashboard/tools/decrypt_file"](),
            ),
            parent_align=ptg.HorizontalAlignment.CENTER,
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
    window.set_title(title="Tools")

    return {
        "layout": None,
        "windows": [
            {"window": window, "assign": ""},
        ],
    }
