# flake8: noqa
from src.pages.auth import *
from src.pages.dashboard import *

routes = {
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
