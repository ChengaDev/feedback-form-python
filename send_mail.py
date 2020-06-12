import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '57647633f17109'
    password = '27fa5f6003c552'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = "gazit.chen@gmail.com"
    receiver_email = "gazit.chen@gmail.com"
    msg = MIMEText(message, 'html')
    msg['Subject'] = "Lexus Feedback"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send Email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
