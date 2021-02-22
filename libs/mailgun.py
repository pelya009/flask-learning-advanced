import os

from typing import List
from requests import Response, post

FAILED_LOAD_API_KEY = "Failed to get MailGun API key: MAILGUN_API_KEY"
FAILED_LOAD_DOMAIN = "Failed to get MailGun domain: MAILGUN_DOMAIN"
ERROR_SENDING_EMAIL = "Error in sending confirmation email"


class MailGunException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class MailGun:

    MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN")
    MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")

    FROM_TITLE = "Stores REST API"
    FROM_EMAIL = "postmaster@sandboxb37ae2bc538d4b8ead7c7e075cfb5ad6.mailgun.org"

    @classmethod
    def send_email(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        if cls.MAILGUN_API_KEY is None:
            raise MailGunException(FAILED_LOAD_API_KEY)
        if cls.MAILGUN_DOMAIN is None:
            raise MailGunException(FAILED_LOAD_DOMAIN)

        response = post(
            f"http://api.mailgun.net/v3/{cls.MAILGUN_DOMAIN}/messages",
            auth=("api", cls.MAILGUN_API_KEY),
            data={
                "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                "to": email,
                "subject": subject,
                "text": text,
                "html": html
            }
        )

        if response.status_code != 200:
            raise MailGunException(ERROR_SENDING_EMAIL)

        return response
