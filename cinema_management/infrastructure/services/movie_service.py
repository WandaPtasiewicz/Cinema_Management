"""Module containing continent service implementation."""
import datetime
from typing import Iterable, List

from cinema_management.core.domains.movie import Movie, MovieIn
from cinema_management.core.repositories.i_movie_repository import IMovieRepository
from cinema_management.core.services.i_movie_service import IMovieService



class MovieService(IMovieService):
    """A class implementing the movie service."""

    _movie_repository: IMovieRepository


    def __init__(self, movie_repository: IMovieRepository) -> None:
        """The initializer of the `movie service`.

        Args:
            repository (IMovieRepository): The reference to the repository.
        """
        self._movie_repository = movie_repository

    async def get_all(self) -> Iterable[Movie]:
        """The method getting all movies from the repository.

        Returns:
            Iterable[Movie]: All movies.
        """

        return await self._movie_repository.get_all_movies()

    async def get_all_upcoming_movies(self) -> List[Movie]:
        """The method getting all upcoming movies from the repository.

        Returns:
            Iterable[Movie]: All movies.
        """
        all_movies = await self.get_all()
        today = datetime.date.today()
        new_movies = [movies for movies in all_movies if movies.premiere > today]

        return new_movies





    async def get_by_id(self, movie_id: int) -> Movie | None:
        """The method getting movie by provided id.

        Args:
            movie_id (int): The id of the movie.

        Returns:
            Movie | None: The movie details.
        """

        return await self._movie_repository.get_by_id(movie_id)

    async def add_movie(self, data: MovieIn) -> Movie | None:
        """The method adding new movie to the data storage.

        Args:
            data (MovieIn): The details of the new movie.

        Returns:
            Movie | None: Full details of the newly added movie.
        """


        return await self._movie_repository.add_movie(data)

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

        return await self._movie_repository.update_movie(
            movie_id=movie_id,
            data=data,
        )

    async def delete_movie(self, movie_id: int) -> bool:
        """The method updating removing movie from the data storage.

        Args:
            movie_id (int): The id of the movie.

        Returns:
            bool: Success of the operation.
        """

        return await self._movie_repository.delete_movie(movie_id)
