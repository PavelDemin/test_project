import random
from functools import lru_cache
from typing import Optional

from fastapi import Depends
from sqlalchemy import and_, or_
from sqlalchemy.sql.expression import func

from db.storage import Storage, get_storage
from models.image import images


class ImageService:
    """
    Класс для выборки URL изображений
    """

    def __init__(self, storage: Storage):
        self.storage = storage

    async def _update_amount_of_shows(self, item_id: int, present_value: int) -> None:
        """
        Метод уменьшает на единицу update_amount_of_shows
        :param item_id: int
        :param present_value: int
        :return: None
        """
        query = images.update().where(images.c.id == item_id).values(needed_amount_of_shows=present_value - 1)
        await self.storage.execute(query)

    async def _get_random_image(self) -> tuple:
        """
        Метод для случайной выборки изображения из БД
        :return: tuple
        """
        query = images.select().where(images.c.needed_amount_of_shows > 0).order_by(func.random()).limit(1)
        return await self.storage.fetch_one(query)

    async def get_image_by_category(self, category=Optional[list[str]]) -> str:
        """
        Метод для выборки изображения по запрошенной категории
        :param category:
        :return: str
        """
        data = []
        if category:
            for category_item in category:
                query = images.select().where(
                    and_(
                        or_(
                            images.c.category1 == category_item,
                            images.c.category2 == category_item,
                            images.c.category3 == category_item,
                            images.c.category4 == category_item,
                            images.c.category5 == category_item,
                            images.c.category6 == category_item,
                            images.c.category7 == category_item,
                            images.c.category8 == category_item,
                            images.c.category9 == category_item,
                            images.c.category10 == category_item,
                        ),
                        images.c.needed_amount_of_shows > 0
                    )
                )
                row = await self.storage.fetch_all(query)
                data.extend(row)
            if len(data) > 0:
                data_list = list(set(data))
                data_list.sort(key=lambda x: x[2], reverse=True)  # сортировка по наибольшему число показов
                weights = [i[2] for i in data_list]
                select_row = random.choices(data_list, weights=weights, k=1)[0]
            else:
                select_row = await self._get_random_image()
        else:
            select_row = await self._get_random_image()

        await self._update_amount_of_shows(select_row[0], select_row[2])

        return select_row[1]


@lru_cache()
def get_image_service(storage=Depends(get_storage)) -> ImageService:
    return ImageService(storage)
