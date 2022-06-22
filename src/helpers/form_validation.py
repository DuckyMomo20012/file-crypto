import re
from datetime import datetime
from pathlib import Path

import pytermgui as ptg

from src.components.modules import ErrorModal


def requiredField(manager: ptg.WindowManager, field: ptg.InputField, label: str):
    if len(field.value) == 0:
        errorMsg = f"{label} field is required"
        ErrorModal(manager, errorMsg)
        return False

    return True


def fileField(manager: ptg.WindowManager, field: ptg.InputField, label: str):

    filePath = Path(field.value)

    # NOTE: This function supports both absolute and relative file paths
    # E.g:
    # - src/pages/routes.py
    # - ./src/__init__.py
    # - /home/alice/Desktop/file-crypto/app.py
    if not filePath.is_file():
        errorMsg = f"{label} field is not a valid file path"
        ErrorModal(manager, errorMsg)
        return False

    return True


def folderField(manager: ptg.WindowManager, field: ptg.InputField, label: str):

    filePath = Path(field.value)

    # NOTE: This function supports both absolute and relative folder paths
    # E.g:
    # - src/pages/
    # - ./
    # - ../
    # - ./../
    # - /home/alice/Desktop/file-crypto
    # - /home/alice/Desktop/file-crypto/
    if not filePath.is_dir():
        errorMsg = f"{label} field is not a valid folder path"
        ErrorModal(manager, errorMsg)
        return False

    return True


def emailField(manager: ptg.WindowManager, field: ptg.InputField, label: str):
    # NOTE: Ref: https://stackoverflow.com/a/66809700/12512981

    email_format = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    email = field.value

    if not re.match(email_format, email, re.IGNORECASE):
        errorMsg = f"{label} field is not a valid email address"
        ErrorModal(manager, errorMsg)
        return False

    return True


def dateField(manager: ptg.WindowManager, field: ptg.InputField, label: str):
    # NOTE: Ref: https://stackoverflow.com/a/37045601/12512981

    try:
        dateString = field.value

        if dateString != datetime.strptime(dateString, "%Y-%m-%d").strftime("%Y-%m-%d"):
            raise ValueError
        return True
    except ValueError:
        errorMsg = f"{label} field is not a valid date"
        ErrorModal(manager, errorMsg)
        return False
