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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_score_control_form(object):
    def setupUi(self, score_control_form):
        if not score_control_form.objectName():
            score_control_form.setObjectName(u"score_control_form")
        score_control_form.resize(240, 30)
        score_control_form.setMaximumSize(QSize(240, 30))
        self.horizontalLayout = QHBoxLayout(score_control_form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_insert_score = QPushButton(score_control_form)
        self.pushButton_insert_score.setObjectName(u"pushButton_insert_score")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_insert_score.sizePolicy().hasHeightForWidth())
        self.pushButton_insert_score.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_insert_score)

        self.pushButton_get_score = QPushButton(score_control_form)
        self.pushButton_get_score.setObjectName(u"pushButton_get_score")
        sizePolicy.setHeightForWidth(self.pushButton_get_score.sizePolicy().hasHeightForWidth())
        self.pushButton_get_score.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_get_score)


        self.retranslateUi(score_control_form)

        QMetaObject.connectSlotsByName(score_control_form)
    # setupUi

    def retranslateUi(self, score_control_form):
        score_control_form.setWindowTitle(QCoreApplication.translate("score_control_form", u"Form", None))
        self.pushButton_insert_score.setText(QCoreApplication.translate("score_control_form", u"\ub370\uc774\ud130 \ucd94\uac00", None))
        self.pushButton_get_score.setText(QCoreApplication.translate("score_control_form", u"\ubaa8\ub4e0 \uc804\uc801 \uac00\uc838\uc624\uae30", None))
    # retranslateUi

