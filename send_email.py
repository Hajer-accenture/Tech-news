import os
import sendgrid
from requests import HTTPError
from sendgrid.helpers.mail import Mail, Email, To, Content


def send_email(subject, body):
    api_key = os.environ.get("SENDGRID_API_KEY")
    email_to = os.environ.get("EMAIL_TO")
    email_from = os.environ.get("EMAIL_FROM")
    sg = sendgrid.SendGridAPIClient(api_key=api_key)
    from_email = Email(email_from)
    to_email = To(email_to)
    mail = Mail(from_email, to_email, subject, body)

    # Send an HTTP POST request to /mail/send
    try:
        response = sg.send(mail)
        print(response.status_code)
        print(response.headers)
    except HTTPError as e:
        print("error here")
        print (e)


if __name__ == "__main__":
    send_email("test", "Test if email sending is working")
