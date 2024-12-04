from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt

from ui.score_control_form import Ui_score_control_form

class ScoreControlWidget(QWidget, Ui_score_control_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

if "__main__" == __name__:
    app = QApplication([])
    window = ScoreControlWidget()
    window.show()
    app.exec()