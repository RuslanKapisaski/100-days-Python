from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice
from flask_bootstrap import Bootstrap5
from wtforms import Form, StringField, TextAreaField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL
from wtforms.widgets import Select
from dotenv import load_dotenv
import os



app = Flask(__name__)
Bootstrap5(app)
# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(700), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

with app.app_context():
    db.create_all()

# Flask Forms
class CafeForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()])
    map_url = StringField('Map URL', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    seats = SelectField('Seats', choices=["0-10", "10-20", "20-30", "30-40", "40-50", "50+"],validators=[DataRequired()])
    has_toilet = SelectField('Toilet', choices=["Yes", "No"])
    has_wifi = SelectField('Wifi', choices=["Yes", "No"])
    has_sockets = SelectField('Sockets', choices=["Yes", "No"])
    can_take_calls = SelectField('Can Take Calls', choices=["Yes", "No"])
    coffee_price = StringField('Coffee Price')
    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    pass


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/all", methods=['GET','POST'])
def get_all():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return render_template('cafes.html', cafes=all_cafes)

@app.route("/cafe/<int:cafe_id>")
def cafe_detail(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    form = DeleteForm()
    return render_template("cafe_detail.html", cafe=cafe, form=form)

@app.route("/add", methods=["POST", "GET"])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})

    return render_template("add.html", form=form)


@app.route("/cafe/<int:cafe_id>/edit", methods=["GET", "POST"])
def edit_cafe(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    form = CafeForm(obj=cafe)
    if form.validate_on_submit():
        cafe.name = form.name.data
        cafe.map_url = form.map_url.data
        cafe.img_url = form.img_url.data
        cafe.location = form.location.data
        cafe.seats = form.seats.data
        cafe.has_toilet = form.has_toilet.data == "Yes"
        cafe.has_wifi = form.has_wifi.data == "Yes"
        cafe.has_sockets = form.has_sockets.data == "Yes"
        cafe.can_take_calls = form.can_take_calls.data == "Yes"
        cafe.coffee_price = form.coffee_price.data
        db.session.commit()
        return redirect(url_for('cafe_detail', cafe_id=cafe.id))
    return render_template("add.html", form=form)

@app.route("/cafe/<int:cafe_id>/delete", methods=["POST"])
def delete_cafe(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for("get_all"))

if __name__ == '__main__':
    app.run(debug=True)
