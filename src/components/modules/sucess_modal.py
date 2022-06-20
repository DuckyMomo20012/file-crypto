import pytermgui as ptg


def SuccessModal(manager: ptg.WindowManager, msg: str) -> None:

    successModal = manager.alert(
        ptg.Label(
            msg,
            size_policy=ptg.SizePolicy.STATIC,
        ),
        "",
        ptg.Button("OK", lambda *_: successModal.close()),
    )
    successModal.styles["border"] = "[window__border--success]{item}"
    successModal.styles["corner"] = "[window__corner--success]{item}"
    successModal.set_title("[window__title--success]Success")

    return None
