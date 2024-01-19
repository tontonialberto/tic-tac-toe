from unittest import TestCase
from unittest.mock import Mock

from tictactoe.move_prompt.ConsoleMovePrompt import ConsoleMovePrompt

class TestConsoleMovePrompt(TestCase):
    def test_prompt_should_display_output_message(self):
        output_stream = Mock()
        prompt = ConsoleMovePrompt(output_stream=output_stream)
        
        prompt.prompt()
        
        output_stream.assert_called_once_with("Row: ")