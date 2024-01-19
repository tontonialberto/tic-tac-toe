from typing import Callable, Tuple
from tictactoe.domain.MovePrompt import MovePrompt

class ConsoleMovePrompt(MovePrompt):
    def __init__(self, output_stream: Callable[[str], None]):
        self.__write = output_stream
    
    def prompt(self) -> Tuple[int, int]:
        self.__write("Row: ")
        return (0,0)