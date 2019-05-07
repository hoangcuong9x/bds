from mongoengine import Document, StringField, IntField, DateTimeField

class New(Document):
    meta = {
        "strict": False
    }
    sdt = IntField()
    