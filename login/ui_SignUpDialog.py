# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SignUpDialogNICAAR.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_SignUpDialog(object):
    def setupUi(self, SignUpDialog):
        if not SignUpDialog.objectName():
            SignUpDialog.setObjectName(u"SignUpDialog")
        SignUpDialog.resize(348, 171)
        self.lineEdit = QLineEdit(SignUpDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 10, 231, 31))
        self.label = QLabel(SignUpDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(13, 15, 51, 21))
        self.label_2 = QLabel(SignUpDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(13, 55, 51, 21))
        self.lineEdit_2 = QLineEdit(SignUpDialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 50, 231, 31))
        self.lineEdit_3 = QLineEdit(SignUpDialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(100, 90, 231, 31))
        self.label_3 = QLabel(SignUpDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(13, 95, 81, 21))
        self.pushButton = QPushButton(SignUpDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 130, 321, 31))

        self.retranslateUi(SignUpDialog)

        QMetaObject.connectSlotsByName(SignUpDialog)
    # setupUi

    def retranslateUi(self, SignUpDialog):
        SignUpDialog.setWindowTitle(QCoreApplication.translate("SignUpDialog", u"\u6ce8\u518c", None))
        self.label.setText(QCoreApplication.translate("SignUpDialog", u"\u7528\u6237\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("SignUpDialog", u"\u5bc6\u7801\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("SignUpDialog", u"\u518d\u6b21\u8f93\u5165\u5bc6\u7801\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("SignUpDialog", u"\u6ce8\u518c", None))
    # retranslateUi

