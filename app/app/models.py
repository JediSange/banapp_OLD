from mongoengine import *
import datetime

class Champion(Document):
  champion_id = IntField(required=True, min_value=1, primary_key=True)
  image_url = StringField()
  name = StringField(required=True)
  score = IntField(required=True)
  tags = ListField(field=StringField())

class Vote(Document):
  ip_address = StringField(required=True)
  champion_id = IntField(required=True, min_value=1)
  value = IntField(required=True, min_value=-1, max_value=1)
  created = DateTimeField(required=True, default=datetime.datetime.now)

  meta = {
    'indexes': ['ip_address', 'champion_id']
  }
