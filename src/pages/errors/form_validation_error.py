import pytermgui as ptg


def FormValidationError(manager: ptg.WindowManager, errorMsg: str):

    alertModal = manager.alert(
        ptg.Label(
            errorMsg,
            size_policy=ptg.SizePolicy.STATIC,
        ),
        "",
        ptg.Button("OK", lambda *_: alertModal.close()),
    )

    return None
