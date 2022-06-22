from typing import Any, Callable, Optional

import pytermgui as ptg


def SuccessModal(
    manager: ptg.WindowManager,
    msg: str,
    onclick: Optional[Callable[[ptg.Button], Any]] = None,
) -> None:
    def handleClick() -> None:
        if onclick is not None:
            onclick()
        successModal.close()

    successModal = manager.alert(
        ptg.Label(
            msg,
            size_policy=ptg.SizePolicy.STATIC,
        ),
        "",
        ptg.Button("OK", lambda *_: handleClick()),
    )

    successModal.is_noresize = True
    successModal.overflow = ptg.Overflow.RESIZE
    successModal.set_title("[window__title--success]Success")
    successModal.styles["border_focused"] = "[window__border--success]{item}"
    successModal.styles["border"] = "[window__border--success]{item}"
    successModal.styles["corner_focused"] = "[window__corner--success]{item}"
    successModal.styles["corner"] = "[window__corner--success]{item}"

    return None
