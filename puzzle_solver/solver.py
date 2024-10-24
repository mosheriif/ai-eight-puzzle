from .state import State


class Solver:
    def __init__(self, board: int) -> None:
        self.board = board
        self.dirs = [
            (-1, 'LEFT'),  # Left
            (1, 'RIGHT'),  # Right
            (-3, 'UP'),    # Up
            (3, 'DOWN')    # Down
        ]

    def is_solved(self, state: State) -> bool:
        return state.board == 12345678

    def solve(self):
        pass

    def is_valid_tile(self, before: int, after: int) -> bool:
        if after < 0 or after >= 9:
            return False
        if abs(before - after) == 1 and (before // 3) != (after // 3):
            return False
        return True

    def get_empty_tile(self, board: int) -> int:
        pos = 8
        while board % 10 != 0:
            board //= 10
            pos -= 1
        return pos

    def change_two_tiles(self, board: int, first: int, second: int) -> int:
        value = (board // (10 ** (8 - second))) % 10
        board -= value * 10 ** (8 - second)
        board += value * 10 ** (8 - first)
        return board
