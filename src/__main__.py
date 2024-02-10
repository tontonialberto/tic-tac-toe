from functools import partial
from tictactoe.constants import GRID_SIZE
from tictactoe.domain.TicTacToe import TicTacToe
from tictactoe.domain.Grid import Grid
from tictactoe.domain.Turn import Turn
from tictactoe.game_status_presenter.ConsoleGameStatusPresenter import (
    ConsoleGameStatusPresenter,
)
from tictactoe.move_prompt.ConsoleMovePrompt import (
    ConsoleMovePrompt,
    ConsoleMovePromptOptions,
)


def main():
    grid = Grid(size=GRID_SIZE)
    prompt_options = ConsoleMovePromptOptions(max_value=GRID_SIZE - 1)
    move_prompt = ConsoleMovePrompt(
        input_stream=input, output_stream=print, options=prompt_options
    )
    presenter_output_stream = partial(print, end="")
    status_presenter = ConsoleGameStatusPresenter(
        grid=grid, output_stream=presenter_output_stream
    )
    initial_turn = Turn.PlayerOne
    tic_tac_toe = TicTacToe(
        grid=grid,
        move_prompt=move_prompt,
        status_presenter=status_presenter,
        initial_turn=initial_turn,
    )
    while not tic_tac_toe.has_ended():
        tic_tac_toe.iterate()


if __name__ == "__main__":
    main()
