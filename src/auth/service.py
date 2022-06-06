from src.auth.model import User


def getOneUser(username):
    return User.objects(username=username).first()
