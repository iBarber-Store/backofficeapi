from sqlalchemy import Column, Integer, Float
from app.config.database import Base

class Price(Base):
    __tablename__ = "Price"
    id = Column(Integer, primary_key=True, auto_increment=True)
    price = Column(Float)
    price_full = Column("priceFull", Float)
    product = Column(Integer)

    def __init__(self, price: float, price_full: float, product: int, id=0):
        self.id = id
        self.price = price
        self.price_full = price_full
        self.product = product

    @staticmethod
    def from_dict(obj: any) -> 'Price':
        assert isinstance(obj, dict)
        id = int(obj.get("id") if obj.get("id") is not None else "0")
        price = float(obj.get("price"))
        price_full = float(obj.get("priceFull") if obj.get("priceFull") is not None else obj.get("price_full"))
        product = int(obj.get("product"))
        return Price(price, price_full, product, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = int(self.id)
        result["price"] = float(self.price)
        result["priceFull"] = float(self.price_full)
        result["product"] = int(self.product)
        return result
