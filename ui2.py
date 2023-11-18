# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 640)
        MainWindow.setStyleSheet("background-color:    #87CEFA")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hand = QtWidgets.QLabel(self.centralwidget)
        self.hand.setGeometry(QtCore.QRect(190, 10, 400, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.hand.setFont(font)
        self.hand.setStyleSheet("background-color:#6A5ACD;\n"
"border: 2px solid #f66867;\n"
"color: white;\n"
"border-radius: 20\n"
"\n"
"")
        self.hand.setObjectName("hand")
        self.main_inf = QtWidgets.QLabel(self.centralwidget)
        self.main_inf.setGeometry(QtCore.QRect(5, 100, 770, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.main_inf.setFont(font)
        self.main_inf.setStyleSheet("background-color:#B0E0E6;\n"
"color: white;")
        self.main_inf.setText("")
        self.main_inf.setObjectName("main_inf")
        self.main_inf_2 = QtWidgets.QLabel(self.centralwidget)
        self.main_inf_2.setGeometry(QtCore.QRect(5, 225, 770, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.main_inf_2.setFont(font)
        self.main_inf_2.setStyleSheet("background-color:#B0E0E6;\n"
"color: white;")
        self.main_inf_2.setText("")
        self.main_inf_2.setObjectName("main_inf_2")
        self.main_inf_3 = QtWidgets.QLabel(self.centralwidget)
        self.main_inf_3.setGeometry(QtCore.QRect(5, 350, 770, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.main_inf_3.setFont(font)
        self.main_inf_3.setStyleSheet("background-color:#B0E0E6;\n"
"color: white;")
        self.main_inf_3.setText("")
        self.main_inf_3.setObjectName("main_inf_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hand.setText(_translate("MainWindow", "Основная информация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
