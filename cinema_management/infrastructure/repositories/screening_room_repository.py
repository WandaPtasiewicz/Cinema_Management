"""Module containing screening_room repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join

from cinema_management.core.repositories.i_screening_room_repository import IScreening_roomRepository
from cinema_management.core.domains.screeningroom import ScreeningRoom, ScreeningRoomIn
from cinema_management.db import (
    screening_rooms_table,
    database,
)

class Screening_roomRepository(IScreening_roomRepository):
    """A class representing continent DB repository."""

    async def get_all_screening_rooms(self) -> Iterable[Any]:
        """The method getting all screening_rooms from the data storage.

        Returns:
            Iterable[Any]: Screening_rooms in the data storage.
        """

        query = (
            select(screening_rooms_table)
            .order_by(screening_rooms_table.c.number.asc())
        )
        screening_rooms = await database.fetch_all(query)

        return [ScreeningRoom.from_record(screening_room) for screening_room in screening_rooms]

    async def get_by_id(self, screening_room_id: int) -> Any | None:
        """The method getting screening_room by provided id.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            Any | None: The screening_room details.
        """

        screening_room = await self._get_by_id(screening_room_id)

        return ScreeningRoom.from_record(screening_room) if screening_room else None

    async def add_screening_room(self, data: ScreeningRoomIn) -> Any | None:
        """The method adding new screening_room to the data storage.

        Args:
            data (ScreeningRoomIn): The details of the new screening_room.

        Returns:
            ScreeningRoom: Full details of the newly added screening_room.

        Returns:
            Any | None: The newly added screening_room.
        """

        query = screening_rooms_table.insert().values(**data.model_dump())
        new_screening_room_id = await database.execute(query)
        new_screening_room = await self._get_by_id(new_screening_room_id)

        return ScreeningRoom(**dict(new_screening_room)) if new_screening_room else None

    async def update_screening_room(
            self,
            screening_room_id: int,
            data: ScreeningRoomIn,
    ) -> Any | None:
        """The method updating screening_room data in the data storage.

        Args:
            screening_room_id (int): The id of the screening_room.
            data (ScreeningRoomIn): The details of the updated screening_room.

        Returns:
            Any | None: The updated screening_room details.
        """

        if self._get_by_id(screening_room_id):
            query = (
                screening_rooms_table.update()
                .where(screening_rooms_table.c.id == screening_room_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            screening_room = await self._get_by_id(screening_room_id)

            return ScreeningRoom(**dict(screening_room)) if screening_room else None

        return None

    async def delete_screening_room(self, screening_room_id: int) -> bool:
        """The method updating removing screening_room from the data storage.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(screening_room_id):
            query = screening_rooms_table \
                .delete() \
                .where(screening_rooms_table.c.id == screening_room_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, screening_room_id: int) -> Record | None:
        """A private method getting screening_room from the DB based on its ID.

        Args:
            screening_room_id (int): The ID of the screening_room.

        Returns:
            Any | None: Screening_room record if exists.
        """

        query = (
            screening_rooms_table.select()
            .where(screening_rooms_table.c.id == screening_room_id)
        )

        return await database.fetch_one(query)