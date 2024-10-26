from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class TransitionWidget(QWidget):
    def __init__(self, previous_state, next_state):
        super().__init__()

        self.previous_state = previous_state
        self.next_state = next_state

        vbox = QHBoxLayout()

        self.back_btn = QPushButton('Back')
        self.forward_btn = QPushButton('Forward')

        vbox.addWidget(self.back_btn)
        vbox.addWidget(self.forward_btn)

        self.setLayout(vbox)

        self.back_btn.clicked.connect(self.back_action)
        self.forward_btn.clicked.connect(self.forward_action)

    def back_action(self):
        self.previous_state()

    def forward_action(self):
        self.next_state()
