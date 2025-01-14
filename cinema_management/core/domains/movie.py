"""Module containing movie-related domain models"""
from asyncpg import Record
from pydantic import BaseModel, ConfigDict
from datetime import date

class MovieIn(BaseModel):
    """Model representing movie's DTO attributes."""
    name: str
    length: float
    premiere: date
    director: str

class Movie(MovieIn):
    """Model representing movie's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "Movie":
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            MovieDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),  # type: ignore
            name=record_dict.get("name"),  # type: ignore
            length=record_dict.get("length"), # type: ignore
            premiere=record_dict.get("premiere"), # type: ignore
            director=record_dict.get("director"), # type: ignore
        )