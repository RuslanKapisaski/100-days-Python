from flask import Flask, render_template
import requests

app = Flask(__name__)

blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"

@app.route('/')
def home():
    response = requests.get(blogs_url)
    blogs = response.json()
    return render_template("index.html", blogs=blogs)

@app.route('/blog/<int:number>')
def get_blog(number):
    response = requests.get(f'{blogs_url}/{number-1}')
    post = response.json()
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
