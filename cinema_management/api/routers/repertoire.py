"""A module containing continent endpoints."""

from typing import Iterable, List
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from cinema_management.container import Container
from cinema_management.core.domains.repertoire import Repertoire, RepertoireIn
from cinema_management.core.services.i_repertoire_service import IRepertoireService
from cinema_management.core.services.i_reservation_service import IReservationService

router = APIRouter()


@router.post("/create", response_model=Repertoire, status_code=201)
@inject
async def create_repertoire(
        repertoire: RepertoireIn,
        service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> dict:
    """An endpoint for adding new repertoire.

    Args:
        repertoire (RepertoireIn): The repertoire data.
        service (IRepertoireService, optional): The injected service dependency.

    Returns:
        dict: The new repertoire attributes.
    """

    new_repertoire = await service.add_repertoire(repertoire)

    return new_repertoire.model_dump() if new_repertoire else {}


@router.get("/taken_seats/{repertoire_id}",response_model=dict,status_code=200,)
@inject
async def number_of_taken_seats(
        repertoire_id: int,
        service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> dict | None:
    """An endpoint for getting reservation by id.

    Args:
        repertoire_id (int): The id of the reservation.
        service (IReservationService, optional): The injected service dependency.

    Returns:
        dict | None: The reservation details.
    """

    if taken_seats := await service.number_of_taken_seats(repertoire_id):
        return {
            "taken_seats": taken_seats
        }

    raise HTTPException(status_code=404, detail="Reservation not found")


@router.get("/free_seats/{repertoire_id}", response_model=dict, status_code=200)
@inject
async def available_seats(
        repertoire_id: int,
        service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> Iterable:
    """An endpoint for getting all repertoires.

    Args:
        repertoire_id(int): id of the repertoire.
        service (IRepertoireService, optional): The injected service dependency.

    Returns:
        Iterable: The repertoire attributes collection.
    """

    if  await service.get_by_id(repertoire_id):
        return {
            "available_seats": service.available_seats(repertoire_id)
        }

    raise HTTPException(status_code=404, detail="Reservation not found")

@router.get("/all", response_model=Iterable[Repertoire], status_code=200)
@inject
async def get_all_repertoires(
        service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> Iterable:
    """An endpoint for getting all repertoires.

    Args:
        service (IRepertoireService, optional): The injected service dependency.

    Returns:
        Iterable: The repertoire attributes collection.
    """

    repertoires = await service.get_all()

    return repertoires



@router.get("/{repertoire_id}",response_model=Repertoire,status_code=200,)
@inject
async def get_repertoire_by_id(
        repertoire_id: int,
        service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> dict | None:
    """An endpoint for getting repertoire by id.

    Args:
        repertoire_id (int): The id of the repertoire.
        service (IRepertoireService, optional): The injected service dependency.

    Returns:
        dict | None: The repertoire details.
    """

    if repertoire := await service.get_by_id(repertoire_id):
        return repertoire.model_dump()

    raise HTTPException(status_code=404, detail="Repertoire not found")

@router.get("/movie_id/{movie_id}",response_model=List[Repertoire],status_code=200,)
@inject
async def get_repertoire_by_movie_id(
        movie_id: int,
        service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> dict | None:
    """An endpoint for getting repertoire by movie id.

    Args:
        movie_id (int): The id of the movie.
        service (IRepertoireService, optional): The injected service dependency.

    Returns:
        dict | None: The repertoire details.
    """

    if repertoire := await service.get_by_movie_id(movie_id):
        return repertoire

    raise HTTPException(status_code=404, detail="Repertoire not found")

@router.get("/screening_room_id/{movie_id}",response_model=List[Repertoire],status_code=200,)
@inject
async def get_repertoire_by_screening_room_id(
        screening_room_id: int,
        service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> dict | None:
    """An endpoint for getting repertoire by screening_room id.

    Args:
        screening_room_id (int): The id of the movie.
        service (IRepertoireService, optional): The injected service dependency.

    Returns:
        dict | None: The repertoire details.
    """

    if repertoire := await service.get_by_screening_room_id(screening_room_id):
        return repertoire

    raise HTTPException(status_code=404, detail="Repertoire not found")



@router.put("/{repertoire_id}", response_model=Repertoire, status_code=201)
@inject
async def update_repertoire(
        repertoire_id: int,
        updated_repertoire: RepertoireIn,
        service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> dict:
    """An endpoint for updating repertoire data.

    Args:
        repertoire_id (int): The id of the repertoire.
        updated_repertoire (RepertoireIn): The updated repertoire details.
        service (IRepertoireService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if repertoire does not exist.

    Returns:
        dict: The updated repertoire details.
    """

    if await service.get_by_id(repertoire_id=repertoire_id):
        await service.update_repertoire(
            repertoire_id=repertoire_id,
            data=updated_repertoire,
        )
        return {**updated_repertoire.model_dump(), "id": repertoire_id}

    raise HTTPException(status_code=404, detail="Repertoire not found")


@router.delete("/{repertoire_id}", status_code=204)
@inject
async def delete_repertoire(
        repertoire_id: int,
        reservation_service: IReservationService = Depends(Provide[Container.reservation_service]),
        repertoire_service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> None:
    """An endpoint for deleting repertoires.

    Args:
        repertoire_id (int): The id of the repertoire.
        reservation_service (IReservationService, optional): The injected service dependency.
        repertoire_service (IRepertoireService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if repertoire does not exist.
        HTTPException: 409 if repertoire does not exist.
    """
    if await reservation_service.get_by_repertoire_id(repertoire_id):
        raise HTTPException(status_code=409, detail="can not delete repertoire with existing repertoire")

    if await repertoire_service.get_by_id(repertoire_id=repertoire_id):
        await repertoire_service.delete_repertoire(repertoire_id)

        return

    raise HTTPException(status_code=404, detail="Repertoire not found")