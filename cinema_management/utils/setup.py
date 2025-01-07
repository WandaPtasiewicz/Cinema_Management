from dependency_injector.wiring import Provide
from datetime import date
from datetime import time

from cinema_management.core.domains.movie import MovieIn
from cinema_management.core.domains.screening_room import Screening_roomIn
from cinema_management.core.domains.reservation import ReservationIn
from cinema_management.core.domains.repertoire import RepertoireIn
from cinema_management.core.services.i_reservation_service import IReservationService
from cinema_management.core.services.i_repertoire_service import IRepertoireService
from cinema_management.core.services.i_screening_room_service import IScreening_roomService
from cinema_management.core.services.i_movie_service import IMovieService
from cinema_management.container import Container

async def main(
        movie_service: IMovieService = Provide[Container.movie_service],
        repertoire_service: IRepertoireService = Provide[Container.repertoire_service],
        reservation_service: IReservationService = Provide[Container.reservation_service],
        screening_room_service: IScreening_roomService = Provide[Container.screening_room_service]

):
    await movie_service.add_movie(MovieIn(
        name="shrek",
        length=2.7,
        premiere=date(2022, 12, 25),
        director="Maciej Kornatow"
    ))

    await movie_service.add_movie(MovieIn(
        name="Sonic 3",
        length=2.2,
        premiere=date(2022, 12, 18),
        director="Kranowski Michal"
    ))

    await movie_service.add_movie(MovieIn(
        name="Kaczki",
        length=1.7,
        premiere=date(2022, 11, 25),
        director="Ania Kot"
    ))

    await movie_service.add_movie(MovieIn(
        name="Minionki",
        length=2.7,
        premiere=date(2022, 10, 11),
        director="Kamil Slimak"
    ))

    await movie_service.add_movie(MovieIn(
        name="Panda",
        length=1.5,
        premiere=date(2022, 5, 25),
        director="Kamil Kowal"
    ))

    await movie_service.add_movie(MovieIn(
        name="Żelazny facet",
        length=2.7,
        premiere=date(2025, 2, 2),
        director="Kamil Kowal"
    ))

    await movie_service.add_movie(MovieIn(
        name="lubisie",
        length=1.2,
        premiere=date(2025, 2, 9),
        director="Kamil Kowal"
    ))

    await screening_room_service.add_screening_room(Screening_roomIn(
        number= 1,
        rows_count= 11,
        seats_in_row= 20
    ))

    await screening_room_service.add_screening_room(Screening_roomIn(
        number= 2,
        rows_count= 3,
        seats_in_row= 3
    ))

    await screening_room_service.add_screening_room(Screening_roomIn(
        number= 3,
        rows_count= 10,
        seats_in_row= 13
    ))

    await screening_room_service.add_screening_room(Screening_roomIn(
        number= 4,
        rows_count= 13,
        seats_in_row= 22
    ))

 