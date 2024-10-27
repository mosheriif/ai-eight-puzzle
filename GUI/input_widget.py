from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt 
from puzzle_solver.validate_input import validator

class InputWidget(QWidget):
    def __init__(self, update_grid):
        super().__init__()
        self.update_grid = update_grid

        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)

        self.input_field = QLineEdit()
        self.input_field.setStyleSheet('border-radius: 5px; width: 150px; height: 40px; background-color: #ece5da; padding: 5px;')
        self.input_field.setPlaceholderText('Enter initial board')

        self.update_btn = QPushButton('Update')
        self.update_btn.setStyleSheet('background-color: #6b705c; border-radius: 5px; width: 90px; height: 40px; color: #f5f5f5; font-weight: bold;')

        vbox.addWidget(self.input_field, 0, alignment=Qt.AlignBottom)
        vbox.addWidget(self.update_btn, 0, alignment=Qt.AlignTop)

        self.setLayout(vbox)

        self.update_btn.clicked.connect(self.on_click)

    def on_click(self):
        new_state = self.input_field.text()
        valid, comment = validator.isSolvable(new_state)
        if valid:
            self.update_grid(int(new_state))
        else:
            QMessageBox.warning(self, 'Invalid Input', comment)
            self.input_field.clear()
