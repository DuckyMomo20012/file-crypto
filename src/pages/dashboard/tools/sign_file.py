from pathlib import Path

import pytermgui as ptg
from pydash import debounce  # type: ignore

import session
from src.api.auth.service import getOneUser
from src.components import ErrorModal
from src.constants import BUTTON_DEBOUNCE_TIME
from src.helpers.cryptography import signFile, verify_password
from src.helpers.file import writeFileToFolder
from src.helpers.form_validation import fileField, folderField, requiredField
from src.helpers.page_manager import goToPrevPage
from src.types.Page import Page


def SignFile() -> Page:
    filePathField = ptg.InputField()
    passwordField = ptg.InputField()
    passwordField.styles["value"] = "invisible"
    saveFolderPathField = ptg.InputField()

    # DONE: Implement sign file logic
    def handleSignClick():
        if not requiredField(window.manager, filePathField, label="File path"):
            return
        if not requiredField(window.manager, passwordField, label="Your password"):
            return

        if not fileField(window.manager, filePathField, label="File path"):
            return

        if not folderField(
            window.manager, saveFolderPathField, label="Save folder path"
        ):
            return

        # NOTE: Remember to check if this is a valid folder & file directory
        filePath = filePathField.value
        password = passwordField.value
        saveFolderPath = saveFolderPathField.value

        user = getOneUser(session.user.email)

        # Verify password to make sure the passphrase is correct
        if not verify_password(password, user.password):
            ErrorModal(window.manager, "Invalid password")
            return

        # NOTE: Because writeFileToFolder will extract file name for us, so we
        # are just doing extras here :v. But we need file name to display toast
        # message correctly.
        fileName = Path(filePath).name
        window.manager.toast(f"Signing file {fileName}...")

        # Sign file
        signature = signFile(user.privateKey, filePath, passphrase=password)

        # Write signature to file
        writeFileToFolder(fileName + ".sig", saveFolderPath, signature, mode="wb")

        # Go to previous page
        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label("File path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(filePathField),
        ptg.Label("Your password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(passwordField),
        ptg.Label(
            "Save folder path (optional)", parent_align=ptg.HorizontalAlignment.LEFT
        ),
        ptg.Container(saveFolderPathField),
        "",
        ptg.Splitter(
            ptg.Button(
                "Sign file",
                lambda *_: handleSignClick(),
            ),
            ptg.Button(
                "Close",
                debounce(lambda *_: goToPrevPage(window.manager), BUTTON_DEBOUNCE_TIME),
            ),
        ),
    )

    window.center()
    window.is_modal = True
    window.is_noresize = True
    window.overflow = ptg.Overflow.RESIZE
    window.set_title("[window__title]Sign your file")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
