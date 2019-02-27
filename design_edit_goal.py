# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edit_goal.ui',
# licensing of 'ui_edit_goal.ui' applies.
#
# Created: Mon Feb 25 21:49:32 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 350)
        Form.setMinimumSize(QtCore.QSize(400, 350))
        Form.setMaximumSize(QtCore.QSize(400, 350))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.T_Topic = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Topic.sizePolicy().hasHeightForWidth())
        self.T_Topic.setSizePolicy(sizePolicy)
        self.T_Topic.setObjectName("T_Topic")
        self.verticalLayout.addWidget(self.T_Topic)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.T_Description = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Description.sizePolicy().hasHeightForWidth())
        self.T_Description.setSizePolicy(sizePolicy)
        self.T_Description.setObjectName("T_Description")
        self.verticalLayout.addWidget(self.T_Description)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.SB_Points = QtWidgets.QSpinBox(Form)
        self.SB_Points.setMaximum(10000)
        self.SB_Points.setObjectName("SB_Points")
        self.horizontalLayout_3.addWidget(self.SB_Points)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.B_Ok = QtWidgets.QPushButton(Form)
        self.B_Ok.setObjectName("B_Ok")
        self.horizontalLayout.addWidget(self.B_Ok)
        self.B_Cancel = QtWidgets.QPushButton(Form)
        self.B_Cancel.setObjectName("B_Cancel")
        self.horizontalLayout.addWidget(self.B_Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Goals", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Topic :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Description :", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Points :", None, -1))
        self.RB_Recurrent.setText(QtWidgets.QApplication.translate("Form", "Recurrent", None, -1))
        self.RB_OnlyTime.setText(QtWidgets.QApplication.translate("Form", "Only Time", None, -1))
        self.B_Ok.setText(QtWidgets.QApplication.translate("Form", "Ok", None, -1))
        self.B_Cancel.setText(QtWidgets.QApplication.translate("Form", "Cancel", None, -1))

