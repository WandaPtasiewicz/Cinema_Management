"""Module containing repertoire repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable

from cinema_management.core.domains.repertoire import RepertoireIn


class IRepertoireRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_all_repertoires(self) -> Iterable[Any]:
        """The abstract getting all repertoires from the data storage.

        Returns:
            Iterable[Any]: Repertoires in the data storage.
        """

    @abstractmethod
    async def get_by_id(self, repertoire_id: int) -> Any | None:
        """The abstract getting repertoire by provided id.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            Any | None: The repertoire details.
        """

    @abstractmethod
    async def add_repertoire(self, data: RepertoireIn) -> Any | None:
        """The abstract adding new repertoire to the data storage.

        Args:
            data (RepertoireIn): The details of the new repertoire.

        Returns:
            Any | None: The newly added repertoire.
        """

    @abstractmethod
    async def update_repertoire(
            self,
            repertoire_id: int,
            data: RepertoireIn,
    ) -> Any | None:
        """The abstract updating repertoire data in the data storage.

        Args:
            repertoire_id (int): The id of the repertoire.
            data (RepertoireIn): The details of the updated repertoire.

        Returns:
            Any | None: The updated repertoire details.
        """

    @abstractmethod
    async def delete_repertoire(self, repertoire_id: int) -> bool:
        """The abstract updating removing repertoire from the data storage.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            bool: Success of the operation.
        """