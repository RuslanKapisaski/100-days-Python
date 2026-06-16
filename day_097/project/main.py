from flask import Flask, render_template, redirect
import stripe
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


@app.route("/")
def home():
    products = [
        {
            "name": "Python Course",
            "price": "$19",
            "amount": 1900
        },
        {
            "name": "Flask Course",
            "price": "$29",
            "amount": 2900
        },
        {
            "name": "Data Science Course",
            "price": "$39",
            "amount": 3900
        }
    ]

    return render_template(
        "index.html",
        products=products
    )


@app.route("/checkout/<int:amount>")
def checkout(amount):

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": "Digital Product",
                    },
                    "unit_amount": amount,
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url="http://127.0.0.1:5000/success",
        cancel_url="http://127.0.0.1:5000/cancel",
    )

    return redirect(session.url, code=303)


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/cancel")
def cancel():
    return render_template("cancel.html")


if __name__ == "__main__":
    app.run(debug=True)