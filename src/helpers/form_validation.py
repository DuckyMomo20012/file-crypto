import pytermgui as ptg


def requiredField(manager: ptg.WindowManager, field: ptg.InputField, label: str):
    if len(field.value) == 0:
        errorMsg = f"{label} field is required"
        manager.routes["errors/form_validation_error"](manager, errorMsg)
        return False

    return True


def fileField(manager: ptg.WindowManager, field: ptg.InputField, label: str):
    from pathlib import Path

    filePath = Path(field.value)

    # NOTE: This function supports both absolute and relative file paths
    # E.g:
    # - src/pages/routes.py
    # - ./src/__init__.py
    # - /home/alice/Desktop/file-crypto/app.py
    if not filePath.is_file():
        errorMsg = f"{label} field is not a valid file path"
        manager.routes["errors/form_validation_error"](manager, errorMsg)
        return False

    return True
