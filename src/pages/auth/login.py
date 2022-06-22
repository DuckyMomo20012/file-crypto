import pytermgui as ptg

import session
from src.api.auth.service import getOneUser
from src.components import ErrorModal, SuccessModal
from src.helpers.cryptography import verify_password
from src.helpers.form_validation import emailField as emailFieldValidator
from src.helpers.form_validation import requiredField
from src.helpers.page_manager import exitApp, switchPage


def handleSuccessModalClose(window: ptg.Window, modal: ptg.Window) -> None:
    modal.close()
    switchPage(window.manager, window.manager.routes["dashboard"]())


def Login():

    # NOTE: When we use manager.add in app.py, manager it will assign
    # window.manager to itself, so we can access window.manager here.

    emailField = ptg.InputField()
    passwordField = ptg.InputField()
    passwordField.styles["value"] = "invisible"

    def handleSubmitClick() -> None:

        if not requiredField(window.manager, emailField, label="Email"):
            return
        if not requiredField(window.manager, passwordField, label="Password"):
            return

        if not emailFieldValidator(window.manager, emailField, label="Email"):
            return

        # TODO: Implement login logic
        # TODO: Validate email and password
        email = emailField.value
        password = passwordField.value

        user = getOneUser(email)

        if user and verify_password(password, user.password):
            SuccessModal(
                window.manager,
                "Login successful!",
                onclick=lambda *_: switchPage(
                    window.manager, window.manager.routes["dashboard"]()
                ),
            )

            # NOTE: We store user to session here
            session.user = user

        else:
            ErrorModal(window.manager, "Invalid email or password")

    window = ptg.Window(
        "",
        ptg.Splitter(
            ptg.Label(
                "Don't have an account?",
                size_policy=ptg.SizePolicy.STATIC,
            ),
            ptg.Button(
                "Sign up",
                lambda *_: switchPage(
                    window.manager, window.manager.routes["auth/register"]()
                ),
                parent_align=ptg.HorizontalAlignment.LEFT,
            ),
            parent_align=ptg.HorizontalAlignment.CENTER,
        ),
        "",
        ptg.Label("Email", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(emailField),
        ptg.Label("Password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(passwordField),
        "",
        ptg.Splitter(
            ptg.Button("Login", lambda *_: handleSubmitClick()),
            ptg.Button("Exit", lambda *_: exitApp(window.manager)),
        ),
    )

    window.center()
    window.is_noresize = True
    window.overflow = ptg.Overflow.RESIZE
    window.set_title(title="[window__title]Login")
    window.vertical_align = ptg.VerticalAlignment.TOP

    return {
        "layout": None,
        "windows": [
            {"window": window, "assign": ""},
        ],
    }
