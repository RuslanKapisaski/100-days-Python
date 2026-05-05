from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

app = Flask(__name__)
url = "https://api.npoint.io/674f5423f73deab1e9a7"
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


@app.route("/")
def home():
    response = requests.get(url)
    posts = response.json()
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=email,
            to_addrs=EMAIL,
            msg=f"Subject: New Contact Form Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        )
        return '<h1>Successfully sent your message</h1>'

@app.route('/post/<int:post_id>')
def post(post_id):
    response = requests.get(f"{url}/{post_id-1}")
    post = response.json()
    return render_template("post.html", post=post)


if __name__ == '__main__':
    app.run(debug=True)
