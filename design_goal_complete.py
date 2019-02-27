# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_goal_complete.ui',
# licensing of 'ui_goal_complete.ui' applies.
#
# Created: Sun Feb 24 17:33:55 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.L_Topic = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_Topic.sizePolicy().hasHeightForWidth())
        self.L_Topic.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.L_Topic.setFont(font)
        self.L_Topic.setObjectName("L_Topic")
        self.horizontalLayout.addWidget(self.L_Topic)
        self.L_Points = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_Points.sizePolicy().hasHeightForWidth())
        self.L_Points.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.L_Points.setFont(font)
        self.L_Points.setObjectName("L_Points")
        self.horizontalLayout.addWidget(self.L_Points)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.L_Description = QtWidgets.QLabel(Form)
        self.L_Description.setObjectName("L_Description")
        self.verticalLayout.addWidget(self.L_Description)
        self.TE_Details = QtWidgets.QPlainTextEdit(Form)
        self.TE_Details.setObjectName("TE_Details")
        self.verticalLayout.addWidget(self.TE_Details)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.B_Complete = QtWidgets.QPushButton(Form)
        self.B_Complete.setObjectName("B_Complete")
        self.horizontalLayout_2.addWidget(self.B_Complete)
        self.B_Quit = QtWidgets.QPushButton(Form)
        self.B_Quit.setObjectName("B_Quit")
        self.horizontalLayout_2.addWidget(self.B_Quit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Goal", None, -1))
        self.L_Topic.setText(QtWidgets.QApplication.translate("Form", "Topic", None, -1))
        self.L_Points.setText(QtWidgets.QApplication.translate("Form", "Points", None, -1))
        self.L_Description.setText(QtWidgets.QApplication.translate("Form", "Description", None, -1))
        self.B_Complete.setText(QtWidgets.QApplication.translate("Form", "Complete", None, -1))
        self.B_Quit.setText(QtWidgets.QApplication.translate("Form", "Quit", None, -1))

