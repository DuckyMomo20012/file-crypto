import mongoengine as me


class User(me.Document):
    username = me.StringField()
    password = me.StringField()
    meta = {"collection": "users"}
