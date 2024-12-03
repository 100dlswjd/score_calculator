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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_add_form(object):
    def setupUi(self, add_form):
        if not add_form.objectName():
            add_form.setObjectName(u"add_form")
        add_form.resize(240, 80)
        add_form.setMinimumSize(QSize(240, 80))
        add_form.setMaximumSize(QSize(240, 80))
        self.verticalLayout = QVBoxLayout(add_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(add_form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(add_form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(add_form)

        QMetaObject.connectSlotsByName(add_form)
    # setupUi

    def retranslateUi(self, add_form):
        add_form.setWindowTitle(QCoreApplication.translate("add_form", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("add_form", u"\uc774\ub984 \ub610\ub294 \ubcc4\uba85\uc744 \uc801\uc5b4\uc8fc\uc138\uc694", None))
        self.pushButton.setText(QCoreApplication.translate("add_form", u"\uc0ac\uc6a9\uc790 \ucd94\uac00", None))
    # retranslateUi

