from typing import Optional

import pytermgui as ptg
from pydash import debounce  # type: ignore

import routes
import session
from src.api.auth.service import getOneUser, updateUserKeys, updateUserPassword
from src.components import ErrorModal, SuccessModal
from src.constants import BUTTON_DEBOUNCE_TIME
from src.helpers.cryptography import hash_password, updatePassphrase, verify_password
from src.helpers.form_validation import requiredField
from src.helpers.page_manager import clearNavigation, drawPage, goToPrevPage
from src.types.Page import Page


def handleSuccessModalClose(manager: Optional[ptg.WindowManager]) -> None:
    if manager is None:
        return

    manager.toast("Logging out...")
    clearNavigation(manager)
    drawPage(manager, routes.routes["auth/login"]())


def ChangePassword() -> Page:

    oldPasswordField = ptg.InputField()
    oldPasswordField.styles["value"] = "invisible"
    newPasswordField = ptg.InputField()
    newPasswordField.styles["value"] = "invisible"
    confirmNewPasswordField = ptg.InputField()
    confirmNewPasswordField.styles["value"] = "invisible"

    def handleConfirmClick() -> None:
        if not requiredField(window.manager, oldPasswordField, label="Old password"):
            return
        if not requiredField(window.manager, newPasswordField, label="New password"):
            return
        if not requiredField(
            window.manager, confirmNewPasswordField, label="Confirm new password"
        ):
            return

        oldPassword = oldPasswordField.value
        newPassword = newPasswordField.value
        confirmNewPassword = confirmNewPasswordField.value

        if session.user is None:
            return

        user = getOneUser(session.user.email)

        # DONE: Check if old password is correct and new password is valid and
        # match with confirm new password

        if newPassword == confirmNewPassword:

            if verify_password(oldPassword, user.password):

                # Update privateKey and publicKey
                newPrivateKey, newPublicKey = updatePassphrase(
                    user.privateKey, oldPassword, newPassword
                )

                # Update password

                updateUserKeys(
                    email=session.user.email,
                    publicKey=newPublicKey,
                    privateKey=newPrivateKey,
                )

                updateUserPassword(session.user.email, hash_password(newPassword))

                SuccessModal(
                    window.manager,
                    "Password changed successfully",
                    onclick=lambda *_: handleSuccessModalClose(window.manager),
                )

            else:
                ErrorModal(window.manager, "Old password is incorrect")

        else:
            ErrorModal(
                window.manager, "New password and confirm new password do not match"
            )

    window = ptg.Window(
        "",
        ptg.Label("Old password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(oldPasswordField),
        ptg.Label("New password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(newPasswordField),
        ptg.Label("Confirm new password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(confirmNewPasswordField),
        "",
        ptg.Splitter(
            # NOTE: We don't use window.close() because we want to keep track of
            # navigation and this is a page not a modal or an alert. We use
            # goToPrevPage to pop this page from the navigation stack.
            ptg.Button("Confirm", lambda *_: handleConfirmClick()),
            ptg.Button(
                "Cancel",
                debounce(lambda *_: goToPrevPage(window.manager), BUTTON_DEBOUNCE_TIME),
            ),
        ),
    )

    window.center()
    window.is_modal = True
    window.is_noresize = True
    # NOTE: overflow RESIZE doesn't play animation when window is opened.
    window.overflow = ptg.Overflow.RESIZE
    window.set_title(title="[window__title]Change password")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
