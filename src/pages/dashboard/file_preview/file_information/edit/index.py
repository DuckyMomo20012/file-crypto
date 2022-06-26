from datetime import datetime
from typing import Any

import pytermgui as ptg
from pydash import debounce

import routes
import session
from src.api.file_crypto.service import updateFileOneField
from src.helpers.form_validation import dateField, requiredField
from src.helpers.page_manager import drawPage, goToPrevPage, switchCurrPageWindowSlot
from src.types.Page import Page


# NOTE: This merely copy pastes the code from
# dashboard/settings/your_information/edit/index.py
# Should we create a component for this page?
# NOTE: We also need fileName parameter to be passed to this function
def EditFileInformation(
    label: str, oldValue: Any, fileName: str, fieldName: str, validator: str = ""
) -> Page:

    inputField = ptg.InputField()

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

        updateFileOneField(session.user.email, fileName, fieldName, newValue)

        # NOTE: Remember to go back to previous page TWICE, so we close edit
        # page AND information page! Just like edit user information page.

        # Close the file information window
        goToPrevPage(window.manager)
        goToPrevPage(window.manager)
        # Clear nav bar window AND file preview window (body)
        switchCurrPageWindowSlot(window.manager, "nav_bar", clear=True)
        switchCurrPageWindowSlot(window.manager, "body", clear=True)
        # And redraw the dashboard page
        drawPage(window.manager, routes.routes["dashboard"]())

    window = ptg.Window(
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
                "Cancel", debounce(lambda *_: goToPrevPage(window.manager), 1000)
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
