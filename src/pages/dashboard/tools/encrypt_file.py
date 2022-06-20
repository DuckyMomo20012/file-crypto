import pytermgui as ptg

from src.helpers.index import goToPrevPage
from src.helpers.form_validation import requiredField, fileField, folderField
from src.components import SuccessModal, ErrorModal

from src.api.auth.service import getOneUser

from src.helpers.cryptography import encryptFile


def EncryptFile():
    filePathField = ptg.InputField()
    receiverEmailField = ptg.InputField()
    saveFolderPathField = ptg.InputField()

    # TODO: Implement sign file logic
    def handleEncryptClick():
        if not requiredField(window.manager, filePathField, label="File path"):
            return

        if not fileField(window.manager, filePathField, label="File path"):
            return

        if not folderField(
            window.manager, saveFolderPathField, label="Save folder path"
        ):
            return

        # NOTE: Remember to check if this is a valid folder & file directory
        filePath = filePathField.value
        receiverEmail = receiverEmailField.value
        saveFolderPath = saveFolderPathField.value

        receiver = getOneUser(receiverEmail)

        # Verify receiver email is exist
        if not receiver:
            ErrorModal(window.manager, "Receiver email does not exist")
            return

        # Encrypt file
        if encryptFile(receiver.publicKey, filePath, folderPath=saveFolderPath):
            SuccessModal(window.manager, "File encrypted successfully")
        else:
            ErrorModal(window.manager, "Failed to encrypt file")

        # Go to previous page
        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label("File path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(filePathField),
        ptg.Label("Receiver email", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(receiverEmailField),
        ptg.Label(
            "Save folder path (optional)", parent_align=ptg.HorizontalAlignment.LEFT
        ),
        ptg.Container(saveFolderPathField),
        "",
        ptg.Splitter(
            ptg.Button("Cancel", lambda *_: goToPrevPage(window.manager)),
            ptg.Button(
                "Encrypt file",
                lambda *_: handleEncryptClick(),
            ),
        ),
    )

    window.set_title("Encrypt your file")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
