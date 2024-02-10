from tictactoe.domain.MovePrompt import Move, MovePrompt
from tictactoe.domain.Grid import CellSymbol, Grid
from tictactoe.domain.GameStatusPresenter import GameStatusPresenter
from tictactoe.domain.Turn import Turn
from tictactoe.domain.exceptions import InvalidMove, NoSuchPlayerAssociatedToSymbol


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
        cell_symbol = self.__get_cell_symbol_by_player(self.__player_turn)
        self.__grid.set_cell(row, column, cell_symbol)
        self.__status_presenter.show()
        self.__next_player_turn()

    def get_player_turn(self) -> Turn:
        return self.__player_turn

    def has_ended(self) -> bool:
        has_ended = False
        grid_size = self.__grid.get_size()

        if not has_ended:
            # main diagonal
            consecutive_p1_cells = 0
            consecutive_p2_cells = 0
            for i in range(grid_size):
                cell_symbol = self.__grid.get_cell(i, i)
                if cell_symbol != CellSymbol.Empty:
                    player = self.__get_player_by_cell_symbol(cell_symbol)
                    if player == Turn.PlayerOne:
                        consecutive_p1_cells += 1
                    elif player == Turn.PlayerTwo:
                        consecutive_p2_cells += 1
            if (consecutive_p1_cells == grid_size) or (
                consecutive_p2_cells == grid_size
            ):
                has_ended = True

        if not has_ended:
            # antidiagonal
            consecutive_p1_cells = 0
            consecutive_p2_cells = 0
            for i in range(grid_size):
                j = grid_size - i - 1
                cell_symbol = self.__grid.get_cell(i, j)
                if cell_symbol != CellSymbol.Empty:
                    player = self.__get_player_by_cell_symbol(cell_symbol)
                    if player == Turn.PlayerOne:
                        consecutive_p1_cells += 1
                    elif player == Turn.PlayerTwo:
                        consecutive_p2_cells += 1
            if (consecutive_p1_cells == grid_size) or (
                consecutive_p2_cells == grid_size
            ):
                has_ended = True

        if not has_ended:
            # horizontal
            consecutive_p1_cells = 0
            consecutive_p2_cells = 0
            for i in range(grid_size):
                consecutive_p1_cells = 0
                consecutive_p2_cells = 0
                for j in range(grid_size):
                    cell_symbol = self.__grid.get_cell(i, j)
                    if cell_symbol != CellSymbol.Empty:
                        player = self.__get_player_by_cell_symbol(cell_symbol)
                        if player == Turn.PlayerOne:
                            consecutive_p1_cells += 1
                        elif player == Turn.PlayerTwo:
                            consecutive_p2_cells += 1
                if (consecutive_p1_cells == grid_size) or (
                    consecutive_p2_cells == grid_size
                ):
                    has_ended = True

        if not has_ended:
            # vertical
            consecutive_p1_cells = 0
            consecutive_p2_cells = 0
            for j in range(grid_size):
                consecutive_p1_cells = 0
                consecutive_p2_cells = 0
                for i in range(grid_size):
                    cell_symbol = self.__grid.get_cell(i, j)
                    if cell_symbol != CellSymbol.Empty:
                        player = self.__get_player_by_cell_symbol(cell_symbol)
                        if player == Turn.PlayerOne:
                            consecutive_p1_cells += 1
                        elif player == Turn.PlayerTwo:
                            consecutive_p2_cells += 1
                if (consecutive_p1_cells == grid_size) or (
                    consecutive_p2_cells == grid_size
                ):
                    has_ended = True

        if not has_ended:
            # check if it's a draw
            its_a_draw = True
            for i in range(grid_size):
                for j in range(grid_size):
                    cell_symbol = self.__grid.get_cell(i, j)
                    if cell_symbol == CellSymbol.Empty:
                        its_a_draw = False
            has_ended = its_a_draw
        return has_ended

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

    def __get_cell_symbol_by_player(self, player_turn: Turn) -> CellSymbol:
        if player_turn == Turn.PlayerOne:
            return CellSymbol.Circle
        else:
            return CellSymbol.Cross

    def __get_player_by_cell_symbol(self, cell_symbol: CellSymbol) -> Turn:
        if cell_symbol == CellSymbol.Circle:
            return Turn.PlayerOne
        elif cell_symbol == CellSymbol.Cross:
            return Turn.PlayerTwo
        else:
            raise NoSuchPlayerAssociatedToSymbol()
