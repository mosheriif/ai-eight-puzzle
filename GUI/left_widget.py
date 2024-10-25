from PyQt5.QtWidgets import QWidget, QVBoxLayout

from .grid_puzzle import GridPuzzle
from .transition_widget import TransitionWidget
from .algorithms_buttons import AlgorithmsButtons


class LeftWidget(QWidget):
    def __init__(self, update_content):
        super().__init__()

        vbox = QVBoxLayout()

        self.grid_puzzle = GridPuzzle()
        self.transition_widget = TransitionWidget(
            self.grid_puzzle.previous_state, self.grid_puzzle.next_state)
        self.algorithms_buttons = AlgorithmsButtons(
            self.grid_puzzle.get_state, self.grid_puzzle.start_animation, update_content)

        vbox.addWidget(self.grid_puzzle)
        vbox.addWidget(self.transition_widget)
        vbox.addWidget(self.algorithms_buttons)

        self.setLayout(vbox)
