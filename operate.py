# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operate.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_operate(object):
    def setupUi(self, operate):
        operate.setObjectName("operate")
        operate.resize(1000, 675)
        operate.setStyleSheet("QWidget#centralwidget\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(operate)
        self.centralwidget.setObjectName("centralwidget")
        self.come_late_text = QtWidgets.QLabel(self.centralwidget)
        self.come_late_text.setGeometry(QtCore.QRect(35, 15, 105, 46))
        self.come_late_text.setStyleSheet("font: 75 35px \"微软雅黑\";\n"
"color: rgb(112, 112, 112);\n"
"")
        self.come_late_text.setObjectName("come_late_text")
        self.leave_early_text = QtWidgets.QLabel(self.centralwidget)
        self.leave_early_text.setGeometry(QtCore.QRect(430, 15, 105, 46))
        self.leave_early_text.setStyleSheet("font: 75 35px \"微软雅黑\";\n"
"color: rgb(112, 112, 112);\n"
"")
        self.leave_early_text.setObjectName("leave_early_text")
        self.search = QtWidgets.QToolButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(805, 100, 200, 180))
        self.search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon)
        self.search.setIconSize(QtCore.QSize(240, 180))
        self.search.setAutoRaise(True)
        self.search.setObjectName("search")
        self.today = QtWidgets.QToolButton(self.centralwidget)
        self.today.setGeometry(QtCore.QRect(805, 400, 200, 180))
        self.today.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/tody.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.today.setIcon(icon1)
        self.today.setIconSize(QtCore.QSize(240, 180))
        self.today.setAutoRaise(True)
        self.today.setObjectName("today")
        self.out = QtWidgets.QToolButton(self.centralwidget)
        self.out.setGeometry(QtCore.QRect(860, 607, 150, 60))
        self.out.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.out.setIcon(icon2)
        self.out.setIconSize(QtCore.QSize(147, 70))
        self.out.setAutoRaise(True)
        self.out.setObjectName("out")
        self.leave_early = QtWidgets.QLabel(self.centralwidget)
        self.leave_early.setGeometry(QtCore.QRect(401, 80, 390, 460))
        self.leave_early.setText("")
        self.leave_early.setPixmap(QtGui.QPixmap(":/img/list.png"))
        self.leave_early.setObjectName("leave_early")
        self.come_late = QtWidgets.QLabel(self.centralwidget)
        self.come_late.setGeometry(QtCore.QRect(10, 80, 390, 460))
        self.come_late.setText("")
        self.come_late.setPixmap(QtGui.QPixmap(":/img/list.png"))
        self.come_late.setObjectName("come_late")
        self.num = QtWidgets.QLabel(self.centralwidget)
        self.num.setGeometry(QtCore.QRect(10, 570, 345, 75))
        self.num.setText("")
        self.num.setPixmap(QtGui.QPixmap(":/img/num_in.png"))
        self.num.setObjectName("num")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(430, 570, 345, 75))
        self.name.setText("")
        self.name.setPixmap(QtGui.QPixmap(":/img/name_in.png"))
        self.name.setObjectName("name")
        self.list1 = QtWidgets.QTableWidget(self.centralwidget)
        self.list1.setGeometry(QtCore.QRect(50, 100, 330, 400))
        self.list1.setAutoFillBackground(False)
        self.list1.setStyleSheet("font: 75 25px \"微软雅黑\";\n"
"color: rgb(112, 112, 112);")
        self.list1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.list1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.list1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.list1.setAutoScrollMargin(10)
        self.list1.setDragEnabled(False)
        self.list1.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.list1.setShowGrid(True)
        self.list1.setGridStyle(QtCore.Qt.DashDotLine)
        self.list1.setWordWrap(True)
        self.list1.setObjectName("list1")
        self.list1.setColumnCount(2)
        self.list1.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.list1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.list1.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.list1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.list1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.list1.setItem(0, 0, item)
        self.list1.verticalHeader().setSortIndicatorShown(False)
        self.list2 = QtWidgets.QTableWidget(self.centralwidget)
        self.list2.setGeometry(QtCore.QRect(440, 100, 330, 400))
        self.list2.setAutoFillBackground(False)
        self.list2.setStyleSheet("font: 75 25px \"微软雅黑\";\n"
"color: rgb(112, 112, 112);")
        self.list2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.list2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.list2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.list2.setAutoScrollMargin(10)
        self.list2.setDragEnabled(False)
        self.list2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.list2.setShowGrid(True)
        self.list2.setGridStyle(QtCore.Qt.DashDotLine)
        self.list2.setWordWrap(True)
        self.list2.setObjectName("list2")
        self.list2.setColumnCount(2)
        self.list2.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.list2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.list2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.list2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.list2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.list2.setItem(0, 0, item)
        self.list2.verticalHeader().setSortIndicatorShown(False)
        self.num_text = QtWidgets.QLineEdit(self.centralwidget)
        self.num_text.setGeometry(QtCore.QRect(120, 590, 180, 33))
        self.num_text.setStyleSheet("font: 25px \"微软雅黑\";\n"
"color: rgb(112, 112, 112);")
        self.num_text.setText("")
        self.num_text.setFrame(False)
        self.num_text.setObjectName("num_text")
        self.name_text = QtWidgets.QLineEdit(self.centralwidget)
        self.name_text.setGeometry(QtCore.QRect(530, 590, 180, 33))
        self.name_text.setStyleSheet("font: 25px \"微软雅黑\";\n"
"color: rgb(112, 112, 112);")
        self.name_text.setText("")
        self.name_text.setFrame(False)
        self.name_text.setObjectName("name_text")
        operate.setCentralWidget(self.centralwidget)

        self.retranslateUi(operate)
        QtCore.QMetaObject.connectSlotsByName(operate)

    def retranslateUi(self, operate):
        _translate = QtCore.QCoreApplication.translate
        operate.setWindowTitle(_translate("operate", "MainWindow"))
        self.come_late_text.setText(_translate("operate", "迟到："))
        self.leave_early_text.setText(_translate("operate", "早退："))

        self.list1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        item = self.list1.horizontalHeaderItem(0)
        item.setText(_translate("operate", "姓名"))
        item = self.list1.horizontalHeaderItem(1)
        item.setText(_translate("operate", "时间"))
        __sortingEnabled = self.list1.isSortingEnabled()
        self.list1.setSortingEnabled(False)
        self.list1.setSortingEnabled(__sortingEnabled)

        self.list2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        item = self.list2.horizontalHeaderItem(0)
        item.setText(_translate("operate", "姓名"))
        item = self.list2.horizontalHeaderItem(1)
        item.setText(_translate("operate", "时间"))
        __sortingEnabled = self.list2.isSortingEnabled()
        self.list2.setSortingEnabled(False)
        self.list2.setSortingEnabled(__sortingEnabled)
        self.num_text.setPlaceholderText(_translate("operate", "请输入学号"))
        self.name_text.setPlaceholderText(_translate("operate", "请输入姓名"))
import rsc_rc
