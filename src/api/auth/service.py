from schema import User


def getOneUser(email):
    return User.objects(email=email).first()


def getAllUsers():
    return User.objects()


def addUser(email, name, dateOfBirth, phone, address, password, publicKey, privateKey):
    user = User(
        email=email,
        name=name,
        dateOfBirth=dateOfBirth,
        phone=phone,
        address=address,
        password=password,
        publicKey=publicKey,
        privateKey=privateKey,
    )
    user.save()
    return user


def updateUser(
    email, name, dateOfBirth, phone, address, password, publicKey, privateKey
):
    user = User.objects(email=email).first()
    user.email = email
    user.name = name
    user.dateOfBirth = dateOfBirth
    user.phone = phone
    user.address = address
    user.password = password
    user.publicKey = publicKey
    user.privateKey = privateKey
    user.save()
    return user


def updatePassword(email, password):
    user = User.objects(email=email).first()
    user.password = password
    user.save()
    return user
