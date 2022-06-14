from src.pages.auth import *
from src.pages.dashboard import *


routes = {
    "auth/login": Login,
    "auth/register": Register,
    "auth/logout": Logout,
    "dashboard": DashBoard,
    "dashboard/settings": Settings,
    "dashboard/settings/change_password": ChangePassword,
    "dashboard/upload_file": UploadFile,
}
