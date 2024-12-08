from abc import ABC, abstractmethod

from contexts.shared.domain.events.domain_event import DomainEvent


class EventBus(ABC):
    @abstractmethod
    def publish_domain_events(self, domain_events: list[DomainEvent]) -> None:
        pass
