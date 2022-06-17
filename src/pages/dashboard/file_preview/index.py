import pytermgui as ptg

from src.helpers.index import drawPage, switchCurrPageWindowSlot


def FilePreview(fileName: str, fileContent: str):

    contentField = ptg.InputField(fileContent, multiline=True)

    # TODO: Implement this function to encrypt the file content and then update
    # file on the database
    def handleSaveClick():

        # NOTE: We remove whitespace from the edited content and original
        # content to check changes. So, if file was edited with "newlines",
        # "tabs" or "whitespace" will result in no changes.

        # NOTE: Why? Because "InputField" will join all lines with a newline on
        # window resize. So, we can't compare directly the edited content with
        # the original content.
        originalContent = "".join(fileContent.split())

        editedContent = "".join(contentField.value.split())

        if not editedContent == originalContent:
            window.manager.toast("File edited. Saving file...")
            # TODO: Update file on the database

            # ...

            handleCloseClick()
        else:
            window.manager.toast("No changes made.")

    def handleCloseClick():

        switchCurrPageWindowSlot(
            window.manager,
            "body",
            clear=True,
        ),

    window = ptg.Window(
        ptg.Splitter(
            ptg.Label(fileName, parent_align=ptg.HorizontalAlignment.LEFT),
            ptg.Button("Save", lambda *_: handleSaveClick()),
            ptg.Button(
                "Download",
                lambda *_: drawPage(
                    window.manager,
                    window.manager.routes["dashboard/file_preview/download_file"](
                        fileName
                    ),
                ),
            ),
            ptg.Button(
                "Close",
                lambda *_: handleCloseClick(),
                parent_align=ptg.HorizontalAlignment.RIGHT,
            ),
        ),
        "",
        contentField,
    )

    window.overflow = ptg.Overflow.SCROLL
    window.vertical_align = ptg.VerticalAlignment.TOP

    return {
        "layout": None,
        "windows": [{"window": window, "assign": "body"}],
    }
