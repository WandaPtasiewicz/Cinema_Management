"""Module containing reservation-related domain models"""

from typing import Optional
from asyncpg import Record
from pydantic import BaseModel, ConfigDict
from datetime import date


class ReservationIn(BaseModel):
    """Model representing reservation's DTO attributes."""
    repertoire_id: int
    firstName: str
    lastName: str
    telephone: str
    email: str
    price: float
    number_of_seats:int


class Reservation(ReservationIn):
    """Model representing reservation's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "Reservation":
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            ReservationDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),  # type: ignore
            repertoire_id=record_dict.get("repertoire_id"),  # type: ignore
            firstName=record_dict.get("firstName"), # type: ignore
            lastName=record_dict.get("lastName"), # type: ignore
            telephone=record_dict.get("telephone"), # type: ignore
            email=record_dict.get("email"), # type: ignore
            price=record_dict.get("price"), # type: ignore
            number_of_seats=record_dict.get("number_of_seats"), # type: ignore
        )