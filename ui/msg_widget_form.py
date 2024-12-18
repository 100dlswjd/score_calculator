# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'msg_widget_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_msg_form(object):
    def setupUi(self, msg_form):
        if not msg_form.objectName():
            msg_form.setObjectName(u"msg_form")
        msg_form.resize(240, 80)
        msg_form.setMaximumSize(QSize(240, 80))
        self.horizontalLayout = QHBoxLayout(msg_form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(msg_form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color:#F5F0CD;\n"
"border:2px solid #FBF6F0;\n"
"border-radius:14px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(24, 24))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color:#FADA7A;\n"
"border:2px solid #FBF6F0;\n"
"border-radius:10px;\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_msg = QLabel(self.frame)
        self.label_msg.setObjectName(u"label_msg")
        self.label_msg.setStyleSheet(u"QLabel{\n"
"color:#68675d;\n"
"border:None;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:#1a1a17;\n"
"}\n"
"\n"
"")
        self.label_msg.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_msg)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(msg_form)

        QMetaObject.connectSlotsByName(msg_form)
    # setupUi

    def retranslateUi(self, msg_form):
        msg_form.setWindowTitle(QCoreApplication.translate("msg_form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("msg_form", u"x", None))
        self.label_msg.setText(QCoreApplication.translate("msg_form", u"TextLabel", None))
    # retranslateUi

