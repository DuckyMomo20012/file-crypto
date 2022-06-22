import pytermgui as ptg

import session
from src.api.auth.service import getOneUser
from src.api.file_crypto.service import getOneFile
from src.components import ErrorModal, SuccessModal
from src.helpers.cryptography import decryptData, verify_password
from src.helpers.file import writeFileToFolder
from src.helpers.form_validation import folderField, requiredField
from src.helpers.page_manager import goToPrevPage
from src.types.Page import Page


def DownloadFile(fileName: str) -> Page:
    passwordField = ptg.InputField()
    passwordField.styles["value"] = "invisible"
    saveFolderPathField = ptg.InputField()

    # DONE: Implement download file logic
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

        user = getOneUser(session.user.email)

        if not verify_password(password, user.password):
            ErrorModal(window.manager, "Invalid password")
            return

        window.manager.toast(f"Downloading {fileName}...")

        file = getOneFile(user.email, fileName)

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

    window.center()
    window.is_modal = True
    window.is_noresize = True
    window.overflow = ptg.Overflow.RESIZE
    window.set_title("Download file")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
