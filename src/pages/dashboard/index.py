from functools import partial

import pytermgui as ptg

import routes
import session
from src.api.auth.service import getOneUser
from src.api.file_crypto.service import getAllFiles
from src.components import ConfirmModal
from src.components.layouts.AppShell import AppShell

# from src.components.modules.footer import Footer
from src.helpers.page_manager import drawPage, exitApp, switchCurrPageWindowSlot
from src.types.Page import Page


# DONE: Implement this function to fetch data from the database and return
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


def DashBoard() -> Page:
    # from app import manager as super_manager

    def handleUploadClick():

        drawPage(navBar.manager, routes.routes["dashboard/upload_file"]())

    # NOTE: A little hack to bind the fileName to the switchCurrPageWindowSlot
    # function and to avoid late binding problem, otherwise we will ONLY get the
    # last fileName in the list. E.g: file3, file6, file9,...
    def handleButtonClick(_button, fileName):

        return switchCurrPageWindowSlot(
            manager=navBar.manager,
            targetAssign="body",
            newWindow=routes.routes["dashboard/file_preview/password_prompt"](
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
        "[#81a1c1 bold]Dashboard",
        box="EMPTY",
    )
    # header.styles.fill = "[@#81a1c1]{item}"

    def getCollapsibleList():
        for dates in sorted(files.keys(), reverse=True):
            dateCollapsible = ptg.Collapsible(
                dates,
                *[
                    ptg.Button(
                        f'{"└─" if file == files[dates][-1] else "├─"} {file["name"]}',
                        onclick=partial(
                            handleButtonClick,
                            fileName=file["name"],
                        ),
                        parent_align=ptg.HorizontalAlignment.LEFT,
                    )
                    for file in files[dates]
                ],
                parent_align=ptg.HorizontalAlignment.LEFT,
            )
            # This is why I have to create this function, I need to access
            # "trigger" attribute from the collapsible to left align the
            # collapsible label
            dateCollapsible.trigger.parent_align = ptg.HorizontalAlignment.LEFT
            yield dateCollapsible

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
            #         routes.routes["dashboard/download_shared_file"](),
            #     ),
            #     parent_align=ptg.HorizontalAlignment.CENTER,
            # ),
        ),
        "",
        "[nord11 bold italic underline]My files",
        "",
        *getCollapsibleList(),
    )

    # navBar.is_noresize = True
    navBar.is_static = True
    navBar.overflow = ptg.Overflow.SCROLL
    navBar.vertical_align = ptg.VerticalAlignment.TOP

    hamburger = ptg.Window(
        ptg.Splitter(
            ptg.Button(
                "Settings",
                lambda *_: drawPage(
                    hamburger.manager, routes.routes["dashboard/settings"]()
                ),
            ),
            ptg.Button(
                "Tools",
                lambda *_: drawPage(
                    hamburger.manager, routes.routes["dashboard/tools"]()
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

    # footer = Footer()

    return {
        "layout": AppShell(),
        "windows": [
            {"window": header, "assign": "header"},
            {"window": hamburger, "assign": "hamburger"},
            {"window": exitBar, "assign": "exit"},
            {"window": navBar, "assign": "nav_bar"},
            # {"window": footer, "assign": "footer"},
        ],
    }
