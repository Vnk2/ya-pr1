import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from ui2 import Ui_MainWindow



class Help_window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui2 = Ui_MainWindow()
        self.ui2.setupUi(self)
        self.init_UIn()

    def init_UIn(self):
        self.setWindowTitle("Проверка слов")
        text1 = """    Приветствую, данное приложение было разработано с использованием библиотеки PyQt5.
    Основная цель: Помощь в подготовке к словарным диктантам по разным языкам, изучению
    и усваиванию новых слов."""
        self.ui2.main_inf.setText(text1)

        text2 = """    Функции, доступные в приложении:
    1: Дозапись в словарик
    2: Проверка себя на знание слов, записанных в словарь"""
        self.ui2.main_inf_2.setText(text2)

#
def start_help():
    app = QtWidgets.QApplication(sys.argv)
    application2 = Help_window()
    application2.show()
    sys.exit(app.exec())




#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
