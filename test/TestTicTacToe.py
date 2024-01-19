from src.domain.MovePrompt import MovePrompt
from src.domain.TicTacToe import TicTacToe
from src.domain.Grid import Grid
from src.domain.GameStatusPresenter import GameStatusPresenter
from unittest.mock import Mock
import unittest

class TicTacToeTest(unittest.TestCase):
    
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