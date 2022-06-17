import pytermgui as ptg


def FormValidationError(manager: ptg.WindowManager, errorMsg: str):

    alertModal = manager.alert(
        errorMsg,
        "",
        ptg.Button("OK", lambda *_: alertModal.close()),
    )

    return None
