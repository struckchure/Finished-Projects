import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


Q = {
    "What is the only sea on Earth with no coastline?",
    "What is the largest country based on surface area?",
    "What is the official language of the Canadian province Quebec?",
    "What is the longest river in South America?",
    "How many U.S. states border the Gulf of Mexico?",
    "In which U.S. state would you find Mount Rushmore?",
    "Brazil was once a colony of which European country?",
    "What is the largest lake in Africa?",
    "Which city is located both in Asia and Europe?",
    "What colorful body of water separates Saudi Arabia from Africa?",
    "What city is the capital of China?",
}
score = 0


class Question(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.title = "EDUCTIONAL QUIZ"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()
        self.show()

    def initUI(self):
        self.A1 = QLabel()
        self.A1.setAlignment(Qt.AlignLeft)
        self.A3 = QLabel()
        self.A3.setAlignment(Qt.AlignCenter)
        self.A4 = QLabel()
        self.A4.setAlignment(Qt.AlignBottom)
        self.A5 = QLabel()
        self.A5.setAlignment(Qt.AlignLeft)
        self.A6 = QLabel()
        self.A6.setAlignment(Qt.AlignLeft)

        self.b1 = QPushButton()
        self.b1.setCheckable(True)

        self.b2 = QPushButton()
        self.b2.setCheckable(True)

        self.b3 = QPushButton()
        self.b3.setCheckable(True)

        # button
        self.button = QPushButton("start")
        # self.button.setFont ( "arial" )
        self.button.setFlat(True)
        self.button.setStyleSheet("background-color :green")
        self.button2 = QPushButton(" exit")
        # self.button2.setFont ( "ariel: 20")
        self.button.setFlat(True)
        self.button.setStyleSheet("background-color :green")
        # self.button.clicked.connect ( self.Action )
        # self.button2.clicked.connect ( self.exitt )

        # layout
        aLayout = QVBoxLayout()
        aLayout.addWidget(self.A1)
        aLayout.addWidget(self.A3)
        aLayout.addWidget(self.A4)
        aLayout.addWidget(self.A5)
        aLayout.addWidget(self.A6)
        aLayout.addWidget(self.b1)
        aLayout.addWidget(self.b2)
        aLayout.addWidget(self.b3)

        Lay = QVBoxLayout()
        Lay.addWidget(self.button)
        Lay.addWidget(self.button2)
        self.setLayout(Lay)

        self.timer = QBasicTimer
        self.step = 0
        buttons = [self.b1, self.b2, self.b3, self.A4]
        for btn in buttons:
            btn.setFont(QFont("arial", 12))
            btn.setStyleSheet("color:black")

    def timerEvent(self, event):
        global Q
        data = Q
        if self.step == 0:
            self.A4.setText("QUESTION 1")
            self.A1.setText("%s" % (data[0]))
            self.b1.setText("sargaso sea")
            self.b2.setText("red sea")
            self.b3.setText("south china sea")

        elif self.step == 1:
            self.A4.setText("QUESTION 2")
            self.A1.setText("%s" % (data[1]))
            self.b1.setText("china")
            self.b2.setText("india")
            self.b3.setText("russia")

        elif self.step == 2:
            self.A4.setText("QUESTION 3")
            self.A1.setText("%s" % (data[2]))
            self.b1.setText("English")
            self.b2.setText("spanish")
            self.b3.setText("frech")

        elif self.step == 3:
            self.A4.setText("QUESTION 4")
            self.A1.setText("%s" % (data[3]))
            self.b1.setText("Amazon")
            self.b2.setText("nile")
            self.b3.setText("Danbe")

        elif self.step == 4:
            self.A4.setText("QUESTION 5")
            self.A1.setText("%s" % (data[4]))
            self.b1.setText("five")
            self.b2.setText("seven")
            self.b3.setText("ten")

        elif self.step == 5:
            self.A4.setText("QUESTION 6")
            self.A1.setText("%s" % (data[5]))
            self.b1.setText("north dakota")
            self.b2.setText("south dakota")
            self.b3.setText("new york")

        elif self.step == 6:
            self.A4.setText("QUESTION 7")
            self.A1.setText("%s" % (data[6]))
            self.b1.setText("portugal")
            self.b2.setText("france")
            self.b3.setText("England")
        elif self.step == 7:
            self.A4.setText("QUETION 8")
            self.A1.setText("%s" % (data[7]))
            self.b1.setText("lake albert")
            self.b2.setText("lake victoria")
            self.b3.setText("lake kivu")
        elif self.step == 8:
            self.A4.setText("QUESTION 9")
            self.A1.setText("%s" % (data[8]))
            self.b1.setText("cairo")
            self.b2.setText("baghdad")
            self.b3.setText("Istanbul")
        elif self.step == 9:
            self.A4.setText("QUESTION 10")
            self.A1.setText("%s" % (data[9]))
            self.b1.setText("red sea ")
            self.b2.setText("Baltic Sea")
            self.b3.setText("indian sea")
        elif self.step == 10:
            self.A4.setText("QUESTION 11")
            self.A1.setText("%s" % (data[10]))
            self.b1.setText("Shanghai")
            self.b2.setText("Beijing")
            self.b3.setText("Suzhou")

        def anwer(self, ans):
            global score
            if ans.text() == "":
                ans.setText("")
                score = score + 10
                self.A6.setText("score:%" % (score))
            elif ans.text() == "":
                ans.setText("")
                score = score + 20
                self.A6.setText("score:%" % (score))

            elif ans.text() == "":
                ans.setText("")
                score = score + 30
                self.A6.setText("score:%" % (score))

            elif ans.text() == "":
                ans.setText("")
                score = score + 40
                self.A6.setText("score:%" % (score))

            elif ans.text() == "":
                ans.setText("")
                score = score + 50
                self.A6.setText("score:%" % (score))

            elif ans.text() == "":
                ans.setText("")
                score = score + 60
                self.A6.setText("score:%" % (score))
            elif ans.text() == "":
                ans.setText("")
                score = score + 70
                self.A6.setText("score:%" % (score))
            elif ans.text() == "":
                ans.setText("")
                score = score + 80
                self.A6.setText("score:%" % (score))
            elif ans.text() == "":
                ans.setText("")
                score = score + 90
                self.A6.setText("score:%" % (score))
            elif ans.text() == "":
                ans.setText("")
                score = score + 100
                self.A6.setText("score:%" % (score))

            else:
                b.setText("incorrect answer")
                score = socre - 10
                self.A6.setText("score:%s" % (score))
