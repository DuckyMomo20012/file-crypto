import pytermgui as ptg
from src.helpers.index import switchPage


def handleSuccessModalClose(window: ptg.Window, modal: ptg.Window) -> None:
    modal.close()
    switchPage(window, window.manager.routes["dashboard"]())


def Login() -> ptg.Window:

    # NOTE: When we use manager.add in app.py, manager it will assign window.manager to
    # itself, so we can access window.manager here.

    emailField = ptg.InputField()
    passwordField = ptg.InputField()
    passwordField.styles["value"] = "invisible"

    def handleSubmitClick() -> None:

        # TODO: Implement login logic
        # TODO: Validate email and password
        email = emailField.value
        password = passwordField.value

        if email == "admin" and password == "admin":
            alertModal = window.manager.alert(
                "Login successful!",
                ptg.Button(
                    "OK", lambda *_: handleSuccessModalClose(window, alertModal)
                ),
            )

        else:
            alertModal = window.manager.alert(
                "Login failed!",
                ptg.Button("OK", lambda *_: alertModal.close()),
            )

    window = ptg.Window(
        "",
        ptg.Splitter(
            ptg.Label(
                "Don't have an account?",
                size_policy=ptg.SizePolicy.STATIC,
            ),
            ptg.Button(
                "Sign up",
                lambda *_: switchPage(window, window.manager.routes["register"]()),
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
        ptg.Button("Login", lambda *_: handleSubmitClick()),
    )

    window.set_title(title="Login")
    window.overflow = ptg.Overflow.SCROLL
    window.vertical_align = ptg.VerticalAlignment.TOP
    window.center()

    return {
        "layout": None,
        "windows": [
            {"window": window, "assign": ""},
        ],
    }
