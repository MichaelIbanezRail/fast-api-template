# app/db.py

import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)


class Locations(ormar.Model):
    class Meta(BaseMeta):
        tablename = "locations"

    id: int = ormar.Integer(primary_key=True)
    userId: str = ormar.Integer(unique=False, nullable=False)
    unixtime: float = ormar.Float(unique=False, nullable=False)
    lat: float = ormar.Float(unique=False, nullable=False)
    lon: float = ormar.Float(unique=False, nullable=False)
    speed: float = ormar.Float(unique=False, nullable=False)


class ContainerRecord(ormar.Model):
    class Meta(BaseMeta):
        tablename = "container_records"

    id: int = ormar.Integer(primary_key=True)
    userId: str = ormar.Integer(unique=False, nullable=False)
    unixtime: float = ormar.Float(unique=False, nullable=False)
    filename: str = ormar.String(max_length=128, unique=False, nullable=False)
    imageid: str = ormar.String(max_length=128, unique=False, nullable=False)
    container_id: str = ormar.String(max_length=128, unique=False, nullable=False)
    container_numbers: int = ormar.Integer(unique=False, nullable=False)
    container_check_digit: int = ormar.Integer(unique=False, nullable=False)
    lat: float = ormar.Float(unique=False, nullable=False)
    lon: float = ormar.Float(unique=False, nullable=False)
    speed: float = ormar.Float(unique=False, nullable=False)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
