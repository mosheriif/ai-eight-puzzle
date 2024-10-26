from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class OutputWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout()

        self.nodes_expanded = QLabel("")
        self.path_cost = QLabel("")
        self.search_depth = QLabel("")
        self.time_taken = QLabel("")
        self.moves = QLabel("")
        self.moves.setWordWrap(True)

        layout.addWidget(self.nodes_expanded)
        layout.addWidget(self.path_cost)
        layout.addWidget(self.search_depth)
        layout.addWidget(self.time_taken)
        layout.addWidget(self.moves)

        self.setLayout(layout)

    def update_content(self, content):
        self.nodes_expanded.setText(
            f'Nodes Expanded: {str(content['nodes_expanded'])}')
        self.path_cost.setText(f'Path Cost: {str(content['cost_of_path'])}')
        self.search_depth.setText(
            f'Search Depth: {str(content['search_depth'])}')
        self.time_taken.setText(
            f'Time Taken: {str(round(content['time_taken'], 4))} ms')
        self.moves.setText(f'Moves: {str(content['path_to_goal'])}')
