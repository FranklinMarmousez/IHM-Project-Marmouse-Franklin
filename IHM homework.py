# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:35:40 2023

@author: frank
"""



from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox, QRadioButton, QTextEdit



class Different_questions(QWidget):
    def __init__(self, single_question, single_choice, single_answer, multiple_question, multiple_choices, multiple_correct_answer, text_question, text_answer, hints):
        super().__init__()
        self.setWindowTitle("Questions")
        qVBoxLayout = QVBoxLayout()
        single_question_label= QLabel(single_question)
        multiple_question_label = QLabel(multiple_question)
        self.qRadioBox= []
        self.qCheckBoxes = []
        qVBoxLayout.addWidget(single_question_label)
        for qRadioBoxes in single_choice:
            radio_button=QRadioButton(qRadioBoxes)
            self.qRadioBox.append(radio_button)
            qVBoxLayout.addWidget(radio_button)
        qVBoxLayout.addWidget(multiple_question_label)
        for multiple_choice in multiple_choices:
            self.qCheckBoxes.append(QCheckBox(multiple_choice))
        for qCheckBox in self.qCheckBoxes:
            qVBoxLayout.addWidget(qCheckBox)
        self.setLayout(qVBoxLayout)
        self.multiple_correct_answer = multiple_correct_answer
        text_question_label= QLabel(text_question)
        qVBoxLayout.addWidget(text_question_label)
        self.text_answer_txt=QTextEdit()
        qVBoxLayout.addWidget(self.text_answer_txt)
        buttons = QPushButton("Check")
        qVBoxLayout.addWidget(buttons)
        buttons.clicked.connect(self.check_answer)

    def check_answer(self):
        answer=[]
        for qRadioBoxes in self.qRadioBox:
            if qRadioBoxes.isChecked():
                answer.append(qRadioBoxes.text())
        multiple_correct_answers =[]
        for qCheckBox in self.qCheckBoxes:
            if qCheckBox.isChecked():
                multiple_correct_answers.append(qCheckBox.text())
        text_answer_result=self.text_answer_txt.toPlainText()
        if multiple_correct_answers == self.multiple_correct_answer and answer==single_answer and text_answer_result.lower()==text_answer.lower():
            qMessageBox = QMessageBox()
            qMessageBox.setWindowTitle("Correct!")
            qMessageBox.setText("Correct.")
            qMessageBox.exec()
        else:
            qMessageBox = QMessageBox()
            qMessageBox.setWindowTitle("Incorrect!")
            qMessageBox.setText(hints)
            qMessageBox.exec()


app = QApplication([])
single_question="Who painted the Mona Lisa?"
single_choice=["Michelangelo","Leonardo da Vinci","Mirò"]
single_answer=["Leonardo da Vinci"]
question = "Who are the two philosophers who are credited with laying the foundation for Western philosophy?"
choices = ["Socrates", "Plato", "Confucius", "Kant"]
correct_answer = ["Socrates", "Plato"]
text_question="What is the largest country in the world by area?"
text_answer="Russia"
hints="He was born at Vinci which is a small town near Florence.\n They were ancient Greek philosophers \n The country's capital  is Moscow."
window = Different_questions(single_question,single_choice,single_answer,question, choices, correct_answer, text_question, text_answer, hints)
window.show()
app.exec()