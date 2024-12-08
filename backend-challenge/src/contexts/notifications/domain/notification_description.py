from pydantic import BaseModel


class NotificationDescription(BaseModel):
    value: str
