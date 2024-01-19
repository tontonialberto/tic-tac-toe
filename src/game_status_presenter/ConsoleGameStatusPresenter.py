from domain.GameStatusPresenter import GameStatusPresenter

class ConsoleGameStatusPresenter(GameStatusPresenter):
    def show(self) -> None:
        print("Show's been called")
        pass