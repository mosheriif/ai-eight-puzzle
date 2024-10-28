from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class GridPuzzle(QWidget):
    def __init__(self):
        super().__init__()

        self.current_state = 12345678
        self.current_step = 0
        self.all_states = []
        self.timer = QTimer(self)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.initUI()

    def initUI(self):
        for i in range(9):
            button = QLabel(f"{i}")
            button.setFont(QFont('Arial', 20))
            button.setStyleSheet('border-radius: 50px;')
            button.setAlignment(Qt.AlignCenter)
            button.setFixedHeight(160)

            # if i == 0:
            #     button.setStyleSheet(
            #         'background-color: #484030; color: white; border-radius: 5px;')
            # else:
            #     button.setStyleSheet(
            #         'background-color: #ffa500; color: #ad3333; border-radius: 5px;')

            if i == 0:
                button.setStyleSheet(
                    'background-color: #2a9d8f; color: white; border-radius: 5px;')
            else:
                button.setStyleSheet(
                    'background-color: #f4a261; color: #ad3333; border-radius: 5px;')

            self.grid_layout.addWidget(button, i // 3, i % 3)

    def update_grid(self, new_state):
        self.current_state = new_state
        pos = 8
        while pos >= 0:
            button = self.grid_layout.itemAtPosition(
                pos // 3, pos % 3).widget()
            button.setText(str(new_state % 10))

            if new_state % 10 == 0:
                button.setStyleSheet(
                    'background-color: #2a9d8f; color: white; border-radius: 5px;')
            else:
                button.setStyleSheet(
                    'background-color: #f4a261; color: #ad3333; border-radius: 5px;')

            new_state //= 10
            pos -= 1

    def get_state(self):
        return self.current_state

    def start_animation(self, states):
        self.all_states = states
        self.current_step = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_grid_step)
        self.timer.start(500)

    def update_grid_step(self):
        if self.current_step < len(self.all_states):
            state = self.all_states[self.current_step]
            self.update_grid(state)

            self.current_step += 1
        else:
            self.timer.stop()

    def previous_state(self):
        if self.current_step > 0:
            self.current_step -= 1
            state = self.all_states[self.current_step]
            self.update_grid(state)

    def next_state(self):
        if self.current_step < len(self.all_states):
            state = self.all_states[self.current_step]
            self.update_grid(state)

            self.current_step += 1
