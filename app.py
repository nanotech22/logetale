from flask import Flask, render_template, url_for, Markup, request, flash, redirect
from flask_mail import Mail, Message
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from config import Config

app = Flask(__name__)

app.config.from_object('config.Config')


#Mail 
mail = Mail(app)




@app.route("/")
def index():
    return render_template("pages/index.html", pgname="Home", no_navbar=True, added_css = "index.css")


@app.route('/personal')
def personal():
    return render_template('pages/personal.html', pgname="Personal", no_navbar=True, added_css="personal.css")









class LoginForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message="Not a valid email address.")])
    text = TextAreaField('Message', validators=[DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Send')



#todo: use sendgrid to send emails, since gmail doesn't allow less secure apps to do it anymore. 
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        d = request.form.to_dict()

        message_html = '<h1>Message from: ' + d['username'] +'</h1>'
        message_html += '<h3>Email address: ' + d['email'] + '</h3>'
        message_html += d['text']

        print(message_html)
        
        msg = Message('Logetale Website Contact Message', recipients=['websitenowgf@gmail.com', 'leo.herr@colorado.edu'])
        msg.body = ('')
        msg.html = (message_html)
        mail.send(msg)
        flash(f'Your message was sent.')
        return redirect(url_for('index'))
    else:
        return render_template("pages/contact.html", pgname="Contact", no_navbar=True, form=form, added_css="css/contact.css")







#@app.route('/contact')
#def contact():
#    return render_template('pages/contact.html', pgname="Contact", no_navbar=True, added_css="contact.css")






















if __name__ == "__main__":
    app.run()


