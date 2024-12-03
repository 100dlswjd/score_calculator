from PySide6.QtWidgets import QApplication, QWidget, QDialog

from ui.add_widget_form import Ui_add_form

import db.db_tool as db_tool

class AddWidget(QDialog, Ui_add_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("사용자 추가")
        self.pushButton_add.clicked.connect(self.add_member)
        
    def add_member(self):
        name = self.lineEdit.text()
        db_tool.add_member(name)
        self.close()