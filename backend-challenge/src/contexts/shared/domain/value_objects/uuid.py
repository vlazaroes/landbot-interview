import uuid

from pydantic import UUID4, BaseModel


class UUID(BaseModel):
    value: UUID4

    @staticmethod
    def create() -> "UUID":
        return UUID(value=uuid.uuid4())
