from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bootstrap = Bootstrap5(app)

class WTForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


@app.route("/", methods=['GET', 'POST'])
def login():
    my_form = WTForm()

    if my_form.validate_on_submit():
        match_email = "admin@gmail.com"
        match_password = "12345678"

        if (my_form.password.data == match_password
                and my_form.email.data == match_email):
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=my_form)



if __name__ == '__main__':
    app.run(debug=True)
