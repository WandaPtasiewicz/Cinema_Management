"""Module containing movie repository abstractions."""

from abc import ABC, abstractmethod
from typing import Any, Iterable
from cinema_management.core.domains.movie import MovieIn

class IMovieRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_all_movies(self) -> Iterable[Any]:
        """The abstract getting all movies from the data storage.

        Returns:
            Iterable[Any]: Movies in the data storage.
        """

    @abstractmethod
    async def get_by_id(self, movie_id: int) -> Any | None:
        """The abstract getting movie by provided id.

        Args:
            movie_id (int): The id of the movie.

        Returns:
            Any | None: The movie details.
        """

    @abstractmethod
    async def add_movie(self, data: MovieIn) -> Any | None:
        """The abstract adding new movie to the data storage.

        Args:
            data (MovieIn): The details of the new movie.

        Returns:
            Any | None: The newly added movie.
        """

    @abstractmethod
    async def update_movie(
            self,
            movie_id: int,
            data: MovieIn,
    ) -> Any | None:
        """The abstract updating movie data in the data storage.

        Args:
            movie_id (int): The id of the movie.
            data (MovieIn): The details of the updated movie.

        Returns:
            Any | None: The updated movie details.
        """

    @abstractmethod
    async def delete_movie(self, movie_id: int) -> bool:
        """The abstract updating removing movie from the data storage.

        Args:
            movie_id (int): The id of the movie.

        Returns:
            bool: Success of the operation.
        """