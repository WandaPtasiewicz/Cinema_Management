"""Module containing continent service implementation."""

from typing import Iterable, List

from cinema_management.core.domains.repertoire import Repertoire, RepertoireIn
from cinema_management.core.repositories.i_repertoire_repository import IRepertoireRepository
from cinema_management.core.services.i_repertoire_service import IRepertoireService
from cinema_management.core.services.i_reservation_service import IReservationService
from cinema_management.core.services.i_screening_room_service import IScreening_roomService


class RepertoireService(IRepertoireService):
    """A class implementing the repertoire service."""

    _repertoire_repository: IRepertoireRepository
    _reservation_service: IReservationService
    _screening_room_service: IScreening_roomService


    def __init__(self,
                 repertoire_repository: IRepertoireRepository,
                 reservation_service: IReservationService,
                 screening_room_service: IScreening_roomService) -> None:
        """The initializer of the `repertoire service`.

        Args:
            repertoire_repository (IRepertoireRepository): The reference to the repository.
            reservation_service (IReservationService): The reference to the reservation service.
            screening_room_service (IScreening_roomService): The reference to the screening_room service.
        """
        self._repertoire_repository = repertoire_repository
        self._reservations_service = reservation_service
        self._screening_room_service = screening_room_service



    async def get_all(self) -> Iterable[Repertoire]:
        """The method getting all repertoires from the repository.

        Returns:
            Iterable[Repertoire]: All repertoires.
        """

        return await self._repertoire_repository.get_all_repertoires()

    async def number_of_taken_seats(self, repertoire_id: int) -> int:
        """The method getting number of free seats by provided repertoire_id.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            number of free seats.
        """
        reservations = await self._reservations_service.get_by_repertoire_id(repertoire_id)
        taken_seats = 0
        for reservation in reservations:
            taken_seats += reservation.number_of_seats

        return taken_seats


    async def available_seats(self, repertoire_id: int) -> int:
        """The method getting number of free seats by provided repertoire_id.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            number of free seats.
        """

        taken_seats = await self.number_of_taken_seats(repertoire_id)
        repertoire = await self.get_by_id(repertoire_id)
        screening_room = await self._screening_room_service.get_by_id(repertoire.screening_room_id)
        free_seats = screening_room.number_of_seats()

        return free_seats - taken_seats



    async def get_by_screening_room_id(self, screening_room_id: int) -> List[Repertoire] | None:
        """The method getting repertoire by provided screening_room id.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            Repertoire | None: The repertoire details.
        """
        all_repertoires = await self.get_all()
        filtered_repertoires = [repertoire for repertoire in all_repertoires if repertoire.screening_room_id == screening_room_id]

        return filtered_repertoires

    async def get_by_movie_id(self, movie_id: int) -> List[Repertoire] | None:
        """The method getting repertoire by provided movie id.

        Args:
            movie_id (int): The id of the movie.

        Returns:
            Repertoire | None: The repertoire details.
        """
        all_repertoires = await self.get_all()
        filtered_repertoires = [repertoire for repertoire in all_repertoires if repertoire.movie_id == movie_id]

        return filtered_repertoires

    async def get_by_id(self, repertoire_id: int) -> Repertoire | None:
        """The method getting repertoire by provided id.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            Repertoire | None: The repertoire details.
        """

        return await self._repertoire_repository.get_by_id(repertoire_id)

    async def add_repertoire(self, data: RepertoireIn) -> Repertoire | None:
        """The method adding new repertoire to the data storage.

        Args:
            data (RepertoireIn): The details of the new repertoire.

        Returns:
            Repertoire | None: Full details of the newly added repertoire.
        """


        return await self._repertoire_repository.add_repertoire(data)

    async def update_repertoire(
            self,
            repertoire_id: int,
            data: RepertoireIn,
    ) -> Repertoire | None:
        """The method updating repertoire data in the data storage.

        Args:
            repertoire_id (int): The id of the repertoire.
            data (RepertoireIn): The details of the updated repertoire.

        Returns:
            Repertoire | None: The updated repertoire details.
        """

        return await self._repertoire_repository.update_repertoire(
            repertoire_id=repertoire_id,
            data=data,
        )

    async def delete_repertoire(self, repertoire_id: int) -> bool:
        """The method updating removing repertoire from the data storage.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            bool: Success of the operation.
        """

        return await self._repertoire_repository.delete_repertoire(repertoire_id)



