from pydantic import BaseModel


class Notification(BaseModel):
    topic: str
    description: str
