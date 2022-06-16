import pytermgui as ptg

from src.helpers.index import goToPrevPage


def UploadFile():

    filePathField = ptg.InputField()

    def handleUploadClick():
        filePath = filePathField.value
        window.manager.toast(f"Uploading {filePath}...")

        # TODO: Implement upload logic

        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
        ptg.Label("File path", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(filePathField),
        "",
        ptg.Splitter(
            ptg.Button("Cancel", lambda *_: goToPrevPage(window.manager)),
            ptg.Button(
                "Upload",
                lambda *_: handleUploadClick(),
            ),
        ),
    )

    window.set_title(title="Upload file")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
