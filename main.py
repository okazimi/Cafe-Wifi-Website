from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


# INITIALIZE FLASK SERVER
app = Flask(__name__)
# INITIALIZE BOOTSTRAP
Bootstrap(app)

# CONNECT TO DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CAFE TABLE CONFIGURATION
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    hours = db.Column(db.String(250), nullable=False)
    cafe_url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    wifi = db.Column(db.Boolean, nullable=False)
    sockets = db.Column(db.Boolean, nullable=False)
    food = db.Column(db.Boolean, nullable=False)
    outdoor = db.Column(db.Boolean, nullable=False)
    restroom = db.Column(db.Boolean, nullable=False)
    pets = db.Column(db.Boolean, nullable=False)
    parking = db.Column(db.Boolean, nullable=False)

    #  METHOD TO TRANSFORM JSON DATA INTO DICTIONARY
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# # CREATE DATABASE/TABLE
# db.create_all()

# GLOBAL VARIABLES
# QUERY DATABASE FOR ALL CAFES
ALL_CAFES = db.session.query(Cafe).all()
# BUTTON COUNTERS
WIFI = 0
SOCKETS = 0
FOOD = 0
OUTDOOR = 0
RESTROOM = 0
PETS = 0
PARKING = 0


# HOME PAGE
@app.route("/home", methods=["GET", "POST"])
def home():
    # REFERENCE GLOBAL VARIABLES
    global ALL_CAFES, WIFI, SOCKETS, FOOD, OUTDOOR, RESTROOM, PETS, PARKING

    # CHECK FILTER
    if request.method == "POST":

        # CHECK WIFI DOUBLE CLICK
        if request.form.get("wifi") is not None and WIFI == 1:
            # RESET WIFI COUNTER
            WIFI = 0
            # QUERY DATABASE FOR ALL CAFES
            ALL_CAFES = db.session.query(Cafe).all()
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES)
        # CHECK WIFI FILTER
        elif request.form.get("wifi") is not None and WIFI == 0:
            # INCREMENT WIFI COUNTER
            WIFI = 1
            # FETCH CAFES WITH WIFI
            ALL_CAFES = db.session.query(Cafe).filter_by(wifi="True")
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES, wifi_pressed="active")

        # CHECK SOCKETS DOUBLE CLICK
        if request.form.get("sockets") is not None and SOCKETS == 1:
            # RESET SOCKET COUNTER
            SOCKETS = 0
            # QUERY DATABASE FOR ALL CAFES
            ALL_CAFES = db.session.query(Cafe).all()
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES)
        # CHECK SOCKETS FILTER
        elif request.form.get("sockets") is not None and SOCKETS == 0:
            # INCREMENT SOCKET COUNTER
            SOCKETS = 1
            # FETCH CAFES WITH SOCKETS
            ALL_CAFES = db.session.query(Cafe).filter_by(sockets="True")
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES, sockets_pressed="active")

        # CHECK FOOD DOUBLE CLICK
        if request.form.get("food") is not None and FOOD == 1:
            # RESET FOOD COUNTER
            FOOD = 0
            # QUERY DATABASE FOR ALL CAFES
            ALL_CAFES = db.session.query(Cafe).all()
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES)
        # CHECK FOOD FILTER
        elif request.form.get("food") is not None and FOOD == 0:
            # INCREMENT FOOD COUNTER
            FOOD = 1
            # FETCH CAFES WITH FOOD
            ALL_CAFES = db.session.query(Cafe).filter_by(food="True")
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES, food_pressed="active")

        # CHECK OUTDOOR DOUBLE CLICK
        if request.form.get("outdoor") is not None and OUTDOOR == 1:
            # RESET OUTDOOR COUNTER
            OUTDOOR = 0
            # QUERY DATABASE FOR ALL CAFES
            ALL_CAFES = db.session.query(Cafe).all()
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES)
        # CHECK OUTDOOR FILTER
        elif request.form.get("outdoor") is not None and OUTDOOR == 0:
            # INCREMENT OUTDOOR COUNTER
            OUTDOOR = 1
            # FETCH CAFES WITH OUTDOOR
            ALL_CAFES = db.session.query(Cafe).filter_by(outdoor="True")
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES, outdoor_pressed="active")

        # CHECK RESTROOM DOUBLE CLICK
        if request.form.get("restroom") is not None and RESTROOM == 1:
            # RESET RESTROOM COUNTER
            RESTROOM = 0
            # QUERY DATABASE FOR ALL CAFES
            ALL_CAFES = db.session.query(Cafe).all()
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES)
        # CHECK RESTROOM FILTER
        elif request.form.get("restroom") is not None and RESTROOM == 0:
            # INCREMENT RESTROOM COUNTER
            RESTROOM = 1
            # FETCH CAFES WITH RESTROOM
            ALL_CAFES = db.session.query(Cafe).filter_by(restroom="True")
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES, restroom_pressed="active")

        # CHECK PETS DOUBLE CLICK
        if request.form.get("pets") is not None and PETS == 1:
            # RESET PETS COUNTER
            PETS = 0
            # QUERY DATABASE FOR ALL CAFES
            ALL_CAFES = db.session.query(Cafe).all()
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES)
        # CHECK PETS FILTER
        elif request.form.get("pets") is not None and PETS == 0:
            # INCREMENT PETS COUNTER
            PETS = 1
            # FETCH CAFES WITH PETS
            ALL_CAFES = db.session.query(Cafe).filter_by(pets="True")
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES, pets_pressed="active")

        # CHECK PARKING DOUBLE CLICK
        if request.form.get("parking") is not None and PARKING == 1:
            # RESET PARKING COUNTER
            PARKING = 0
            # QUERY DATABASE FOR ALL CAFES
            ALL_CAFES = db.session.query(Cafe).all()
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES)
        # CHECK PARKING FILTER
        elif request.form.get("parking") is not None and PARKING == 0:
            # INCREMENT PARKING COUNTER
            PARKING = 1
            # FETCH CAFES WITH PARKING
            ALL_CAFES = db.session.query(Cafe).filter_by(parking="True")
            # RENDER HOME PAGE
            return render_template("index.html", cafes=ALL_CAFES, parking_pressed="active")

    # RENDER HOME PAGE
    return render_template("index.html", cafes=ALL_CAFES)


# RUN APPLICATION
if __name__ == '__main__':
    app.run(debug=True)
