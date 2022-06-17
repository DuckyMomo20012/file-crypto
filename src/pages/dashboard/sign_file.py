import pytermgui as ptg

from src.helpers.index import goToPrevPage


def SignFile():
    fileLocationField = ptg.InputField()
    saveLocationField = ptg.InputField()

    # TODO: Implement sign file logic
    def handleSignClick():
        # NOTE: Remember to check if this is a valid folder & file directory
        fileLocation = fileLocationField.value
        saveLocation = saveLocationField.value

        window.manager.toast(f"Downloading {fileLocation}...")
        # ...

        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label("File location", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(fileLocationField),
        ptg.Label("Save folder location", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(saveLocationField),
        "",
        ptg.Splitter(
            ptg.Button("Cancel", lambda *_: goToPrevPage(window.manager)),
            ptg.Button(
                "Sign file",
                lambda *_: handleSignClick(),
            ),
        ),
    )

    window.set_title("Sign you file")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
