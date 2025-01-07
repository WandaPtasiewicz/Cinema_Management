"""Module containing movie repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore
from sqlalchemy import select, join

from cinema_management.core.repositories.i_movie_repository import IMovieRepository
from cinema_management.core.domains.movie import Movie, MovieIn
from cinema_management.db import (
    movies_table,
    database,
)

class MovieRepository(IMovieRepository):
    """A class representing continent DB repository."""

    async def get_all_movies(self) -> Iterable[Any]:
        """The method getting all movies from the data storage.

        Returns:
            Iterable[Any]: Movies in the data storage.
        """

        query = (
            select(movies_table)
            .order_by(movies_table.c.name.asc())
        )
        movies = await database.fetch_all(query)

        return [Movie.from_record(movie) for movie in movies]

    async def get_by_id(self, movie_id: int) -> Any | None:
        """The method getting movie by provided id.

        Args:
            movie_id (int): The id of the movie.

        Returns:
            Any | None: The movie details.
        """

        movie = await self._get_by_id(movie_id)

        return Movie.from_record(movie) if movie else None

    async def add_movie(self, data: MovieIn) -> Any | None:
        """The method adding new movie to the data storage.

        Args:
            data (MovieIn): The details of the new movie.

        Returns:
            Movie: Full details of the newly added movie.

        Returns:
            Any | None: The newly added movie.
        """

        query = movies_table.insert().values(**data.model_dump())
        new_movie_id = await database.execute(query)
        new_movie = await self._get_by_id(new_movie_id)

        return Movie(**dict(new_movie)) if new_movie else None

    async def update_movie(
            self,
            movie_id: int,
            data: MovieIn,
    ) -> Any | None:
        """The method updating movie data in the data storage.

        Args:
            movie_id (int): The id of the movie.
            data (MovieIn): The details of the updated movie.

        Returns:
            Any | None: The updated movie details.
        """

        if self._get_by_id(movie_id):
            query = (
                movies_table.update()
                .where(movies_table.c.id == movie_id)
                .values(**data.model_dump())
            )
            await database.execute(query)

            movie = await self._get_by_id(movie_id)

            return Movie(**dict(movie)) if movie else None

        return None

    async def delete_movie(self, movie_id: int) -> bool:
        """The method updating removing movie from the data storage.

        Args:
            movie_id (int): The id of the movie.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(movie_id):
            query = movies_table \
                .delete() \
                .where(movies_table.c.id == movie_id)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, movie_id: int) -> Record | None:
        """A private method getting movie from the DB based on its ID.

        Args:
            movie_id (int): The ID of the movie.

        Returns:
            Any | None: Movie record if exists.
        """

        query = (
            movies_table.select()
            .where(movies_table.c.id == movie_id)
            .order_by(movies_table.c.name.asc())
        )

        return await database.fetch_one(query)