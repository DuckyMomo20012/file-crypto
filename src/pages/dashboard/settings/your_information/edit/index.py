from datetime import datetime
from typing import Any

import pytermgui as ptg
from pydash import debounce

import session
from src.api.auth.service import updateUserOneField
from src.constants import BUTTON_DEBOUNCE_TIME
from src.helpers.form_validation import dateField, requiredField
from src.helpers.page_manager import goToPrevPage
from src.types.Page import Page


def EditUserInformation(
    label: str, oldValue: Any, fieldName: str, validator: str = ""
) -> Page:

    inputField = ptg.InputField()

    # DONE: Implement edit functionality
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

    window: ptg.Window = ptg.Window(
        "",
        ptg.Label(
            f"Old {label.lower()}:",
            parent_align=ptg.HorizontalAlignment.LEFT,
        ),
        ptg.Label(
            f"[nord8]{oldValue}" if oldValue else "[dim]Not set",
            parent_align=ptg.HorizontalAlignment.LEFT,
        ),
        ptg.Label(
            f"New {label.lower()}:",
            parent_align=ptg.HorizontalAlignment.LEFT,
        ),
        ptg.Container(inputField),
        "",
        ptg.Splitter(
            ptg.Button("Confirm", lambda *_: handleConfirmClick()),
            ptg.Button(
                "Cancel",
                debounce(lambda *_: goToPrevPage(window.manager), BUTTON_DEBOUNCE_TIME),
            ),
        ),
    )

    window.center()
    window.is_modal = True
    window.is_noresize = True
    window.overflow = ptg.Overflow.RESIZE
    window.set_title(title="[window__title]Edit Information")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
