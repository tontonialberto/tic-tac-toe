from abc import ABC, abstractmethod


class GameStatusPresenter(ABC):
    @abstractmethod
    def show_welcome_message(self) -> None:
        pass

    @abstractmethod
    def show(self) -> None:
        pass
