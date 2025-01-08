"""A module containing continent endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from cinema_management.container import Container
from cinema_management.core.domains.repertoire import Repertoire, RepertoireIn
from cinema_management.core.services.i_repertoire_service import IRepertoireService

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

@router.get("/free_seats/{repertoire_id}", response_model=dict, status_code=200)
@inject
async def available_seats(
        repertoire_id: int,
        service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> Iterable:
    """An endpoint for getting all repertoires.

    Args:
        service (IRepertoireService, optional): The injected service dependency.

    Returns:
        Iterable: The repertoire attributes collection.
    """

    if available_seats := await service.available_seats(repertoire_id):
        return {
            "available_seats": available_seats
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


@router.get(
    "/user/{user_id}",
    response_model=Iterable[Repertoire],
    status_code=200,
)
@inject
async def get_repertoires_by_user(
        user_id: int,
        service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> Iterable:
    """An endpoint for getting repertoires by user who added them.

    Args:
        user_id (int): The id of the user.
        service (IRepertoireService, optional): The injected service dependency.

    Returns:
        Iterable: The repertoire details collection.
    """

    repertoires = await service.get_by_user(user_id)

    return repertoires


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
        service (IRepertoiretService, optional): The injected service dependency.

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
        service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> None:
    """An endpoint for deleting repertoires.

    Args:
        repertoire_id (int): The id of the repertoire.
        service (IcontinentService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if repertoire does not exist.
    """

    if await service.get_by_id(repertoire_id=repertoire_id):
        await service.delete_repertoire(repertoire_id)

        return

    raise HTTPException(status_code=404, detail="Repertoire not found")