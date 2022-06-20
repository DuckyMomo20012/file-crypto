from environs import Env
from mongoengine import connect
import pytermgui as ptg

from src.pages.routes import routes
from src.helpers.index import drawPage

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
