import pytermgui as ptg

from src.helpers.index import goToPrevPage


def DownloadFile(fileName: str):
    saveLocationField = ptg.InputField()

    # TODO: Implement download file logic
    def handleDownloadClick():
        # fileName = ...

        # NOTE: Remember to check if this is a valid folder directory
        saveLocation = saveLocationField.value

        window.manager.toast(f"Downloading {fileName}...")
        # ...

        goToPrevPage(window.manager)

    window = ptg.Window(
        "",
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

    window.set_title("Download file")
    window.overflow = ptg.Overflow.RESIZE
    window.center()
    window.is_noresize = True
    window.is_modal = True

    return {
        "layout": None,
        "windows": [{"window": window, "assign": ""}],
    }
