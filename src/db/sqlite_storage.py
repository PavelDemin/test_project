import databases
from databases.interfaces import Record
from sqlalchemy.sql.selectable import Select

from .base import Storage


class SqliteStorage(Storage):

    """
    Класс адаптер для БД SQLite
    """

    def __init__(self, conn: databases.Database):
        self.conn = conn

    async def execute(self, query: Select) -> Record:
        return await self.conn.execute(query)

    async def fetch_one(self, query: Select) -> Record:
        return await self.conn.fetch_one(query)

    async def fetch_all(self, query: Select) -> list[Record]:
        return await self.conn.fetch_all(query)
