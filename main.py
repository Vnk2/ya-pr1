import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from ui import Ui_MainWindow
import sqlite3 as sq
from random import randint
import helper

all_label = ["line_1_1", "line_2_1", "line_3_1", "line_4_1", "kine_1_2", "line_2_2", "line_3_2", "line_4_2"]


class Test_word(QtWidgets.QMainWindow):

    g = []

    def __init__(self):
        super(Test_word, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.init_UI4()

    def start_helper1(self):
        self.help = helper.Help_window(self)
        self.help.show()

    def init_UI(self):
        self.setWindowTitle("Проверка слов")
        self.setWindowIcon(QIcon("images.png"))
        self.ui.line_1_1.setPlaceholderText("pass")
        self.ui.line_2_1.setPlaceholderText("pass")
        self.ui.line_3_1.setPlaceholderText("pass")
        self.ui.line_4_1.setPlaceholderText("pass")

        self.ui.line_1_2.setPlaceholderText("pass")
        self.ui.line_2_2.setPlaceholderText("pass")
        self.ui.line_3_2.setPlaceholderText("pass")
        self.ui.line_4_2.setPlaceholderText("pass")
        self.ui.pushButton_2.clicked.connect(self.init_UI2)
        self.ui.pushButton_3.clicked.connect(self.init_UI3)

    def init_UI2(self):
        global g
        g = self.random_word()
        self.setWindowTitle("Проверка слов")

        self.ui.line_1_1.setText("")
        self.ui.line_2_1.setText("")
        self.ui.line_3_1.setText("")
        self.ui.line_4_1.setText("")

        self.ui.line_1_1.setPlaceholderText("Введите слово")
        self.ui.line_2_1.setPlaceholderText("Введите слово")
        self.ui.line_3_1.setPlaceholderText("Введите слово")
        self.ui.line_4_1.setPlaceholderText("Введите слово")

        self.ui.line_1_2.setText(g[0])
        self.ui.line_2_2.setText(g[2])
        self.ui.line_3_2.setText(g[4])
        self.ui.line_4_2.setText(g[6])
        self.ui.pushButton.clicked.connect(self.compair_answer)

    def init_UI3(self):
        self.setWindowTitle("Ввод слов для перевода")
        self.setWindowIcon(QIcon("images.png"))
        self.ui.line_1_1.setPlaceholderText("слово")
        self.ui.line_2_1.setPlaceholderText("слово")
        self.ui.line_3_1.setPlaceholderText("слово")
        self.ui.line_4_1.setPlaceholderText("слово")
        self.ui.pushButton.setText("Добавить")

        self.ui.line_1_2.setPlaceholderText("превод")
        self.ui.line_2_2.setPlaceholderText("превод")
        self.ui.line_3_2.setPlaceholderText("превод")
        self.ui.line_4_2.setPlaceholderText("превод")

        self.ui.pushButton.clicked.connect(self.add_value)

    def random_word(self):
        self.true_answer = []
        with sq.connect("words_save.db") as con:
            cur = con.cursor()
            m = cur.execute(f"""SELECT translate FROM save""").fetchall()
            f = cur.execute(f"""SELECT word FROM save""").fetchall()
            for x in range(4):
                n = randint(0, len(m) - 1)
                self.true_answer.append(m[n][0])
                self.true_answer.append(f[n][0])
                m.pop(n), f.pop(n)
        return self.true_answer

    def init_UI4(self):
        self.ui.pushButton_4.clicked.connect(self.start_helper1)

    def compair_answer(self):
        good_pix_map = QPixmap("C:\\Users\\user\\Desktop\\ya_pr1\\foto\\good.png")
        bad_pix_map = QPixmap("C:\\Users\\user\\Desktop\\ya_pr1\\foto\\bad.png")
        self.answer_0 = self.ui.line_1_1.text()
        self.answer_1 = self.ui.line_2_1.text()
        self.answer_2 = self.ui.line_3_1.text()
        self.answer_3 = self.ui.line_4_1.text()
        m = 1
        for x in range(4):
            if eval(f"self.answer_{x}") == str(g[m]):
                eval(f"self.ui.check_{x + 1}.setPixmap(good_pix_map)")
            else:
                eval(f"self.ui.check_{x + 1}.setPixmap(bad_pix_map)")
            m += 2

    def add_value(self):
        self.name_1 = self.ui.line_1_1.text()
        self.name_2 = self.ui.line_2_1.text()
        self.name_3 = self.ui.line_3_1.text()
        self.name_4 = self.ui.line_4_1.text()

        self.translate_1 = self.ui.line_1_2.text()
        self.translate_2 = self.ui.line_2_2.text()
        self.translate_3 = self.ui.line_3_2.text()
        self.translate_4 = self.ui.line_4_2.text()
        self.all_word = [self.name_1, self.translate_1, self.name_2,self.translate_2, self.name_3, self.translate_3,
                         self.name_4, self.translate_4]
        for x in range(0, int(len(self.all_word)) // 2 + 3, 2):
            with sq.connect("words_save.db") as con:
                name = self.all_word[x]
                translate = self.all_word[x + 1]
                print(name, translate)
                cur = con.cursor()
                print(f"INSERT INTO save VALUES('{name}', '{translate}')")
                cur.execute(f"INSERT INTO save VALUES('{name}', '{translate}')")



# class Add_in_list:
#
#     def __init__(self, all_word):
#         self.all_word = all_word
#
#     def add_value(self):
#         for x in range(0, int(len(self.all_word)) // 2 + 3, 2):
#             with sq.connect("words_save.db") as con:
#                 name = self.all_word[x]
#                 translate = self.all_word[x + 1]
#                 print(name, translate)
#                 cur = con.cursor()
#                 print(f"INSERT INTO save VALUES('{name}', '{translate}')")
#                 cur.execute(f"INSERT INTO save VALUES('{name}', '{translate}')")



app = QtWidgets.QApplication([])
application = Test_word()
application.show()
sys.exit(app.exec())
