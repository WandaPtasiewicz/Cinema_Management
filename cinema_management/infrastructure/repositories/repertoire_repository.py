"""Module containing repertoire repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join

from cinema_management.core.repositories.i_repertoire_repository import IRepertoireRepository
from cinema_management.core.domains.repertoire import Repertoire, RepertoireIn
from cinema_management.db import (
    repertoires_table,
    database,
)

class RepertoireRepository(IRepertoireRepository):
    """A class representing continent DB repository."""

    async def get_all_repertoires(self) -> Iterable[Any]:
        """The method getting all repertoires from the data storage.

        Returns:
            Iterable[Any]: Repertoires in the data storage.
        """

        query = (
            select(repertoires_table)
            .order_by(repertoires_table.c.name.asc())
        )
        repertoires = await database.fetch_all(query)

        return [Repertoire.from_record(repertoire) for repertoire in repertoires]

    async def get_by_id(self, repertoire_id: int) -> Any | None:
        """The method getting repertoire by provided id.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            Any | None: The repertoire details.
        """

        repertoire = await self._get_by_id(repertoire_id)

        return Repertoire.from_record(repertoire) if repertoire else None

    async def add_repertoire(self, data: RepertoireIn) -> Any | None:
        """The method adding new repertoire to the data storage.

        Args:
            data (RepertoireIn): The details of the new repertoire.

        Returns:
            Repertoire: Full details of the newly added repertoire.

        Returns:
            Any | None: The newly added repertoire.
        """

        query = repertoires_table.insert().values(**data.model_dump())
        new_repertoire_id = await database.execute(query)
        new_repertoire = await self._get_by_id(new_repertoire_id)

        return Repertoire(**dict(new_repertoire)) if new_repertoire else None

    async def update_repertoire(
            self,
            repertoire_id: int,
            data: RepertoireIn,
    ) -> Any | None:
        """The method updating repertoire data in the data storage.

        Args:
            repertoire_id (int): The id of the repertoire.
            data (RepertoireIn): The details of the updated repertoire.

        Returns:
            Any | None: The updated repertoire details.
        """

        if self._get_by_id(repertoire_id):
            query = (
                repertoires_table.update()
                .where(repertoires_table.c.id == repertoire_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            repertoire = await self._get_by_id(repertoire_id)

            return Repertoire(**dict(repertoire)) if repertoire else None

        return None

    async def delete_repertoire(self, repertoire_id: int) -> bool:
        """The method updating removing repertoire from the data storage.

        Args:
            repertoire_id (int): The id of the repertoire.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(repertoire_id):
            query = repertoires_table \
                .delete() \
                .where(repertoires_table.c.id == repertoire_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, repertoire_id: int) -> Record | None:
        """A private method getting repertoire from the DB based on its ID.

        Args:
            repertoire_id (int): The ID of the repertoire.

        Returns:
            Any | None: Repertoire record if exists.
        """

        query = (
            repertoires_table.select()
            .where(repertoires_table.c.id == repertoire_id)
        )

        return await database.fetch_one(query)