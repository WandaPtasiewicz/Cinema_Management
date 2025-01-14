from dependency_injector.wiring import Provide
from datetime import date
from datetime import time

from cinema_management.core.domains.movie import MovieIn
from cinema_management.core.domains.screeningroom import ScreeningRoomIn
from cinema_management.core.domains.reservation import ReservationIn
from cinema_management.core.domains.repertoire import RepertoireIn
from cinema_management.core.services.i_reservation_service import IReservationService
from cinema_management.core.services.i_repertoire_service import IRepertoireService
from cinema_management.core.services.i_screening_room_service import IScreening_roomService
from cinema_management.core.services.i_movie_service import IMovieService
from cinema_management.container import Container
from cinema_management.db import screening_rooms_table


async def main(
        movie_service: IMovieService = Provide[Container.movie_service],
        repertoire_service: IRepertoireService = Provide[Container.repertoire_service],
        reservation_service: IReservationService = Provide[Container.reservation_service],
        screening_room_service: IScreening_roomService = Provide[Container.screening_room_service]

):
    movies=[]
    screening_rooms =[]
    repertoires =[]
    reservations=[]

    movies.append(await movie_service.add_movie(MovieIn(
        name="shrek",
        length=2.7,
        premiere=date(2024, 12, 25),
        director="Maciej Kornatow"
    )))

    movies.append(await movie_service.add_movie(MovieIn(
        name="sonic",
        length=2.2,
        premiere=date(2024, 12, 12),
        director="Maciej Kornatow"
    )))

    movies.append(await movie_service.add_movie(MovieIn(
        name="glawiator 2",
        length=2.7,
        premiere=date(2025, 11, 25),
        director="Maciej Kornatow"
    )))

    movies.append(await movie_service.add_movie(MovieIn(
        name="catman",
        length=2.7,
        premiere=date(2025, 2, 25),
        director="Maciej Kornatow"
    )))


    movies.append(await movie_service.add_movie(MovieIn(
        name="wicked",
        length=3.1,
        premiere=date(2024, 12, 1),
        director="Maciej Kornatow"
    )))

    movies.append(await movie_service.add_movie(MovieIn(
        name="Grinch",
        length=2.11,
        premiere=date(200, 2, 12),
        director="Maciej Kornatow"
    )))

    movies.append(await movie_service.add_movie(MovieIn(
        name="Smerfy",
        length=1.8,
        premiere=date(2025, 1, 30),
        director="Maciej Kornatow"
    )))

    movies.append(await movie_service.add_movie(MovieIn(
        name="Awatar",
        length=3.4,
        premiere=date(2013, 2, 7),
        director="Maciej Kornatow"
    )))

    movies.append(await movie_service.add_movie(MovieIn(
        name="Warcraft",
        length=3.3,
        premiere=date(2018, 5, 12),
        director="Maciej Kornatow"
    )))

    movies.append(await movie_service.add_movie(MovieIn(
        name="Matylda",
        length=2.8,
        premiere=date(2025, 12, 1),
        director="Maciej Kornatow"
    )))

    screening_rooms.append(await screening_room_service.add_screening_room(ScreeningRoomIn(
        number= 1,
        rows_count= 13,
        seats_in_row= 22
    )))

    screening_rooms.append(await screening_room_service.add_screening_room(ScreeningRoomIn(
        number= 2,
        rows_count= 2,
        seats_in_row= 2
    )))

    screening_rooms.append(await screening_room_service.add_screening_room(ScreeningRoomIn(
        number= 3,
        rows_count= 14,
        seats_in_row= 36
    )))


    repertoires.append(await repertoire_service.add_repertoire(RepertoireIn(
        movie_id= movies[1].id,
        screening_room_id = screening_rooms[1].id,
        start_time= time(12,10),
        date =date(2025,1,8)
    )))

    repertoires.append(await repertoire_service.add_repertoire(RepertoireIn(
        movie_id= movies[0].id,
        screening_room_id = screening_rooms[1].id,
        start_time= time(14,30),
        date =date(2025,1,8)
    )))

    repertoires.append(await repertoire_service.add_repertoire(RepertoireIn(
        movie_id= movies[0].id,
        screening_room_id = screening_rooms[1].id,
        start_time= time(17,20),
        date =date(2025,1,8)
    )))

    repertoires.append(await repertoire_service.add_repertoire(RepertoireIn(
        movie_id= movies[3].id,
        screening_room_id = screening_rooms[2].id,
        start_time= time(20,00),
        date =date(2025,1,8)
    )))

    reservations.append(await reservation_service.add_reservation(ReservationIn(
        repertoire_id= repertoires[0].id,
        firstName= "Franek",
        lastName= "Kowalski",
        telephone= "666000999",
        email= "kamil@gmail.com",
        number_of_seats=2

    )))

    reservations.append(await reservation_service.add_reservation(ReservationIn(
        repertoire_id= repertoires[1].id,
        firstName= "Marek",
        lastName= "Kowalski",
        telephone= "666000999",
        email= "kamil@gmail.com",
        number_of_seats=2

    )))

    reservations.append(await reservation_service.add_reservation(ReservationIn(
        repertoire_id= repertoires[2].id,
        firstName= "Marek",
        lastName= "Kowalski",
        telephone= "666000999",
        email= "kamil@gmail.com",
        number_of_seats=2

    )))



 