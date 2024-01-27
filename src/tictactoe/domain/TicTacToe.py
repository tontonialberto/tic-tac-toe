from tictactoe.domain.MovePrompt import Move, MovePrompt
from tictactoe.domain.Grid import CellSymbol, Grid
from tictactoe.domain.GameStatusPresenter import GameStatusPresenter
from tictactoe.domain.exceptions import InvalidMove

class TicTacToe:
    def __init__(self, grid: Grid, move_prompt: MovePrompt, status_presenter: GameStatusPresenter):
        self.__grid = grid
        self.__move_prompt = move_prompt
        self.__status_presenter = status_presenter
        
    def iterate(self):
        row, column = self.__get_move()
        self.__grid.set_cell(row, column, CellSymbol.Circle)
        self.__status_presenter.show()
        
    def __get_move(self) -> Move:
        is_valid_move = False
        row, column = (0, 0) # dummy workaround to avoid type checker complaints
        while not is_valid_move:
            try:
                row, column = self.__move_prompt.prompt()
                is_valid_move = True
                return row, column
            except InvalidMove:
                pass
        return row, column