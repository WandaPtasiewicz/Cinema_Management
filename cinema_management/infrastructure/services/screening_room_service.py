"""Module containing continent service implementation."""

from typing import Iterable

from cinema_management.core.domains.screening_room import Screening_room, Screening_roomIn
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

    async def get_all(self) -> Iterable[Screening_room]:
        """The method getting all screening_rooms from the repository.

        Returns:
            Iterable[Screening_room]: All screening_rooms.
        """

        return await self._screening_room_repository.get_all_screening_rooms()

    async def get_by_id(self, screening_room_id: int) -> Screening_room | None:
        """The method getting screening_room by provided id.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            Screening_room | None: The screening_room details.
        """

        return await self._screening_room_repository.get_by_id(screening_room_id)

    async def add_screening_room(self, data: Screening_roomIn) -> Screening_room | None:
        """The method adding new screening_room to the data storage.

        Args:
            data (Screening_roomIn): The details of the new screening_room.

        Returns:
            Screening_room | None: Full details of the newly added screening_room.
        """


        return await self._screening_room_repository.add_screening_room(data)

    async def update_screening_room(
            self,
            screening_room_id: int,
            data: Screening_roomIn,
    ) -> Screening_room | None:
        """The method updating screening_room data in the data storage.

        Args:
            screening_room_id (int): The id of the screening_room.
            data (Screening_roomIn): The details of the updated screening_room.

        Returns:
            Screening_room | None: The updated screening_room details.
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
