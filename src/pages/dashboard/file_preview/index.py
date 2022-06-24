from functools import partial
from typing import Optional

import pytermgui as ptg
from pygments.styles import STYLE_MAP  # type: ignore

import routes
import session
from src.api.auth.service import getOneUser
from src.api.file_crypto.service import deleteFile, getOneFile, updateFile
from src.components import ConfirmModal
from src.helpers.cryptography import decryptData, encryptData
from src.helpers.highlight import syntaxHighlight
from src.helpers.page_manager import drawPage, switchCurrPageWindowSlot
from src.types.Page import Page


# NOTE: Currently we just can switch between "edit" mode and "preview" mode.
# I added a function to remove highlight from the code, it works but in the
# InputField, we CAN'T edit the highlighted content, it will throw errors on
# edit.
def FilePreview(
    fileName: str, passphrase: str, preview: bool = False, theme: str = "dracula"
) -> Optional[Page]:

    if session.user is None:
        return None

    user = getOneUser(session.user.email)

    file = getOneFile(user.email, fileName)

    if file is None:
        return None

    decryptedData = decryptData(
        privateKey=user.privateKey,
        # FIXME: Hardcoded passphrase for testing
        passphrase=passphrase,
        encryptedSessionKey=file.sessionKey,
        nonce=file.nonce,
        tag=file.tag,
        cipherText=file.cipher.read(),
    )

    fileContent = decryptedData if decryptedData is not None else ""

    editContentField = ptg.InputField(fileContent, multiline=True)
    # NOTE: We can use this way to add syntax highlight to the code when
    # editing. But the performance is EXTREMELY slow.
    # editContentField.styles.value = lambda _, text: ptg.tim.parse(
    #     syntaxHighlight(fileName, text, theme)
    # )

    previewContentField = ptg.Label(syntaxHighlight(fileName, fileContent, theme))
    previewContentField.parent_align = ptg.HorizontalAlignment.LEFT

    def handleDeleteClick():
        def handleConfirmDeleteClick():
            try:
                deleteFile(user.email, fileName)
            except AttributeError:
                pass
            finally:
                # Close the file preview window by swapping with empty window
                handleCloseClick()
                # Clear nav bar window
                switchCurrPageWindowSlot(window.manager, "nav_bar", clear=True)
                # And redraw the dashboard page
                drawPage(window.manager, routes.routes["dashboard"]())

        ConfirmModal(
            window.manager,
            "Are you sure you want to delete this file?",
            confirmOnClick=lambda *_: handleConfirmDeleteClick(),
            cancelOnClick=lambda *_: None,
        )

    # DONE: Implement this function to encrypt the file content and then update
    # file on the database
    def handleSaveClick():

        # NOTE: We remove whitespace from the edited content and original
        # content to check changes. So, if file was edited with "newlines",
        # "tabs" or "whitespace" will result in no changes.

        # NOTE: Why? Because "InputField" will join all lines with a newline on
        # window resize. So, we can't compare directly the edited content with
        # the original content.
        originalContent = "".join(fileContent.split())

        editedContent = "".join(editContentField.value.split())

        if not editedContent == originalContent:
            window.manager.toast("File edited. Saving file...")
            # DONE: Update file on the database

            encryptedData = encryptData(
                user.publicKey, editContentField.value.encode("utf-8")
            )

            if encryptedData:
                encryptedSessionKey, nonce, tag, cipherText = encryptedData

                updateFile(
                    user.email, fileName, encryptedSessionKey, nonce, tag, cipherText
                )

                window.manager.toast("File saved successfully!")

            else:
                window.manager.toast("Failed to save file!")

            handleCloseClick()
        else:
            window.manager.toast("No changes made.")

    def handleModeButtonClick():

        # Toggle between edit and preview mode
        switchCurrPageWindowSlot(
            manager=window.manager,
            targetAssign=("body"),
            newWindow=routes.routes["dashboard/file_preview"](
                fileName=fileName, passphrase=passphrase, preview=not preview
            ),
        )

    def handleCloseClick():

        switchCurrPageWindowSlot(
            window.manager,
            "body",
            clear=True,
        ),

    # NOTE: onclick function will pass Button itself as a first argument and we
    # don't care about it, so we add a dummy argument "args" to the function to
    # "absorb" it.
    def handleThemeButtonClick(*args, theme: str):

        switchCurrPageWindowSlot(
            manager=window.manager,
            targetAssign=("body"),
            newWindow=routes.routes["dashboard/file_preview"](
                fileName=fileName, passphrase=passphrase, preview=preview, theme=theme
            ),
        )

    # Some themes cause error on printing the content, so we have blacklist them
    themes = [
        theme
        for theme in list(STYLE_MAP.keys())
        if theme not in ("borland", "lilypond", "trac", "bw", "algol", "algol_nu")
    ]

    # NOTE: We CAN'T pass function correctly when we are in loop. Instead, we
    # use partial to "bind" the arguments to the function.
    themeButtons = [
        ptg.Button(theme, partial(handleThemeButtonClick, theme=theme))
        for theme in themes
    ]

    # NOTE: We can swap between Save button and ThemeMenu to save space

    # We only show the theme buttons if we are in preview mode
    themeMenu = ptg.Collapsible(
        "Theme",
        ptg.Container(
            *themeButtons,
            height=5,
            width=20,
            overflow=ptg.Overflow.SCROLL,
            parent_align=ptg.HorizontalAlignment.LEFT,
        ),
    )

    # In preview mode, we don't show the save button
    saveButton = ptg.Button("Save", lambda *_: handleSaveClick())

    functionButton = themeMenu if preview else saveButton

    # File content window slot will dynamically change depending on the mode
    fileContentSlot = editContentField if not preview else previewContentField

    # Also, the mode button will change between "Preview" and "Edit"
    modeButton = ptg.Button(
        "Preview mode" if not preview else "Edit mode",
        lambda *_: handleModeButtonClick(),
    )

    window = ptg.Window(
        "",
        ptg.Splitter(
            modeButton,
            functionButton,
            ptg.Button("Delete", lambda *_: handleDeleteClick()),
            ptg.Button(
                "Download",
                lambda *_: drawPage(
                    window.manager,
                    routes.routes["dashboard/file_preview/download_file"](fileName),
                ),
            ),
            ptg.Button(
                "Close",
                lambda *_: handleCloseClick(),
                parent_align=ptg.HorizontalAlignment.RIGHT,
            ),
        ),
        "",
        fileContentSlot,
    )

    window.overflow = ptg.Overflow.SCROLL
    window.set_title(f"[window__title]{fileName}")
    window.vertical_align = ptg.VerticalAlignment.TOP

    return {
        "layout": None,
        "windows": [{"window": window, "assign": "body"}],
    }
