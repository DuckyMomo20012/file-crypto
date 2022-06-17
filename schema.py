import mongoengine as me


class User(me.Document):
    email = me.StringField()
    name = me.StringField()
    dateOfBirth = me.DateTimeField()
    phone = me.StringField()
    address = me.StringField()
    password = me.StringField()
    publicKey = me.StringField()
    privateKey = me.StringField()
    meta = {"collection": "users"}


class FileCrypto(me.Document):
    name = me.StringField()
    path = me.StringField()
    content = me.FileField()
    size = me.IntField()
    sessionKey = me.StringField()
    meta = {"collection": "files"}


class SignedFile(me.Document):
    name = me.StringField()
    path = me.StringField()
    content = me.FileField()
    size = me.IntField()
    meta = {"collection": "signed_files"}


class SignFile(me.Document):
    name = me.StringField()
    path = me.StringField()
    content = me.FileField()
    size = me.IntField()
    meta = {"collection": "sign_files"}
