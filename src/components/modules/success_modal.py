from typing import Any, Callable, Optional

import pytermgui as ptg
from pydash import debounce  # type: ignore

from src.constants import BUTTON_DEBOUNCE_TIME


def SuccessModal(
    manager: Optional[ptg.WindowManager],
    msg: str,
    onclick: Optional[Callable[..., Any]] = None,
) -> None:
    if not manager:
        return None

    def handleClick() -> None:
        if onclick is not None:
            onclick()
        successModal.close()

    successModal = manager.alert(
        "",
        ptg.Label(
            msg,
            size_policy=ptg.SizePolicy.STATIC,
        ),
        "",
        ptg.Button("OK", debounce(lambda *_: handleClick(), BUTTON_DEBOUNCE_TIME)),
    )

    successModal.is_noresize = True
    successModal.overflow = ptg.Overflow.RESIZE
    successModal.set_title("[window__title--success]Success")
    successModal.styles["border_focused"] = "[window__border--success]{item}"
    successModal.styles["border"] = "[window__border--success]{item}"
    successModal.styles["corner_focused"] = "[window__corner--success]{item}"
    successModal.styles["corner"] = "[window__corner--success]{item}"

    return None
