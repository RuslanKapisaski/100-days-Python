from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def blog():
    blogs_url ="https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blogs_url)
    blogs = response.json()

    return render_template("index.html", blogs=blogs)

if __name__ == '__main__':
    app.run(debug=True)