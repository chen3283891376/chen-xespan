# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_cloudpanoMvsUr.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(620, 532)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pub_1 = QPushButton(self.centralwidget)
        self.pub_1.setObjectName(u"pub_1")
        self.pub_1.setGeometry(QRect(530, 10, 75, 24))
        self.treeWidget = QTreeWidget(self.centralwidget)
        font = QFont()
        font.setHintingPreference(QFont.PreferDefaultHinting)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, font);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(10, 40, 601, 431))
        self.treeWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.treeWidget.setStyleSheet(u"")
        self.treeWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.treeWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.treeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.treeWidget.setTabKeyNavigation(False)
        self.treeWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setProperty(u"showSortIndicator", False)
        self.pub_2 = QPushButton(self.centralwidget)
        self.pub_2.setObjectName(u"pub_2")
        self.pub_2.setEnabled(False)
        self.pub_2.setGeometry(QRect(10, 480, 191, 24))
        self.pub_2.setCheckable(False)
        self.pub_2.setAutoDefault(False)
        self.pub_2.setFlat(False)
        self.pub_3 = QPushButton(self.centralwidget)
        self.pub_3.setObjectName(u"pub_3")
        self.pub_3.setEnabled(False)
        self.pub_3.setGeometry(QRect(210, 480, 201, 24))
        self.pub_4 = QPushButton(self.centralwidget)
        self.pub_4.setObjectName(u"pub_4")
        self.pub_4.setEnabled(False)
        self.pub_4.setGeometry(QRect(420, 480, 191, 24))
        self.pub_5 = QPushButton(self.centralwidget)
        self.pub_5.setObjectName(u"pub_5")
        self.pub_5.setEnabled(True)
        self.pub_5.setGeometry(QRect(450, 10, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pub_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PySide6 Xes\u7f51\u76d8\uff08", None))
#if QT_CONFIG(tooltip)
        self.pub_1.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u4f60\u7684\u82f1\u96c4\u5427\uff08", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pub_1.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u4f60\u7684\u82f1\u96c4\u5427\uff08", None))
#endif // QT_CONFIG(statustip)
        self.pub_1.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\uff08", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u5927\u5c0f", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None));
#if QT_CONFIG(tooltip)
        self.pub_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u524d\u5148\u770b\u770b\uff1f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pub_2.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u524d\u5148\u770b\u770b\uff1f", None))
#endif // QT_CONFIG(statustip)
        self.pub_2.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
#if QT_CONFIG(tooltip)
        self.pub_3.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u8fd9\u4e2a\u82f1\u96c4\uff08", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pub_3.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u8fd9\u4e2a\u82f1\u96c4\uff08", None))
#endif // QT_CONFIG(statustip)
        self.pub_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
#if QT_CONFIG(tooltip)
        self.pub_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pub_4.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4f60\u4e0d\u8981\u4e71\u5220\u554a\u5582\uff08", None))
#endif // QT_CONFIG(statustip)
        self.pub_4.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
#if QT_CONFIG(tooltip)
        self.pub_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pub_5.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5206\u4eab\u4e00\u4e0b\uff1f", None))
#endif // QT_CONFIG(statustip)
        self.pub_5.setText(QCoreApplication.translate("MainWindow", u"\u5206\u4eab", None))
    # retranslateUi

