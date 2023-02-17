from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from database.config import Base

class Weather(Base):
    __tablename__ = "weather"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String)
    was_rainy = Column(Integer)