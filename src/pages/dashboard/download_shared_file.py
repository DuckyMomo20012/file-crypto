import pytermgui as ptg

from src.helpers.index import goToPrevPage


def DownloadSharedFile():
    ownerEmailField = ptg.InputField()
    fileNameField = ptg.InputField()

    # TODO: Implement download shared file logic
    def handleDownloadClick():
        ownerEmail = ownerEmailField.value
        fileName = fileNameField.value
        window.manager.toast(f"Downloading {fileName}...")
        # ...

    window = ptg.Window(
        "",
        ptg.Label("Owner email", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(ownerEmailField),
        ptg.Label("File name", parent_align=ptg.HorizontalAlignment.LEFT),
        ptg.Container(fileNameField),
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
