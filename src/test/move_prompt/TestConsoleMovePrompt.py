from unittest import TestCase
from unittest.mock import Mock, call
from parameterized import parameterized  # type: ignore
from tictactoe.constants import GRID_SIZE
from tictactoe.domain.exceptions import InvalidMove

from tictactoe.move_prompt.ConsoleMovePrompt import (
    ConsoleMovePrompt,
    ConsoleMovePromptOptions,
)
from tictactoe.move_prompt.constants import MSG_MOVE_PROMPT_COLUMN, MSG_MOVE_PROMPT_ROW


class TestConsoleMovePrompt(TestCase):
    PROMPT_OPTIONS = ConsoleMovePromptOptions(max_value=GRID_SIZE - 1)

    def test_prompt_should_display_output_message(self):
        input_stream = Mock()
        input_stream.side_effect = ["1", "2"]
        output_stream = Mock()
        prompt = ConsoleMovePrompt(
            input_stream=input_stream,
            output_stream=output_stream,
            options=self.PROMPT_OPTIONS,
        )

        prompt.prompt()

        output_stream.assert_has_calls(
            [call(MSG_MOVE_PROMPT_ROW), call(MSG_MOVE_PROMPT_COLUMN)], any_order=False
        )

    def test_prompt_should_read_move_from_input_stream(self):
        input_stream = Mock()
        input_stream.side_effect = ["1", "2"]
        output_stream = Mock()
        prompt = ConsoleMovePrompt(
            input_stream=input_stream,
            output_stream=output_stream,
            options=self.PROMPT_OPTIONS,
        )

        move = prompt.prompt()

        self.assertEqual(move[0], 1)
        self.assertEqual(move[1], 2)

    @parameterized.expand(  # type: ignore
        [
            ("Not a number", "0"),
            ("0", "Not a number"),
            ("-1", "0"),
            ("0", "-1"),
            (str(GRID_SIZE), "0"),
            ("0", str(GRID_SIZE)),
        ]
    )
    def test_prompt_should_fail_if_input_is_invalid(
        self, row_input: str, column_input: str
    ):
        input_stream = Mock()
        input_stream.side_effect = [row_input, column_input]
        output_stream = Mock()
        prompt = ConsoleMovePrompt(
            input_stream=input_stream,
            output_stream=output_stream,
            options=self.PROMPT_OPTIONS,
        )

        def raised():
            prompt.prompt()

        self.assertRaises(InvalidMove, raised)
