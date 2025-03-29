# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ShareDialogVYoZWp.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_ShareDialog(object):
    def setupUi(self, ShareDialog):
        if not ShareDialog.objectName():
            ShareDialog.setObjectName(u"ShareDialog")
        ShareDialog.resize(311, 153)
        self.tabWidget = QTabWidget(ShareDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 291, 141))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 70, 131, 31))
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 70, 121, 31))
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(10, 10, 261, 41))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 20, 261, 31))
        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 70, 121, 31))
        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(150, 70, 121, 31))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(ShareDialog)
        self.pushButton_2.clicked.connect(ShareDialog.close)
        self.pushButton_4.clicked.connect(ShareDialog.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ShareDialog)
    # setupUi

    def retranslateUi(self, ShareDialog):
        ShareDialog.setWindowTitle(QCoreApplication.translate("ShareDialog", u"\u5206\u4eab", None))
        self.pushButton.setText(QCoreApplication.translate("ShareDialog", u"\u62f7\u8d1d", None))
        self.pushButton_2.setText(QCoreApplication.translate("ShareDialog", u"\u53d6\u6d88", None))
        self.lineEdit.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ShareDialog", u"\u5206\u4eab", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("ShareDialog", u"\u8f93\u5165\u522b\u4eba\u7ed9\u4f60\u7684\u5206\u4eab\u7801\uff08", None))
        self.pushButton_3.setText(QCoreApplication.translate("ShareDialog", u"\u4e0b\u8f7d", None))
        self.pushButton_4.setText(QCoreApplication.translate("ShareDialog", u"\u53d6\u6d88", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ShareDialog", u"\u522b\u4eba\u7684\u5206\u4eab\uff1f", None))
    # retranslateUi

