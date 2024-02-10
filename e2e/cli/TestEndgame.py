import subprocess
from typing import Tuple
from unittest import TestCase
from parameterized import parameterized  # type: ignore

from e2e.cli.constants import TICTACTOE_RUN_COMMAND


class TestEndgame(TestCase):

    # fmt: off
    @parameterized.expand([  # type: ignore
        (
            "Player one wins on the main diagonal.",
            [
                "0", "0",
                "1", "2",
                "1", "1",
                "0", "2",
                "2", "2"
            ],
            "\n".join([
                " - - - ",
                "|O| |X|",
                " - - - ",
                "| |O|X|",
                " - - - ",
                "| | |O|",
                " - - -"
            ])
        ),
        (
            "Player two wins on the antidiagonal.",
            [
                "0", "0",
                "0", "2",
                "2", "2",
                "1", "1",
                "1", "0",
                "2", "0",
            ],
            "\n".join([
                " - - - ",
                "|O| |X|",
                " - - - ",
                "|O|X| |",
                " - - - ",
                "|X| |O|",
                " - - - "
            ])
        ),
        (
            "It's a draw.",
            [
                "0", "1",
                "0", "0",
                "1", "1",
                "0", "2",
                "2", "0",
                "2", "1",
                "2", "2",
                "1", "2",
                "1", "0",
            ],
            "\n".join([
                " - - - ",
                "|X|O|X|",
                " - - - ",
                "|O|O|X|",
                " - - - ",
                "|O|X|O|",
                " - - - "
            ])
        ),
    ])
    # fmt: on
    def test_endgame(
        self, description: str, moves: Tuple[str, str], expected_endgame: str
    ):
        process = subprocess.Popen(
            TICTACTOE_RUN_COMMAND,
            shell=True,
            universal_newlines=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        stdout = process.communicate("\n".join(moves))[0]

        print(description)
        print(stdout)
        self.assertIn(expected_endgame, stdout)
        self.assertEqual(0, process.returncode)
