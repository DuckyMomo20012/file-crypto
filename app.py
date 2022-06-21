import pytermgui as ptg
from environs import Env
from mongoengine import connect

from src.helpers.index import drawPage
from src.pages.routes import routes

env = Env()
# Read .env into os.environ
env.read_env()

connect(host=env.str("MONGODB_HOST"))

with ptg.WindowManager() as manager:
    styles = open("styles.yaml").read()

    loader = ptg.YamlLoader()
    loader.load(styles)

    manager.routes = routes

    # Add navigation history stack
    manager.navigation = []

    # drawPage(manager, manager.routes["dashboard"]())
    drawPage(manager, manager.routes["auth/login"]())

    manager.run()
