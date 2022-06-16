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
        "2020-01-01": ["file1", "file2", "file3"],
        "2020-01-02": ["file4", "file5", "file6"],
        "2020-01-03": ["file7", "file8", "file9"],
        "2020-01-04": ["file10", "file11", "file12"],
        "2020-01-05": ["file13", "file14", "file15"],
    }


def DashBoard() -> None:
    # from app import manager as super_manager

    def handleUploadClick():

        drawPage(navBar.manager, navBar.manager.routes["dashboard/upload_file"]())

    # NOTE: A little hack to bind the fileName to the switchCurrPageWindowSlot
    # function and to avoid late binding problem, otherwise we will ONLY get the
    # last fileName in the list. E.g: file3, file6, file9,...
    def handleButtonClick(*args, fileName):

        return switchCurrPageWindowSlot(
            manager=navBar.manager,
            targetAssign=("body"),
            newWindow=navBar.manager.routes["dashboard/file_preview"](fileName),
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
        "",
        *[
            ptg.Collapsible(
                dates,
                *[
                    ptg.Button(
                        label=fileName,
                        onclick=partial(handleButtonClick, fileName=fileName),
                    )
                    for fileName in files[dates]
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
