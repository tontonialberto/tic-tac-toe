from abc import ABC, abstractmethod


class GameStatusPresenter(ABC):
    @abstractmethod
    def show(self) -> None:
        pass
