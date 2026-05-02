from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    current_year = time.strftime("%Y")
    return render_template('index.html',year=current_year)



if __name__ == "__main__":
    app.run(debug=True)