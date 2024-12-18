from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt, Slot, QTimer, QThread, Signal
from PySide6.QtGui import QMouseEvent

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
        
        self.label_msg.setText("")
        self.connect_timer = QTimer()
        self.count = 0
        
        self.server_thread = ServerConnector()
        self.server_thread.connectd.connect(self.on_server_connected)
        self.server_thread.failed.connect(self.server_close)
        
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
        self.close()
        
    def server_close(self):
        self.connect_timer.stop()
        self.label_msg.setText("서버 연결 실패")
        self.close()
        
if __name__ == "__main__":
    app = QApplication([])
    window = MsgWidget()
    window.show()
    window.connect_start()
    app.exec()
