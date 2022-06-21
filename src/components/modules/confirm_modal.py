import pytermgui as ptg

from typing import Any, Callable, Optional


def ConfirmModal(
    manager: ptg.WindowManager,
    msg: str,
    confirmOnClick: Optional[Callable[[ptg.Button], Any]] = None,
    cancelOnClick: Optional[Callable[[ptg.Button], Any]] = None,
) -> None:
    def handleConfirmClick() -> None:
        if confirmOnClick is not None:
            confirmOnClick()
        confirmModal.close()

    def handleCancelClick() -> None:
        if cancelOnClick is not None:
            cancelOnClick()
        confirmModal.close()

    confirmModal = manager.alert(
        ptg.Label(
            msg,
            size_policy=ptg.SizePolicy.STATIC,
        ),
        "",
        ptg.Splitter(
            ptg.Button("Yes", lambda *_: handleConfirmClick()),
            ptg.Button("No", lambda *_: handleCancelClick()),
        ),
    )
    confirmModal.styles["border"] = "[window__border--warning]{item}"
    confirmModal.styles["border_focused"] = "[window__border--warning]{item}"
    confirmModal.styles["corner"] = "[window__corner--warning]{item}"
    confirmModal.styles["corner_focused"] = "[window__corner--warning]{item}"
    confirmModal.set_title("[window__title--warning]Confirm")
    confirmModal.overflow = ptg.Overflow.RESIZE

    return None