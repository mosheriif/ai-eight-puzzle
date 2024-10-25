import time

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout
from puzzle_solver.a_star import A_Star
from puzzle_solver.utils import manhattan_distance


class AlgorithmsButtons(QWidget):
    def __init__(self, get_state, start_animation, update_content) -> None:
        super().__init__()

        self.get_state = get_state
        self.start_animation = start_animation
        self.update_content = update_content

        layout = QHBoxLayout()

        self.bfs = QPushButton("BFS")
        self.dfs = QPushButton("DFS")
        self.ids = QPushButton("IDS")
        self.a_star_manhattan = QPushButton("A* Manhattan")
        self.a_star_euclidean = QPushButton("A* Euclidean")

        layout.addWidget(self.bfs)
        layout.addWidget(self.dfs)
        layout.addWidget(self.ids)
        layout.addWidget(self.a_star_manhattan)
        layout.addWidget(self.a_star_euclidean)

        self.setLayout(layout)

        self.a_star_manhattan.clicked.connect(self.on_click)

    def on_click(self):

        solver = A_Star(self.get_state(), manhattan_distance)

        start = time.time()
        res = solver.solve()
        end = time.time()

        res['time_taken'] = end - start

        self.start_animation(res['goal_steps'])
        self.update_content(res)
