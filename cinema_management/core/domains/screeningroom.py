"""Module containing movie-related domain models"""


from asyncpg import Record
from pydantic import BaseModel, ConfigDict



class ScreeningRoomIn(BaseModel):
    """Model representing movie's DTO attributes."""
    number: int
    rows_count: int
    seats_in_row: int


class ScreeningRoom(ScreeningRoomIn):
    """Model representing movie's attributes in the database."""
    id: int

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    @classmethod
    def from_record(cls, record: Record) -> "ScreeningRoom":
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

    def number_of_seats(self) -> int:
        return self.seats_in_row * self.rows_count