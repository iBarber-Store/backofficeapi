from sqlalchemy import Column, Integer, String, Boolean
from app.config.database import Base

class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, auto_increment=True)
    name = Column(String)
    description = Column(String)
    schedule = Column(Integer)
    branch_office = Column("branchOffice", Integer)

    def __init__(self, name: str, description: str, schedule: int, branch_office: int, id=0):
        self.id = id
        self.name = name
        self.description = description
        self.schedule = schedule
        self.branch_office = branch_office

    @staticmethod
    def from_dict(obj: any) -> 'Product':
        assert isinstance(obj, dict)
        id = int(obj.get("id") if obj.get("id") is not None else "0")
        name = str(obj.get("name"))
        description = str(obj.get("description"))
        schedule = int(obj.get("schedule")) if obj.get("schedule") is not None else None
        branch_office = int(obj.get("branchOffice") if obj.get("branchOffice") is not None else obj.get("branch_office"))
        return Product(name, description, schedule, branch_office, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = int(self.id)
        result["name"] = str(self.name)
        result["description"] = str(self.description)
        result["schedule"] = int(self.schedule) if self.schedule is not None else None
        result["branchOffice"] = int(self.branch_office)
        return result
