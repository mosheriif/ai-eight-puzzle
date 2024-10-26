from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget
from .left_widget import LeftWidget
from .right_widget import RightWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("8 Puzzle Solver")
        self.setGeometry(700, 300, 600, 400)

        hbox = QHBoxLayout()

        self.left_part = LeftWidget(self.update_content)
        self.right_part = RightWidget(self.left_part.grid_puzzle.update_grid)

        hbox.addWidget(self.left_part)
        hbox.addWidget(self.right_part)

        central_widget = QWidget()
        central_widget.setLayout(hbox)
        self.setCentralWidget(central_widget)

    def update_content(self, content):
        self.right_part.output_widget.update_content(content)