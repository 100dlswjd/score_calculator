# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scoreboard_form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_Scoreboard(object):
    def setupUi(self, Scoreboard):
        if not Scoreboard.objectName():
            Scoreboard.setObjectName(u"Scoreboard")
        Scoreboard.resize(229, 121)
        self.centralwidget = QWidget(Scoreboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox_site = QComboBox(self.centralwidget)
        self.comboBox_site.setObjectName(u"comboBox_site")

        self.verticalLayout.addWidget(self.comboBox_site)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        Scoreboard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Scoreboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 229, 22))
        Scoreboard.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Scoreboard)
        self.statusbar.setObjectName(u"statusbar")
        Scoreboard.setStatusBar(self.statusbar)

        self.retranslateUi(Scoreboard)

        QMetaObject.connectSlotsByName(Scoreboard)
    # setupUi

    def retranslateUi(self, Scoreboard):
        Scoreboard.setWindowTitle(QCoreApplication.translate("Scoreboard", u"Scoreboard", None))
        self.pushButton.setText(QCoreApplication.translate("Scoreboard", u"\uc0ac\uc6a9\uc790 \ucd94\uac00", None))
    # retranslateUi

