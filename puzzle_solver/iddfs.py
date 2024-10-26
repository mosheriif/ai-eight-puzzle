from .solver import Solver
from .state import State

class dfs(Solver):
    def __init__(self, board: int) -> None:
        super().__init__(board)

    def solve(self):
        empty_tile = self.get_empty_tile(self.board)
        initial_state = State(board=self.board, empty_tile=empty_tile)
        idepth = -1
        state = initial_state

        while not (self.is_solved(state)):
            idepth += 1
            state = initial_state

            visited, expanded = set(), set([initial_state])
            frontier = []
            max_depth = 0
            frontier.append((initial_state, 0))

            while frontier:
                state, depth = frontier.pop()
                visited.add(state)
                max_depth = max(max_depth, depth)

                if self.is_solved(state):
                    break

                empty_tile = state.empty_tile

                for dir, move in self.dirs:
                    if self.is_valid_tile(empty_tile, empty_tile + dir):
                        new_empty_tile = empty_tile + dir
                        new_board = self.change_two_tiles(
                            state.board, empty_tile, new_empty_tile)

                        new_state = State(
                            board=new_board, empty_tile=new_empty_tile, parent=state, move=move)

                        if (new_state not in visited) and (depth + 1 <= idepth):
                            frontier.append((new_state, depth + 1))
                            expanded.add(new_state)
    
        return {
            'path_to_goal': state.get_moves()[1:],
            'cost_of_path': idepth,
            'nodes_expanded': len(expanded),
            'search_depth': max_depth,
            'goal_steps': state.get_path()
        }