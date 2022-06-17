import pytermgui as ptg

from src.helpers.index import goToPrevPage
from src.helpers.form_validation import requiredField, fileField


def SignFile():
    filePathField = ptg.InputField()
    saveFolderPathField = ptg.InputField()

    # TODO: Implement sign file logic
    def handleSignClick():
        if not requiredField(window.manager, filePathField, label="File path"):
            return
        if not requiredField(
            window.manager, saveFolderPathField, label="Save folder path"
        ):
            return

        if not fileField(window.manager, filePathField, label="File path"):
            return

        # NOTE: Remember to check if this is a valid folder & file directory
        filePath = filePathField.value
        saveFolderPath = saveFolderPathField.value

        window.manager.toast(f"Downloading {filePath}...")
        # ...

        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label("File path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(filePathField),
        ptg.Label("Save folder path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(saveFolderPathField),
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
