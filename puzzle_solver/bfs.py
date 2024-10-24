from collections import deque
from .state import State
from .solver import Solver


class BFS(Solver):
    def __init__(self, board: int) -> None:
        super().__init__(board)

    def solve(self):
        empty_tile = self.get_empty_tile(self.board)
        initial_state = State(board=self.board, empty_tile=empty_tile)
        visited, expanded = set(), set([initial_state])

        frontier = deque([initial_state])

        while frontier:
            state = frontier.popleft()

            if self.is_solved(state):
                break

            visited.add(state)

            empty_tile = state.empty_tile
            for dir, move in self.dirs:
                if self.is_valid_tile(empty_tile, empty_tile + dir):
                    new_empty_tile = empty_tile + dir
                    new_board = self.change_two_tiles(
                        state.board, empty_tile, new_empty_tile)

                    new_state = State(
                        board=new_board, empty_tile=new_empty_tile, parent=state, move=move)

                    if new_state not in visited:
                        new_state.g_n = state.g_n + 1
                        frontier.append(new_state)
                        expanded.add(new_state)

        return {
            'path_to_goal': state.get_moves()[1:],
            'cost_of_path': state.g_n,
            'nodes_expanded': len(expanded),
            'search_depth': state.g_n,
            'goal_steps': state.get_path()
        }
