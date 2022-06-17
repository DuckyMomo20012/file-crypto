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
    "dashboard/download_shared_file": DownloadSharedFile,
    "dashboard/sign_file": SignFile,
    "dashboard/verify_signed_file": VerifySignedFile,
}
