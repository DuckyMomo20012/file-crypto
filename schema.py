import mongoengine as me  # type: ignore


class User(me.Document):
    email = me.StringField()
    name = me.StringField()
    dateOfBirth = me.DateTimeField()
    phone = me.StringField()
    address = me.StringField()
    password = me.BinaryField()
    publicKey = me.BinaryField()
    privateKey = me.BinaryField()
    meta = {"collection": "users"}


class FileCrypto(me.Document):
    name = me.StringField()
    sessionKey = me.BinaryField()
    nonce = me.BinaryField()
    tag = me.BinaryField()
    cipher = me.FileField()
    emailUser = me.StringField()
    meta = {"collection": "files"}
