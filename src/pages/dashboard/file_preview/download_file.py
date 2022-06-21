import pytermgui as ptg

from src.helpers.index import goToPrevPage
from src.helpers.form_validation import requiredField, folderField
from src.components import SuccessModal, ErrorModal

import config

from src.api.auth.service import getOneUser
from src.api.file_crypto.service import getOneFile

from src.helpers.cryptography import decryptData, verify_password

from src.helpers.file import writeFileToFolder


def DownloadFile(fileName: str):
    passwordField = ptg.InputField()
    passwordField.styles["value"] = "invisible"
    saveFolderPathField = ptg.InputField()

    # TODO: Implement download file logic
    def handleDownloadClick():
        if not requiredField(window.manager, passwordField, label="Your password"):
            return

        if not folderField(
            window.manager, saveFolderPathField, label="Save folder path"
        ):
            return

        # fileName = ...

        # NOTE: Remember to check if this is a valid folder directory
        password = passwordField.value
        saveFolderPath = saveFolderPathField.value

        user = getOneUser(config.session.email)

        if not verify_password(password, user.password):
            ErrorModal(window.manager, "Invalid password")
            return

        window.manager.toast(f"Downloading {fileName}...")

        file = getOneFile(fileName)

        decryptedData = decryptData(
            privateKey=user.privateKey,
            passphrase=password,
            encryptedSessionKey=file.sessionKey,
            nonce=file.nonce,
            tag=file.tag,
            cipherText=file.cipher.read(),
        )

        if decryptedData:

            writeFileToFolder(
                filePath=fileName,
                folderPath=saveFolderPath,
                content=decryptedData,
            )

            SuccessModal(window.manager, "File downloaded successfully!")

        else:
            ErrorModal(window.manager, "Error downloading file!")

        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label("Your password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(passwordField),
        ptg.Label("Save folder path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(saveFolderPathField),
        "",
        ptg.Splitter(
            ptg.Button("Cancel", lambda *_: goToPrevPage(window.manager)),
            ptg.Button(
                "Download",
                lambda *_: handleDownloadClick(),
            ),
        ),
    )

    window.set_title("Download file")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
