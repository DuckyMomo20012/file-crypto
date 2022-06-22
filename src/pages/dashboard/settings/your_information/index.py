import pytermgui as ptg

import session
from src.api.auth.service import getOneUser
from src.helpers.page_manager import drawPage, goToPrevPage


def YourInformation():

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
                    window.manager.routes["dashboard/settings/your_information/edit"](
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
                    window.manager.routes["dashboard/settings/your_information/edit"](
                        label="Date of birth",
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
                    window.manager.routes["dashboard/settings/your_information/edit"](
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
                    window.manager.routes["dashboard/settings/your_information/edit"](
                        label="Address", oldValue=user.address, fieldName="address"
                    ),
                ),
            ),
        ),
        ptg.Button("Back", lambda *_: goToPrevPage(window.manager)),
    )

    window.set_title("Your Information")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
