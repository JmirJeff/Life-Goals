# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui',
# licensing of 'ui_mainwindow.ui' applies.
#
# Created: Tue Feb 26 21:08:09 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 505)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_GroupBox = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_GroupBox.setObjectName("verticalLayout_GroupBox")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 488, 363))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_GroupBox.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.L_Points = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.L_Points.setFont(font)
        self.L_Points.setObjectName("L_Points")
        self.horizontalLayout.addWidget(self.L_Points)
        self.verticalLayout_GroupBox.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.B_Register = QtWidgets.QPushButton(self.centralwidget)
        self.B_Register.setObjectName("B_Register")
        self.verticalLayout.addWidget(self.B_Register)
        self.B_Goals = QtWidgets.QPushButton(self.centralwidget)
        self.B_Goals.setObjectName("B_Goals")
        self.verticalLayout.addWidget(self.B_Goals)
        self.B_Rewards = QtWidgets.QPushButton(self.centralwidget)
        self.B_Rewards.setObjectName("B_Rewards")
        self.verticalLayout.addWidget(self.B_Rewards)
        self.B_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.B_Exit.setObjectName("B_Exit")
        self.verticalLayout.addWidget(self.B_Exit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 30))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGoals = QtWidgets.QAction(MainWindow)
        self.actionGoals.setObjectName("actionGoals")
        self.actionRewards = QtWidgets.QAction(MainWindow)
        self.actionRewards.setObjectName("actionRewards")
        self.menuEdit.addAction(self.actionGoals)
        self.menuEdit.addAction(self.actionRewards)
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Life Goals", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Points:  ", None, -1))
        self.L_Points.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.B_Register.setText(QtWidgets.QApplication.translate("MainWindow", "Register", None, -1))
        self.B_Goals.setText(QtWidgets.QApplication.translate("MainWindow", "Goals", None, -1))
        self.B_Rewards.setText(QtWidgets.QApplication.translate("MainWindow", "Rewards", None, -1))
        self.B_Exit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.actionGoals.setText(QtWidgets.QApplication.translate("MainWindow", "Goals", None, -1))
        self.actionRewards.setText(QtWidgets.QApplication.translate("MainWindow", "Rewards", None, -1))

