import pytermgui as ptg

from src.helpers.index import goToPrevPage
from src.helpers.form_validation import requiredField


def DownloadSharedFile():
    ownerEmailField = ptg.InputField()
    fileNameField = ptg.InputField()
    saveFolderPathField = ptg.InputField()

    # TODO: Implement download shared file logic
    def handleDownloadClick():
        if not requiredField(window.manager, ownerEmailField, label="Owner email"):
            return
        if not requiredField(window.manager, fileNameField, label="File name"):
            return
        if not requiredField(
            window.manager, saveFolderPathField, label="Save folder path"
        ):
            return

        ownerEmail = ownerEmailField.value
        fileName = fileNameField.value

        # NOTE: Remember to check if this is a valid folder directory
        saveFolderPath = saveFolderPathField.value

        window.manager.toast(f"Downloading {fileName}...")
        # ...

        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label("Owner email", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(ownerEmailField),
        ptg.Label("File name", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(fileNameField),
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

    window.set_title("Download shared file")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
