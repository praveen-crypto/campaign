from email.mime.text import MIMEText
import smtplib

def send_mail(to_email,message):
    from_email='theparttimewriters@gmail.com'
    msg = MIMEText(message)
    #msg.set_unixfrom('author')
    msg['To'] =  to_email
    msg['From'] = from_email
    msg['Subject'] = 'Verification'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print('reached1')
    server.ehlo()
    server.starttls()
    server.ehlo()
    print('reached2')
    server.login(from_email, 'the_parttime_writers')
    server.sendmail(from_email,to_email,msg.as_string())
    print('reached3')
    server.quit()

    print('successfully sent the mail.')


send_mail('kumarspraveen57@gmail.com', 'This is a Test Message.')


