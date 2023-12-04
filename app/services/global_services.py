from models.database import SessionLocal, engine
from models.models import Orders, Base

from sqlalchemy.orm import Session


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def get_order(db: Session, id: int):
    try:
        order = db.query(Orders).filter_by(id=id).first()
        if order:
            return order
        else:
            return None
    except:
        return {"error": "error quering orders"}


async def create_order(db: Session, new_order_data):
    try:
        db_new_order = Orders(
            id = new_order_data['id'],
            first_name = new_order_data['client_first_name'],
            phone_number= new_order_data['client_phone'],
            order_type= new_order_data['type'],
            ready= False,
            status = new_order_data['status']
        )

        db.add(db_new_order)
        db.commit()

        return 1
    except:
        return {"error": "error creating order"}
