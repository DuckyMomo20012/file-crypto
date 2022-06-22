from typing import Optional

import pytermgui as ptg

import routes
import session
from src.api.auth.service import getOneUser
from src.api.file_crypto.service import deleteFile, getOneFile, updateFile
from src.components import ConfirmModal
from src.helpers.cryptography import decryptData, encryptData
from src.helpers.page_manager import drawPage, switchCurrPageWindowSlot
from src.types.Page import Page


def FilePreview(fileName: str, passphrase: str) -> Optional[Page]:

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

    contentField = ptg.InputField(fileContent, multiline=True)

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

        editedContent = "".join(contentField.value.split())

        if not editedContent == originalContent:
            window.manager.toast("File edited. Saving file...")
            # DONE: Update file on the database

            encryptedData = encryptData(
                user.publicKey, contentField.value.encode("utf-8")
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

    def handleCloseClick():

        switchCurrPageWindowSlot(
            window.manager,
            "body",
            clear=True,
        ),

    window = ptg.Window(
        ptg.Splitter(
            ptg.Label(fileName, parent_align=ptg.HorizontalAlignment.LEFT),
            ptg.Button("Delete", lambda *_: handleDeleteClick()),
            ptg.Button("Save", lambda *_: handleSaveClick()),
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
        contentField,
    )

    window.overflow = ptg.Overflow.SCROLL
    window.vertical_align = ptg.VerticalAlignment.TOP

    return {
        "layout": None,
        "windows": [{"window": window, "assign": "body"}],
    }
