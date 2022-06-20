import pytermgui as ptg


def ErrorModal(manager: ptg.WindowManager, errorMsg: str) -> None:

    errorModal = manager.alert(
        ptg.Label(
            errorMsg,
            size_policy=ptg.SizePolicy.STATIC,
        ),
        "",
        ptg.Button("OK", lambda *_: errorModal.close()),
    )
    errorModal.styles["border"] = "[window__border--error]{item}"
    errorModal.styles["corner"] = "[window__corner--error]{item}"
    errorModal.set_title("[window__title--error]Error")

    return None
