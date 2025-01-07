"""Module containing screening_room service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from cinema_management.core.domains.screening_room import Screening_room, Screening_roomIn


class IScreening_roomService(ABC):
    """A class representing screening_room repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[Screening_room]:
        """The method getting all screening_rooms from the repository.

        Returns:
            Iterable[Screening_room]: All screening_rooms.
        """


    @abstractmethod
    async def get_by_id(self, screening_room_id: int) -> Screening_room | None:
        """The method getting screening_room by provided id.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            Screening_room | None: The screening_room details.
        """


    @abstractmethod
    async def add_screening_room(self, data: Screening_roomIn) -> Screening_room | None:
        """The method adding new screening_room to the data storage.

        Args:
            data (Screening_roomIn): The details of the new screening_room.

        Returns:
            Screening_room | None: Full details of the newly added screening_room.
        """

    @abstractmethod
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

    @abstractmethod
    async def delete_screening_room(self, screening_room_id: int) -> bool:
        """The method updating removing screening_room from the data storage.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            bool: Success of the operation.
        """


