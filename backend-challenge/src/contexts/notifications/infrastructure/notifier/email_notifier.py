import smtplib
import ssl
from email.message import EmailMessage

from contexts.notifications.domain.notification import Notification
from contexts.notifications.domain.notifier import Notifier


class EmailNotifier(Notifier):
    def __init__(
        self,
        hostname: str,
        port: int,
        username: str,
        password: str,
        sender: str,
        recipient: str,
    ) -> None:
        self.__hostname = hostname
        self.__port = port
        self.__username = username
        self.__password = password
        self.__sender = sender
        self.__recipient = recipient

    def notify(self, notification: Notification) -> None:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            host=self.__hostname, port=self.__port, context=context
        ) as smtp:
            email = self.__create_email(notification)
            smtp.login(user=self.__username, password=self.__password)
            smtp.sendmail(
                from_addr=self.__sender,
                to_addrs=self.__recipient,
                msg=email.as_string(),
            )

    def __create_email(self, notification: Notification) -> EmailMessage:
        email = EmailMessage()
        email["From"] = self.__sender
        email["To"] = self.__recipient
        email["Subject"] = "🔔 Webhook Notification"
        email.set_content(notification.description.value)
        return email
