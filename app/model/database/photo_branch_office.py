from sqlalchemy import Column, Integer, String
from app.config.database import Base

class PhotoBranchOffice(Base):
    __tablename__ = "PhotoBranchOffice"
    id = Column(Integer, primary_key=True, auto_increment=True)
    file_path = Column("filePath", String)
    display_order = Column("displayOrder", Integer)
    branch_office = Column("branchOffice", Integer)

    def __init__(self, file_path: str, display_order: int, branch_office: int, id=0):
        self.id = id
        self.file_path = file_path
        self.display_order = display_order
        self.branch_office = branch_office

    @staticmethod
    def from_dict(obj: any) -> 'PhotoBranchOffice':
        assert isinstance(obj, dict)
        id = int(obj.get("id") if obj.get("id") is not None else "0")
        file_path = str(obj.get("filePath") if obj.get("filePath") is not None else obj.get("file_path"))
        display_order = int(obj.get("displayOrder") if obj.get("displayOrder") is not None else obj.get("display_order"))
        branch_office = int(obj.get("branchOffice") if obj.get("branchOffice") is not None else obj.get("branch_office"))
        return PhotoBranchOffice(file_path, display_order, branch_office, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = int(self.id)
        result["filePath"] = str(self.file_path)
        result["displayOrder"] = int(self.display_order)
        result["branchOffice"] = int(self.branch_office)
        return result
