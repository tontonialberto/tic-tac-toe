from typing import Tuple
from domain.MovePrompt import MovePrompt

class ConsoleMovePrompt(MovePrompt):
    def prompt(self) -> Tuple[int, int]:
        return (0,0)