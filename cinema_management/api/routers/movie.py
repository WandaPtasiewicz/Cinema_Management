"""A module containing continent endpoints."""

from typing import Iterable, List
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from cinema_management.container import Container
from cinema_management.core.domains.movie import Movie, MovieIn
from cinema_management.core.services.i_movie_service import IMovieService
from cinema_management.core.services.i_repertoire_service import IRepertoireService

router = APIRouter()


@router.post("/create", response_model=Movie, status_code=201)
@inject
async def create_movie(
        movie: MovieIn,
        service: IMovieService = Depends(Provide[Container.movie_service]),
) -> dict:
    """An endpoint for adding new movie.

    Args:
        movie (MovieIn): The movie data.
        service (IMovieService, optional): The injected service dependency.

    Returns:
        dict: The new movie attributes.
    """

    new_movie = await service.add_movie(movie)


    return new_movie.model_dump() if new_movie else {}

@router.get("/all", response_model=Iterable[Movie], status_code=200)
@inject
async def get_all_movies(
        service: IMovieService = Depends(Provide[Container.movie_service]),
) -> Iterable:
    """An endpoint for getting all movies.

    Args:
        service (IMovieService, optional): The injected service dependency.

    Returns:
        Iterable: The movie attributes collection.
    """

    movies = await service.get_all()

    return movies

@router.get("/upcoming_movies", response_model=List[Movie], status_code=200)
@inject
async def get_all_upcoming_movies(
        service: IMovieService = Depends(Provide[Container.movie_service]),
) -> Iterable:
    """An endpoint for getting all movies.

    Args:
        service (IMovieService, optional): The injected service dependency.

    Returns:
        Iterable: The movie attributes collection.
    """

    movies = await service.get_all_upcoming_movies()

    return movies


@router.get("/{movie_id}",response_model=Movie,status_code=200,)
@inject
async def get_movie_by_id(
        movie_id: int,
        service: IMovieService = Depends(Provide[Container.movie_service]),
) -> dict | None:
    """An endpoint for getting movie by id.

    Args:
        movie_id (int): The id of the movie.
        service (IMovieService, optional): The injected service dependency.

    Returns:
        dict | None: The movie details.
    """

    if movie := await service.get_by_id(movie_id):
        return movie.model_dump()

    raise HTTPException(status_code=404, detail="Movie not found")



@router.put("/{movie_id}", response_model=Movie, status_code=201)
@inject
async def update_movie(
        movie_id: int,
        updated_movie: MovieIn,
        service: IMovieService = Depends(Provide[Container.movie_service]),
) -> dict:
    """An endpoint for updating movie data.

    Args:
        movie_id (int): The id of the movie.
        updated_movie (MovieIn): The updated movie details.
        service (IMovieService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if movie does not exist.

    Returns:
        dict: The updated movie details.
    """

    if await service.get_by_id(movie_id=movie_id):
        await service.update_movie(
            movie_id=movie_id,
            data=updated_movie,
        )
        return {**updated_movie.model_dump(), "id": movie_id}

    raise HTTPException(status_code=404, detail="Movie not found")


@router.delete("/{movie_id}", status_code=204)
@inject
async def delete_movie(
        movie_id: int,
        movie_service: IMovieService = Depends(Provide[Container.movie_service]),
        repertoire_service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> None:
    """An endpoint for deleting movies.

    Args:
        movie_id (int): The id of the movie.
        movie_service (IMovieService, optional): The injected service dependency.
        repertoire_service (IRepertoireService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if movie does not exist.
        HTTPException: 409 if can not delete movie with existing repertoire.


    """

    if await repertoire_service.get_by_movie_id(movie_id):
        raise HTTPException(status_code=409, detail="can not delete movie with existing repertoire")


    if await movie_service.get_by_id(movie_id=movie_id):
        await movie_service.delete_movie(movie_id)

        return

    raise HTTPException(status_code=404, detail="Movie not found")