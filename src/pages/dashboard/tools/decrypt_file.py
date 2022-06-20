import pytermgui as ptg

from src.helpers.index import goToPrevPage
from src.helpers.form_validation import requiredField, fileField, folderField
from src.components import SuccessModal, ErrorModal

import config

from src.api.auth.service import getOneUser

from src.helpers.cryptography import verify_password, decryptFile


def DecryptFile():
    filePathField = ptg.InputField()
    passwordField = ptg.InputField()
    passwordField.styles["value"] = "invisible"
    saveFolderPathField = ptg.InputField()

    # TODO: Implement sign file logic
    def handleDecryptClick():
        if not requiredField(
            window.manager, filePathField, label="Encrypted file path"
        ):
            return

        if not fileField(window.manager, filePathField, label="Encrypted file path"):
            return

        if not folderField(
            window.manager, saveFolderPathField, label="Save folder path"
        ):
            return

        # NOTE: Remember to check if this is a valid folder & file directory
        filePath = filePathField.value
        password = passwordField.value
        saveFolderPath = saveFolderPathField.value

        user = getOneUser(config.session.email)

        # Verify password to make sure the passphrase is correct
        if not verify_password(password, user.password):
            ErrorModal(window.manager, "Invalid password")
            return

        # Decrypt file
        if decryptFile(
            user.privateKey, filePath, passphrase=password, folderPath=saveFolderPath
        ):
            SuccessModal(window.manager, "File decrypted successfully")
        else:
            ErrorModal(
                window.manager,
                "Failed to decrypt file or user does not have permission!",
            )

        # Go to previous page
        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label("Encrypted file path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(filePathField),
        ptg.Label("Your password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(passwordField),
        ptg.Label(
            "Save folder path (optional)", parent_align=ptg.HorizontalAlignment.LEFT
        ),
        ptg.Container(saveFolderPathField),
        "",
        ptg.Splitter(
            ptg.Button("Cancel", lambda *_: goToPrevPage(window.manager)),
            ptg.Button(
                "Decrypt file",
                lambda *_: handleDecryptClick(),
            ),
        ),
    )

    window.set_title("Decrypt your file")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
