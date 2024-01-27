from enum import Enum
from typing import List

from tictactoe.domain.exceptions import InvalidCellPosition


class CellSymbol(Enum):
    Empty = "EMPTY"
    Cross = "CROSS"
    Circle = "CIRCLE"

class Grid:
    def __init__(self, size: int) -> None:
        self.__size = size
        self.__cells = [CellSymbol.Empty for _ in range(size * size)]
    
    def set_cell(self, row: int, column: int, symbol: CellSymbol) -> None:
        cell_index = self.__coordinates_to_index(row, column)
        self.__cells[cell_index] = symbol
    
    def get_cell(self, row: int, column: int) -> CellSymbol:
        cell_index = self.__coordinates_to_index(row, column)
        return self.__cells[cell_index]
    
    def get_cells(self) -> List[CellSymbol]:
        return self.__cells
    
    def get_size(self) -> int:
        return self.__size
    
    def __coordinates_to_index(self, row: int, column: int) -> int:
        if (row < 0 or row >= self.__size) or (column < 0 or column >= self.__size):
            raise InvalidCellPosition()
        index = (row * self.__size) + column
        return index