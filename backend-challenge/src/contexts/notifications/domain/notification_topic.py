from pydantic import BaseModel


class NotificationTopic(BaseModel):
    value: str
