from unittest import TestCase
from unittest.mock import Mock, call
from tictactoe.domain.exceptions import InvalidMove
from parameterized import parameterized # type: ignore

from tictactoe.move_prompt.ConsoleMovePrompt import ConsoleMovePrompt
from tictactoe.move_prompt.constants import MSG_MOVE_PROMPT_COLUMN, MSG_MOVE_PROMPT_ROW

class TestConsoleMovePrompt(TestCase):
    def test_prompt_should_display_output_message(self):
        input_stream = Mock()
        input_stream.side_effect = ["1", "2"]
        output_stream = Mock()
        prompt = ConsoleMovePrompt(input_stream=input_stream, output_stream=output_stream)
        
        prompt.prompt()
        
        output_stream.assert_has_calls([call(MSG_MOVE_PROMPT_ROW), call(MSG_MOVE_PROMPT_COLUMN)], any_order=False)
        
    def test_prompt_should_read_move_from_input_stream(self):
        input_stream = Mock()
        input_stream.side_effect = ["1", "2"]
        output_stream = Mock()
        prompt = ConsoleMovePrompt(input_stream=input_stream, output_stream=output_stream)
        
        move = prompt.prompt()
        
        self.assertEqual(move[0], 1)
        self.assertEqual(move[1], 2)
        
    @parameterized.expand([ # type: ignore
        ("Not a number", "0"),
        ("0", "Not a number"),
        ("-1", "0"),
        ("0", "-1"),
        ("3", "0"),
        ("0", "3"),
    ])
    def test_prompt_should_fail_if_input_is_invalid(self, row_input: str, column_input: str):
        input_stream = Mock()
        input_stream.side_effect = [row_input, column_input]
        output_stream = Mock()
        prompt = ConsoleMovePrompt(input_stream=input_stream, output_stream=output_stream)
        
        def raised():
            prompt.prompt()
            
        self.assertRaises(InvalidMove, raised)