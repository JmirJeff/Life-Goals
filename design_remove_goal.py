# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_remove_goal.ui',
# licensing of 'ui_remove_goal.ui' applies.
#
# Created: Mon Feb 25 21:16:55 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(310, 172)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.B_Yes = QtWidgets.QPushButton(Form)
        self.B_Yes.setObjectName("B_Yes")
        self.horizontalLayout.addWidget(self.B_Yes)
        self.B_No = QtWidgets.QPushButton(Form)
        self.B_No.setObjectName("B_No")
        self.horizontalLayout.addWidget(self.B_No)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Are you sure?", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Are you sure?", None, -1))
        self.B_Yes.setText(QtWidgets.QApplication.translate("Form", "Yes", None, -1))
        self.B_No.setText(QtWidgets.QApplication.translate("Form", "No", None, -1))

