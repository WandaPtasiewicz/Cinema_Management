"""Module providing containers injecting dependencies."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from cinema_management.infrastructure.repositories.movie_repository import MovieRepository
from cinema_management.infrastructure.repositories.screening_room_repository import   Screening_roomRepository
from cinema_management.infrastructure.repositories.repertoire_repository import  RepertoireRepository
from cinema_management.infrastructure.repositories.reservation_repository import  ReservationRepository

from cinema_management.infrastructure.services.movie_service import MovieService
from cinema_management.infrastructure.services.screening_room_service import  ScreeningRoomService
from cinema_management.infrastructure.services.repertoire_service import RepertoireService
from cinema_management.infrastructure.services.reservation_service import ReservationService

class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""

    movie_repository = Singleton(MovieRepository)
    screening_room_repository = Singleton(Screening_roomRepository)
    repertoire_repository = Singleton(RepertoireRepository)
    reservation_repository = Singleton(ReservationRepository)



    movie_service = Factory(
        MovieService,
        movie_repository=movie_repository,
    )
    reservation_service = Factory(
        ReservationService,
        reservation_repository=reservation_repository,

    )

    screening_room_service = Factory(
        ScreeningRoomService,
        screening_room_repository=screening_room_repository,
    )
    repertoire_service = Factory(
        RepertoireService,
        repertoire_repository=repertoire_repository,
        reservation_service = reservation_service,
        screening_room_service = screening_room_service
    )
