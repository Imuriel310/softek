from sqlalchemy.orm.session import Session
from entity.weather import Weather
from database.config import SessionLocal


def get_rainy_days() -> list:
    with SessionLocal() as session:
        # Retrieve all unit measures from the database
        unit_measure_data = session.query(Weather).all()
        return unit_measure_data