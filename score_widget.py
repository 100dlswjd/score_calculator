from PySide6.QtWidgets import QApplication, QWidget

from ui.score_widget_form import Ui_score_form

class ScoreWidget(QWidget, Ui_score_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.participate = False
        self.pushButton_m.setEnabled(self.participate)
        self.pushButton_p.setEnabled(self.participate)
        self.checkBox_name.stateChanged.connect(self.checkbox_change)
        
        self.pushButton_p.clicked.connect(self.btn_p_click)
        self.pushButton_m.clicked.connect(self.btn_m_click)
        
    def set_name(self, name):
        self.checkBox_name.setText(name)
        
    def btn_p_click(self):
        self.label_score.setText(str(int(self.label_score.text()) + 1))
        
    def btn_m_click(self):
        self.label_score.setText(str(int(self.label_score.text()) - 1))
        
    def checkbox_change(self):
        if self.checkBox_name.isChecked():
            self.participate = True
        else:
            self.participate = False
        self.pushButton_m.setEnabled(self.participate)
        self.pushButton_p.setEnabled(self.participate)
        
if __name__ == "__main__":
    app = QApplication([])
    window = ScoreWidget()
    window.show()
    app.exec()