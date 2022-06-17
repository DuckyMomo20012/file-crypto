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


def updateUser(
    email: str,
    fieldName: str,
    newValue: str,
):
    user = User.objects(email=email).first()
    user[fieldName] = newValue
    user.save()
    return user


def updatePassword(email, password):
    user = User.objects(email=email).first()
    user.password = password
    user.save()
    return user
