from sqlalchemy import Boolean, Column, \
Integer, String

from .database import Base

class Orders(Base):
    """
    Database model used for Orders class
    """
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    phone_number = Column(String(16))
    order_type = Column(String(11))
    ready = Column(Boolean)
    status = Column(String(50))


