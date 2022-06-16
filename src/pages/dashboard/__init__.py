from .index import DashBoard
from .settings.index import Settings
from .settings.change_password.index import ChangePassword
from .settings.your_information.index import YourInformation
from .settings.your_information.edit.index import EditInformation
from .upload_file import UploadFile
from .file_preview.index import FilePreview

__all__ = [
    "DashBoard",
    "Settings",
    "ChangePassword",
    "YourInformation",
    "EditInformation",
    "UploadFile",
    "FilePreview",
]
