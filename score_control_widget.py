from PySide6.QtWidgets import QApplication, QWidget


from ui.score_control_form import Ui_score_control_form

class ScoreControlWidget(QWidget, Ui_score_control_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        