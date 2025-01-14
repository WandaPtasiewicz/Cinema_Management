"""A module containing continent endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from cinema_management.container import Container
from cinema_management.core.domains.reservation import Reservation, ReservationIn
from cinema_management.core.services.i_reservation_service import IReservationService
from cinema_management.core.services.i_repertoire_service import IRepertoireService

router = APIRouter()


@router.post("/create", response_model=Reservation, status_code=201)
@inject
async def create_reservation(
        reservation: ReservationIn,
        reservation_service: IReservationService = Depends(Provide[Container.reservation_service]),
        repertoire_service: IRepertoireService = Depends(Provide[Container.repertoire_service]),
) -> dict:
    """An endpoint for adding new reservation.


    Args:
        reservation (ReservationIn): The reservation data.
        reservation_service (IReservationService, optional): The injected service dependency.
        repertoire_service (IReservationService, optional): The injected service dependency.

    Returns:
        dict: The new reservation attributes.
    """
    if reservation.number_of_seats > await repertoire_service.available_seats(reservation.repertoire_id):
        raise HTTPException(status_code=400, detail="There is no available seats")


    new_reservation = await reservation_service.add_reservation(reservation)

    return new_reservation.model_dump() if new_reservation else {}

@router.get("/all", response_model=Iterable[Reservation], status_code=200)
@inject
async def get_all_reservations(
        service: IReservationService = Depends(Provide[Container.reservation_service]),
) -> Iterable:
    """An endpoint for getting all reservations.

    Args:
        service (IReservationService, optional): The injected service dependency.

    Returns:
        Iterable: The reservation attributes collection.
    """

    reservations = await service.get_all()

    return reservations



@router.get("/id/{reservation_id}",response_model=Reservation,status_code=200,)
@inject
async def get_reservation_by_id(
        reservation_id: int,
        service: IReservationService = Depends(Provide[Container.reservation_service]),
) -> dict | None:
    """An endpoint for getting reservation by id.

    Args:
        reservation_id (int): The id of the reservation.
        service (IReservationService, optional): The injected service dependency.

    Returns:
        dict | None: The reservation details.
    """

    if reservation := await service.get_by_id(reservation_id):
        return reservation.model_dump()

    raise HTTPException(status_code=404, detail="Reservation not found")

@router.get("/repertoire_id/{repertoire_id}",response_model=Iterable[Reservation],status_code=200,)
@inject
async def get_reservation_by_repertoire_id(
        repertoire_id: int,
        service: IReservationService = Depends(Provide[Container.reservation_service]),
) -> dict | None:
    """An endpoint for getting reservation by id.

    Args:
        repertoire_id (int): The id of the reservation.
        service (IReservationService, optional): The injected service dependency.

    Returns:
        dict | None: The reservation details.
    """

    if reservations := await service.get_by_repertoire_id(repertoire_id):
        return reservations

    raise HTTPException(status_code=404, detail="Reservation not found")

@router.get("/invoice/{repertoire_id,address}",response_model=dict,status_code=200,)
@inject
async def invoice(
        repertoire_id: int,
        address: str,
        service: IReservationService = Depends(Provide[Container.reservation_service]),
) -> dict | None:
    """An endpoint for getting reservation by id.

    Args:
        repertoire_id (int): The id of the reservation.
        address (str): The address.
        service (IReservationService, optional): The injected service dependency.

    Returns:
        dict | None: The reservation details.
    """
    if await service.get_by_id(repertoire_id):
        return await service.invoice(repertoire_id, address)

    raise HTTPException(status_code=404, detail="Reservation not found")



@router.put("/{reservation_id}", response_model=Reservation, status_code=201)
@inject
async def update_reservation(
        reservation_id: int,
        updated_reservation: ReservationIn,
        service: IReservationService = Depends(Provide[Container.reservation_service]),
) -> dict:
    """An endpoint for updating reservation data.

    Args:
        reservation_id (int): The id of the reservation.
        updated_reservation (ReservationIn): The updated reservation details.
        service (IReservationService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if reservation does not exist.

    Returns:
        dict: The updated reservation details.
    """

    if await service.get_by_id(reservation_id=reservation_id):
        await service.update_reservation(
            reservation_id=reservation_id,
            data=updated_reservation,
        )
        return {**updated_reservation.model_dump(), "id": reservation_id}

    raise HTTPException(status_code=404, detail="Reservation not found")


@router.delete("/{reservation_id}", status_code=204)
@inject
async def delete_reservation(
        reservation_id: int,
        service: IReservationService = Depends(Provide[Container.reservation_service]),
) -> None:
    """An endpoint for deleting reservations.

    Args:
        reservation_id (int): The id of the reservation.
        service (IReservationService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if reservation does not exist.
    """

    if await service.get_by_id(reservation_id=reservation_id):
        await service.delete_reservation(reservation_id)

        return

    raise HTTPException(status_code=404, detail="Reservation not found")