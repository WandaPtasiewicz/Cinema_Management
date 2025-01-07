from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exception_handlers import http_exception_handler


from cinema_management.api.routers.movie import router as movie_router
from cinema_management.api.routers.reservation import router as reservation_router
from cinema_management.api.routers.repertoire import router as repertoire_router
from cinema_management.api.routers.screening_room import router as screening_room_router

from cinema_management.container import Container
from cinema_management.db import database
from cinema_management.db import init_db
from cinema_management.utils import setup

container = Container()
container.wire(modules=[

    "cinema_management.api.routers.movie",
    "cinema_management.api.routers.screening_room",
    "cinema_management.api.routers.repertoire",
    "cinema_management.api.routers.reservation",
    "cinema_management.utils.setup"
])


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    """Lifespan function working on app startup."""
    await init_db()
    await database.connect()
    await  setup.main()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(movie_router, prefix="/movie")
app.include_router(screening_room_router, prefix="/screening_room")
app.include_router(repertoire_router, prefix="/repertoire")
app.include_router(reservation_router, prefix="/reservation")