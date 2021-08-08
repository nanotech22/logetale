from flask import Flask, render_template, url_for, Markup, request, flash, redirect
from flask_mail import Mail, Message
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from config import Config

app = Flask(__name__)

app.config.from_object('config.Config')




@app.route("/")
def index():
    return render_template("pages/index.html", pgname="Home", no_navbar=True, added_css = "index.css")






















if __name__ == "__main__":
    app.run()


