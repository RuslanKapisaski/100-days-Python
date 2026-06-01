from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

class Base (DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Message(db.Model):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(30))
    email: Mapped[str] = mapped_column(db.String(30))
    subject: Mapped[str] = mapped_column(db.String(60))
    content: Mapped[str] = mapped_column(db.String(500))

    def __repr__(self):
        return f"<Message id={self.id} - created successfully>"

with app.app_context():
    db.create_all()
    print("Database created successfully")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        new_message = Message(
        username = request.form.get("name"),
        email = request.form.get("email"),
        subject = request.form.get("subject"),
        content = request.form.get("message"))
        db.session.add(new_message)
        db.session.commit()
        print('Message added successfully')
        return render_template("index.html")

    return render_template("contact.html")

@app.route("/reviews")
def reviews():
    return render_template("testimonials.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)