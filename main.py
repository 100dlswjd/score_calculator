
import ctypes
import os
import json
import sys
import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PySide6.QtGui import QClipboard, QMouseEvent, QPixmap
from PySide6.QtCore import Qt, Slot, QThread, Signal, QTimer

from ui.scoreboard_form import Ui_Scoreboard

from score_widget import ScoreWidget
from add_widget import AddWidget
from score_control_widget import ScoreControlWidget

from ui.msg_widget_form import Ui_msg_form

db_tool = None

class ServerConnector(QThread):
    connectd = Signal()
    failed = Signal()
    def run(self):
        global db_tool
        try:
            import db.db_tool_server as tool
            db_tool = tool
            # import db.db_tool as tool
            self.connectd.emit()
        except:
            self.failed.emit()

class MsgWidget(QWidget, Ui_msg_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
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

class MsgDialog(QDialog, Ui_msg_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.close)
        
        self.label_msg.setText("")
        self.connect_timer = QTimer()
        self.count = 0
        
        self.server_thread = ServerConnector()
        self.server_thread.connectd.connect(self.on_server_connected)
        self.server_thread.failed.connect(self.server_close)
        
        self.connect_sucssesful = False
        
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
        
    def connection_timer(self):
        self.count += 1
        msg = "서버 연결중"
        self.label_msg.setText(msg + "." * self.count)
        if self.count > 3:
            self.count = 0
            
    def connect_start(self):
        self.connect_timer.timeout.connect(self.connection_timer)
        self.connect_timer.start(500)
        self.server_thread.start()
        
    def on_server_connected(self):
        self.connect_timer.stop()
        self.label_msg.setText("서버 연결 성공")
        self.connect_sucssesful = True
        self.close()
        
    def server_close(self):
        self.connect_timer.stop()
        self.label_msg.setText("서버 연결 실패")
        self.connect_sucssesful = False
        

config_path = os.path.join(os.path.expandvars("%userprofile%"),"documents","ddatg","scoreboard","config.json")

example_data ={
    "1": "롤토체스",
    "2": "서든어택",
    "3": "롤"
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
        self.add_widget.set_db_tool(db_tool)
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
        
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        db_name = db_tool.db_name
        table_name = db_tool.table_name
        
        query = f"insert into {db_name}.{table_name} (SITE, REG_DATE"
        # query = f"insert into {table_name} (SITE, REG_DATE"
        
        for data in insert_data:
            query += f", {data[0]}"
        query += ") values ("
        # query += f"{site}, datetime('{now}')"
        query += f"{site}, '{now}'"
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
        self.msg_widget = MsgWidget()
        self.msg_widget.label_msg.setText("점수가 복사되었습니다.")
        self.msg_widget.show()
        
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
    try:
        icon_path = resource_path("score_board.png")

        app = QApplication([])
        app.setWindowIcon(QPixmap(icon_path))

        # 서버 연결 위젯 실행
        msg_widget = MsgDialog()
        msg_widget.setModal(True)  # MsgWidget을 모달 다이얼로그로 설정
        msg_widget.connect_start()

        # MsgWidget 실행
        msg_widget.exec()  # MsgWidget이 닫힐 때까지 대기

        if msg_widget.connect_sucssesful:
            # 연결 성공 시 메인 윈도우 실행
            print("asdasdasd")
            window = ScoreBoard()
            window.show()
            app.exec()  # 이벤트 루프 실행
        else:
            # 연결 실패 시 프로그램 종료
            sys.exit(0)
    except:
        exit(0)