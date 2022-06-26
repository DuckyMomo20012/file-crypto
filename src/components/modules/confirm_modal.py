from typing import Any, Callable, Optional

import pytermgui as ptg
from pydash import debounce


# NOTE: Only window which doesn't animate when closing NEEDS to be set debounce
# for "Close" button. Usually form or modal windows, which is set overflow:
# RESIZE
def ConfirmModal(
    manager: Optional[ptg.WindowManager],
    msg: str,
    confirmOnClick: Optional[Callable[..., Any]] = None,
    cancelOnClick: Optional[Callable[..., Any]] = None,
) -> None:
    if not manager:
        return None

    def handleConfirmClick() -> None:
        if confirmOnClick is not None:
            confirmOnClick()
        confirmModal.close()

    def handleCancelClick() -> None:
        if cancelOnClick is not None:
            cancelOnClick()
        confirmModal.close()

    confirmModal = manager.alert(
        "",
        ptg.Label(
            msg,
            size_policy=ptg.SizePolicy.STATIC,
        ),
        "",
        ptg.Splitter(
            ptg.Button("Yes", debounce(lambda *_: handleConfirmClick(), 1000)),
            ptg.Button("No", debounce(lambda *_: handleCancelClick(), 1000)),
        ),
    )

    confirmModal.is_noresize = True
    confirmModal.overflow = ptg.Overflow.RESIZE
    confirmModal.set_title("[window__title--warning]Confirm")
    confirmModal.styles["border_focused"] = "[window__border--warning]{item}"
    confirmModal.styles["border"] = "[window__border--warning]{item}"
    confirmModal.styles["corner_focused"] = "[window__corner--warning]{item}"
    confirmModal.styles["corner"] = "[window__corner--warning]{item}"

    return None
