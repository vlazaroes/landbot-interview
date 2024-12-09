from abc import ABC, abstractmethod

from contexts.notifications.domain.notification import Notification


class Notifier(ABC):
    @abstractmethod
    def notify(self, notification: Notification) -> None:
        pass
