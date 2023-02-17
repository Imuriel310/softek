# import necessary modules and classes
from sqlalchemy.orm.session import Session
from sqlalchemy import func
from entity.customer_orders import CustomerOrders
from database.config import SessionLocal




def get_customer_orders() -> dict:
    with SessionLocal() as session:
        sales_data = session.query(CustomerOrders).all()
        return sales_data


