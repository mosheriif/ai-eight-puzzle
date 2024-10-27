import time

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout
from puzzle_solver.a_star import A_Star
from puzzle_solver.utils import manhattan_distance, euclidean_distance
from puzzle_solver.bfs import BFS
from puzzle_solver.dfs import dfs
from puzzle_solver.iddfs import iddfs


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


        self.bfs.setStyleSheet('background-color: #6b705c; border-radius : 25; width: 90; height: 40; color: #f5f5f5; font-weight: bold; padding: 5;')
        self.dfs.setStyleSheet('background-color: #6b705c; border-radius : 25; width: 90; height: 40; color: #f5f5f5; font-weight: bold; padding: 5;')
        self.ids.setStyleSheet('background-color: #6b705c; border-radius : 25; width: 90; height: 40; color: #f5f5f5; font-weight: bold; padding: 5;')
        self.a_star_manhattan.setStyleSheet('background-color: #6b705c; border-radius : 25; width: 90; height: 40; color: #f5f5f5; font-weight: bold; padding: 5;')
        self.a_star_euclidean.setStyleSheet('background-color: #6b705c; border-radius : 25; width: 90; height: 40; color: #f5f5f5; font-weight: bold; padding: 5;')

        layout.addWidget(self.bfs)
        layout.addWidget(self.dfs)
        layout.addWidget(self.ids)
        layout.addWidget(self.a_star_manhattan)
        layout.addWidget(self.a_star_euclidean)

        self.setLayout(layout)

        self.bfs.clicked.connect(self.on_click)
        self.dfs.clicked.connect(self.on_click)
        self.ids.clicked.connect(self.on_click)
        self.a_star_manhattan.clicked.connect(self.on_click)
        self.a_star_euclidean.clicked.connect(self.on_click)

    def on_click(self):

        if self.bfs.clicked:
            solver = BFS(self.get_state())
        elif self.dfs.clicked:
            solver = dfs(self.get_state())
        elif self.ids.clicked:
            solver = iddfs(self.get_state())
        elif self.a_star_manhattan.clicked:
            solver = A_Star(self.get_state(), manhattan_distance)
        elif self.a_star_euclidean.clicked:
            solver = A_Star(self.get_state(), euclidean_distance)

        start = time.time()
        res = solver.solve()
        end = time.time()

        res['time_taken'] = end - start

        self.start_animation(res['goal_steps'])
        self.update_content(res)
