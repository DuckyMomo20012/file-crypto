from typing import Optional

import pytermgui as ptg

import routes
import session
from src.api.auth.service import getOneUser
from src.helpers.page_manager import drawPage, goToPrevPage
from src.types.Page import Page


def YourInformation() -> Optional[Page]:

    if session.user is None:
        return None

    user = getOneUser(session.user.email)

    dob = user.dateOfBirth.strftime("%Y-%m-%d")

    window = ptg.Window(
        "",
        ptg.Label(
            f"Email: {user.email}",
            parent_align=ptg.HorizontalAlignment.LEFT,
        ),
        ptg.Splitter(
            ptg.Label(
                f"Name: {user.name}",
                parent_align=ptg.HorizontalAlignment.LEFT,
            ),
            ptg.Button(
                "Edit",
                lambda *_: drawPage(
                    window.manager,
                    routes.routes["dashboard/settings/your_information/edit"](
                        label="Name", oldValue=user.name, fieldName="name"
                    ),
                ),
            ),
        ),
        ptg.Splitter(
            ptg.Label(
                f"Date of birth: {dob}",
                parent_align=ptg.HorizontalAlignment.LEFT,
            ),
            ptg.Button(
                "Edit",
                lambda *_: drawPage(
                    window.manager,
                    routes.routes["dashboard/settings/your_information/edit"](
                        label="Date of birth (YYYY-MM-DD)",
                        oldValue=dob,
                        fieldName="dateOfBirth",
                        validator="dateField",
                    ),
                ),
            ),
        ),
        ptg.Splitter(
            ptg.Label(
                f"Phone number: {user.phone}",
                parent_align=ptg.HorizontalAlignment.LEFT,
            ),
            ptg.Button(
                "Edit",
                lambda *_: drawPage(
                    window.manager,
                    routes.routes["dashboard/settings/your_information/edit"](
                        label="Phone number", oldValue=user.phone, fieldName="phone"
                    ),
                ),
            ),
        ),
        ptg.Splitter(
            ptg.Label(
                f"Address: {user.address}",
                parent_align=ptg.HorizontalAlignment.LEFT,
            ),
            ptg.Button(
                "Edit",
                lambda *_: drawPage(
                    window.manager,
                    routes.routes["dashboard/settings/your_information/edit"](
                        label="Address", oldValue=user.address, fieldName="address"
                    ),
                ),
            ),
        ),
        ptg.Button("Back", lambda *_: goToPrevPage(window.manager)),
    )

    window.center()
    window.is_modal = True
    window.overflow = ptg.Overflow.RESIZE
    window.set_title("Your Information")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
