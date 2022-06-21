from typing import Any
import pytermgui as ptg
from src.helpers.index import goToPrevPage
from src.helpers.form_validation import *

from src.api.auth.service import updateUserOneField

import session

from datetime import datetime


def EditInformation(label: str, oldValue: Any, fieldName: str, validator: str = ""):

    inputField = ptg.InputField()

    # TODO: Implement edit functionality
    def handleConfirmClick():
        if not requiredField(window.manager, inputField, label=f"New {label.lower()}"):
            return

        # NOTE: use fieldName is used to edit user information easily. E.g:
        # user['fieldName'] = inputField.value

        newValue = inputField.value

        if validator == "dateField":
            if not dateField(window.manager, inputField, label=f"New {label.lower()}"):
                return

            newValue = datetime.strptime(inputField.value, "%Y-%m-%d")

        window.manager.toast("Updating information...")

        updateUserOneField(session.user.email, fieldName, newValue)

        # NOTE: We go back to two pages, close settings page, so when user open
        # settings again, it will show the updated information.
        goToPrevPage(window.manager)
        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label(
            f"Old {label.lower()}: {oldValue}",
            parent_align=ptg.HorizontalAlignment.LEFT,
        ),
        ptg.Label(
            f"New {label.lower()}:",
            parent_align=ptg.HorizontalAlignment.LEFT,
        ),
        ptg.Container(inputField),
        "",
        ptg.Splitter(
            ptg.Button("Cancel", lambda *_: goToPrevPage(window.manager)),
            ptg.Button("Confirm", lambda *_: handleConfirmClick()),
        ),
    )

    window.set_title(title="Edit Information")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
