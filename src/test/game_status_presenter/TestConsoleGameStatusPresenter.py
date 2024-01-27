from typing import Iterable
from unittest import TestCase
from unittest.mock import Mock, call
from parameterized import parameterized # type: ignore
from tictactoe.constants import GRID_SIZE

from tictactoe.domain.Grid import CellSymbol, Grid
from tictactoe.game_status_presenter.ConsoleGameStatusPresenter import ConsoleGameStatusPresenter


class TestGameStatusPresenter(TestCase):
    @parameterized.expand([ # type: ignore
        (
            [CellSymbol.Empty for _ in range(GRID_SIZE * GRID_SIZE)],
            " - - - \n" \
            "| | | |\n" \
            " - - - \n" \
            "| | | |\n" \
            " - - - \n" \
            "| | | |\n" \
            " - - - \n"
        ),
        (
            [
                CellSymbol.Circle, CellSymbol.Empty, CellSymbol.Empty,
                CellSymbol.Empty, CellSymbol.Empty, CellSymbol.Cross,
                CellSymbol.Empty, CellSymbol.Empty, CellSymbol.Empty,
            ],
            " - - - \n" \
            "|O| | |\n" \
            " - - - \n" \
            "| | |X|\n" \
            " - - - \n" \
            "| | | |\n" \
            " - - - \n"
        ),
        (
            [
                CellSymbol.Circle, CellSymbol.Cross, CellSymbol.Empty,
                CellSymbol.Empty, CellSymbol.Circle, CellSymbol.Cross,
                CellSymbol.Empty, CellSymbol.Empty, CellSymbol.Circle,
            ],
            " - - - \n" \
            "|O|X| |\n" \
            " - - - \n" \
            "| |O|X|\n" \
            " - - - \n" \
            "| | |O|\n" \
            " - - - \n"
        )
    ])
    def test_show_empty_grid(self, cells: Iterable[CellSymbol], expected_output: str):
        grid = Mock(spec=Grid)
        grid.get_cell.side_effect = cells
        grid.get_size.return_value = GRID_SIZE
        output_stream = Mock()
        presenter = ConsoleGameStatusPresenter(grid=grid, output_stream=output_stream)
        
        presenter.show()
        
        output_stream.assert_has_calls([call(c) for c in expected_output])
        