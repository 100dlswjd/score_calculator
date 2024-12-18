# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'score_control_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_score_control_form(object):
    def setupUi(self, score_control_form):
        if not score_control_form.objectName():
            score_control_form.setObjectName(u"score_control_form")
        score_control_form.resize(240, 32)
        score_control_form.setMinimumSize(QSize(240, 32))
        score_control_form.setMaximumSize(QSize(240, 32))
        score_control_form.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(score_control_form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(score_control_form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color:#B1F0F7;\n"
"border:2px solid #FBF6F0;\n"
"border-bottom-left-radius:14px;\n"
"border-bottom-right-radius:14px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_get_score = QPushButton(self.frame)
        self.pushButton_get_score.setObjectName(u"pushButton_get_score")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_get_score.sizePolicy().hasHeightForWidth())
        self.pushButton_get_score.setSizePolicy(sizePolicy)
        self.pushButton_get_score.setMinimumSize(QSize(0, 24))
        self.pushButton_get_score.setStyleSheet(u"QPushButton{\n"
"background-color:#c1ffff;\n"
"border:2px solid #FBF6F0;\n"
"border-radius:12px;\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_get_score)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_insert_score = QPushButton(self.frame)
        self.pushButton_insert_score.setObjectName(u"pushButton_insert_score")
        sizePolicy.setHeightForWidth(self.pushButton_insert_score.sizePolicy().hasHeightForWidth())
        self.pushButton_insert_score.setSizePolicy(sizePolicy)
        self.pushButton_insert_score.setMinimumSize(QSize(0, 24))
        self.pushButton_insert_score.setStyleSheet(u"QPushButton{\n"
"background-color:#c1ffff;\n"
"border:2px solid #FBF6F0;\n"
"border-radius:12px;\n"
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
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color:#759a9a;;\n"
"border-color:#b5b1ad;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_insert_score)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(score_control_form)

        QMetaObject.connectSlotsByName(score_control_form)
    # setupUi

    def retranslateUi(self, score_control_form):
        score_control_form.setWindowTitle(QCoreApplication.translate("score_control_form", u"Form", None))
        self.pushButton_get_score.setText(QCoreApplication.translate("score_control_form", u"  \ubaa8\ub4e0 \uc804\uc801 \uac00\uc838\uc624\uae30 ", None))
        self.pushButton_insert_score.setText(QCoreApplication.translate("score_control_form", u"  \ub370\uc774\ud130 \ucd94\uac00  ", None))
    # retranslateUi

