from .MovePrompt import MovePrompt
from .Grid import Grid
from .GameStatusPresenter import GameStatusPresenter

class TicTacToe:
    def __init__(self, grid: Grid, move_prompt: MovePrompt, status_presenter: GameStatusPresenter):
        self.__grid = grid
        self.__move_prompt = move_prompt
        self.__status_presenter = status_presenter
        
    def iterate(self):
        row, column = self.__move_prompt.prompt()
        self.__grid.set_square(row, column)
        self.__status_presenter.show()