import pytermgui as ptg

import session
from src.api.auth.service import getOneUser
from src.components import ErrorModal
from src.helpers.cryptography import signFile, verify_password
from src.helpers.file import writeFileToFolder
from src.helpers.form_validation import fileField, folderField, requiredField
from src.helpers.page_manager import goToPrevPage


def SignFile():
    filePathField = ptg.InputField()
    passwordField = ptg.InputField()
    passwordField.styles["value"] = "invisible"
    saveFolderPathField = ptg.InputField()

    # TODO: Implement sign file logic
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

        window.manager.toast(f"Signing file {filePath}...")

        # Sign file
        signature = signFile(user.privateKey, filePath, passphrase=password)

        # Write signature to file
        writeFileToFolder(filePath + ".sig", saveFolderPath, signature, mode="wb")

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
            ptg.Button("Close", lambda *_: goToPrevPage(window.manager)),
        ),
    )

    window.center()
    window.is_modal = True
    window.is_noresize = True
    window.overflow = ptg.Overflow.RESIZE
    window.set_title("Sign your file")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
