from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Customer

# import requests
import json




app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def main():
    """Homepage."""

    return render_template("main.html")

@app.route('/api/orders.json')
def orders():


    customers = [
        {   "id": customer.c_id,
            "name": customer.name,
            "drink": customer.drink
        }
        for customer in Customer.query.all()]
    

    return jsonify(customers)




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    #DebugToolbarExtension(app)

    app.run(host="0.0.0.0")