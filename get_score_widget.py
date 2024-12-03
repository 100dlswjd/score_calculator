from PySide6.QtWidgets import QApplication, QWidget


from ui.get_score_widget_form import Ui_get_score_form

class GetScoreWidget(QWidget, Ui_get_score_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        