import pytermgui as ptg

from functools import partial

import session

from src.components.layouts.AppShell import AppShell
from src.helpers.index import drawPage, exitApp, switchCurrPageWindowSlot
from src.components import ConfirmModal

from src.api.auth.service import getOneUser

from src.api.file_crypto.service import getAllFiles

# TODO: Implement this function to fetch data from the database and return
# format like this
# NOTE: Any suggestions for a better way to do this?
def getFiles():

    user = getOneUser(session.user.email)

    files = getAllFiles(user.email)

    returnedFiles = {}

    for file in files:
        # NOTE: We can read file metadata from the database using file.metadata.
        # E.g: fileField.upload_date, fileField.length, fileField.chunkSize, etc.
        date = file.cipher.upload_date.strftime("%Y-%m-%d")
        if date not in returnedFiles:
            returnedFiles[date] = []
        returnedFiles[date].append({"name": file.name})

    # NOTE: Date can have different formats, but recommend using YYYY-MM-DD or
    # DD-MM-YYYY, with a "-" or "/" as a separator
    # return {
    #     "2020-01-01": [
    #         {"name": "app.py"},
    #         {"name": "app.py"},
    #         {"name": "app.py"},
    #     ],
    # }
    return returnedFiles


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
            targetAssign="body",
            newWindow=navBar.manager.routes["dashboard/file_preview/password_prompt"](
                fileName=fileName
            ),
        )

    def handleExitClick():

        ConfirmModal(
            exitBar.manager,
            "Are you sure you want to exit?",
            confirmOnClick=lambda *_: exitApp(hamburger.manager),
            cancelOnClick=lambda *_: None,
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
            # ptg.Button(
            #     "Download shared file",
            #     lambda *_: drawPage(
            #         navBar.manager,
            #         navBar.manager.routes["dashboard/download_shared_file"](),
            #     ),
            #     parent_align=ptg.HorizontalAlignment.CENTER,
            # ),
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
                        ),
                        parent_align=ptg.HorizontalAlignment.LEFT,
                    )
                    for file in files[dates]
                ],
                parent_align=ptg.HorizontalAlignment.LEFT,
                size_policy=ptg.SizePolicy.STATIC,
                # FIXME: Don't hardcode this width
                width=14,  # Total size for date is 14 blocks
            )
            for dates in sorted(files.keys(), reverse=True)
        ],
    )
    navBar.is_static = True
    # navBar.is_noresize = True
    navBar.vertical_align = ptg.VerticalAlignment.TOP
    navBar.overflow = ptg.Overflow.SCROLL

    hamburger = ptg.Window(
        ptg.Splitter(
            ptg.Button(
                "⚙️ ",
                lambda *_: drawPage(
                    hamburger.manager, hamburger.manager.routes["dashboard/settings"]()
                ),
            ),
            ptg.Button(
                "🧰",
                lambda *_: drawPage(
                    hamburger.manager, hamburger.manager.routes["dashboard/tools"]()
                ),
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
