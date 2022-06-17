import pytermgui as ptg

from src.helpers.index import goToPrevPage
from src.helpers.form_validation import requiredField


def DownloadSharedFile():
    ownerEmailField = ptg.InputField()
    fileNameField = ptg.InputField()
    saveLocationField = ptg.InputField()

    # TODO: Implement download shared file logic
    def handleDownloadClick():
        if not requiredField(window.manager, ownerEmailField, label="Owner email"):
            return
        if not requiredField(window.manager, fileNameField, label="File name"):
            return
        if not requiredField(
            window.manager, saveLocationField, label="Save folder location"
        ):
            return

        ownerEmail = ownerEmailField.value
        fileName = fileNameField.value

        # NOTE: Remember to check if this is a valid folder directory
        saveLocation = saveLocationField.value

        window.manager.toast(f"Downloading {fileName}...")
        # ...

        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label("Owner email", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(ownerEmailField),
        ptg.Label("File name", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(fileNameField),
        ptg.Label("Save folder location", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(saveLocationField),
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
