from abc import abstractmethod

from databases.interfaces import Record
from sqlalchemy.sql.selectable import Select


class Storage:

    @abstractmethod
    async def execute(self, query: Select) -> Record:
        raise NotImplementedError

    @abstractmethod
    async def fetch_one(self, query: Select) -> tuple:
        raise NotImplementedError

    @abstractmethod
    async def fetch_all(self, query: Select) -> list[tuple]:
        raise NotImplementedError
