from unittest import TestCase
from parameterized import parameterized # type: ignore
from tictactoe.constants import GRID_SIZE

from tictactoe.domain.Grid import CellSymbol, Grid
from tictactoe.domain.exceptions import InvalidCellPosition

class TestGrid(TestCase):
    def test_should_have_correct_size(self):
        grid = Grid(size=GRID_SIZE)
        
        self.assertEqual(GRID_SIZE, grid.get_size())
        self.assertEqual(GRID_SIZE * GRID_SIZE, len(grid.get_cells()))
        
    def test_should_be_empty_after_init(self):
        grid = Grid(size=GRID_SIZE)
        for cell in grid.get_cells():
            self.assertEqual(CellSymbol.Empty, cell)
            
    def test_should_set_and_get_cell_correctly(self):
        grid = Grid(size=GRID_SIZE)
        grid.set_cell(0, 0, CellSymbol.Circle)
        self.assertEqual(CellSymbol.Circle, grid.get_cell(0, 0))
    
    @parameterized.expand([ # type: ignore
        (GRID_SIZE, GRID_SIZE + 1, GRID_SIZE + 1),
        (GRID_SIZE, -1, 0),
        (GRID_SIZE, 0, -1),
    ])
    def test_should_fail_if_cell_is_invalid(self, grid_size: int, row: int, column: int):
        grid = Grid(size=grid_size)
        
        def raised():
            grid.set_cell(row, column, CellSymbol.Circle)
        
        self.assertRaises(InvalidCellPosition, raised)