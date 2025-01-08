"""Module containing continent service implementation."""

from typing import Iterable

from cinema_management.core.domains.reservation import Reservation, ReservationIn
from cinema_management.core.repositories.i_reservation_repository import IReservationRepository
from cinema_management.core.services.i_reservation_service import IReservationService



class ReservationService(IReservationService):
    """A class implementing the reservation service."""

    _reservation_repository: IReservationRepository


    def __init__(self, reservation_repository: IReservationRepository) -> None:
        """The initializer of the `reservation service`.

        Args:
            repository (IReservationRepository): The reference to the repository.
        """
        self._reservation_repository = reservation_repository

    async def get_all(self) -> Iterable[Reservation]:
        """The method getting all reservations from the repository.

        Returns:
            Iterable[Reservation]: All reservations.
        """

        return await self._reservation_repository.get_all_reservations()







    async def get_by_id(self, reservation_id: int) -> Reservation | None:
        """The method getting reservation by provided id.

        Args:
            reservation_id (int): The id of the reservation.

        Returns:
            Reservation | None: The reservation details.
        """

        return await self._reservation_repository.get_by_id(reservation_id)

    async def get_by_repertoire_id(self, repertoire_id: int) -> Reservation | None:
        """The method getting reservation by provided id.

        Args:
            repertoire_id (int): The id of the reservation.

        Returns:
            Reservation | None: The reservation details.
        """

        return await self._reservation_repository.get_by_repertoire_id(repertoire_id)

    async def add_reservation(self, data: ReservationIn) -> Reservation | None:
        """The method adding new reservation to the data storage.

        Args:
            data (ReservationIn): The details of the new reservation.

        Returns:
            Reservation | None: Full details of the newly added reservation.
        """


        return await self._reservation_repository.add_reservation(data)

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

        return await self._reservation_repository.update_reservation(
            reservation_id=reservation_id,
            data=data,
        )

    async def delete_reservation(self, reservation_id: int) -> bool:
        """The method updating removing reservation from the data storage.

        Args:
            reservation_id (int): The id of the reservation.

        Returns:
            bool: Success of the operation.
        """

        return await self._reservation_repository.delete_reservation(reservation_id)
