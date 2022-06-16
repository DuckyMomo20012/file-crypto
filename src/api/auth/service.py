from schema import User


def getOneUser(email):
    return User.objects(email=email).first()
