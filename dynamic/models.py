import datetime
from peewee import Field, Model, PrimaryKeyField, CharField, DateTimeField, fn, PostgresqlDatabase, TextField
from playhouse.postgres_ext import JSONField
from dynamic.settings import DB_CONFIG

database = PostgresqlDatabase(**DB_CONFIG)


class GeometryField(Field): # postgis的geometry字段
    db_field = 'geometry'

    def db_value(self, value):
        return fn.ST_GeomFromGeoJSON(value)

    def python_value(self, value):
        return 'use a python package like shapely to parse the data'

class BaseModel(Model):
    class Meta:
        database = database

class Feature_Services(BaseModel):
    gid = PrimaryKeyField(index=True)
    id = CharField()
    name = CharField(max_length=32, verbose_name='feature_services name')
    schema = CharField()
    bound = GeometryField(index=True)
    attribution = JSONField()
    tileurl = CharField()
    description = TextField()
    create_time = DateTimeField(verbose_name='create time',
                                default=datetime.datetime.utcnow)

    class Meta:
        table_name = 'feature_services'


class Function_Services(BaseModel):
    id = PrimaryKeyField(index=True)
    name = CharField(max_length=32, verbose_name='feature_services name')
    schema = CharField()
    create_time = DateTimeField(verbose_name='create time',
                                default=datetime.datetime.utcnow)
    class Meta:
        table_name = 'function_services'
