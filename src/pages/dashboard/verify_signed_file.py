import pytermgui as ptg

from src.helpers.index import goToPrevPage
from src.helpers.form_validation import requiredField


def VerifySignedFile():
    filePathField = ptg.InputField()
    signaturePathField = ptg.InputField()

    # TODO: Implement verify signed file logic
    def handleVerifyClick():
        if not requiredField(window.manager, filePathField, label="File path"):
            return
        if not requiredField(
            window.manager, signaturePathField, label="Signature file path"
        ):
            return

        # NOTE: Remember to check if this is a valid file directory
        filePath = filePathField.value
        signaturePath = signaturePathField.value

        window.manager.toast(f"Verifying {filePath}...")

        if True:
            emailUser = "example@gmail.com"
            alertModal = window.manager.alert(
                "Signature verified",
                f"User {emailUser} signed file",
                "",
                ptg.Button("OK", lambda *_: alertModal.close()),
            )
        else:
            alertModal = window.manager.alert(
                "Signature verification failed",
                "Unknown user signed file",
                "",
                ptg.Button("OK", lambda *_: alertModal.close()),
            )

    window = ptg.Window(
        "",
        ptg.Label("File path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(filePathField),
        ptg.Label("Signature file path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(signaturePathField),
        "",
        ptg.Splitter(
            ptg.Button("Cancel", lambda *_: goToPrevPage(window.manager)),
            ptg.Button(
                "Verify",
                lambda *_: handleVerifyClick(),
            ),
        ),
    )

    window.set_title("Verify signed file")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
