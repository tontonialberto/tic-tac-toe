from typing import Callable
from tictactoe.domain.MovePrompt import MovePrompt, Move
from tictactoe.domain.exceptions import InvalidMove
from tictactoe.move_prompt.constants import MSG_MOVE_PROMPT_COLUMN, MSG_MOVE_PROMPT_ROW

class ConsoleMovePrompt(MovePrompt):
    def __init__(self, input_stream: Callable[[], str], output_stream: Callable[[str], None]):
        self.__read = input_stream
        self.__write = output_stream
    
    def prompt(self) -> Move:
        self.__write(MSG_MOVE_PROMPT_ROW)
        row_str = self.__read()
        
        self.__write(MSG_MOVE_PROMPT_COLUMN)
        column_str = self.__read()
        
        try:
            row = int(row_str)
            column = int(column_str)
        except ValueError:
            raise InvalidMove()
        
        if row < 0 or row > 2:
            raise InvalidMove()
        if column < 0 or column > 2:
            raise InvalidMove()
        
        return int(row), int(column)