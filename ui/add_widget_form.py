# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_widget_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_add_form(object):
    def setupUi(self, add_form):
        if not add_form.objectName():
            add_form.setObjectName(u"add_form")
        add_form.resize(240, 100)
        add_form.setMinimumSize(QSize(240, 100))
        add_form.setMaximumSize(QSize(240, 100))
        self.verticalLayout = QVBoxLayout(add_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(add_form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color:#F5F0CD;\n"
"border:2px solid #FBF6F0;\n"
"border-radius:14px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(24, 24))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color:#FADA7A;\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"background-color:#fffde5;\n"
"}")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_add = QPushButton(self.frame)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QSize(0, 24))
        self.pushButton_add.setStyleSheet(u"QPushButton{\n"
"background-color:#FADA7A;\n"
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

        self.horizontalLayout.addWidget(self.pushButton_add)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(add_form)

        QMetaObject.connectSlotsByName(add_form)
    # setupUi

    def retranslateUi(self, add_form):
        add_form.setWindowTitle(QCoreApplication.translate("add_form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("add_form", u"x", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("add_form", u"\uc774\ub984 \ub610\ub294 \ubcc4\uba85\uc744 \uc801\uc5b4\uc8fc\uc138\uc694", None))
        self.pushButton_add.setText(QCoreApplication.translate("add_form", u" \uc0ac\uc6a9\uc790 \ucd94\uac00 ", None))
    # retranslateUi

