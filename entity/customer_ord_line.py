from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base
from .unit_measure import UnitMeasure

class CustomerOrdLine(Base):
    __tablename__ = 'customer_ord_lines'

    id = Column(Integer, primary_key=True)
    order_number = Column(String)
    item_name = Column(String)
    status = Column(String)
    