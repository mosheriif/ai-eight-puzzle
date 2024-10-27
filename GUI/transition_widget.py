from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QPolygon, QColor, QBrush
from PyQt5.QtCore import QPoint, Qt

class ArrowButton(QPushButton):
    def __init__(self, direction, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.direction = direction  # 'left' or 'right'
        self.setFixedSize(50, 50)  # Set a fixed size for the button
        self.setStyleSheet("background-color: transparent; border: none;")  # Make background transparent
        self.hovered = False  # Track hover state

    def enterEvent(self, event):
        self.hovered = True
        self.update()  # Repaint the button
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.hovered = False
        self.update()  # Repaint the button
        super().leaveEvent(event)

    def paintEvent(self, event):
        # Set up the painter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Set brush color based on hover state
        color = QColor("darkgray") if self.hovered else QColor("lightgray")
        brush = QBrush(color)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        # Define the points for the arrow shape based on the direction
        if self.direction == 'left':
            points = [QPoint(self.width(), 0), QPoint(0, self.height() // 2), QPoint(self.width(), self.height())]
        elif self.direction == 'right':
            points = [QPoint(0, 0), QPoint(self.width(), self.height() // 2), QPoint(0, self.height())]

        # Draw the arrow shape as a polygon
        arrow = QPolygon(points)
        painter.drawPolygon(arrow)

        # End painting
        painter.end()

class TransitionWidget(QWidget):
    def __init__(self, previous_state, next_state):
        super().__init__()

        self.previous_state = previous_state
        self.next_state = next_state

        vbox = QHBoxLayout()

        # Create custom "Back" and "Forward" buttons with arrow shapes
        self.back_btn = ArrowButton('left')
        self.forward_btn = ArrowButton('right')

        vbox.addWidget(self.back_btn)
        vbox.addWidget(self.forward_btn)

        self.setLayout(vbox)

        self.back_btn.clicked.connect(self.back_action)
        self.forward_btn.clicked.connect(self.forward_action)

    def back_action(self):
        self.previous_state()

    def forward_action(self):
        self.next_state()
