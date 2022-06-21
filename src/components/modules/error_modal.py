from typing import Any, Callable, Optional

import pytermgui as ptg


def ErrorModal(
    manager: ptg.WindowManager,
    msg: str,
    onclick: Optional[Callable[[ptg.Button], Any]] = None,
) -> None:
    def handleClick() -> None:
        if onclick is not None:
            onclick()
        errorModal.close()

    errorModal = manager.alert(
        ptg.Label(
            msg,
            size_policy=ptg.SizePolicy.STATIC,
        ),
        "",
        ptg.Button("OK", lambda *_: handleClick()),
    )
    errorModal.styles["border"] = "[window__border--error]{item}"
    errorModal.styles["border_focused"] = "[window__border--error]{item}"
    errorModal.styles["corner"] = "[window__corner--error]{item}"
    errorModal.styles["corner_focused"] = "[window__corner--error]{item}"
    errorModal.set_title("[window__title--error]Error")
    errorModal.overflow = ptg.Overflow.RESIZE
    errorModal.is_noresize = True

    return None
