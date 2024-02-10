from typing import Dict
from tictactoe.constants import GRID_SIZE
from tictactoe.domain.MovePrompt import MovePrompt
from tictactoe.domain.TicTacToe import TicTacToe
from tictactoe.domain.Grid import CellSymbol, Grid
from tictactoe.domain.GameStatusPresenter import GameStatusPresenter
from tictactoe.domain.Turn import Turn
from tictactoe.domain.exceptions import InvalidMove
from unittest.mock import ANY, Mock
from unittest import TestCase
from parameterized import parameterized  # type: ignore


class TicTacToeTest(TestCase):

    def test_show_welcome_message_at_first_iteration(self):
        grid = Mock(spec=Grid)
        grid.get_cell.side_effect = [CellSymbol.Empty, CellSymbol.Empty]
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.return_value = [(ANY, ANY), (ANY, ANY)]
        presenter = Mock(spec=GameStatusPresenter)

        game = TicTacToe(
            move_prompt=move_prompt,
            grid=grid,
            status_presenter=presenter,
            initial_turn=Turn.PlayerOne,
        )
        game.iterate()
        game.iterate()

        presenter.show_welcome_message.assert_called_once()

    def test_should_prompt_for_move_and_update_grid_and_display_status_when_iterating(
        self,
    ):
        grid = Mock(spec=Grid)
        grid.get_cell.return_value = CellSymbol.Empty
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.return_value = (0, 0)
        presenter = Mock(spec=GameStatusPresenter)

        game = TicTacToe(
            move_prompt=move_prompt,
            grid=grid,
            status_presenter=presenter,
            initial_turn=Turn.PlayerOne,
        )
        game.iterate()

        move_prompt.prompt.assert_called_once()
        grid.set_cell.assert_called_once_with(0, 0, ANY)
        presenter.show.assert_called_once()

    def test_should_prompt_again_for_move_if_invalid_input(self):
        grid = Mock(spec=Grid)
        grid.get_cell.return_value = CellSymbol.Empty
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.side_effect = [InvalidMove(), InvalidMove(), (0, 0)]
        presenter = Mock(spec=GameStatusPresenter)

        game = TicTacToe(
            grid=grid,
            move_prompt=move_prompt,
            status_presenter=presenter,
            initial_turn=Turn.PlayerOne,
        )
        game.iterate()

        self.assertEqual(3, move_prompt.prompt.call_count)

    def test_should_prompt_again_for_move_if_cell_already_taken(self):
        grid = Mock(spec=Grid)
        grid.get_cell.side_effect = [
            CellSymbol.Circle,
            CellSymbol.Cross,
            CellSymbol.Empty,
        ]
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.side_effect = [(ANY, ANY), (ANY, ANY), (ANY, ANY)]
        presenter = Mock(spec=GameStatusPresenter)

        game = TicTacToe(
            grid=grid,
            move_prompt=move_prompt,
            status_presenter=presenter,
            initial_turn=ANY,
        )
        game.iterate()

        self.assertEqual(3, move_prompt.prompt.call_count)

    @parameterized.expand(  # type: ignore
        [
            (Turn.PlayerOne, Turn.PlayerTwo),
            (Turn.PlayerTwo, Turn.PlayerOne),
        ]
    )
    def test_should_change_player_turn_after_move(
        self, current_turn: Turn, expected_next_turn: Turn
    ):
        grid = Mock(spec=Grid)
        grid.get_cell.return_value = CellSymbol.Empty
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.return_value = (ANY, ANY)
        status_presenter = Mock(spec=GameStatusPresenter)

        game = TicTacToe(
            grid=grid,
            move_prompt=move_prompt,
            status_presenter=status_presenter,
            initial_turn=current_turn,
        )
        game.iterate()

        self.assertEqual(expected_next_turn, game.get_player_turn())

    @parameterized.expand(  # type: ignore
        [
            (Turn.PlayerOne, CellSymbol.Circle),
            (Turn.PlayerTwo, CellSymbol.Cross),
        ]
    )
    def test_should_use_cell_symbol_to_make_move_according_to_player_turn(
        self, current_turn: Turn, expected_cell_symbol: CellSymbol
    ):
        grid = Mock(spec=Grid)
        grid.get_cell.return_value = CellSymbol.Empty
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.return_value = (ANY, ANY)
        status_presenter = Mock(spec=GameStatusPresenter)

        game = TicTacToe(
            grid=grid,
            move_prompt=move_prompt,
            status_presenter=status_presenter,
            initial_turn=current_turn,
        )
        game.iterate()

        grid.set_cell.assert_called_once_with(ANY, ANY, expected_cell_symbol)

    # fmt: off
    @parameterized.expand([  # type: ignore
        (
            GRID_SIZE,
            False,
            {
                "0:0": CellSymbol.Empty, "0:1": CellSymbol.Empty, "0:2": CellSymbol.Empty,
                "1:0": CellSymbol.Empty, "1:1": CellSymbol.Empty, "1:2": CellSymbol.Empty,
                "2:0": CellSymbol.Empty, "2:1": CellSymbol.Empty, "2:2": CellSymbol.Empty,
            },
        ),
        (
            GRID_SIZE,
            False,
            {
                "0:0": CellSymbol.Circle, "0:1": CellSymbol.Empty, "0:2": CellSymbol.Empty,
                "1:0": CellSymbol.Empty, "1:1": CellSymbol.Cross, "1:2": CellSymbol.Empty,
                "2:0": CellSymbol.Empty, "2:1": CellSymbol.Empty, "2:2": CellSymbol.Circle,
            },
        ),
        (
            GRID_SIZE,
            False,
            {
                "0:0": CellSymbol.Circle, "0:1": CellSymbol.Cross, "0:2": CellSymbol.Cross,
                "1:0": CellSymbol.Cross, "1:1": CellSymbol.Circle, "1:2": CellSymbol.Circle,
                "2:0": CellSymbol.Circle, "2:1": CellSymbol.Empty, "2:2": CellSymbol.Empty,
            },
        ),
        (
            GRID_SIZE,
            True,
            {
                "0:0": CellSymbol.Circle, "0:1": CellSymbol.Empty, "0:2": CellSymbol.Empty,
                "1:0": CellSymbol.Empty, "1:1": CellSymbol.Circle, "1:2": CellSymbol.Empty,
                "2:0": CellSymbol.Empty, "2:1": CellSymbol.Empty, "2:2": CellSymbol.Circle,
            },
        ),
        (
            GRID_SIZE,
            True,
            {
                "0:0": CellSymbol.Cross, "0:1": CellSymbol.Empty, "0:2": CellSymbol.Empty,
                "1:0": CellSymbol.Empty, "1:1": CellSymbol.Cross, "1:2": CellSymbol.Empty,
                "2:0": CellSymbol.Empty, "2:1": CellSymbol.Empty, "2:2": CellSymbol.Cross,
            },
        ),
        (
            GRID_SIZE,
            True,
            {
                "0:0": CellSymbol.Empty, "0:1": CellSymbol.Empty, "0:2": CellSymbol.Circle,
                "1:0": CellSymbol.Empty, "1:1": CellSymbol.Circle, "1:2": CellSymbol.Empty,
                "2:0": CellSymbol.Circle, "2:1": CellSymbol.Empty, "2:2": CellSymbol.Empty,
            },
        ),
        (
            GRID_SIZE,
            True,
            {
                "0:0": CellSymbol.Empty, "0:1": CellSymbol.Empty, "0:2": CellSymbol.Cross,
                "1:0": CellSymbol.Empty, "1:1": CellSymbol.Cross, "1:2": CellSymbol.Empty,
                "2:0": CellSymbol.Cross, "2:1": CellSymbol.Empty, "2:2": CellSymbol.Empty,
            },
        ),
        (
            GRID_SIZE,
            True,
            {
                "0:0": CellSymbol.Circle, "0:1": CellSymbol.Circle, "0:2": CellSymbol.Circle,
                "1:0": CellSymbol.Empty, "1:1": CellSymbol.Empty, "1:2": CellSymbol.Empty,
                "2:0": CellSymbol.Empty, "2:1": CellSymbol.Empty, "2:2": CellSymbol.Empty,
            },
        ),
        (
            GRID_SIZE,
            True,
            {
                "0:0": CellSymbol.Empty, "0:1": CellSymbol.Empty, "0:2": CellSymbol.Empty,
                "1:0": CellSymbol.Empty, "1:1": CellSymbol.Empty, "1:2": CellSymbol.Empty,
                "2:0": CellSymbol.Cross, "2:1": CellSymbol.Cross, "2:2": CellSymbol.Cross,
            },
        ),
        (
            GRID_SIZE,
            True,
            {
                "0:0": CellSymbol.Empty, "0:1": CellSymbol.Empty, "0:2": CellSymbol.Empty,
                "1:0": CellSymbol.Cross, "1:1": CellSymbol.Cross, "1:2": CellSymbol.Cross,
                "2:0": CellSymbol.Empty, "2:1": CellSymbol.Empty, "2:2": CellSymbol.Empty,
            },
        ),
        (
            GRID_SIZE,
            True,
            {
                "0:0": CellSymbol.Circle, "0:1": CellSymbol.Empty, "0:2": CellSymbol.Empty,
                "1:0": CellSymbol.Circle, "1:1": CellSymbol.Empty, "1:2": CellSymbol.Empty,
                "2:0": CellSymbol.Circle, "2:1": CellSymbol.Empty, "2:2": CellSymbol.Empty,
            },
        ),
        (
            GRID_SIZE,
            True,
            {
                "0:0": CellSymbol.Empty, "0:1": CellSymbol.Empty, "0:2": CellSymbol.Cross,
                "1:0": CellSymbol.Empty, "1:1": CellSymbol.Empty, "1:2": CellSymbol.Cross,
                "2:0": CellSymbol.Empty, "2:1": CellSymbol.Empty, "2:2": CellSymbol.Cross,
            },
        ),
        (
            GRID_SIZE,
            True,
            {
                "0:0": CellSymbol.Empty, "0:1": CellSymbol.Cross, "0:2": CellSymbol.Empty,
                "1:0": CellSymbol.Empty, "1:1": CellSymbol.Cross, "1:2": CellSymbol.Empty,
                "2:0": CellSymbol.Empty, "2:1": CellSymbol.Cross, "2:2": CellSymbol.Empty,
            },
        ),
        (
            GRID_SIZE,
            True,
            {
                "0:0": CellSymbol.Cross, "0:1": CellSymbol.Circle, "0:2": CellSymbol.Cross,
                "1:0": CellSymbol.Cross, "1:1": CellSymbol.Circle, "1:2": CellSymbol.Circle,
                "2:0": CellSymbol.Circle, "2:1": CellSymbol.Cross, "2:2": CellSymbol.Circle,
            },
        ),
    ])
    # fmt: on
    def test_has_ended(
        self,
        grid_size: int,
        expected_has_ended: bool,
        grid_configuration: Dict[str, CellSymbol],
    ):
        grid = Mock(spec=Grid)

        def fn_grid_configuration(row: int, column: int) -> CellSymbol:
            return grid_configuration[f"{row}:{column}"]

        grid_size = GRID_SIZE
        grid.get_size.return_value = grid_size
        grid.get_cell.side_effect = fn_grid_configuration
        move_prompt = Mock(spec=MovePrompt)
        status_presenter = Mock(spec=GameStatusPresenter)

        game = TicTacToe(
            grid=grid,
            move_prompt=move_prompt,
            status_presenter=status_presenter,
            initial_turn=ANY,
        )

        self.assertEqual(expected_has_ended, game.has_ended())
