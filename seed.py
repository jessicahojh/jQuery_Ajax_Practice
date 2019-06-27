from sqlalchemy import func
from model import *
from server import app


def load_customers():

    c_1 = Customer(name="Jess", drink="Boba")
    c_2 = Customer(name="TK", drink="Coffee")

    db.session.add(c_1)
    db.session.add(c_2)
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.drop_all() #prevents dupe seeding
    db.create_all()


    load_customers()
  