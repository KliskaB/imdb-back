import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender():
    def send_email(self, user_email, user_verification_token):
        port = 465 
        password = "Proba123!"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("imdb.back@gmail.com", password)
            sender_email = "imdb.back@gmail.com"
            receiver_email = user_email
            message = MIMEMultipart("alternative")
            message["Subject"] = "Verify your email address"
            message["From"] = sender_email
            message["To"] = receiver_email
            text = """\
                Hi,
                How are you?
                Please, verify your email address."""
            html = """\
                <html>
                <body>
                    <p>Hi,<br>
                    Your verification token is<br>
                    <b> """ + user_verification_token + """ </b>
                    </p>
                </body>
                </html>
                """
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            message.attach(part1)
            message.attach(part2)
            server.sendmail(sender_email, receiver_email, message.as_string())

    