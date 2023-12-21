from sqlalchemy import Column, Integer
from app.config.database import Base

class BranchOfficeDetail(Base):
    __tablename__ = "BranchOfficeDetail"
    id = Column(Integer, primary_key=True, auto_increment=True)
    hair_cut_duration = Column("hairCutDuration", Integer)
    qualifying = Column(Integer)
    ratings = Column(Integer)
    branch_office = Column("branchOffice", Integer)

    def __init__(self, hair_cut_duration: int, qualifying: int, ratings: int, branch_office: int, id=0):
        self.id = id
        self.hair_cut_duration = hair_cut_duration
        self.qualifying = qualifying
        self.ratings = ratings
        self.branch_office = branch_office

    @staticmethod
    def from_dict(obj: any) -> 'BranchOfficeDetail':
        assert isinstance(obj, dict)
        id = int(obj.get("id") if obj.get("id") is not None else "0")
        hair_cut_duration = int(obj.get("hairCutDuration") if obj.get("hairCutDuration") is not None else obj.get("hair_cut_duration"))
        qualifying = int(obj.get("qualifying"))
        ratings = int(obj.get("ratings"))
        branch_office = int(obj.get("branchOffice") if obj.get("branchOffice") is not None else obj.get("branch_office"))
        return BranchOfficeDetail(hair_cut_duration, qualifying, ratings, branch_office, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = int(self.id)
        result["hairCutDuration"] = int(self.hair_cut_duration)
        result["qualifying"] = int(self.qualifying)
        result["ratings"] = int(self.ratings)
        result["branchOffice"] = int(self.branch_office)
        return result
