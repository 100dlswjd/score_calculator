from PySide6.QtWidgets import QApplication, QWidget

from ui.score_widget_form import Ui_score_form

def resource_path(relative_path):
    import sys
    import os
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path).replace("\\", "/")

class ScoreWidget(QWidget, Ui_score_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.participate = False
        
        # 체크박스 이미지 변경
        self.checkbox_styleSheet = "QCheckBox::indicator:checked {image: url(" + resource_path("check_icon.png") + ");} QCheckBox::indicator:unchecked {image: url(" + resource_path("x_icon.png") + ");}" 
        
        self.checkBox_name.setStyleSheet(self.checkbox_styleSheet)
        
        
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
    