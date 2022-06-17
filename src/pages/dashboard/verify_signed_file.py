import pytermgui as ptg

from src.helpers.index import goToPrevPage


def VerifySignedFile():
    fileLocationField = ptg.InputField()
    signatureLocationField = ptg.InputField()

    # TODO: Implement verify signed file logic
    def handleVerifyClick():
        # NOTE: Remember to check if this is a valid file directory
        fileLocation = fileLocationField.value
        signatureLocation = signatureLocationField.value

        window.manager.toast(f"Verifying {fileLocation}...")

        if True:
            emailUser = "example@gmail.com"
            alertModal = window.manager.alert(
                "Signature verified",
                f"User {emailUser} signed file",
                ptg.Button("OK", lambda *_: alertModal.close()),
            )
        else:
            alertModal = window.manager.alert(
                "Signature verification failed",
                "Unknown user signed file",
                ptg.Button("OK", lambda *_: alertModal.close()),
            )

    window = ptg.Window(
        "",
        ptg.Label("File location", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(fileLocationField),
        ptg.Label("Signature file location", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(signatureLocationField),
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
