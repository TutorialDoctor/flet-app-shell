from peewee import *
from datetime import datetime

database = SqliteDatabase('src/db/database.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

# One-To-One
class UserInfo(BaseModel):
        address = CharField()
        images_path = CharField(null=True)
        videos_path = CharField(null=True)
        system_prompt = CharField(null=True)

        class Meta:
            table_name = 'user_info'
        
class User(BaseModel):
    id = AutoField(null=True)
    email = CharField(null=True,max_length=60,unique=True)
    user_type = CharField(null=True,default="guest")
    first_name = CharField(null=True,max_length=50)
    last_name = CharField(null=True,max_length=50)
    password = CharField(null=True,max_length=80)
    gallery_name = CharField(null=True,max_length=256)
    password_hash = CharField(null=True,max_length=128)
    role_id = IntegerField(null=True)
    phone = CharField(null=True)
    address = CharField(null=True)
    profile_image =CharField(null=True)
    location = CharField(null=True)
    university = CharField(null=True)
    employer = CharField(null=True)
    employed_since = DateTimeField(null=True)
    birthday = CharField(null=True)
    ip_address = CharField(null=True)
    browser = CharField(null=True)
    forum_id = IntegerField(null=True)
    status = IntegerField(null=True)
    created_at = DateTimeField(default=datetime.now,null=True)
    updated_at = DateTimeField(default=datetime.now,null=True)
    version = CharField(null=True)
    info = ForeignKeyField(UserInfo, backref='user',null=True)

    class Meta:
        table_name = 'users'
        primary_key = False

# One-To-Many
class Items(BaseModel):
    user = ForeignKeyField(User, backref='items',null=True)
    name = CharField(null=True)
    item_type = CharField(null=True)
    class Meta:
            table_name = 'items'

class Images(BaseModel):
    user = ForeignKeyField(User, backref='images',null=True)
    title = CharField(null=True)
    description = TextField(null=True)
    url = CharField(null=True)
    data = BlobField(null=True)
    extension = CharField(null=True)
    class Meta:
            table_name = 'images'

class Videos(BaseModel):
    user = ForeignKeyField(User, backref='videos',null=True)
    title = CharField(null=True)
    description = TextField(null=True)
    url = CharField(null=True)
    data = BlobField(null=True)
    extension = CharField(null=True)
    class Meta:
            table_name = 'videos'

# Many-To-Many
class UserItems(BaseModel):
        user = ForeignKeyField(User, backref='items',null=True)
        item = ForeignKeyField(Items, backref='items',null=True)
        class Meta:
            table_name = 'user_items'