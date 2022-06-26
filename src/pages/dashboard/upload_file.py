from pathlib import Path

import pytermgui as ptg
from pydash import debounce  # type: ignore

import routes
import session
from src.api.auth.service import getOneUser
from src.api.file_crypto.service import uploadFileNoDuplicate
from src.components import ErrorModal, SuccessModal
from src.constants import BUTTON_DEBOUNCE_TIME
from src.helpers.cryptography import encryptData
from src.helpers.file import readFile
from src.helpers.form_validation import fileField, requiredField
from src.helpers.page_manager import drawPage, goToPrevPage, switchCurrPageWindowSlot
from src.types.Page import Page


def UploadFile() -> Page:

    filePathField = ptg.InputField()

    def handleUploadClick():
        if not requiredField(window.manager, filePathField, label="File path"):
            return

        if not fileField(window.manager, filePathField, label="File path"):
            return

        filePath = filePathField.value

        # DONE: Implement upload logic

        user = getOneUser(session.user.email)

        fileContent = readFile(filePath, mode="rb")

        encryptedData = encryptData(user.publicKey, fileContent)

        if encryptedData:
            encryptedSessionKey, nonce, tag, cipherText = encryptedData

            # Because we have already checked if this is a valid file name, not
            # a folder path, so we don't have to check if this is an empty
            # string '' here (Path.name will return empty string if folder path)
            fileName = Path(filePath).name
            window.manager.toast(f"Uploading {fileName}...")

            uploadFileNoDuplicate(
                name=fileName,
                sessionKey=encryptedSessionKey,
                nonce=nonce,
                tag=tag,
                cipher=cipherText,
                emailUser=user.email,
            )

            SuccessModal(window.manager, "File uploaded successfully!")

        else:
            ErrorModal(window.manager, "Error uploading file!")

        # Close the upload file window
        goToPrevPage(window.manager)
        # Clear nav bar window
        switchCurrPageWindowSlot(window.manager, "nav_bar", clear=True)
        # And redraw the dashboard page
        drawPage(window.manager, routes.routes["dashboard"]())

    window = ptg.Window(
        "",
        ptg.Label("File path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(filePathField),
        "",
        ptg.Splitter(
            ptg.Button(
                "Upload",
                lambda *_: handleUploadClick(),
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
    window.set_title(title="[window__title]Upload file")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
