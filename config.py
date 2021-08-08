import os

class Config():

    #debug mode
    DEBUG = True


    #mail api stuff
    SENDGRID_API_KEY="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"

    #secret key for forms, prevent CSRF attack
    SECRET_KEY = "2Ogp0L9O0Ssq1YXkMIPe"

    #mail config
    MAIL_SERVER = "smtp.sendgrid.net"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = "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"
    MAIL_DEFAULT_SENDER = "websitenowgf@gmail.com"

    #recaptcha
    #RECAPTCHA_PUBLIC_KEY = ""
    #RECAPTCHA_PRIVATE_KEY = ""