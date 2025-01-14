"""Module containing repertoire-related domain models"""

from asyncpg import Record
from pydantic import BaseModel, ConfigDict
from datetime import date
from datetime import time


class RepertoireIn(BaseModel):
    """Model representing repertoire's DTO attributes."""
    movie_id: int
    screening_room_id: int
    start_time: time
    date: date



class Repertoire(RepertoireIn):
    """Model representing repertoire's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "Repertoire":
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            RepertoireDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),  # type: ignore
            movie_id=record_dict.get("movie_id"),  # type: ignore
            screening_room_id=record_dict.get("screening_room_id"), # type: ignore
            start_time=record_dict.get("start_time"), # type: ignore
            date=record_dict.get("date"), # type: ignore
        )