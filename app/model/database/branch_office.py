from sqlalchemy import Column, Integer, String
from app.config.database import Base

class BranchOffice(Base):
    __tablename__ = "BranchOffice"
    id = Column(Integer, primary_key=True, auto_increment=True)
    another_name = Column("anotherName", String)
    description = Column(String)
    logo = Column(String)
    branch = Column(Integer)

    def __init__(self, another_name: str, description: str, logo: str, branch: int, id=0):
        self.id = id
        self.another_name = another_name
        self.description = description
        self.logo = logo
        self.branch = branch

    @staticmethod
    def from_dict(obj: any) -> 'BranchOffice':
        assert isinstance(obj, dict)
        id = int(obj.get("id") if obj.get("id") is not None else "0")
        another_name = str(obj.get("anotherName") if obj.get("anotherName") is not None else obj.get("another_name"))
        description = str(obj.get("description"))
        logo = str(obj.get("logo"))
        branch = int(obj.get("branch"))
        return BranchOffice(another_name, description, logo, branch, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = int(self.id)
        result["anotherName"] = str(self.another_name)
        result["logo"] = str(self.logo)
        result["description"] = str(self.description)
        result["branch"] = int(self.branch)
        return result
