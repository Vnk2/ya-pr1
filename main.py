import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from ui import Ui_MainWindow
import sqlite3 as sq
from random import randint
import helper


all_label = ["line_1_1", "line_2_1", "line_3_1", "line_4_1", "kine_1_2", "line_2_2", "line_3_2", "line_4_2"]


# КЛАСС основного окна
class Test_word(QtWidgets.QMainWindow):
    #
    check_1 = 0
    g = []

    def __init__(self):
        super(Test_word, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.init_UI4()

    # Запуск вторго окна
    def start_helper1(self):
        self.help = helper.Help_window(self)
        self.help.show()

    # Функция при открытии приложения
    def init_UI(self):

        self.setWindowTitle("Проверка слов")
        self.setWindowIcon(QIcon("images.png"))
        self.ui.line_1_1.setPlaceholderText("режим")
        self.ui.line_2_1.setPlaceholderText("не")
        self.ui.line_3_1.setPlaceholderText("выбран")
        self.ui.line_4_1.setPlaceholderText("pass")

        self.ui.line_1_2.setPlaceholderText("режим")
        self.ui.line_2_2.setPlaceholderText("не")
        self.ui.line_3_2.setPlaceholderText("выбран")
        self.ui.line_4_2.setPlaceholderText("pass")
        self.ui.pushButton_2.clicked.connect(self.init_UI2)
        self.ui.pushButton_3.clicked.connect(self.init_UI3)

    #Класс при нажатии на кнопку проверка слов вывод рандомных слов
    def init_UI2(self):
        global g
        global check_1
        check_1 = 1
        g = self.random_word()

        self.setWindowTitle("Проверка слов")
        self.ui.pushButton.setText("Проверка слов")

        self.ui.line_1_1.setText("")
        self.ui.line_2_1.setText("")
        self.ui.line_3_1.setText("")
        self.ui.line_4_1.setText("")

        self.ui.line_1_1.setPlaceholderText("Введите слово")
        self.ui.line_2_1.setPlaceholderText("Введите слово")
        self.ui.line_3_1.setPlaceholderText("Введите слово")
        self.ui.line_4_1.setPlaceholderText("Введите слово")

        a = QPixmap("a.jpg")
        self.ui.check_4.setPixmap(a)
        self.ui.check_1.setPixmap(a)
        self.ui.check_2.setPixmap(a)
        self.ui.check_3.setPixmap(a)

        self.ui.line_1_2.setText(g[0])
        self.ui.line_2_2.setText(g[2])
        self.ui.line_3_2.setText(g[4])
        self.ui.line_4_2.setText(g[6])
        self.ui.pushButton.clicked.connect(self.compair_answer)

    # Класс для ввода новых слов
    def init_UI3(self):

        global check_1
        check_1 = 0

        self.setWindowTitle("Ввод слов для перевода")
        self.setWindowIcon(QIcon("images.png"))

        self.ui.line_1_1.setPlaceholderText("слово")
        self.ui.line_2_1.setPlaceholderText("слово")
        self.ui.line_3_1.setPlaceholderText("слово")
        self.ui.line_4_1.setPlaceholderText("слово")

        a = QPixmap("a.jpg")
        self.ui.check_4.setPixmap(a)
        self.ui.check_1.setPixmap(a)
        self.ui.check_2.setPixmap(a)
        self.ui.check_3.setPixmap(a)

        self.ui.pushButton.setText("Добавить")
        self.ui.line_1_2.setText("")
        self.ui.line_2_2.setText("")
        self.ui.line_3_2.setText("")
        self.ui.line_4_2.setText("")

        self.ui.line_1_2.setPlaceholderText("превод")
        self.ui.line_2_2.setPlaceholderText("превод")
        self.ui.line_3_2.setPlaceholderText("превод")
        self.ui.line_4_2.setPlaceholderText("превод")

        self.ui.pushButton.clicked.connect(self.add_value)

    # Выбор рандомных слов для проверки
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

    # Функция вызова другого окна
    def init_UI4(self):
        self.ui.pushButton_4.clicked.connect(self.start_helper1)

    # Функция сравнивания введённых слов
    def compair_answer(self):

        good_pix_map = QPixmap("C:\\Users\\user\\Desktop\\ya_pr1\\foto\\good.png")
        bad_pix_map = QPixmap("C:\\Users\\user\\Desktop\\ya_pr1\\foto\\bad.png")
        m = 1
        self.answer_0 = self.ui.line_1_1.text()
        self.answer_1 = self.ui.line_2_1.text()
        self.answer_2 = self.ui.line_3_1.text()
        self.answer_3 = self.ui.line_4_1.text()

        for x in range(4):
            if eval(f"self.answer_{x}") == str(g[m]):
                eval(f"self.ui.check_{x + 1}.setPixmap(good_pix_map)")
            else:
                eval(f"self.ui.check_{x + 1}.setPixmap(bad_pix_map)")
            m += 2

    # Функция ввода значений
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

        M = Add_in_list(self.all_word, check_1)
        M.add_bd()


# Класс добавления в базу данных
class Add_in_list:

    def __init__(self, all_word, check_1):
        self.check_1 = check_1
        self.all_word = all_word
        self.not_twice = 0
        self.take = []
        self.m = []
        self.n = []
        self.g = []

    # Функция поиска повторений
    def find_twice(self, all_word_new):

        self.not_twice = list(set(all_word_new))

        for x in range(len(self.not_twice)):
            if all_word_new.count(self.not_twice[x]) == 1:
                self.g.append(self.not_twice[x])
        return self.g

    # Функция проверки наличия слова в базе данных
    def check_in_bd(self):
        with sq.connect("words_save.db") as con:
            cur = con.cursor()
            self.take = cur.execute("""SELECT word FROM save""").fetchall()
            self.m = [self.all_word[x] for x in range(len(self.all_word)) if x not in self.take and x % 2 == 0]
            return self.m

    # Функция добавления в бд
    def add_bd(self):
        if self.check_1 == 0:
            self.m = Add_in_list.check_in_bd(self)
            self.n = Add_in_list.find_twice(self, self.m)

            if len(self.m) == len(self.all_word) // 2 and len(self.n) == len(self.all_word) // 2:
                for x in range(0, int(len(self.all_word)) // 2 + 3, 2):
                    with sq.connect("words_save.db") as con:
                        name = self.all_word[x]
                        translate = self.all_word[x + 1]
                        cur = con.cursor()
                        print(f"INSERT INTO save VALUES('{name}', '{translate}')")
                        cur.execute(f"INSERT INTO save VALUES('{name}', '{translate}')")
            else:
                with sq.connect("words_save.db") as con:
                    cur = con.cursor()
                    self.take = cur.execute("""SELECT word FROM save""").fetchall()
                    self.m = [x for x in self.all_word if x in self.take and x % 2 == 0]


app = QtWidgets.QApplication([])
application = Test_word()
application.show()
sys.exit(app.exec())
