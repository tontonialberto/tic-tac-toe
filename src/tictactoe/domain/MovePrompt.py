from abc import ABC, abstractmethod
from typing import Tuple

class MovePrompt(ABC):
    @abstractmethod
    def prompt(self) -> Tuple[int, int]:
        pass