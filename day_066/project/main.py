from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET','POST'])
def random():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = choice(all_cafes)
    return jsonify(cafe={
        'id': random_cafe.id,
        'name': random_cafe.name,
        'map_url': random_cafe.map_url,
        'img_url': random_cafe.img_url,
        'location': random_cafe.location,
        'seats': random_cafe.seats,
        'toilet': random_cafe.has_toilet,
        'wifi': random_cafe.has_wifi,
        'can_take_calls': random_cafe.can_take_calls,
        'coffee_price': random_cafe.coffee_price
    })

@app.route("/all", methods=['GET','POST'])
def get_all():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes= [{
        'id': cafe.id,
        'name': cafe.name,
        'map_url': cafe.map_url,
        'img_url': cafe.img_url,
        'location': cafe.location,
        'seats': cafe.seats,
        'toilet': cafe.has_toilet,
        'wifi': cafe.has_wifi,
        'can_take_calls': cafe.can_take_calls,
        'coffee_price': cafe.coffee_price
    }for cafe in all_cafes])

@app.route("/search")
def find_by_location():
    query_location = request.args.get("loc")
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalars().all()
    if len(cafes) > 0:
        return jsonify(cafes=[{
    'id': cafe.id,
    'name': cafe.name,
    'map_url': cafe.map_url,
    'img_url': cafe.img_url,
    'location': cafe.location,
    'seats': cafe.seats,
    'toilet': cafe.has_toilet,
    'wifi': cafe.has_wifi,
    'can_take_calls': cafe.can_take_calls,
    'coffee_price': cafe.coffee_price
    } for cafe in cafes])
    else:
        return jsonify({'Not found!': "Sorry, we do not have a cafe at this location"})

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(entity=Cafe, ident=cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.get(entity=Cafe, ident=cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe."}), 200
    else:
        return jsonify(respose={"failed":"No cafe with that id was found."}), 404


if __name__ == '__main__':
    app.run(debug=True)
