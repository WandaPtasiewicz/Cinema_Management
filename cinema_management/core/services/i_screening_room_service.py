"""Module containing screening_room service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from cinema_management.core.domains.screeningroom import ScreeningRoom, ScreeningRoomIn


class IScreening_roomService(ABC):
    """A class representing screening_room repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[ScreeningRoom]:
        """The method getting all screening_rooms from the repository.

        Returns:
            Iterable[ScreeningRoom]: All screening_rooms.
        """




    @abstractmethod
    async def get_by_id(self, screening_room_id: int) -> ScreeningRoom | None:
        """The method getting screening_room by provided id.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            ScreeningRoom | None: The screening_room details.
        """


    @abstractmethod
    async def add_screening_room(self, data: ScreeningRoomIn) -> ScreeningRoom | None:
        """The method adding new screening_room to the data storage.

        Args:
            data (ScreeningRoomIn): The details of the new screening_room.

        Returns:
            ScreeningRoom | None: Full details of the newly added screening_room.
        """

    @abstractmethod
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

    @abstractmethod
    async def delete_screening_room(self, screening_room_id: int) -> bool:
        """The method updating removing screening_room from the data storage.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            bool: Success of the operation.
        """


