import pytermgui as ptg

import routes
from src.api.auth.service import addUser, getOneUser
from src.components import ErrorModal, SuccessModal
from src.helpers.cryptography import generateUserKeys, hash_password
from src.helpers.form_validation import emailField as emailFieldValidator
from src.helpers.form_validation import requiredField
from src.helpers.page_manager import exitApp, switchPage
from src.types.Page import Page


def Register() -> Page:

    emailField = ptg.InputField()
    passwordField = ptg.InputField()
    passwordField.styles["value"] = "invisible"
    confirmPasswordField = ptg.InputField()
    confirmPasswordField.styles["value"] = "invisible"

    def handleSubmitClick() -> None:

        if not requiredField(window.manager, emailField, label="Email"):
            return
        if not requiredField(window.manager, passwordField, label="Password"):
            return
        if not requiredField(
            window.manager, confirmPasswordField, label="Confirm password"
        ):
            return

        if not emailFieldValidator(window.manager, emailField, label="Email"):
            return

        # DONE: Implement register logic
        # DONE: Validate email, password and confirm password
        email = emailField.value
        password = passwordField.value
        confirmPassword = confirmPasswordField.value

        if password == confirmPassword:

            user = getOneUser(email)

            if user:
                ErrorModal(window.manager, "Email already exists")
                return

            # NOTE: Should we use plain password as passphrase or hashed password?
            privateKey, publicKey = generateUserKeys(password)

            # Add new user to database
            addUser(
                email,
                hash_password(password),
                publicKey=publicKey,
                privateKey=privateKey,
            )

            SuccessModal(
                window.manager,
                "Register successful!",
                onclick=lambda *_: switchPage(
                    window.manager, routes.routes["auth/login"]()
                ),
            )
        else:
            ErrorModal(window.manager, "Password and confirm password do not match!")
            return

    window = ptg.Window(
        "",
        ptg.Splitter(
            ptg.Label("Already have an account?", size_policy=ptg.SizePolicy.STATIC),
            ptg.Button(
                "Sign in",
                lambda *_: switchPage(window.manager, routes.routes["auth/login"]()),
                parent_align=ptg.HorizontalAlignment.LEFT,
            ),
            parent_align=ptg.HorizontalAlignment.CENTER,
        ),
        "",
        ptg.Label("Email", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(emailField),
        ptg.Label("Password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(passwordField),
        ptg.Label("Confirm password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(confirmPasswordField),
        "",
        ptg.Splitter(
            ptg.Button("Register", lambda *_: handleSubmitClick()),
            ptg.Button("Exit", lambda *_: exitApp(window.manager)),
        ),
    )

    window.center()
    window.is_noresize = True
    window.overflow = ptg.Overflow.RESIZE
    window.set_title(title="Register")
    window.vertical_align = ptg.VerticalAlignment.TOP

    return {
        "layout": None,
        "windows": [
            {"window": window, "assign": ""},
        ],
    }
