from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QMouseEvent

from ui.add_widget_form import Ui_add_form

import db.db_tool as db_tool

class AddWidget(QDialog, Ui_add_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("사용자 추가")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.lineEdit.returnPressed.connect(self.pushButton_add.click)
        self.pushButton_add.clicked.connect(self.add_member)
        self.pushButton.clicked.connect(self.close)
        
    @Slot()
    def mousePressEvent(self, event: QMouseEvent) -> None:        
        try:
            self.dragPos = event.globalPosition().toPoint()            
        except:
            pass
        
    @Slot()
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
        except:
            pass
        
    @Slot()
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.dragPos = None
        
    def add_member(self):
        name = self.lineEdit.text()
        db_tool.add_member(name)
        self.close()
        
if __name__ == "__main__":
    app = QApplication([])
    window = AddWidget()
    window.show()
    app.exec()