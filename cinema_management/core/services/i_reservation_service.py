"""Module containing reservation service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable, List

from cinema_management.core.domains.reservation import Reservation, ReservationIn


class IReservationService(ABC):
    """A class representing reservation repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[Reservation]:
        """The method getting all reservations from the repository.

        Returns:
            Iterable[Reservation]: All reservations.
        """


    @abstractmethod
    async def get_by_id(self, reservation_id: int) -> Reservation | None:
        """The method getting reservation by provided id.

        Args:
            reservation_id (int): The id of the reservation.

        Returns:
            Reservation | None: The reservation details.
        """

    @abstractmethod
    async def get_by_repertoire_id(self, repertoire_id: int) -> List[Reservation] | None:
        """The method getting reservation by provided repertoire_id.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            Reservation | None: The reservation details.
        """

    @abstractmethod
    async def count_all_reservation_repertoire_id(self, repertoire_id: int) -> int:
        """The method getting number of reservations by provided repertoire_id.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            number of reservations.
        """

    @abstractmethod
    async def invoice(self,reservation_id: id,address: str) -> dict:
        """The method getting invoice by provided repertoire_id.

        Args:
            reservation_id (int): The id of the repertoire.
            address (str): The address.

        Returns:
            invoice.
        """

    @abstractmethod
    async def add_reservation(self, data: ReservationIn) -> Reservation | None:
        """The method adding new reservation to the data storage.

        Args:
            data (ReservationIn): The details of the new reservation.

        Returns:
            Reservation | None: Full details of the newly added reservation.
        """

    @abstractmethod
    async def update_reservation(
            self,
            reservation_id: int,
            data: ReservationIn,
    ) -> Reservation | None:
        """The method updating reservation data in the data storage.

        Args:
            reservation_id (int): The id of the reservation.
            data (ReservationIn): The details of the updated reservation.

        Returns:
            Reservation | None: The updated reservation details.
        """

    @abstractmethod
    async def delete_reservation(self, reservation_id: int) -> bool:
        """The method updating removing reservation from the data storage.

        Args:
            reservation_id (int): The id of the reservation.

        Returns:
            bool: Success of the operation.
        """

