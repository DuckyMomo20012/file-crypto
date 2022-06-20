from schema import User

import datetime


def getOneUser(email):
    return User.objects(email=email).first()


def getAllUsers():
    return User.objects()


def addUser(
    email,
    password,
    name="",
    dateOfBirth=datetime.date(1900, 1, 1),
    phone="",
    address="",
    publicKey="",
    privateKey="",
):
    name = email

    user = User(
        email=email,
        password=password,
        name=name,
        dateOfBirth=dateOfBirth,
        phone=phone,
        address=address,
        publicKey=publicKey,
        privateKey=privateKey,
    )
    user.save()
    return user


def updateUserManyFields(
    email,
    name="",
    dateOfBirth=datetime.date(1900, 1, 1),
    phone="",
    address="",
    publicKey="",
    privateKey="",
):
    user = User.objects(email=email).first()
    user.name = name
    user.dateOfBirth = dateOfBirth
    user.phone = phone
    user.address = address
    user.publicKey = publicKey
    user.privateKey = privateKey
    user.save()
    return user


def updateUserOneField(
    email: str,
    fieldName: str,
    newValue: str,
):
    user = User.objects(email=email).first()
    user[fieldName] = newValue
    user.save()
    return user


def updateUserPassword(email, password):
    user = User.objects(email=email).first()
    user.password = password
    user.save()
    return user


def updateUserKeys(email, publicKey, privateKey):
    user = User.objects(email=email).first()
    user.publicKey = publicKey
    user.privateKey = privateKey
    user.save()
    return user
