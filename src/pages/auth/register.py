import pytermgui as ptg
from src.helpers.index import switchPage


def handleSuccessModalClose(window: ptg.Window, modal: ptg.Window) -> None:
    modal.close()
    switchPage(window.manager, window.manager.routes["auth/login"]())


def Register() -> ptg.Window:

    emailField = ptg.InputField()
    passwordField = ptg.InputField()
    passwordField.styles["value"] = "invisible"
    confirmPasswordField = ptg.InputField()
    confirmPasswordField.styles["value"] = "invisible"

    def handleSubmitClick() -> None:

        # TODO: Implement register logic
        # TODO: Validate email, password and confirm password
        email = emailField.value
        password = passwordField.value
        confirmPassword = confirmPasswordField.value

        if password == confirmPassword:
            alertModal = window.manager.alert(
                "Register successful!",
                "",
                ptg.Button(
                    "OK", lambda *_: handleSuccessModalClose(window, alertModal)
                ),
            )
        else:
            alertModal = window.manager.alert(
                "Register failed!",
                "",
                ptg.Button("OK", lambda *_: alertModal.close()),
            )

    window = ptg.Window(
        "",
        ptg.Splitter(
            ptg.Label("Already have an account?", size_policy=ptg.SizePolicy.STATIC),
            ptg.Button(
                "Sign in",
                lambda *_: switchPage(
                    window.manager, window.manager.routes["auth/login"]()
                ),
                parent_align=ptg.HorizontalAlignment.LEFT,
            ),
            chars={"separator": " "},
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
        ptg.Button("Register", lambda *_: handleSubmitClick()),
    )

    window.set_title(title="Register")
    window.overflow = ptg.Overflow.RESIZE
    window.vertical_align = ptg.VerticalAlignment.TOP
    window.center()
    window.is_noresize = True

    return {
        "layout": None,
        "windows": [
            {"window": window, "assign": ""},
        ],
    }
