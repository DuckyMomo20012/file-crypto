from typing import Union

import pytermgui as ptg
from pydash import debounce  # type: ignore

import routes
import session
from src.api.auth.service import getOneUser
from src.api.file_crypto.service import getOneFile
from src.constants import BUTTON_DEBOUNCE_TIME
from src.helpers.page_manager import drawPage, goToPrevPage
from src.types.Page import Page


def FileInformation(fileName: str) -> Union[Page, None]:

    if session.user is None:
        return None

    user = getOneUser(session.user.email)

    file = getOneFile(user.email, fileName)

    window: ptg.Window = ptg.Window(
        "",
        ptg.Splitter(
            ptg.Label(
                f"[italic]Name:[/] [nord8]{file.name}",
                parent_align=ptg.HorizontalAlignment.LEFT,
            ),
            ptg.Button(
                "Edit",
                lambda *_: drawPage(
                    window.manager,
                    routes.routes["dashboard/file_preview/file_information/edit"](
                        label="Name",
                        oldValue=file.name,
                        fileName=fileName,
                        fieldName="name",
                    ),
                ),
            ),
        ),
        ptg.Label(
            f"[italic]Size:[/] [nord8]{file.cipher.length} bytes",
            parent_align=ptg.HorizontalAlignment.LEFT,
        ),
        ptg.Label(
            f"[italic]Upload date:[/]"
            f' [nord8]{file.cipher.upload_date.strftime("%Y-%m-%d")}',
            parent_align=ptg.HorizontalAlignment.LEFT,
        ),
        "",
        ptg.Button(
            "Close",
            debounce(lambda *_: goToPrevPage(window.manager), BUTTON_DEBOUNCE_TIME),
        ),
    )

    window.center()
    window.is_modal = True
    window.overflow = ptg.Overflow.RESIZE
    window.set_title(f"[window__title]{fileName} Information")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
