from typing import Optional

import magic
import pytermgui as ptg

import routes
import session
from src.api.auth.service import getOneUser
from src.api.file_crypto.service import deleteFile, getOneFile, updateFile
from src.components import ConfirmModal, Footer
from src.constants import (
    DEFAULT_PREVIEW_THEME,
    IMAGE_PREVIEW_PADDING,
    IMAGE_PREVIEW_WIDTH,
)
from src.helpers.climage import convert_frombytes
from src.helpers.cryptography import decryptData, encryptData
from src.helpers.file import getSettingField
from src.helpers.highlight import syntaxHighlight
from src.helpers.page_manager import drawPage, switchCurrPageWindowSlot
from src.types.Page import Page, PageWindows

unsupportedEncoding = (
    ptg.Label(
        "[window__title--warning]Warning: The file is not displayed"
        " because it is either binary or uses an unsupported text"
        " encoding.",
    ),
)

unsupportedSyntaxHighlighting = (
    ptg.Label(
        "[window__title--error]Error: Syntax highlight is not"
        " supported for this file type. Please switch to 'no theme'"
        " theme to remove this line.",
        parent_align=ptg.HorizontalAlignment.LEFT,
    ),
)

previewFeatureWarning = (
    "[window__title--warning]Warning: Image preview in ANSI is"
    " preview feature. It may downgrade the performance."
)


# NOTE: Currently we just can switch between "edit" mode and "preview" mode.
# I added a function to remove highlight from the code, it works but in the
# InputField, we CAN'T edit the highlighted content, it will throw errors on
# edit.
def FilePreview(
    fileName: str,
    passphrase: str,
    preview: bool = False,
    theme: str = DEFAULT_PREVIEW_THEME,
    forcePreview: bool = False,
) -> Optional[Page]:

    defaultTheme = getSettingField("workbench.colorTheme")
    if defaultTheme is not None:
        theme = defaultTheme

    # NOTE: We create empty window slots so we can dynamically insert footer
    windowSlots = []

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
        # Clear file preview windows
        switchCurrPageWindowSlot(
            window.manager,
            "body",
            clear=True,
        ),
        # Clear footer windows
        switchCurrPageWindowSlot(
            window.manager,
            "footer",
            clear=True,
        ),

    def handleThemeButtonClick():

        drawPage(
            window.manager,
            routes.routes["dashboard/file_preview/theme_picker"](
                fileName=fileName,
                passphrase=passphrase,
                preview=preview,
                currTheme=theme,
            ),
        )

    # We only show the theme buttons if we are in preview mode
    themeMenu = ptg.Button("Theme", lambda *_: handleThemeButtonClick())

    # In preview mode, we don't show the save button
    saveButton = ptg.Button("Save", lambda *_: handleSaveClick())

    functionButton = themeMenu if preview else saveButton

    # Also, the mode button will change between "Preview" and "Edit"
    modeButton = ptg.Button(
        "Preview mode" if not preview else "Edit mode",
        lambda *_: handleModeButtonClick(),
    )

    windowWidgets = [
        "",
        ptg.Splitter(
            ptg.Button(
                "i",
                lambda *_: drawPage(
                    window.manager,
                    routes.routes["dashboard/file_preview/file_information"](fileName),
                ),
            ),
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
    ]

    def getPreviewField():
        # Plain text preview content
        previewContentField = ptg.Label(fileContent)
        previewContentField.parent_align = ptg.HorizontalAlignment.LEFT
        if theme != "no theme":
            highlightPreviewContent = syntaxHighlight(fileName, fileContent, theme)
            if highlightPreviewContent is not None:
                previewContentField = ptg.Label(highlightPreviewContent)
                previewContentField.parent_align = ptg.HorizontalAlignment.LEFT
            # NOTE: We can add a button label "OK" here, after the error message to
            # switch to 'no theme' theme.
            else:
                windowWidgets.insert(0, unsupportedSyntaxHighlighting)
        return previewContentField

    # A flag to check image preview is opened. If it is, we set min width to
    # reserve image preview space.
    imageForcePreview = False

    # NOTE: You can use command "file app.py" (libmagic) on Unix OS to check
    # file type.
    fileType = magic.from_buffer(fileContent)

    if "text" in fileType and isinstance(fileContent, str):
        if preview:
            previewContentField = getPreviewField()
            windowWidgets.append(previewContentField)
        else:
            editContentField = ptg.InputField(str(fileContent), multiline=True)
            # NOTE: We can use this way to add syntax highlight to the code when
            # editing. But the performance is EXTREMELY slow.
            # editContentField.styles.value = lambda _, text: ptg.tim.parse(
            #     syntaxHighlight(fileName, text, theme)
            # )

            # We create a footer to track cursor and selection length
            footer = Footer(inputField=editContentField)

            # NOTE: We dynamically add the footer to the window slots
            windowSlots.append(PageWindows(window=footer, assign="footer"))

            # Append edit content field to the window widgets
            windowWidgets.append(editContentField)

    elif "image" in fileType and isinstance(fileContent, bytes):
        if preview:
            if forcePreview:
                # NOTE: ANSI image preview feature is extremely slow.
                imageForcePreview = True
                previewContentField = (
                    ptg.Label(
                        convert_frombytes(
                            fileContent,
                            is_truecolor=True,
                            is_256color=False,
                            is_unicode=True,
                            width=IMAGE_PREVIEW_WIDTH,
                        ),
                    ),
                )
                windowWidgets.append(previewContentField)
            else:
                # We print a warning message to warn the user about the preview
                # (beta) feature
                previewContentField = [
                    previewFeatureWarning,
                    "",
                    ptg.Button(
                        "Preview anyway",
                        lambda *_: switchCurrPageWindowSlot(
                            manager=window.manager,
                            targetAssign=("body"),
                            newWindow=routes.routes["dashboard/file_preview"](
                                fileName=fileName,
                                passphrase=passphrase,
                                preview=preview,
                                theme=theme,
                                forcePreview=True,
                            ),
                        ),
                    ),
                ]
                windowWidgets.extend(previewContentField)
    else:
        windowWidgets.append(unsupportedEncoding)

    # NOTE: We spread those widgets here, so we can dynamically insert widget to
    # this window
    window = ptg.Window(*windowWidgets)

    # NOTE: Set window min width so when user resize window, the image won't be
    # broken. Except the terminal size is too small.
    if imageForcePreview:
        window.min_width = IMAGE_PREVIEW_WIDTH + IMAGE_PREVIEW_PADDING * 2

    window.overflow = ptg.Overflow.SCROLL
    window.set_title(
        f"[window__title]{fileName}[/window__title]"
        f' [italic nord15]{"(Preview mode)" if preview else "(Edit mode)"}'
    )
    window.vertical_align = ptg.VerticalAlignment.TOP

    windowSlots.append(PageWindows(window=window, assign="body"))

    return {
        "layout": None,
        "windows": windowSlots,
    }
