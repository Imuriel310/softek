from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

engine = create_engine('sqlite:///softek.db')
Session = sessionmaker(bind=engine)
session = Session()

SessionLocal:Session = sessionmaker(autocommit=False,autoflush=True,bind=engine)
