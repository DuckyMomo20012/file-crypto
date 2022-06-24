import pytermgui as ptg

from src.helpers.form_validation import folderField, requiredField
from src.helpers.page_manager import goToPrevPage
from src.types.Page import Page


def DownloadSharedFile() -> Page:
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

        if not folderField(
            window.manager, saveFolderPathField, label="Save folder path"
        ):
            return

        ownerEmail = ownerEmailField.value  # noqa
        fileName = fileNameField.value

        # NOTE: Remember to check if this is a valid folder directory
        saveFolderPath = saveFolderPathField.value  # noqa

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
            ptg.Button(
                "Download",
                lambda *_: handleDownloadClick(),
            ),
            ptg.Button("Cancel", lambda *_: goToPrevPage(window.manager)),
        ),
    )

    window.center()
    window.is_modal = True
    window.is_noresize = True
    window.overflow = ptg.Overflow.RESIZE
    window.set_title("[window__title]Download shared file")

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
