from pydantic import UUID4, BaseModel


class UUID(BaseModel):
    value: UUID4
