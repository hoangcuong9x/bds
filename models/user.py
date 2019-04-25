from mongoengine import Document, StringField, IntField, DateTimeField

class User(Document):
    meta = {
        "strict": False
    }
    fullname = StringField() # Tên đầy đủ
    username = StringField()
    email = StringField()
    password = StringField()