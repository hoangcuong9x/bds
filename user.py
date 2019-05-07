from mongoengine import Document, StringField, IntField, DateTimeField

class Newbike(Document):
    meta = {
        "strict": False
    }
    sdt = IntField()
    number = IntField()
    username = StringField() 
    email = StringField()
    messenger = StringField()