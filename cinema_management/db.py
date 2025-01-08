"""A module providing database access."""

import asyncio

import databases
import sqlalchemy
from sqlalchemy.exc import OperationalError, DatabaseError
from sqlalchemy.ext.asyncio import create_async_engine
from asyncpg.exceptions import (    # type: ignore
    CannotConnectNowError,
    ConnectionDoesNotExistError,
)

from cinema_management.config import config

metadata = sqlalchemy.MetaData()


movies_table = sqlalchemy.Table(
    "movies",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column("name",sqlalchemy.String),
    sqlalchemy.Column("length",sqlalchemy.Float),
    sqlalchemy.Column("premiere",sqlalchemy.Date),
    sqlalchemy.Column("director",sqlalchemy.String),
)

screening_rooms_table = sqlalchemy.Table(
    "screening_rooms",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column("number",sqlalchemy.Integer),
    sqlalchemy.Column("rows_count",sqlalchemy.Integer),
    sqlalchemy.Column("seats_in_row",sqlalchemy.Integer),

)


repertoires_table = sqlalchemy.Table(
    "repertoires",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column("movie_id",sqlalchemy.ForeignKey("movies.id"),nullable=False),
    sqlalchemy.Column("screening_room_id",sqlalchemy.ForeignKey("screening_rooms.id"),nullable=False),
    sqlalchemy.Column("start_time",sqlalchemy.Time),
    sqlalchemy.Column("date",sqlalchemy.Date),

)
reservations_table = sqlalchemy.Table(
    "reservations",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column("repertoire_id",sqlalchemy.ForeignKey("repertoires.id"),nullable=False),
    sqlalchemy.Column("firstName",sqlalchemy.String),
    sqlalchemy.Column("lastName",sqlalchemy.String),
    sqlalchemy.Column("telephone",sqlalchemy.String),
    sqlalchemy.Column("email",sqlalchemy.String),
    sqlalchemy.Column("number_of_seats",sqlalchemy.Integer),

)
db_uri = (
    f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}/{config.DB_NAME}"
)

engine = create_async_engine(
    db_uri,
    echo=True,
    future=True,
    pool_pre_ping=True,
)

database = databases.Database(
    db_uri,
    force_rollback=True,
)


async def init_db(retries: int = 5, delay: int = 5) -> None:
    """Function initializing the DB.

    Args:
        retries (int, optional): Number of retries of connect to DB.
            Defaults to 5.
        delay (int, optional): Delay of connect do DB. Defaults to 2.
    """
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(metadata.create_all)
            return
        except (
                OperationalError,
                DatabaseError,
                CannotConnectNowError,
                ConnectionDoesNotExistError,
        ) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            await asyncio.sleep(delay)

    raise ConnectionError("Could not connect to DB after several retries.")