class GameException(Exception):
    pass


class InvalidMove(GameException):
    pass


class InvalidCellPosition(GameException):
    pass


class NoSuchPlayerAssociatedToSymbol(GameException):
    pass
