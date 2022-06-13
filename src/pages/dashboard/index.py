import pytermgui as ptg

from src.components.layouts.AppShell import AppShell

# TODO: Implement this function to fetch data from the database and return
# format like this
# NOTE: Any suggestions for a better way to do this?
def getFiles():

    # NOTE: Date can have different formats, but recommend using YYYY-MM-DD or
    # DD-MM-YYYY, with a "-" or "/" as a separator
    return {
        "2020-01-01": ["file1", "file2", "file3"],
        "2020-01-02": ["file1", "file2", "file3"],
        "2020-01-03": ["file1", "file2", "file3"],
        "2020-01-04": ["file1", "file2", "file3"],
        "2020-01-05": ["file1", "file2", "file3"],
    }


# TODO: Implement upload logic
def uploadFile(window, modal, filePathField):
    # Open file from filePathField and upload it to the server

    window.manager.toast(f"Uploading {filePathField}...")
    modal.close()


def DashBoard() -> None:
    def handleUploadClick():

        filePathField = ptg.InputField()

        uploadModal = navBar.manager.alert(
            "File path",
            ptg.Container(filePathField),
            ptg.Splitter(
                ptg.Button("Cancel", lambda *_: uploadModal.close()),
                ptg.Button(
                    "Upload",
                    lambda *_: uploadFile(navBar, uploadModal, filePathField.value),
                ),
            ),
            is_noresize=True,
        )

    files = getFiles()

    header = ptg.Window(
        "Dashboard",
        box="EMPTY",
        is_persistant=True,
    )

    body = ptg.Window("Empty body")
    body.is_static = True
    body.is_noresize = True
    body.vertical_align = ptg.VerticalAlignment.TOP

    navBar = ptg.Window(
        ptg.Button(
            "Upload",
            lambda *_: handleUploadClick(),
            parent_align=ptg.HorizontalAlignment.CENTER,
        ),
        "",
        *[
            ptg.Collapsible(
                dates,
                *[
                    ptg.Label(
                        fileName, parent_align=ptg.HorizontalAlignment.LEFT, padding=1
                    )
                    for fileName in files[dates]
                ],
                parent_align=ptg.HorizontalAlignment.LEFT,
                size_policy=ptg.SizePolicy.STATIC,
                # FIXME: Don't hardcode this width
                width=14,  # Total size for date is 14 blocks
            )
            for dates in files.keys()
        ],
    )
    navBar.is_static = True
    navBar.is_noresize = True
    navBar.vertical_align = ptg.VerticalAlignment.TOP
    navBar.overflow = ptg.Overflow.SCROLL
    return {
        "layout": AppShell(),
        "windows": [
            {"window": header, "assign": "header"},
            {"window": body, "assign": "body"},
            {"window": navBar, "assign": "nav_bar"},
        ],
    }
