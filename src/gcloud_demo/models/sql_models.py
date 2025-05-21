from sqlmodel import SQLModel, Field

class ZipCodeRecord(SQLModel, table=True):
    __tablename__ = "zipcode"
    zipcode: str = Field(primary_key=True, max_length=10, nullable=False)
    exists: bool  # Whether this is a valid zipcode
    latitude: float = Field(nullable=True)
    longitude: float = Field(nullable=True)