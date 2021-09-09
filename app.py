from flask import Flask, render_template, url_for, Markup, request, flash, session, redirect
from flask_mail import Mail, Message
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from config import Config

#sitemap SEO
from flask_sitemap import Sitemap

app = Flask(__name__)
ext = Sitemap(app=app)

app.config.from_object('config.Config')


#Mail 
mail = Mail(app)




@app.route("/")
def index():
    return render_template("pages/index.html", pgname="Home", added_css = "index.css", 
                            metadesc = "Home page of mathematician Leo Herr. Read about Leo's research and teaching or find easy ways to contact him.")


@app.route('/personal')
def personal():
    return render_template('pages/personal.html', pgname="Personal", added_css="personal.css",
                            metadesc = "Personal page of Leo Herr. Read about his hobbies and listen to his music. ")









class LoginForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message="Not a valid email address.")])
    text = TextAreaField('Message', validators=[DataRequired()])
    recaptcha = RecaptchaField()
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
        return render_template("pages/contact.html", pgname="Contact", form=form, added_css="css/contact.css",
                                metadesc = "How to contact Leo Herr. ")







#@app.route('/contact')
#def contact():
#    return render_template('pages/contact.html', pgname="Contact", no_navbar=True, added_css="contact.css")












@ext.register_generator
def index():
    # Not needed if you set SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True
    yield 'index', {}









if __name__ == "__main__":
    app.run()


