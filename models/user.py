from mongoengine import Document, StringField, IntField, DateTimeField

class Newbike(Document):
    meta = {
        "strict": False
    }
    number = IntField()
    username = StringField() 
    email = StringField()