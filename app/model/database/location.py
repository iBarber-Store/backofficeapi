from sqlalchemy import Column, Integer, String, Float
from app.config.database import Base

class Location(Base):
    __tablename__ = "Location"
    id = Column(Integer, primary_key=True, auto_increment=True)
    direction = Column("direction", String)
    latitude = Column(Float)
    longitude = Column(Float)
    branch_office = Column("branchOffice", Integer)

    def __init__(self, direction: str, latitude: float, longitude: float, branch_office: int, id=0):
        self.id = id
        self.direction = direction
        self.latitude = latitude
        self.longitude = longitude
        self.branch_office = branch_office

    @staticmethod
    def from_dict(obj: any) -> 'Location':
        assert isinstance(obj, dict)
        id = int(obj.get("id") if obj.get("id") is not None else "0")
        direction = str(obj.get("direction"))
        latitude = float(obj.get("latitude"))
        longitude = float(obj.get("longitude"))
        branch_office = int(obj.get("branchOffice") if obj.get("branchOffice") is not None else obj.get("branch_office"))
        return Location(direction, latitude,longitude, branch_office, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = int(self.id)
        result["direction"] = str(self.direction)
        result["latitude"] = float(self.latitude)
        result["longitude"] = float(self.longitude)
        result["branchOffice"] = int(self.branch_office)
        return result
