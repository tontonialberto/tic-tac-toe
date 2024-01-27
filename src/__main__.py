from tictactoe.constants import GRID_SIZE
from tictactoe.domain.TicTacToe import TicTacToe
from tictactoe.domain.Grid import Grid
from tictactoe.game_status_presenter.ConsoleGameStatusPresenter import ConsoleGameStatusPresenter
from tictactoe.move_prompt.ConsoleMovePrompt import ConsoleMovePrompt, ConsoleMovePromptOptions

def main():
    grid = Grid()
    prompt_options = ConsoleMovePromptOptions(max_value=GRID_SIZE - 1)
    move_prompt = ConsoleMovePrompt(input_stream=input, output_stream=print, options=prompt_options)
    status_presenter = ConsoleGameStatusPresenter()
    tic_tac_toe = TicTacToe(grid=grid,move_prompt=move_prompt, status_presenter=status_presenter)
    tic_tac_toe.iterate()

if __name__ == "__main__":
    main()