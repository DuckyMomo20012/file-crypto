# flake8: noqa
from typing import Callable, Optional

from src.pages.auth import Login, Logout, Register  # type: ignore
from src.pages.dashboard import (  # type: ignore
    ChangePassword,
    DashBoard,
    DecryptFile,
    DownloadFile,
    DownloadSharedFile,
    EditInformation,
    EncryptFile,
    FilePreview,
    PasswordPrompt,
    Settings,
    SignFile,
    Tools,
    UploadFile,
    VerifySignedFile,
    YourInformation,
)
from src.types.Page import Page

routes: dict[str, Callable[..., Optional[Page]]] = {
    "auth/login": Login,
    "auth/register": Register,
    "auth/logout": Logout,
    "dashboard": DashBoard,
    "dashboard/settings": Settings,
    "dashboard/settings/change_password": ChangePassword,
    "dashboard/settings/your_information": YourInformation,
    "dashboard/settings/your_information/edit": EditInformation,
    "dashboard/upload_file": UploadFile,
    "dashboard/file_preview": FilePreview,
    "dashboard/file_preview/download_file": DownloadFile,
    "dashboard/file_preview/password_prompt": PasswordPrompt,
    "dashboard/download_shared_file": DownloadSharedFile,
    "dashboard/tools": Tools,
    "dashboard/tools/sign_file": SignFile,
    "dashboard/tools/verify_signed_file": VerifySignedFile,
    "dashboard/tools/encrypt_file": EncryptFile,
    "dashboard/tools/decrypt_file": DecryptFile,
}
