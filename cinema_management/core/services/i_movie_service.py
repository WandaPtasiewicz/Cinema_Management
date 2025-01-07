"""Module containing movie service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from cinema_management.core.domains.movie import Movie, MovieIn


class IMovieService(ABC):
    """A class representing movie repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[Movie]:
        """The method getting all movies from the repository.

        Returns:
            Iterable[Movie]: All movies.
        """


    @abstractmethod
    async def get_by_id(self, movie_id: int) -> Movie | None:
        """The method getting movie by provided id.

        Args:
            movie_id (int): The id of the movie.

        Returns:
            Movie | None: The movie details.
        """


    @abstractmethod
    async def add_movie(self, data: MovieIn) -> Movie | None:
        """The method adding new movie to the data storage.

        Args:
            data (MovieIn): The details of the new movie.

        Returns:
            Movie | None: Full details of the newly added movie.
        """

    @abstractmethod
    async def update_movie(
            self,
            movie_id: int,
            data: MovieIn,
    ) -> Movie | None:
        """The method updating movie data in the data storage.

        Args:
            movie_id (int): The id of the movie.
            data (MovieIn): The details of the updated movie.

        Returns:
            Movie | None: The updated movie details.
        """

    @abstractmethod
    async def delete_movie(self, movie_id: int) -> bool:
        """The method updating removing movie from the data storage.

        Args:
            movie_id (int): The id of the movie.

        Returns:
            bool: Success of the operation.
        """