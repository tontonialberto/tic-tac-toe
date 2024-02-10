from tictactoe.domain.MovePrompt import MovePrompt
from tictactoe.domain.TicTacToe import TicTacToe
from tictactoe.domain.Grid import CellSymbol, Grid
from tictactoe.domain.GameStatusPresenter import GameStatusPresenter
from tictactoe.domain.Turn import Turn
from tictactoe.domain.exceptions import InvalidMove
from unittest.mock import ANY, Mock
from unittest import TestCase
from parameterized import parameterized # type: ignore

class TicTacToeTest(TestCase):
    
    def test_should_prompt_for_move_and_update_grid_and_display_status_when_iterating(self):
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.return_value = (0, 0)
        grid = Mock(spec=Grid)
        presenter = Mock(spec=GameStatusPresenter)
        
        game = TicTacToe(move_prompt=move_prompt, grid=grid, status_presenter=presenter, initial_turn=Turn.PlayerOne)
        game.iterate()
        
        move_prompt.prompt.assert_called_once()
        grid.set_cell.assert_called_once_with(0, 0, ANY)
        presenter.show.assert_called_once()
        
    def test_should_ask_again_for_move_if_invalid_input(self):
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.side_effect = [InvalidMove(), InvalidMove(), (0, 0)]
        grid = Mock(spec=Grid)
        presenter = Mock(spec=GameStatusPresenter)
        
        game = TicTacToe(grid=grid, move_prompt=move_prompt, status_presenter=presenter, initial_turn=Turn.PlayerOne)
        game.iterate()
        
        self.assertEqual(3, move_prompt.prompt.call_count)
    
    @parameterized.expand([ # type: ignore
        (Turn.PlayerOne, Turn.PlayerTwo),
        (Turn.PlayerTwo, Turn.PlayerOne),
    ])
    def test_should_change_player_turn_after_move(self, current_turn: Turn, expected_next_turn: Turn):
        grid = Mock(spec=Grid)
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.return_value = (ANY, ANY)
        status_presenter = Mock(spec=GameStatusPresenter)
        
        game = TicTacToe(grid=grid, move_prompt=move_prompt, status_presenter=status_presenter, initial_turn=current_turn)
        game.iterate()
        
        self.assertEqual(expected_next_turn, game.get_player_turn())
        
    @parameterized.expand([ # type: ignore
        (Turn.PlayerOne, CellSymbol.Circle),
        (Turn.PlayerTwo, CellSymbol.Cross)
    ])
    def test_should_use_cell_symbol_to_make_move_according_to_player_turn(self, current_turn: Turn, expected_cell_symbol: CellSymbol):
        grid = Mock(spec=Grid)
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.return_value = (ANY, ANY)
        status_presenter = Mock(spec=GameStatusPresenter)
        
        game = TicTacToe(grid=grid, move_prompt=move_prompt, status_presenter=status_presenter, initial_turn=current_turn)
        game.iterate()
        
        grid.set_cell.assert_called_once_with(ANY, ANY, expected_cell_symbol)