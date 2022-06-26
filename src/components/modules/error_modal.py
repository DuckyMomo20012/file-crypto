from typing import Any, Callable, Optional

import pytermgui as ptg
from pydash import debounce  # type: ignore

from src.constants import BUTTON_DEBOUNCE_TIME


def ErrorModal(
    manager: Optional[ptg.WindowManager],
    msg: str,
    onclick: Optional[Callable[..., Any]] = None,
) -> None:
    if not manager:
        return None

    def handleClick() -> None:
        if onclick is not None:
            onclick()
        errorModal.close()

    errorModal = manager.alert(
        "",
        ptg.Label(
            msg,
            size_policy=ptg.SizePolicy.STATIC,
        ),
        "",
        ptg.Button("OK", debounce(lambda *_: handleClick(), BUTTON_DEBOUNCE_TIME)),
    )

    errorModal.is_noresize = True
    errorModal.overflow = ptg.Overflow.RESIZE
    errorModal.set_title("[window__title--error]Error")
    errorModal.styles["border_focused"] = "[window__border--error]{item}"
    errorModal.styles["border"] = "[window__border--error]{item}"
    errorModal.styles["corner_focused"] = "[window__corner--error]{item}"
    errorModal.styles["corner"] = "[window__corner--error]{item}"

    return None
