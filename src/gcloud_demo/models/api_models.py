from pydantic import BaseModel

class ZipCode(BaseModel):
    zipcode: str
    exists: bool
    source: str
    latitude: float | None
    longitude: float | None