import datetime
import uuid
from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

from contexts.shared.domain.value_objects.uuid import UUID


class DomainEvent(BaseModel, ABC):
    __event_id: UUID = Field(default_factory=uuid.uuid4())
    __ocurred_on: datetime.datetime = Field(default_factory=datetime.datetime.now())

    def get_event_id(self) -> str:
        return str(self.__event_id.value)

    def get_ocurred_on(self) -> str:
        return str(self.__ocurred_on)

    @abstractmethod
    def get_event_name(self) -> str:
        pass

    @abstractmethod
    def serialize(self) -> str:
        pass
