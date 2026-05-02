from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = 'aa10ce11b9809ab168219090d4b3e121'
@app.route('/')
def home():
    return "<h3>Hello to the age guessing app! <br>Please enter your name in the URL in format '/guess/myname'</h3>"

@app.route('/guess/<name>')
def guess(name):

    name_res = requests.get(f'https://api.genderize.io?name={name}&apikey={API_KEY}')
    age_res = requests.get(f"https://api.agify.io?name=michael")
    data1 = name_res.json()
    data2 = age_res.json()
    print(name_res.json())
    name = data1['name']
    gender = data1['gender']
    age = data2['age']
    print(age_res.json())
    # age = res.json().get("age").value()
    return render_template("index.html", name=name,gender=gender,age=age)



if __name__ == '__main__':
    app.run(debug=True)