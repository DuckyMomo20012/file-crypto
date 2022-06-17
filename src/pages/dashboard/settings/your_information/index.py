import pytermgui as ptg
from src.helpers.index import goToPrevPage, drawPage

from src.api.auth.service import getOneUser

import config


def YourInformation():

    user = getOneUser(config.session.email)

    dob = user.dateOfBirth.strftime("%m/%d/%Y")

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
            chars={"separator": ""},
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
                        label="Date of birth", oldValue=dob, fieldName="dateOfBirth"
                    ),
                ),
            ),
            chars={"separator": ""},
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
            chars={"separator": ""},
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
            chars={"separator": ""},
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
