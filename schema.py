from ctypes import sizeof
import email
import mongoengine as me
from requests import session


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
    content = me.BinaryField()
    size = me.IntField()
    sessionKey = me.StringField()
    meta = {"collection": "files"}

class SignedFile(me.Document):
    name = me.StringField()
    path = me.StringField()
    content = me.BinaryField()
    size = me.IntField()
    meta = {"collection": "filesignatures"}

class SignFile(me.Document):
    name = me.StringField()
    path = me.StringField()
    content = me.BinaryField()
    size = me.IntField()
    meta = {"collection": "signfiles"}