import db.db_tool as db_tool
import ctypes
import os
import json
import sys
import datetime

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QClipboard, QMouseEvent, QPixmap
from PySide6.QtCore import Qt, Slot

from ui.scoreboard_form import Ui_Scoreboard

from score_widget import ScoreWidget
from add_widget import AddWidget
from score_control_widget import ScoreControlWidget

config_path = os.path.join(os.path.expandvars("%userprofile%"),"documents","ddatg","scoreboard","config.json")

example_data ={
  "1": "1",
  "2": "2",
  "3": "3"
}
# 파일이 없으면 코드 실행
if not os.path.exists(config_path):
    with open(config_path,"w") as f:
        f.write(json.dumps(example_data,indent=4))
        f.close()
        

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path).replace("\\","/")

class ScoreBoard(QMainWindow, Ui_Scoreboard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        
        self.combobox_setting()
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("scoreboard")
        # 윈도우 타이틀 바 없애기 | 배경 투명
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        # 투명설정
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.refresh_members()
        
        self.pushButton_add_member.clicked.connect(self.add_member)
        self.pushButton_close.clicked.connect(self.close)

    def combobox_setting(self):
        import json
        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for key in data.keys():
                self.comboBox_site.addItem(data[key])
                
    def refresh_members(self):
        # 위젯 초기화
        try:
            for i in reversed(range(self.verticalLayout.count())):
                widget = self.verticalLayout.itemAt(i).widget()
                widget.deleteLater()
        except :
            pass
        
        # 위젯 추가하기
        for name in db_tool.getnames():
            widget = ScoreWidget()
            self.verticalLayout.addWidget(widget)
            widget.set_name(name)   
            
        # 점수 컨트롤 위젯 추가
        self.score_control_widget = ScoreControlWidget()
        self.verticalLayout.addWidget(self.score_control_widget)
        self.score_control_widget.pushButton_insert_score.clicked.connect(self.btn_insert_score_click)
        self.score_control_widget.pushButton_get_score.clicked.connect(self.btn_get_score_click)
        
    @Slot()
    def add_member(self):
        # 위젯 뛰우고 현재 메인 윈도우는 컨트롤 못하게 하기
        self.add_widget = AddWidget()        
        self.add_widget.setModal(True)
        self.add_widget.show()
        self.add_widget.exec()
        
        self.refresh_members()
        
    def btn_insert_score_click(self):
        site = self.comboBox_site.currentIndex() + 1
        
        insert_data = []
        # 위젯 리스트 가져와서 반복문 돌리기
        for i in range(self.verticalLayout.count()):
            widget = self.verticalLayout.itemAt(i).widget()
            try:
                if widget.participate:
                    insert_data.append([widget.checkBox_name.text(), int(widget.label_score.text())])
            except:
                pass
        
        now = datetime.datetime.now()
        
        query = f"insert into score (SITE, REG_DATE"
        for data in insert_data:
            query += f", {data[0]}"
        query += ") values ("
        query += f"{site}, datetime('{now}')"
        for data in insert_data:
            query += f", {data[1]}"
        query += ")"
        db_tool.insert(query)
        self.refresh_members()
        
    def btn_get_score_click(self):
        site = self.comboBox_site.currentIndex() + 1
        name = self.comboBox_site.currentText()
        # 클립보드 복사
        clipboard = QClipboard()
        clipboard.setText(db_tool.get_total_score(site, name) + db_tool.get_1_1_score(site, name))        
        self.refresh_members()
        
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
        
    def closeEvent(self, event):
        db_tool.close()
        return super().closeEvent(event)
        
if __name__ == "__main__":
    icon_path = resource_path("score_board.png")
    app = QApplication([])
    app.setWindowIcon(QPixmap(icon_path))
    window = ScoreBoard()
    window.show()
    app.exec()