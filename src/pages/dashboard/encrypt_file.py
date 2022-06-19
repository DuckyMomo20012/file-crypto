import pytermgui as ptg

from src.helpers.index import goToPrevPage
from src.helpers.form_validation import requiredField, fileField

from src.api.auth.service import getOneUser

from src.helpers.cryptography import encryptFile


def EncryptFile():
    filePathField = ptg.InputField()
    receiverEmailField = ptg.InputField()

    # TODO: Implement sign file logic
    def handleEncryptClick():
        if not requiredField(window.manager, filePathField, label="File path"):
            return

        if not fileField(window.manager, filePathField, label="File path"):
            return

        # NOTE: Remember to check if this is a valid folder & file directory
        filePath = filePathField.value
        receiverEmail = receiverEmailField.value

        receiver = getOneUser(receiverEmail)

        # Verify receiver email is exist
        if not receiver:
            alertModal = window.manager.alert(
                "Receiver email is not exist!",
                "",
                ptg.Button("OK", lambda *_: alertModal.close()),
            )
            return

        # Encrypt file
        if encryptFile(receiver.publicKey, filePath):
            alertModal = window.manager.alert(
                "File encrypted successfully!",
                "",
                ptg.Button("OK", lambda *_: alertModal.close()),
            )
        else:
            alertModal = window.manager.alert(
                "File encryption failed!",
                "",
                ptg.Button("OK", lambda *_: alertModal.close()),
            )

        # Go to previous page
        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label("File path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(filePathField),
        ptg.Label("Receiver email", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(receiverEmailField),
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
