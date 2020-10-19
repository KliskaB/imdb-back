from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class EmailSender():
    def send_email(self, receiver_email, subject, data, template):
        from_email = "imdb.back@gmail.com"
        to = receiver_email
        html_message = render_to_string(template, {'data': data})
        plain_message = strip_tags(html_message)
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

    