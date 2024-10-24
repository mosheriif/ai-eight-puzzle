import heapq
from .state import State
from .solver import Solver


class A_Star(Solver):
    def __init__(self, board: int, heuristic) -> None:
        super().__init__(board)
        self.heuristic = heuristic

    def solve(self):
        empty_tile = self.get_empty_tile(self.board)
        initial_state = State(board=self.board, empty_tile=empty_tile)
        visited, expanded = set(), set([initial_state])
        # g(n) is number of moves. h(n) heuristic estimate
        frontier = []  # Heap (g(n) + h(n), g(n), state).
        max_depth = 0

        # heapq.heappush(frontier, (0, 0, initial_state))
        heapq.heappush(frontier, initial_state)

        while frontier:
            # f_n, g_n, state = heapq.heappop(frontier)
            state = heapq.heappop(frontier)
            max_depth = max(max_depth, state.g_n)

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
                        h_n = self.heuristic(new_board)
                        # cost = g_n + 1 + h_n
                        new_state.g_n = state.g_n + 1
                        new_state.h_n = h_n
                        # heapq.heappush(frontier, (cost, g_n + 1, new_state))
                        heapq.heappush(frontier, new_state)
                        expanded.add(new_state)

        return {
            'path_to_goal': state.get_moves()[1:],
            'cost_of_path': state.g_n + state.h_n,
            'nodes_expanded': len(expanded),
            'search_depth': max_depth,
            'goal_steps': state.get_path()
        }
