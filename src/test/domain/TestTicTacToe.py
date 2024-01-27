from tictactoe.domain.MovePrompt import MovePrompt
from tictactoe.domain.TicTacToe import TicTacToe
from tictactoe.domain.Grid import Grid
from tictactoe.domain.GameStatusPresenter import GameStatusPresenter
from tictactoe.domain.exceptions import InvalidMove
from unittest.mock import Mock
from unittest import TestCase

class TicTacToeTest(TestCase):
    
    def test_should_prompt_for_move_and_update_grid_and_display_status_when_iterating(self):
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.return_value = (0, 0)
        grid = Mock(spec=Grid)
        presenter = Mock(spec=GameStatusPresenter)
        
        game = TicTacToe(move_prompt=move_prompt, grid=grid, status_presenter=presenter)
        game.iterate()
        
        move_prompt.prompt.assert_called_once()
        grid.set_square.assert_called_once_with(0, 0)
        presenter.show.assert_called_once()
        
    def test_should_ask_again_for_move_if_invalid_input(self):
        move_prompt = Mock(spec=MovePrompt)
        move_prompt.prompt.side_effect = [InvalidMove(), InvalidMove(), (0, 0)]
        grid = Mock(spec=Grid)
        presenter = Mock(spec=GameStatusPresenter)
        
        game = TicTacToe(grid=grid, move_prompt=move_prompt, status_presenter=presenter)
        game.iterate()
        
        self.assertEqual(3, move_prompt.prompt.call_count)