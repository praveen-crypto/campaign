from campaign import app
from flask_mail import Mail,Message

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'theparttimewriters@gmail.com',
    MAIL_PASSWORD = 'the_parttime_writers',
))


mail = Mail(app)

def send(otp):
    try:
        sender=("OTP Verification", "theparttimewriters@gmail.com")
        msg = Message("Testing for OTP Verification", sender=sender, recipients=["kumarspraveen57@gmail.com"])
        msg.body = otp
        mail.send(msg)
        return True
    except Exception as e:
        print(e)
        return False
    