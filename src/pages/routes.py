from src.pages.auth import *
from src.pages.dashboard import *
from src.pages.errors import *


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
    "dashboard/download_shared_file": DownloadSharedFile,
    "dashboard/sign_file": SignFile,
    "dashboard/verify_signed_file": VerifySignedFile,
    "dashboard/encrypt_file": EncryptFile,
    "dashboard/decrypt_file": DecryptFile,
    "errors/form_validation_error": FormValidationError,
}
