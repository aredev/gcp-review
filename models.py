import datetime
from peewee import *
from dotenv import load_dotenv
load_dotenv()
import os

if "DEV_MODE" in os.environ:
    # Local development, you can ignore this
    db = MySQLDatabase(os.getenv("DB_NAME"), host=os.getenv("DB_HOST"), user=os.getenv("DB_USERNAME"),
                       password=os.getenv("DB_PASSWORD"))
else:
    # Google Cloud App Engine
    db = MySQLDatabase(os.getenv("DB_NAME"), unix_socket=os.getenv("DB_UNIX_SOCKET"), user=os.getenv("DB_USERNAME"),
                       password=os.getenv("DB_PASSWORD"))


class BaseModel(Model):
    id = AutoField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Text(BaseModel):
    original = CharField()
    translated = CharField()

    @property
    def review(self):
        return self.review.get()


class Review(BaseModel):
    approved_at = DateTimeField(default=datetime.datetime.now)
    text = ForeignKeyField(Text, backref='review')


db.connect()
db.create_tables([Text, Review])
