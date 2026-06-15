from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    pokemon = None

    if request.method == "POST":

        name = request.form["pokemon"].lower()

        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{name}"
        )

        if response.status_code == 200:

            data = response.json()

            pokemon = {
                "name": data["name"].title(),
                "image": data["sprites"]["front_default"],
                "height": data["height"],
                "weight": data["weight"],
                "types": [t["type"]["name"] for t in data["types"]],
                "abilities": [a["ability"]["name"] for a in data["abilities"]]
            }

    return render_template(
        "index.html",
        pokemon=pokemon
    )


if __name__ == "__main__":
    app.run(debug=True)