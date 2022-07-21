import databases

from core.config import config

from .base import Storage
from .sqlite_storage import SqliteStorage

DATABASE_URL = "sqlite:///../{}".format(config.db_name)

database = databases.Database(DATABASE_URL)


def get_storage() -> Storage:
    return SqliteStorage(database)