from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base


class CustomerOrdLine(Base):
    __tablename__ = 'customer_ord_lines'

    id = Column(Integer, primary_key=True)
    order_number = Column(String, primary_key=True)
    item_name = Column(String)
    status = Column(String)
    