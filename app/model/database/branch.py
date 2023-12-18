from sqlalchemy import Column, Integer, String, Boolean
from app.config.database import Base

class Branch(Base):
    __tablename__ = "Branch"
    id = Column(Integer, primary_key=True, auto_increment=True)
    name = Column(String)
    alternative_name = Column("alternativeName", String)
    logo = Column(String)
    enable = Column(Boolean)
    user_access = Column("userAccess", String)

    def __init__(self, name: str, alternative_name: str, logo: str, enable: bool, user_access: str, id=0):
        self.id = id
        self.name = name
        self.alternative_name = alternative_name
        self.logo = logo
        self.enable = enable
        self.user_access = user_access

    @staticmethod
    def from_dict(obj: any) -> 'Branch':
        assert isinstance(obj, dict)
        id = int(obj.get("id") if obj.get("id") is not None else "0")
        name = str(obj.get("name"))
        alternative_name = str(obj.get("alternativeName") if obj.get("alternativeName") is not None else obj.get("alternative_name"))
        logo = str(obj.get("logo"))
        enable = bool(obj.get("enable"))
        user_access = str(obj.get("userAccess") if obj.get("userAccess") is not None else obj.get("user_access"))
        return Branch(name, alternative_name, logo, enable, user_access, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = int(self.id)
        result["name"] = str(self.name)
        result["alternativeName"] = str(self.alternative_name)
        result["logo"] = str(self.logo)
        result["enable"] = bool(self.enable)
        result["userAccess"] = str(self.user_access)
        return result
