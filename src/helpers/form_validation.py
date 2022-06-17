import pytermgui as ptg


def requiredField(manager: ptg.WindowManager, field: ptg.InputField, label: str):
    if len(field.value) == 0:
        errorMsg = f"{label} field is required"
        manager.routes["errors/form_validation_error"](manager, errorMsg)
        return False

    return True
