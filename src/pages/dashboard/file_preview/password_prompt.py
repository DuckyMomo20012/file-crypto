import pytermgui as ptg

from src.helpers.index import switchCurrPageWindowSlot
from src.helpers.form_validation import requiredField
from src.components import ErrorModal

import session

from src.api.auth.service import getOneUser

from src.helpers.cryptography import verify_password


def PasswordPrompt(fileName: str):
    passwordField = ptg.InputField()
    passwordField.styles["value"] = "invisible"

    def handleButtonClick():
        if not requiredField(window.manager, passwordField, label="Your password"):
            return

        password = passwordField.value

        user = getOneUser(session.user.email)

        # Verify password to make sure the passphrase is correct
        if not verify_password(password, user.password):
            ErrorModal(window.manager, "Invalid password")
            return

        switchCurrPageWindowSlot(
            manager=window.manager,
            targetAssign=("body"),
            newWindow=window.manager.routes["dashboard/file_preview"](
                fileName=fileName, passphrase=password
            ),
        )

    window = ptg.Window(
        "",
        ptg.Label("Your password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(passwordField),
        "",
        ptg.Splitter(
            ptg.Button(
                "Cancel",
                lambda *_: switchCurrPageWindowSlot(
                    window.manager,
                    "body",
                    clear=True,
                ),
            ),
            ptg.Button(
                "OK",
                lambda *_: handleButtonClick(),
            ),
        ),
    )

    window.set_title(f"Open file {fileName}")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": "body"}],
    }
