import pytermgui as ptg

from src.helpers.index import goToPrevPage
from src.helpers.form_validation import requiredField, fileField
from src.components import SuccessModal, ErrorModal

import config

from src.helpers.file import readFile

from src.api.auth.service import getOneUser
from src.api.file_crypto.service import uploadFile

from src.helpers.cryptography import encryptData


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

        user = getOneUser(config.session.email)

        fileContent = readFile(filePath, mode="rb")

        encryptedData = encryptData(user.publicKey, fileContent)

        if encryptedData:
            encryptedSessionKey, nonce, tag, cipherText = encryptedData

            uploadFile(
                name=filePath,
                sessionKey=encryptedSessionKey,
                nonce=nonce,
                tag=tag,
                cipher=cipherText,
            )

            SuccessModal(window.manager, "File uploaded successfully!")

        else:
            ErrorModal(window.manager, "Error uploading file!")

        goToPrevPage(window.manager)

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
