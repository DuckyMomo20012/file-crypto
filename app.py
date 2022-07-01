import pytermgui as ptg
import yaml
from environs import Env
from mongoengine import connect

import routes
import session
from src.helpers.file import getSettingField
from src.helpers.page_manager import drawPage

env = Env()
# Read .env into os.environ
env.read_env()

connect(host=env.str("MONGODB_HOST"))

with ptg.WindowManager() as manager:
    styles = open("styles.yaml").read()

    defaultStyles: dict = getSettingField("workbench.styles", {})

    # If defaultStyles is not an empty dict
    if defaultStyles:
        styles = yaml.dump(defaultStyles, allow_unicode=True)

    loader = ptg.YamlLoader()
    loader.load(styles)
    # Add navigation history stack
    session.navigation = []
    drawPage(manager, routes.routes["auth/login"]())
    manager.run()
