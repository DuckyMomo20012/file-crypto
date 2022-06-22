import pytermgui as ptg

import session
from src.api.auth.service import getOneUser
from src.components import ErrorModal
from src.helpers.cryptography import verify_password
from src.helpers.form_validation import requiredField
from src.helpers.page_manager import switchCurrPageWindowSlot


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

    # window.center()
    # window.overflow = ptg.Overflow.RESIZE
    window.is_modal = True
    window.is_noresize = True
    window.set_title(f"Open file {fileName}")
    window.vertical_align = ptg.VerticalAlignment.TOP

    return {
        "layout": None,
        "windows": [{"window": window, "assign": "body"}],
    }
