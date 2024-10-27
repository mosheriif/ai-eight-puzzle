from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea
from PyQt5.QtCore import Qt


class OutputWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout()

        self.nodes_expanded = QLabel("")
        self.path_cost = QLabel("")
        self.search_depth = QLabel("")
        self.time_taken = QLabel("")

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setFixedHeight(100)

        moves_widget = QWidget()
        moves_layout = QVBoxLayout(moves_widget)

        self.moves = QLabel("")
        self.moves.setWordWrap(True)
        moves_layout.addWidget(self.moves)
        scroll_area.setWidget(moves_widget)

        layout.addWidget(self.nodes_expanded)
        layout.addWidget(self.path_cost)
        layout.addWidget(self.search_depth)
        layout.addWidget(self.time_taken)
        layout.addWidget(scroll_area)

        self.setLayout(layout)

    def update_content(self, content):
        self.nodes_expanded.setText(f'Nodes Expanded: {str(content["nodes_expanded"])}')
        self.path_cost.setText(f'Path Cost: {str(content["cost_of_path"])}')
        self.search_depth.setText(f'Search Depth: {str(content["search_depth"])}')
        self.time_taken.setText(f'Time Taken: {str(round(content["time_taken"], 4))} ms')
        self.moves.setText(f'Moves: {str(content["path_to_goal"])}')
