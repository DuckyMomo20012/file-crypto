import pytermgui as ptg

from src.helpers.index import switchCurrPageWindowSlot

# TODO: Implement download functionality
def downloadFile(fileName):
    pass


def FilePreview(fileName: str):

    window = ptg.Window(
        ptg.Splitter(
            ptg.Label(fileName, parent_align=ptg.HorizontalAlignment.LEFT),
            ptg.Button(
                "Download",
                lambda *_: downloadFile(fileName),
            ),
            ptg.Button(
                "Close",
                lambda *_: switchCurrPageWindowSlot(
                    window.manager,
                    "body",
                    clear=True,
                ),
                parent_align=ptg.HorizontalAlignment.RIGHT,
            ),
        ),
    )

    window.vertical_align = ptg.VerticalAlignment.TOP

    return {
        "layout": None,
        "windows": [{"window": window, "assign": "body"}],
    }
