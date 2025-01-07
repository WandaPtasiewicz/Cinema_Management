"""Module containing movie-related domain models"""

from typing import Optional
from asyncpg import Record
from pydantic import BaseModel, ConfigDict
from datetime import date


class Screening_roomIn(BaseModel):
    """Model representing movie's DTO attributes."""
    number: int
    rows_count: float
    seats_in_row: int


class Screening_room(Screening_roomIn):
    """Model representing movie's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "Screening_room":
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            Screening_roomDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),  # type: ignore
            number=record_dict.get("number"),  # type: ignore
            rows_count=record_dict.get("rows_count"), # type: ignore
            seats_in_row=record_dict.get("seats_in_row"), # type: ignore
        )