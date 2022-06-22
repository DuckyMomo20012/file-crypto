import pytermgui as ptg

from src.api.auth.service import getOneUser
from src.components import ErrorModal, SuccessModal
from src.helpers.cryptography import encryptFile
from src.helpers.form_validation import fileField, folderField, requiredField
from src.helpers.page_manager import goToPrevPage
from src.types.Page import Page


def EncryptFile() -> Page:
    filePathField = ptg.InputField()
    receiverEmailField = ptg.InputField()
    saveFolderPathField = ptg.InputField()

    # DONE: Implement encrypt file logic
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
            ptg.Button(
                "Encrypt file",
                lambda *_: handleEncryptClick(),
            ),
            ptg.Button("Close", lambda *_: goToPrevPage(window.manager)),
        ),
    )

    window.center()
    window.is_modal = True
    window.is_noresize = True
    window.overflow = ptg.Overflow.RESIZE
    window.set_title("Encrypt your file")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
