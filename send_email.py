import os
import requests

def send_email(subject, body):
    api_key = os.environ.get("SendGrid_API_KEY")
    email_to = os.environ.get("EMAIL_TO")
    email_from = "noreply@technews.com"

    sendgrid_api = "https://sendgrid.com/v3/mail/send"

    if not (api_key and email_to and email_from):
        raise ValueError("Missing Email environment variables")

    response = requests.post(
        sendgrid_api, headers={
            "Authorization": f"Bearer {api_key}",
            "content_type": "application/json"
        },
        json={
            "personalizations": [{"to": [{"email": email_to}]}],
            "from": {"email": email_from},
            "subject": subject,
            "content": [{"type": "text/plain", "value": body}]
        }
    )

    if response.status_code != 202:
        raise Exception(f"Failed to send email: {response.status_code}, {response.text}")

    print("Email Sent Successfully!")