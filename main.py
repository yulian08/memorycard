import random

from PyQt5.QtWidgets import *

import database

app = QApplication([])

window = QWidget()
window.resize(700, 500)

menu_btn = QPushButton("Меню")
group_box = QGroupBox("Варіанти відповідей")
question_lbl = QLabel("Яблуко")
answer1_btn = QRadioButton("building")
answer2_btn = QRadioButton("home")
answer3_btn = QRadioButton("application")
answer4_btn = QRadioButton("apple")
result_lbl = QLabel("Результат")
result_lbl.hide()

answers = [answer1_btn, answer2_btn, answer3_btn, answer4_btn]
random.shuffle(answers)
vidpovistu_btn = QPushButton("Відповісти")
main_line = QVBoxLayout()
h1 = QHBoxLayout()
h1.addWidget(menu_btn)
h1.addStretch(1)
main_line.addLayout(h1)
main_line.addWidget(question_lbl)


group_line = QVBoxLayout()

group_line_h1 = QHBoxLayout()
group_line_h1.addWidget(answers[0])
group_line_h1.addWidget(answers[1])
group_line.addLayout(group_line_h1)

group_line.addWidget(answers[2])
group_line.addWidget(answers[3])
group_line.addWidget(result_lbl )
group_box.setLayout(group_line)

main_line.addWidget(group_box)
main_line.addWidget(vidpovistu_btn)
window.setLayout(main_line)

def set_question():
    num = database.question_number
    question_lbl.setText(database.question[num]["Запитання"])
    answers[0].setText(database.question[num]["Правильна відповідь"])
    answers[1].setText(database.question[num]["Неправильна 1"])
    answers[2].setText(database.question[num]["Неправильна 2"])
    answers[3].setText(database.question[num]["Неправильна 3"])

set_question()

def answer_click():
    if answers[0].isChecked():
        result_lbl.setText("Правильно!")
    else:
        result_lbl.setText("Неправильно!")
    result_lbl.show()
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()

def next_question_func():
    database.question_number += 1
    set_question()



vidpovistu_btn.clicked.connect(answer_click)
window.show()
app.exec()












































































































































































































































