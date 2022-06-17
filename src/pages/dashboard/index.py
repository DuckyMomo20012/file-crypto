import pytermgui as ptg

from functools import partial

from src.components.layouts.AppShell import AppShell
from src.helpers.index import drawPage, exitApp, switchCurrPageWindowSlot

# TODO: Implement this function to fetch data from the database and return
# format like this
# NOTE: Any suggestions for a better way to do this?
def getFiles():

    # NOTE: Date can have different formats, but recommend using YYYY-MM-DD or
    # DD-MM-YYYY, with a "-" or "/" as a separator
    return {
        "2020-01-01": [
            {"name": "app.py", "content": "Hello World"},
            {"name": "app.py", "content": "Hello World"},
            {"name": "app.py", "content": "Hello World"},
        ],
        "2020-01-02": [
            {"name": "app.py", "content": "Hello World"},
            {"name": "app.py", "content": "Hello World"},
            {"name": "app.py", "content": "Hello World"},
        ],
        "2020-01-03": [
            {"name": "app.py", "content": "Hello World"},
            {"name": "app.py", "content": "Hello World"},
            {"name": "app.py", "content": "Hello World"},
        ],
        "2020-01-04": [
            {"name": "app.py", "content": "Hello World"},
            {"name": "app.py", "content": "Hello World"},
            {"name": "app.py", "content": "Hello World"},
        ],
        "2020-01-05": [
            {"name": "app.py", "content": "Hello World"},
            {"name": "app.py", "content": "Hello World"},
            {"name": "app.py", "content": "Hello World"},
        ],
    }


def DashBoard() -> None:
    # from app import manager as super_manager

    def handleUploadClick():

        drawPage(navBar.manager, navBar.manager.routes["dashboard/upload_file"]())

    # NOTE: A little hack to bind the fileName to the switchCurrPageWindowSlot
    # function and to avoid late binding problem, otherwise we will ONLY get the
    # last fileName in the list. E.g: file3, file6, file9,...
    def handleButtonClick(*args, fileName, fileContent):

        return switchCurrPageWindowSlot(
            manager=navBar.manager,
            targetAssign=("body"),
            newWindow=navBar.manager.routes["dashboard/file_preview"](
                fileName=fileName, fileContent=fileContent
            ),
        )

    def handleExitClick():

        exitModal = exitBar.manager.alert(
            "",
            "Do you really want to logout?",
            "",
            ptg.Splitter(
                ptg.Button("Yes", lambda *_: exitApp(hamburger.manager)),
                ptg.Button("No", lambda *_: exitModal.close()),
            ),
        )

    files = getFiles()

    header = ptg.Window(
        "Dashboard",
        box="EMPTY",
    )

    navBar = ptg.Window(
        ptg.Splitter(
            ptg.Button(
                "Upload",
                lambda *_: handleUploadClick(),
                parent_align=ptg.HorizontalAlignment.CENTER,
            ),
            ptg.Button(
                "Download shared file",
                lambda *_: drawPage(
                    navBar.manager,
                    navBar.manager.routes["dashboard/download_shared_file"](),
                ),
                parent_align=ptg.HorizontalAlignment.CENTER,
            ),
        ),
        ptg.Splitter(
            ptg.Button(
                "Sign file",
                lambda *_: drawPage(
                    navBar.manager, navBar.manager.routes["dashboard/sign_file"]()
                ),
                parent_align=ptg.HorizontalAlignment.CENTER,
            ),
            ptg.Button(
                "Verify signed file",
                lambda *_: drawPage(
                    navBar.manager,
                    navBar.manager.routes["dashboard/verify_signed_file"](),
                ),
                parent_align=ptg.HorizontalAlignment.CENTER,
            ),
        ),
        "",
        "My files",
        "",
        *[
            ptg.Collapsible(
                dates,
                *[
                    ptg.Button(
                        label=file["name"],
                        onclick=partial(
                            handleButtonClick,
                            fileName=file["name"],
                            fileContent=file["content"],
                        ),
                    )
                    for file in files[dates]
                ],
                parent_align=ptg.HorizontalAlignment.LEFT,
                size_policy=ptg.SizePolicy.STATIC,
                # FIXME: Don't hardcode this width
                width=14,  # Total size for date is 14 blocks
            )
            for dates in files.keys()
        ],
    )
    navBar.is_static = True
    # navBar.is_noresize = True
    navBar.vertical_align = ptg.VerticalAlignment.TOP
    navBar.overflow = ptg.Overflow.SCROLL

    hamburger = ptg.Window(
        ptg.Button(
            "⚙️ ",
            lambda *_: drawPage(
                hamburger.manager, hamburger.manager.routes["dashboard/settings"]()
            ),
        ),
        box="EMPTY",
    )

    exitBar = ptg.Window(
        ptg.Button(
            "Exit",
            lambda *_: handleExitClick(),
        ),
        box="EMPTY",
    )

    return {
        "layout": AppShell(),
        "windows": [
            {"window": header, "assign": "header"},
            {"window": hamburger, "assign": "hamburger"},
            {"window": exitBar, "assign": "exit"},
            {"window": navBar, "assign": "nav_bar"},
        ],
    }
