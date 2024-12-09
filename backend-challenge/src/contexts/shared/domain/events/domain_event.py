import datetime
from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

from contexts.shared.domain.value_objects.uuid import UUID


class DomainEvent(BaseModel, ABC):
    event_id: UUID = Field(default_factory=UUID.create)
    ocurred_on: datetime.datetime = Field(default_factory=datetime.datetime.now)

    def get_event_id(self) -> str:
        return str(self.event_id.value)

    def get_ocurred_on(self) -> str:
        return str(self.ocurred_on)

    @abstractmethod
    def get_event_name(self) -> str:
        pass

    @abstractmethod
    def serialize(self) -> str:
        pass
