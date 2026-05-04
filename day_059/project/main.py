from flask import Flask,render_template
import requests

app = Flask(__name__)
url = "https://api.npoint.io/674f5423f73deab1e9a7"

@app.route("/")
def home():
    response = requests.get(url)
    posts = response.json()
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<int:post_id>')
def post(post_id):
    response = requests.get(f"{url}/{post_id-1}")
    post = response.json()
    return render_template("post.html", post=post)


if __name__ == '__main__':
    app.run(debug=True)
