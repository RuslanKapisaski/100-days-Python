from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
Bootstrap5(app)

# DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)

movies = []

# TABLE
class Movie(db.Model):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String(24), unique=True)
    year: Mapped[str] = mapped_column(db.String)
    description: Mapped[str] = mapped_column(db.String(300))
    rating: Mapped[float] = mapped_column(db.Float)
    ranking: Mapped[int] = mapped_column(db.Integer)
    review: Mapped[str] = mapped_column(db.String(100))
    img_url: Mapped[str] = mapped_column(db.String(100))

    def __repr__(self):
        return(f"<Book>: {self.title} - {self.year} created successfully>")

with app.app_context():
    db.create_all()
    print("Database created successfully")

# Forms
class EditForm(FlaskForm):
    rating = FloatField(label='Rating', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')

class CreateForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    year = StringField(label='Year', validators=[DataRequired()])
    description = StringField(label='Description', validators=[DataRequired()])
    rating = FloatField(label='Rating', validators=[DataRequired()])
    ranking = StringField(label='Ranking', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    img_url = StringField(label='Image', validators=[DataRequired()])
    submit = SubmitField(label='Done')

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie)).scalars().all()
    return render_template("index.html",movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        new_movie = Movie(
            title = request.form["title"],
            year = request.form["year"],
            description = request.form["description"],
            rating = request.form["rating"],
            ranking = request.form["ranking"],
            review= request.form["review"],
            img_url= request.form["img_url"]
        )
        db.session.add(new_movie)
        db.session.commit()
        print(f"Movie {new_movie.title} created successfully")
        return redirect(url_for("home"))

    return render_template("add.html", form=CreateForm())

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    movie = db.session.get(Movie, id)
    if not movie:
        print("Movie not found")

    if request.method == "POST":
        movie.rating = request.form["rating"]
        movie.review = request.form["review"]
        db.session.commit()
        print(f"Movie {movie.title} updated successfully")
        return redirect(url_for("home"))

    return render_template("edit.html", form = EditForm(), movie=movie)

@app.route("/delete/<int:id>")
def delete(id):
    movie = db.session.get(Movie, id)
    if not movie:
        print("Movie not found")
    else:
        db.session.delete(movie)
        db.session.commit()
        print(f"Movie {movie.title} deleted successfully")
        return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
