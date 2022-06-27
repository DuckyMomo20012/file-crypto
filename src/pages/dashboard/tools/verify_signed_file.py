import pytermgui as ptg
from pydash import debounce

from src.api.auth.service import getAllUsers
from src.components import ErrorModal, SuccessModal
from src.constants import BUTTON_DEBOUNCE_TIME
from src.helpers.cryptography import verifySignature
from src.helpers.form_validation import fileField, requiredField
from src.helpers.page_manager import goToPrevPage
from src.types.Page import Page


def VerifySignedFile() -> Page:
    filePathField = ptg.InputField()
    signaturePathField = ptg.InputField()

    # DONE: Implement verify signed file logic
    def handleVerifyClick():
        if not requiredField(window.manager, filePathField, label="File path"):
            return
        if not requiredField(
            window.manager, signaturePathField, label="Signature file path"
        ):
            return

        if not fileField(window.manager, filePathField, label="File path"):
            return
        if not fileField(
            window.manager, signaturePathField, label="Signature file path"
        ):
            return

        # NOTE: Remember to check if this is a valid file directory
        filePath = filePathField.value
        signaturePath = signaturePathField.value

        # Verify signature
        window.manager.toast(f"Verifying {filePath}...")

        verified = False
        for user in getAllUsers():
            if verifySignature(user.publicKey, filePath, signaturePath):

                SuccessModal(
                    window.manager, f"Signature verified.\n{user.email} signed"
                )
                verified = True
                break

        if not verified:
            ErrorModal(
                window.manager, "Signature verification failed.\nUnknown user signed"
            )

        # Go to previous page
        goToPrevPage(window.manager)

    window: ptg.Window = ptg.Window(
        "",
        ptg.Label("File path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(filePathField),
        ptg.Label("Signature file path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(signaturePathField),
        "",
        ptg.Splitter(
            ptg.Button(
                "Verify",
                lambda *_: handleVerifyClick(),
            ),
            ptg.Button(
                "Close",
                debounce(lambda *_: goToPrevPage(window.manager), BUTTON_DEBOUNCE_TIME),
            ),
        ),
    )

    window.center()
    window.is_modal = True
    window.is_noresize = True
    window.overflow = ptg.Overflow.RESIZE
    window.set_title("[window__title]Verify signed file")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
