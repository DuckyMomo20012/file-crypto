import pytermgui as ptg


def Register(manager: ptg.WindowManager) -> ptg.Window:

    emailField = ptg.InputField()
    passwordField = ptg.InputField()
    confirmPasswordField = ptg.InputField()

    print(emailField.chars)

    def handleSubmitClick() -> None:

        # TODO: Implement register logic
        email = emailField.value
        password = passwordField.value
        confirmPassword = confirmPasswordField.value

        if password == confirmPassword:
            alertModal = manager.alert(
                "Register successful!",
                ptg.Button("OK", lambda *_: manager.remove(alertModal)),
            )
        else:
            alertModal = manager.alert(
                "Register failed!",
                ptg.Button("OK", lambda *_: manager.remove(alertModal)),
            )

    window = ptg.Window(
        "",
        ptg.Label("Email", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(emailField),
        ptg.Label("Password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(passwordField),
        ptg.Label("Confirm password", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(confirmPasswordField),
        ptg.Button("Register", lambda *_: handleSubmitClick()),
    )

    window.set_title(title="Register")
    window.overflow = ptg.Overflow.SCROLL
    window.vertical_align = ptg.VerticalAlignment.TOP
    window.center()

    return window
