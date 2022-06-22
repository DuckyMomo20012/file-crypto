import pytermgui as ptg

import session
from src.api.auth.service import getOneUser
from src.api.file_crypto.service import uploadFileNoDuplicate
from src.components import ErrorModal, SuccessModal
from src.helpers.cryptography import encryptData
from src.helpers.file import readFile
from src.helpers.form_validation import fileField, requiredField
from src.helpers.page_manager import drawPage, goToPrevPage, switchCurrPageWindowSlot


def UploadFile():

    filePathField = ptg.InputField()

    def handleUploadClick():
        if not requiredField(window.manager, filePathField, label="File path"):
            return

        if not fileField(window.manager, filePathField, label="File path"):
            return

        filePath = filePathField.value
        window.manager.toast(f"Uploading {filePath}...")

        # TODO: Implement upload logic

        user = getOneUser(session.user.email)

        fileContent = readFile(filePath, mode="rb")

        encryptedData = encryptData(user.publicKey, fileContent)

        if encryptedData:
            encryptedSessionKey, nonce, tag, cipherText = encryptedData

            uploadFileNoDuplicate(
                name=filePath,
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
        drawPage(window.manager, window.manager.routes["dashboard"]())

    window = ptg.Window(
        "",
        ptg.Label("File path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(filePathField),
        "",
        ptg.Splitter(
            ptg.Button("Cancel", lambda *_: goToPrevPage(window.manager)),
            ptg.Button(
                "Upload",
                lambda *_: handleUploadClick(),
            ),
        ),
    )

    window.set_title(title="Upload file")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
