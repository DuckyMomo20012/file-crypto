import pytermgui as ptg


def downloadFile(fileName):
    pass


def FilePreview(fileName: str):

    window = ptg.Window(
        ptg.Splitter(
            ptg.Label(fileName, parent_align=ptg.HorizontalAlignment.LEFT),
            ptg.Button(
                "Close", lambda *_: None, parent_align=ptg.HorizontalAlignment.RIGHT
            ),
        ),
    )

    window.is_static = True
    window.is_noresize = True
    window.vertical_align = ptg.VerticalAlignment.TOP

    return {
        "layout": None,
        "windows": [{"window": window, "assign": "body"}],
    }
