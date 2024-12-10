from abc import ABC

from pydantic import BaseModel, Field

from src.contexts.shared.domain.events.domain_event import DomainEvent


class AggregateRoot(BaseModel, ABC):
    domain_events: list[DomainEvent] = Field(default=[])

    def record_domain_event(self, domain_event: DomainEvent) -> None:
        self.domain_events.append(domain_event)

    def pull_domain_events(self) -> list[DomainEvent]:
        domain_events = self.domain_events.copy()
        self.domain_events.clear()
        return domain_events
