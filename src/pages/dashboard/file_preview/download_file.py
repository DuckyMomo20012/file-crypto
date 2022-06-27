import pytermgui as ptg
from pydash import debounce

import session
from src.api.auth.service import getOneUser
from src.api.file_crypto.service import getOneFile
from src.components import ErrorModal, SuccessModal
from src.constants import BUTTON_DEBOUNCE_TIME
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

        if isinstance(decryptedData, str):

            writeFileToFolder(
                filePath=fileName,
                folderPath=saveFolderPath,
                content=decryptedData,
            )

            SuccessModal(window.manager, "File downloaded successfully!")
        elif isinstance(decryptedData, bytes):

            writeFileToFolder(
                filePath=fileName,
                folderPath=saveFolderPath,
                content=decryptedData,
                mode="wb",
            )

            SuccessModal(window.manager, "File downloaded successfully!")

        else:
            ErrorModal(window.manager, "Error downloading file!")

        goToPrevPage(window.manager)

    # NOTE: This fix mypy error: Cannot determine type of "window"
    window: ptg.Window = ptg.Window(
        "",
        ptg.Label("Your password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(passwordField),
        ptg.Label("Save folder path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(saveFolderPathField),
        "",
        ptg.Splitter(
            ptg.Button(
                "Download",
                lambda *_: handleDownloadClick(),
            ),
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
    window.set_title("[window__title]Download file")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
