# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'score_widget_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_score_form(object):
    def setupUi(self, score_form):
        if not score_form.objectName():
            score_form.setObjectName(u"score_form")
        score_form.resize(240, 30)
        score_form.setMinimumSize(QSize(240, 30))
        score_form.setMaximumSize(QSize(240, 30))
        self.horizontalLayout = QHBoxLayout(score_form)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.checkBox_name = QCheckBox(score_form)
        self.checkBox_name.setObjectName(u"checkBox_name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_name.sizePolicy().hasHeightForWidth())
        self.checkBox_name.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.checkBox_name)

        self.pushButton_m = QPushButton(score_form)
        self.pushButton_m.setObjectName(u"pushButton_m")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_m.sizePolicy().hasHeightForWidth())
        self.pushButton_m.setSizePolicy(sizePolicy1)
        self.pushButton_m.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_m)

        self.label_score = QLabel(score_form)
        self.label_score.setObjectName(u"label_score")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_score.sizePolicy().hasHeightForWidth())
        self.label_score.setSizePolicy(sizePolicy2)
        self.label_score.setMinimumSize(QSize(20, 0))
        self.label_score.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_score)

        self.pushButton_p = QPushButton(score_form)
        self.pushButton_p.setObjectName(u"pushButton_p")
        sizePolicy1.setHeightForWidth(self.pushButton_p.sizePolicy().hasHeightForWidth())
        self.pushButton_p.setSizePolicy(sizePolicy1)
        self.pushButton_p.setMinimumSize(QSize(20, 20))
        self.pushButton_p.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_p)

        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(score_form)

        QMetaObject.connectSlotsByName(score_form)
    # setupUi

    def retranslateUi(self, score_form):
        score_form.setWindowTitle(QCoreApplication.translate("score_form", u"Form", None))
        self.checkBox_name.setText(QCoreApplication.translate("score_form", u"CheckBox", None))
        self.pushButton_m.setText(QCoreApplication.translate("score_form", u"-", None))
        self.label_score.setText(QCoreApplication.translate("score_form", u"0", None))
        self.pushButton_p.setText(QCoreApplication.translate("score_form", u"+", None))
    # retranslateUi

