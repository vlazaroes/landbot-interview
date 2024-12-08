import datetime
import uuid
from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

from contexts.shared.domain.value_objects.uuid import UUID


class DomainEvent(BaseModel, ABC):
    event_id: UUID = Field(default_factory=uuid.uuid4())
    ocurred_on: datetime.datetime = Field(default_factory=datetime.datetime.now())

    def get_event_id(self) -> str:
        return str(self.event_id.value)

    @abstractmethod
    def get_event_name(self) -> str:
        pass

    @abstractmethod
    def serialize(self) -> str:
        pass
