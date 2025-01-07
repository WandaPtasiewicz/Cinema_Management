"""Module containing continent service implementation."""

from typing import Iterable

from cinema_management.core.domains.repertoire import Repertoire, RepertoireIn
from cinema_management.core.repositories.i_repertoire_repository import IRepertoireRepository
from cinema_management.core.services.i_repertoire_service import IRepertoireService



class RepertoireService(IRepertoireService):
    """A class implementing the repertoire service."""

    _repertoire_repository: IRepertoireRepository


    def __init__(self, repertoire_repository: IRepertoireRepository) -> None:
        """The initializer of the `repertoire service`.

        Args:
            repository (IRepertoireRepository): The reference to the repository.
        """
        self._repertoire_repository = repertoire_repository

    async def get_all(self) -> Iterable[Repertoire]:
        """The method getting all repertoires from the repository.

        Returns:
            Iterable[Repertoire]: All repertoires.
        """

        return await self._repertoire_repository.get_all_repertoires()

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



