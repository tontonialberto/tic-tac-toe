from enum import Enum
from typing import List


class CellSymbol(Enum):
    Empty = "EMPTY"
    Cross = "CROSS"
    Circle = "CIRCLE"

class Grid:
    def __init__(self, size: int) -> None:
        self.__size = size
    
    def set_cell(self, row: int, column: int) -> None:
        pass
    
    def get_cell(self, row: int, column: int) -> CellSymbol:
        return CellSymbol.Empty
    
    def get_cells(self) -> List[CellSymbol]:
        return []
    
    def get_size(self) -> int:
        return self.__size