import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Quiz.main import QuizHome as Window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("QUIZ APP")
    window = Window()
    window.show()
    app.exec_()
