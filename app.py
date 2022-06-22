import pytermgui as ptg
from environs import Env
from mongoengine import connect

import routes
from src.helpers.page_manager import drawPage

env = Env()
# Read .env into os.environ
env.read_env()

connect(host=env.str("MONGODB_HOST"))

with ptg.WindowManager() as manager:
    styles = open("styles.yaml").read()
    loader = ptg.YamlLoader()
    loader.load(styles)
    # Add navigation history stack
    manager.navigation = []
    drawPage(manager, routes.routes["auth/login"]())
    manager.run()
