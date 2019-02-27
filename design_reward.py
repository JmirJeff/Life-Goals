# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_reward.ui',
# licensing of 'ui_reward.ui' applies.
#
# Created: Tue Feb 26 19:13:12 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.T_Description = QtWidgets.QTextEdit(Form)
        self.T_Description.setObjectName("T_Description")
        self.verticalLayout.addWidget(self.T_Description)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.SB_Points = QtWidgets.QSpinBox(Form)
        self.SB_Points.setMaximum(10000)
        self.SB_Points.setObjectName("SB_Points")
        self.horizontalLayout.addWidget(self.SB_Points)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RB_Recurrent = QtWidgets.QRadioButton(Form)
        self.RB_Recurrent.setChecked(True)
        self.RB_Recurrent.setObjectName("RB_Recurrent")
        self.horizontalLayout_2.addWidget(self.RB_Recurrent)
        self.RB_OnlyTime = QtWidgets.QRadioButton(Form)
        self.RB_OnlyTime.setObjectName("RB_OnlyTime")
        self.horizontalLayout_2.addWidget(self.RB_OnlyTime)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.B_Add = QtWidgets.QPushButton(Form)
        self.B_Add.setObjectName("B_Add")
        self.horizontalLayout_3.addWidget(self.B_Add)
        self.B_Cancel = QtWidgets.QPushButton(Form)
        self.B_Cancel.setObjectName("B_Cancel")
        self.horizontalLayout_3.addWidget(self.B_Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Reward", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Reward", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Points", None, -1))
        self.RB_Recurrent.setText(QtWidgets.QApplication.translate("Form", "Recurrent", None, -1))
        self.RB_OnlyTime.setText(QtWidgets.QApplication.translate("Form", "Only Time", None, -1))
        self.B_Add.setText(QtWidgets.QApplication.translate("Form", "Add", None, -1))
        self.B_Cancel.setText(QtWidgets.QApplication.translate("Form", "Cancel", None, -1))

