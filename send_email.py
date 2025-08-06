import os
import sendgrid
from sendgrid.helpers.mail import Mail


def send_email(subject, body):
    api_key = os.environ.get("SENDGRID_API_KEY")
    email_to = os.environ.get("EMAIL_TO")
    email_from = os.environ.get("EMAIL_FROM")
    sg = sendgrid.SendGridAPIClient(api_key=api_key)

    email_list = [email.strip() for email in email_to.split(",") if email.strip()]
    mail = Mail(email_from, email_list, subject, body)

    # Send an HTTP POST request to /mail/send
    response = sg.send(mail)
    print(response.status_code)
    print(response.headers)


if __name__ == "__main__":
    send_email("test", "Test if email sending is working")
