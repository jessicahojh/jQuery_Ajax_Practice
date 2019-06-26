from sqlalchemy import func
from model import *
from server import app


def load_customers():

    c_1 = User(fname="Liz", lname="Law", email="liz@gmail.com", password="donut", status="resident")
    c_2 = User(fname="Ash", lname="Ma", email="ash@gmail.com", password="lashes", status="resident")

    db.session.add(c_1)
    db.session.add(c_1)
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.drop_all() #prevents dupe seeding
    db.create_all()


    load_customers()
  