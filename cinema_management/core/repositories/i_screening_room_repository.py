"""Module containing screening_room repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from cinema_management.core.domains.screeningroom import ScreeningRoomIn

class IScreeningRoomRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_all_screening_rooms(self) -> Iterable[Any]:
        """The abstract getting all screening_rooms from the data storage.

        Returns:
            Iterable[Any]: Screening_rooms in the data storage.
        """

    @abstractmethod
    async def get_by_id(self, screening_room_id: int) -> Any | None:
        """The abstract getting screening_room by provided id.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            Any | None: The screening_room details.
        """

    @abstractmethod
    async def add_screening_room(self, data: ScreeningRoomIn) -> Any | None:
        """The abstract adding new screening_room to the data storage.

        Args:
            data (ScreeningRoomIn): The details of the new screening_room.

        Returns:
            Any | None: The newly added screening_room.
        """

    @abstractmethod
    async def update_screening_room(
            self,
            screening_room_id: int,
            data: ScreeningRoomIn,
    ) -> Any | None:
        """The abstract updating screening_room data in the data storage.

        Args:
            screening_room_id (int): The id of the screening_room.
            data (ScreeningRoomIn): The details of the updated screening_room.

        Returns:
            Any | None: The updated screening_room details.
        """

    @abstractmethod
    async def delete_screening_room(self, screening_room_id: int) -> bool:
        """The abstract updating removing screening_room from the data storage.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            bool: Success of the operation.
        """