from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class QuestionEmit(QThread):
    countChanged = pyqtSignal(int)

    def __init__(self, duration):
        QThread.__init__(self)
        self.duration = duration

    def run(self):
        try:
            while self.duration > 0:
                self.countChanged.emit(self.duration)
                self.duration -= self.duration
        except Exception as e:
            raise 

'''
USAGE 
    self.submitSEQ = GetQuestions(self.number)
    self.submitSEQ.countChanged.connect(self.view_signal)
    self.submitSEQ.run()
'''