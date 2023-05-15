# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'results.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1065, 866)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 1061, 61))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.result1Label = QLabel(self.layoutWidget)
        self.result1Label.setObjectName(u"result1Label")
        self.result1Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.result1Label)

        self.result2Label = QLabel(self.layoutWidget)
        self.result2Label.setObjectName(u"result2Label")
        self.result2Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.result2Label)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 80, 1061, 781))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget1 = QWidget(self.layoutWidget1)
        self.widget1.setObjectName(u"widget1")

        self.verticalLayout_2.addWidget(self.widget1)

        self.widget_2 = QWidget(self.layoutWidget1)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_2.addWidget(self.widget_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.result1Label.setText(QCoreApplication.translate("Dialog", u"l1", None))
        self.result2Label.setText(QCoreApplication.translate("Dialog", u"l2", None))
    # retranslateUi

