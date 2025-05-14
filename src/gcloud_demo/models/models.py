from sqlmodel import SQLModel, Field

class ZipCode(SQLModel, table=True):
    zipcode: str = Field(primary_key=True, max_length=10, nullable=False)
    exists: bool
    latitude: float = Field(nullable=True)
    longitude: float = Field(nullable=True)