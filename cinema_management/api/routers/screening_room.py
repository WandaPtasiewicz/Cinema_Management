"""A module containing continent endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from cinema_management.container import Container
from cinema_management.core.domains.screening_room import Screening_room, Screening_roomIn
from cinema_management.core.services.i_screening_room_service import IScreening_roomService

router = APIRouter()


@router.post("/create", response_model=Screening_room, status_code=201)
@inject
async def create_screening_room(
        screening_room: Screening_roomIn,
        service: IScreening_roomService = Depends(Provide[Container.screening_room_service]),
) -> dict:
    """An endpoint for adding new screening_room.

    Args:
        screening_room (Screening_roomIn): The screening_room data.
        service (IScreening_roomService, optional): The injected service dependency.

    Returns:
        dict: The new screening_room attributes.
    """

    new_screening_room = await service.add_screening_room(screening_room)



    return new_screening_room.model_dump() if new_screening_room else {}

@router.get("/all", response_model=Iterable[Screening_room], status_code=200)
@inject
async def get_all_screening_rooms(
        service: IScreening_roomService = Depends(Provide[Container.screening_room_service]),
) -> Iterable:
    """An endpoint for getting all screening_rooms.

    Args:
        service (IScreening_roomService, optional): The injected service dependency.

    Returns:
        Iterable: The screening_room attributes collection.
    """

    screening_rooms = await service.get_all()

    return screening_rooms



@router.get("/{screening_room_id}",response_model=Screening_room,status_code=200,)
@inject
async def get_screening_room_by_id(
        screening_room_id: int,
        service: IScreening_roomService = Depends(Provide[Container.screening_room_service]),
) -> dict | None:
    """An endpoint for getting screening_room by id.

    Args:
        screening_room_id (int): The id of the screening_room.
        service (IScreening_roomService, optional): The injected service dependency.

    Returns:
        dict | None: The screening_room details.
    """

    if screening_room := await service.get_by_id(screening_room_id):
        return screening_room.model_dump()

    raise HTTPException(status_code=404, detail="Screening_room not found")


@router.get(
    "/user/{user_id}",
    response_model=Iterable[Screening_room],
    status_code=200,
)
@inject
async def get_screening_rooms_by_user(
        user_id: int,
        service: IScreening_roomService = Depends(Provide[Container.screening_room_service]),
) -> Iterable:
    """An endpoint for getting screening_rooms by user who added them.

    Args:
        user_id (int): The id of the user.
        service (IScreening_roomService, optional): The injected service dependency.

    Returns:
        Iterable: The screening_room details collection.
    """

    screening_rooms = await service.get_by_user(user_id)

    return screening_rooms


@router.put("/{screening_room_id}", response_model=Screening_room, status_code=201)
@inject
async def update_screening_room(
        screening_room_id: int,
        updated_screening_room: Screening_roomIn,
        service: IScreening_roomService = Depends(Provide[Container.screening_room_service]),
) -> dict:
    """An endpoint for updating screening_room data.

    Args:
        screening_room_id (int): The id of the screening_room.
        updated_screening_room (Screening_roomIn): The updated screening_room details.
        service (IScreening_roomtService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if screening_room does not exist.

    Returns:
        dict: The updated screening_room details.
    """

    if await service.get_by_id(screening_room_id=screening_room_id):
        await service.update_screening_room(
            screening_room_id=screening_room_id,
            data=updated_screening_room,
        )
        return {**updated_screening_room.model_dump(), "id": screening_room_id}

    raise HTTPException(status_code=404, detail="Screening_room not found")


@router.delete("/{screening_room_id}", status_code=204)
@inject
async def delete_screening_room(
        screening_room_id: int,
        service: IScreening_roomService = Depends(Provide[Container.screening_room_service]),
) -> None:
    """An endpoint for deleting screening_rooms.

    Args:
        screening_room_id (int): The id of the screening_room.
        service (IcontinentService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if screening_room does not exist.
    """

    if await service.get_by_id(screening_room_id=screening_room_id):
        await service.delete_screening_room(screening_room_id)

        return

    raise HTTPException(status_code=404, detail="Screening_room not found")