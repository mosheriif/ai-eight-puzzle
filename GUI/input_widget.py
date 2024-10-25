from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton


class InputWidget(QWidget):
    def __init__(self, update_grid):
        super().__init__()
        self.update_grid = update_grid

        vbox = QHBoxLayout()

        self.input_field = QLineEdit()
        self.update_btn = QPushButton('Update')

        vbox.addWidget(self.input_field)
        vbox.addWidget(self.update_btn)

        self.setLayout(vbox)

        self.update_btn.clicked.connect(self.on_click)

    def on_click(self):
        new_state = self.input_field.text()
        self.update_grid(int(new_state))
