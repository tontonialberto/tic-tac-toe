from abc import ABC, abstractmethod
from typing import Tuple

from tictactoe.domain.Turn import Turn

Move = Tuple[int, int]


class MovePrompt(ABC):
    @abstractmethod
    def prompt(self, player_turn: Turn) -> Tuple[int, int]:
        pass
