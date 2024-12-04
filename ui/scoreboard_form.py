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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Scoreboard(object):
    def setupUi(self, Scoreboard):
        if not Scoreboard.objectName():
            Scoreboard.setObjectName(u"Scoreboard")
        Scoreboard.resize(240, 79)
        Scoreboard.setMinimumSize(QSize(240, 0))
        Scoreboard.setMaximumSize(QSize(240, 16777215))
        Scoreboard.setStyleSheet(u"")
        self.centralwidget = QWidget(Scoreboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"background-color:#B1F0F7;\n"
"border:2px solid #FBF6F0;\n"
"border-radius:14px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"QLabel{\n"
"color:#2f4650;\n"
"background-color:none;\n"
"border:0px solid #000000;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_title)

        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        self.pushButton_close.setMinimumSize(QSize(24, 24))
        self.pushButton_close.setMaximumSize(QSize(24, 24))
        self.pushButton_close.setStyleSheet(u"QPushButton{\n"
"background-color:#c1ffff;\n"
"border:2px solid #FBF6F0;\n"
"border-radius:4px;\n"
"border-top-right-radius:14px;\n"
"color:#2f4650;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#a3d8d8;\n"
"border:2px solid #e2ddd8;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#7ba3a3;\n"
"border:2px solid #d0ccc7;\n"
"color:#FADA7A;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_close)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 3))
        self.label.setMaximumSize(QSize(16777215, 3))
        self.label.setStyleSheet(u"QLabel{\n"
"background-color:#101616;\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.comboBox_site = QComboBox(self.centralwidget)
        self.comboBox_site.setObjectName(u"comboBox_site")
        self.comboBox_site.setStyleSheet(u"QComboBox{\n"
"background-color:#F5F0CD;\n"
"border:none;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"background-color:#FADA7A;\n"
"}\n"
"\n"
"QComboBox:editable{\n"
"color:#3d5682;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"border:none;\n"
"}\n"
"\n"
"QComboBox:drop-down{\n"
"border:none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"border: 2px solid #FADA7A;\n"
"border-radius:0px;\n"
"selection-background-color: #000000;\n"
"background-color:#F5F0CD;\n"
"color:#3d5682;\n"
"}")

        self.verticalLayout.addWidget(self.comboBox_site)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_add_member = QPushButton(self.centralwidget)
        self.pushButton_add_member.setObjectName(u"pushButton_add_member")
        self.pushButton_add_member.setMinimumSize(QSize(0, 24))
        self.pushButton_add_member.setStyleSheet(u"QPushButton{\n"
"background-color:#c1ffff;\n"
"border:2px solid #FBF6F0;\n"
"border-radius:1px;\n"
"color:#2f4650;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#a3d8d8;\n"
"border:2px solid #e2ddd8;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#7ba3a3;\n"
"border:2px solid #d0ccc7;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_add_member)


        self.verticalLayout.addLayout(self.horizontalLayout)

        Scoreboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(Scoreboard)

        QMetaObject.connectSlotsByName(Scoreboard)
    # setupUi

    def retranslateUi(self, Scoreboard):
        Scoreboard.setWindowTitle(QCoreApplication.translate("Scoreboard", u"Scoreboard", None))
        self.label_title.setText(QCoreApplication.translate("Scoreboard", u"  \uc21c\uc704 \uc790\ub3d9 \uacc4\uc0b0\uae30", None))
        self.pushButton_close.setText(QCoreApplication.translate("Scoreboard", u"x", None))
        self.label.setText("")
        self.pushButton_add_member.setText(QCoreApplication.translate("Scoreboard", u"\uc0ac\uc6a9\uc790 \ucd94\uac00", None))
    # retranslateUi

