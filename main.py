from PySide6.QtWidgets import QApplication, QMainWindow

from ui.scoreboard_form import Ui_Scoreboard

class ScoreBoard(QMainWindow, Ui_Scoreboard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        
        self.combobox_setting()
        
        
        
    def combobox_setting(self):
        import json
        with open('config.json', 'r') as f:
            data = json.load(f)
            for key in data.keys():
                self.comboBox_site.addItem(data[key])
        
if __name__ == "__main__":
    app = QApplication([])
    window = ScoreBoard()
    window.show()
    app.exec()