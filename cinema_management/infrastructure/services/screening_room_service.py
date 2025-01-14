"""Module containing continent service implementation."""

from typing import Iterable

from cinema_management.core.domains.screeningroom import ScreeningRoom, ScreeningRoomIn
from cinema_management.core.repositories.i_screening_room_repository import IScreening_roomRepository
from cinema_management.core.services.i_screening_room_service import IScreening_roomService



class Screening_roomService(IScreening_roomService):
    """A class implementing the screening_room service."""

    _screening_room_repository: IScreening_roomRepository


    def __init__(self, screening_room_repository: IScreening_roomRepository) -> None:
        """The initializer of the `screening_room service`.

        Args:
            screening_room_repository (IScreening_roomRepository): The reference to the repository.
        """
        self._screening_room_repository = screening_room_repository

    async def get_all(self) -> Iterable[ScreeningRoom]:
        """The method getting all screening_rooms from the repository.

        Returns:
            Iterable[ScreeningRoom]: All screening_rooms.
        """

        return await self._screening_room_repository.get_all_screening_rooms()

    async def get_by_id(self, screening_room_id: int) -> ScreeningRoom | None:
        """The method getting screening_room by provided id.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            ScreeningRoom | None: The screening_room details.
        """

        return await self._screening_room_repository.get_by_id(screening_room_id)

    async def add_screening_room(self, data: ScreeningRoomIn) -> ScreeningRoom | None:
        """The method adding new screening_room to the data storage.

        Args:
            data (ScreeningRoomIn): The details of the new screening_room.

        Returns:
            ScreeningRoom | None: Full details of the newly added screening_room.
        """


        return await self._screening_room_repository.add_screening_room(data)

    async def update_screening_room(
            self,
            screening_room_id: int,
            data: ScreeningRoomIn,
    ) -> ScreeningRoom | None:
        """The method updating screening_room data in the data storage.

        Args:
            screening_room_id (int): The id of the screening_room.
            data (ScreeningRoomIn): The details of the updated screening_room.

        Returns:
            ScreeningRoom | None: The updated screening_room details.
        """

        return await self._screening_room_repository.update_screening_room(
            screening_room_id=screening_room_id,
            data=data,
        )

    async def delete_screening_room(self, screening_room_id: int) -> bool:
        """The method updating removing screening_room from the data storage.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            bool: Success of the operation.
        """

        return await self._screening_room_repository.delete_screening_room(screening_room_id)
