import os

class Config():

    #debug mode
    DEBUG = True


    #mail api stuff
    SENDGRID_API_KEY=""
    MAIL_DEFAULT_SENDER=""

    #secret key for forms, prevent CSRF attack
    SECRET_KEY = ""

    #mail config
    MAIL_SERVER = "smtp.sendgrid.net"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = ""
    MAIL_DEFAULT_SENDER = ""

    #recaptcha
    RECAPTCHA_PUBLIC_KEY = ""
    RECAPTCHA_PRIVATE_KEY = ""