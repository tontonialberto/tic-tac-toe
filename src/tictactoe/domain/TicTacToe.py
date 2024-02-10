from tictactoe.domain.MovePrompt import Move, MovePrompt
from tictactoe.domain.Grid import CellSymbol, Grid
from tictactoe.domain.GameStatusPresenter import GameStatusPresenter
from tictactoe.domain.Turn import Turn
from tictactoe.domain.exceptions import InvalidMove


class TicTacToe:
    def __init__(
        self,
        grid: Grid,
        move_prompt: MovePrompt,
        status_presenter: GameStatusPresenter,
        initial_turn: Turn,
    ):
        self.__grid = grid
        self.__move_prompt = move_prompt
        self.__status_presenter = status_presenter
        self.__player_turn = initial_turn

    def iterate(self):
        row, column = self.__get_move()
        cell_symbol = self.__get_cell_symbol_by_player_turn(self.__player_turn)
        self.__grid.set_cell(row, column, cell_symbol)
        self.__status_presenter.show()
        self.__next_player_turn()

    def get_player_turn(self) -> Turn:
        return self.__player_turn

    def __get_move(self) -> Move:
        is_valid_move = False
        row, column = (0, 0)  # dummy workaround to avoid type checker complaints
        while not is_valid_move:
            try:
                row, column = self.__move_prompt.prompt()
                is_valid_move = True
                return row, column
            except InvalidMove:
                pass
        return row, column

    def __next_player_turn(self) -> None:
        if self.__player_turn == Turn.PlayerOne:
            self.__player_turn = Turn.PlayerTwo
        else:
            self.__player_turn = Turn.PlayerOne

    def __get_cell_symbol_by_player_turn(self, player_turn: Turn) -> CellSymbol:
        if player_turn == Turn.PlayerOne:
            return CellSymbol.Circle
        else:
            return CellSymbol.Cross
