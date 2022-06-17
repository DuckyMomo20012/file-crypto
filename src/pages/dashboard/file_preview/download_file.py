import pytermgui as ptg

from src.helpers.index import goToPrevPage
from src.helpers.form_validation import requiredField, folderField


def DownloadFile(fileName: str):
    saveFolderPathField = ptg.InputField()

    # TODO: Implement download file logic
    def handleDownloadClick():
        if not requiredField(
            window.manager, saveFolderPathField, label="Save folder path"
        ):
            return

        if not folderField(
            window.manager, saveFolderPathField, label="Save folder path"
        ):
            return

        # fileName = ...

        # NOTE: Remember to check if this is a valid folder directory
        saveFolderPath = saveFolderPathField.value

        window.manager.toast(f"Downloading {fileName}...")
        # ...

        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label("Save folder path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(saveFolderPathField),
        "",
        ptg.Splitter(
            ptg.Button("Cancel", lambda *_: goToPrevPage(window.manager)),
            ptg.Button(
                "Download",
                lambda *_: handleDownloadClick(),
            ),
        ),
    )

    window.set_title("Download file")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
