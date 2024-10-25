from PyQt5.QtWidgets import QWidget, QVBoxLayout

from .output_widget import OutputWidget
from .input_widget import InputWidget


class RightWidget(QWidget):
    def __init__(self, udpate_grid):
        super().__init__()

        vbox = QVBoxLayout()

        self.output_widget = OutputWidget()
        self.input_widget = InputWidget(udpate_grid)

        vbox.addWidget(self.output_widget)
        vbox.addWidget(self.input_widget)

        self.setLayout(vbox)
