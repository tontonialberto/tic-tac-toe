from abc import ABC, abstractmethod
from typing import Tuple

Move = Tuple[int, int]


class MovePrompt(ABC):
    @abstractmethod
    def prompt(self) -> Tuple[int, int]:
        pass
