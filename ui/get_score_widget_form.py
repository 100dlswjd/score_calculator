# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'get_score_widget_form.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_get_score_form(object):
    def setupUi(self, get_score_form):
        if not get_score_form.objectName():
            get_score_form.setObjectName(u"get_score_form")
        get_score_form.resize(240, 30)
        get_score_form.setMaximumSize(QSize(240, 30))
        self.verticalLayout = QVBoxLayout(get_score_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_get_score = QPushButton(get_score_form)
        self.pushButton_get_score.setObjectName(u"pushButton_get_score")

        self.verticalLayout.addWidget(self.pushButton_get_score)


        self.retranslateUi(get_score_form)

        QMetaObject.connectSlotsByName(get_score_form)
    # setupUi

    def retranslateUi(self, get_score_form):
        get_score_form.setWindowTitle(QCoreApplication.translate("get_score_form", u"Form", None))
        self.pushButton_get_score.setText(QCoreApplication.translate("get_score_form", u"\ubaa8\ub4e0 \uc804\uc801 \uac00\uc838\uc640\uc11c \ud074\ub9bd\ubcf4\ub4dc\uc5d0 \ubcf5\uc0ac", None))
    # retranslateUi

