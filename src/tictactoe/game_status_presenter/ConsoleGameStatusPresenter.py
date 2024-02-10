from typing import Callable
from tictactoe.domain.GameStatusPresenter import GameStatusPresenter
from tictactoe.domain.Grid import CellSymbol, Grid


class ConsoleGameStatusPresenter(GameStatusPresenter):
    def __init__(self, grid: Grid, output_stream: Callable[[str], None]) -> None:
        self.__grid = grid
        self.__write = output_stream

    def show(self) -> None:

        n_rows = self.__grid.get_size()
        n_cells_per_row = self.__grid.get_size()

        def write_horizontal_row():
            for _ in range(n_cells_per_row):
                self.__write(" ")
                self.__write("-")
            self.__write(" ")
            self.__write("\n")

        def write_cell_row(row: int):
            for column in range(n_cells_per_row):
                cell = self.__grid.get_cell(row, column)
                chr = symbol_to_character(cell)
                self.__write("|")
                self.__write(chr)
            self.__write("|")
            self.__write("\n")

        def symbol_to_character(symbol: CellSymbol) -> str:
            if symbol == CellSymbol.Empty:
                return " "
            elif symbol == CellSymbol.Circle:
                return "O"
            else:
                return "X"

        write_horizontal_row()

        for row in range(n_rows):
            write_cell_row(row)
            write_horizontal_row()
