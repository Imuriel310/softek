from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from database.config import Base

class CustomerOrders(Base):
    __tablename__ = "customer_orders"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    ord_id = Column(String)
    ord_dt = Column(String)
    qt_ordd = Column(Integer)
    