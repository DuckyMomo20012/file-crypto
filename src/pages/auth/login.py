import pytermgui as ptg


def Login(manager: ptg.WindowManager) -> ptg.Window:

    emailField = ptg.InputField()
    passwordField = ptg.InputField()
    passwordField.styles["value"] = "invisible"

    def handleSubmitClick() -> None:

        # TODO: Implement login logic
        email = emailField.value
        password = passwordField.value

        if email == "admin" and password == "admin":
            alertModal = manager.alert(
                "Login successful!",
                ptg.Button("OK", lambda *_: manager.remove(alertModal)),
            )
        else:
            alertModal = manager.alert(
                "Login failed!",
                ptg.Button("OK", lambda *_: manager.remove(alertModal)),
            )

    window = ptg.Window(
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

    return window
