from schema import User


def getOneUser(username):
    return User.objects(username=username).first()
