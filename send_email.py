import os
import sendgrid
from sendgrid.helpers.mail import Mail


def send_email(subject, body):
    api_key = os.environ.get("SENDGRID_API_KEY")
    email_to = os.environ.get("EMAIL_TO")
    email_from = os.environ.get("EMAIL_FROM")
    sg = sendgrid.SendGridAPIClient(api_key=api_key)
    print(type(body))
    mail = Mail(email_from, email_to, subject, html_content=body)

    # Send an HTTP POST request to /mail/send
    try:
        response = sg.send(mail)
        print(response.status_code)
        print(response.headers)
    except Exception  as e:
        print("error here")
        print (str(e))


if __name__ == "__main__":
    send_email("test", "Test if email sending is working")
