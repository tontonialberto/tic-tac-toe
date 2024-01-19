from tictactoe.domain.TicTacToe import TicTacToe
from tictactoe.domain.Grid import Grid
from tictactoe.game_status_presenter.ConsoleGameStatusPresenter import ConsoleGameStatusPresenter
from tictactoe.move_prompt.ConsoleMovePrompt import ConsoleMovePrompt

def main():
    grid = Grid()
    move_prompt = ConsoleMovePrompt(output_stream=print)
    status_presenter = ConsoleGameStatusPresenter()
    tic_tac_toe = TicTacToe(grid=grid,move_prompt=move_prompt, status_presenter=status_presenter)
    tic_tac_toe.iterate()

if __name__ == "__main__":
    main()