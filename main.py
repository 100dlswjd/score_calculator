import db.db_tool as db_tool

from PySide6.QtWidgets import QApplication, QMainWindow

from ui.scoreboard_form import Ui_Scoreboard

from score_widget import ScoreWidget
from add_widget import AddWidget
from get_score_widget import GetScoreWidget

class ScoreBoard(QMainWindow, Ui_Scoreboard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        
        self.combobox_setting()
        self.refresh_members()
        self.pushButton_add_member.clicked.connect(self.add_member)
        
    def combobox_setting(self):
        import json
        with open('config.json', 'r') as f:
            data = json.load(f)
            for key in data.keys():
                self.comboBox_site.addItem(data[key])
                
    def refresh_members(self):
        # 위젯 초기화
        print("refreshing")
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
            
        widget = GetScoreWidget()
        self.verticalLayout.addWidget(widget)
        
            
    def add_member(self):
        # 위젯 뛰우고 현재 메인 윈도우는 컨트롤 못하게 하기
        self.add_widget = AddWidget()
        self.add_widget.setModal(True)
        self.add_widget.show()
        self.add_widget.exec()
        
        self.refresh_members()
        
if __name__ == "__main__":
    app = QApplication([])
    window = ScoreBoard()
    window.show()
    app.exec()