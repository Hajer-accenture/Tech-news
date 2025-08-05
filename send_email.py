import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content


def send_email(subject, body):
    api_key = os.environ.get("SendGrid_API_KEY")
    email_to = os.environ.get("EMAIL_TO")
    email_from = "hajer.hammouda@accenture.com"

    sg = sendgrid.SendGridAPIClient(api_key=api_key)
    from_email = Email(email_from)
    to_email = To(email_to)
    content = Content("text/plain", body)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)