import csv
from functools import lru_cache
from pathlib import Path

from db.storage import Storage, get_storage
from models.image import images


class CsvService:
    """
    Класс для работы с CSV данными, выгрузка и загрузка в БД
    """

    def __init__(self, storage: Storage):
        self.storage = storage

    async def load_data_from_csv(self, csv_path: str) -> None:
        """
        Метод выгружает данные из CSV файла и загружает в базу данных
        :param csv_path: str
        :return: None
        """
        with open(Path(__file__).parent.parent / "data" / csv_path, newline='') as file:
            reader = csv.DictReader(file, delimiter=';')
            query = images.insert().values(list(reader))
            await self.storage.execute(query)

    async def delete_table(self) -> None:
        """
        Метод очищает таблицу во время старта приложения
        :return: None
        """
        query = images.delete()
        await self.storage.execute(query)


@lru_cache()
def get_csv_service() -> CsvService:
    storage = get_storage()
    return CsvService(storage)
