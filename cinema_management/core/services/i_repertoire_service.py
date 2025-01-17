"""Module containing repertoire service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable, List
from cinema_management.core.domains.repertoire import Repertoire, RepertoireIn

class IRepertoireService(ABC):
    """A class representing repertoire repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[Repertoire]:
        """The method getting all repertoires from the repository.

        Returns:
            Iterable[Repertoire]: All repertoires.
        """

    @abstractmethod
    async def get_by_id(self, repertoire_id: int) -> Repertoire | None:
        """The method getting repertoire by provided id.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            Repertoire | None: The repertoire details.
        """

    @abstractmethod
    async def get_by_screening_room_id(self, screening_room_id: int) -> List[Repertoire] | None:
        """The method getting repertoire by provided screening_room id.

        Args:
            screening_room_id (int): The id of the screening_room.

        Returns:
            Repertoire | None: The repertoire details.
        """

    @abstractmethod
    async def get_by_movie_id(self, movie_id: int) -> List[Repertoire] | None:
        """The method getting repertoire by provided movie id.

        Args:
            movie_id (int): The id of the movie.

        Returns:
            Repertoire | None: The repertoire details.
        """

    @abstractmethod
    async def number_of_taken_seats(self, repertoire_id: int) -> int:
        """The method getting number of taken seats by provided repertoire_id.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            number of taken seats.
        """

    @abstractmethod
    async def available_seats(self, repertoire_id: int) -> int:
        """The method getting number of free seats by provided repertoire_id.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            number of free seats.
        """

    @abstractmethod
    async def add_repertoire(self, data: RepertoireIn) -> Repertoire | None:
        """The method adding new repertoire to the data storage.

        Args:
            data (RepertoireIn): The details of the new repertoire.

        Returns:
            Repertoire | None: Full details of the newly added repertoire.
        """

    @abstractmethod
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

    @abstractmethod
    async def delete_repertoire(self, repertoire_id: int) -> bool:
        """The method updating removing repertoire from the data storage.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            bool: Success of the operation.
        """