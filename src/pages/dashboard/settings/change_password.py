import pytermgui as ptg

from src.helpers.index import goToPrevPage, clearNavigation, drawPage
from src.helpers.form_validation import requiredField
from src.components import SuccessModal, ErrorModal

import config

from src.api.auth.service import getOneUser, updateUserKeys, updateUserPassword

from src.helpers.cryptography import updatePassphrase, verify_password, hash_password


def handleSuccessModalClose(manager: ptg.WindowManager) -> None:

    manager.toast("Logging out...")
    clearNavigation(manager)
    drawPage(manager, manager.routes["auth/login"]())


def ChangePassword():

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

        user = getOneUser(config.session.email)

        # TODO: Check if old password is correct and new password is valid and
        # match with confirm new password

        if newPassword == confirmNewPassword:

            if verify_password(oldPassword, user.password):

                # Update privateKey and publicKey
                newPrivateKey, newPublicKey = updatePassphrase(
                    user.privateKey, oldPassword, newPassword
                )

                # Update password

                updateUserKeys(
                    email=config.session.email,
                    publicKey=newPublicKey,
                    privateKey=newPrivateKey,
                )

                updateUserPassword(config.session.email, hash_password(newPassword))

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
            # navigation and this is a page not a modal or an alert. We use goToPrevPage to
            # pop this page from the navigation stack.
            ptg.Button("Cancel", lambda *_: goToPrevPage(window.manager)),
            ptg.Button("Confirm", lambda *_: handleConfirmClick()),
        ),
    )

    window.set_title(title="Change password")
    # NOTE: overflow RESIZE doesn't play animation when window is opened.
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
