from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Projects.DiamondRubyQuiz.Tools import Templates
import sys


class QuizHome(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.window_title = 'DiamondRubyQuiz'
		self.window_icon = QIcon('Icons/icon.png')

		self.window_layout = QVBoxLayout()
		# self.window_layout.setSpacing(0)
		self.window_layout.setContentsMargins(0, 0, 0, 0)
		# self.window_layout.setAlignment(Qt.AlignCenter)

		self.main_group = Quiz()
		self.window_layout.addWidget(self.main_group)

		# self.image = 'Icons/039-physics.png'
		# self.image = 'Icons/bg2.jpg'

		self.setAutoFillBackground(True)
		self.autoFillBackground()
		self.setStyleSheet(
			'''
			QWidget {
				background-position: center;
				background-repeat: no-repeat;
				}
			'''
		)
		self.setLayout(self.window_layout)
		self.setWindowTitle(self.window_title)
		self.setWindowIcon(self.window_icon)
		# self.setMinimumSize(600, 500)
		self.showMaximized()


class Quiz(QGroupBox):
	def __init__(self):
		QGroupBox.__init__(self)

		self.main_layout = QVBoxLayout()
		self.main_layout.setSpacing(0)
		# self.main_layout.setContentsMargins(0, 0, 0, 0)
		# self.main_layout.setAlignment(Qt.AlignCenter)

		self.setLayout(self.main_layout)
		self.setStyleSheet(
			'''
			QGroupBox {
				border: 0px;
				padding: 0px;
			}
			'''
		)

		# self.window_layout.addWidget(self.main_group)

		self.navigation_layout = QHBoxLayout()
		self.navigation_layout.setContentsMargins(0, 0, 0, 0)

		self.back_button = QPushButton()
		self.back_button.clicked.connect(self.back_button_slot)
		self.back_button_icon = QIcon('Icons/back_button.png')
		self.back_button.setToolTip('Go back to previous page')
		self.back_button.setIcon(self.back_button_icon)
		self.back_button.setMaximumSize(35, 35)
		self.back_button.setStyleSheet(
			'''
			QPushButton {
				background-color: white;
				border: 2px solid rgb(60, 150, 200);
				border-radius: 5px;
			}
			QPushButton:hover {
				border: 1px solid rgb(60, 150, 200);
			}
			'''
		)

		self.forward_button = QPushButton()
		self.forward_button.clicked.connect(self.forward_button_slot)
		self.forward_button_icon = QIcon('Icons/forward_button.png')
		self.forward_button.setToolTip('Go back to next page')
		self.forward_button.setIcon(self.forward_button_icon)
		self.forward_button.setMaximumSize(35, 35)
		self.forward_button.setStyleSheet(
			'''
			QPushButton {
				background-color: white;
				border: 2px solid rgb(60, 150, 200);
				border-radius: 5px;
			}
			QPushButton:hover {
				border: 1px solid rgb(60, 150, 200);
			}
			'''
		)
		
		self.intitialization()

	def intitialization(self):
		self.background()
		self.centralWIDGET()

	def background(self):
		self.background_layout = QVBoxLayout()
		self.background_layout.setAlignment(Qt.AlignCenter)
		# self.background_layout.setContentsMargins(0, 0, 0, 0)

		self.background_layout.addLayout(self.navigation_layout)
		self.navigation_layout.addWidget(self.back_button)
		self.navigation_layout.addWidget(self.forward_button)

		self.background_group = QGroupBox()
		self.background_group.setLayout(self.background_layout)
		self.background_group.setStyleSheet(
			'''
			QGroupBox {
				border: 0px
				padding: 0px;
			}
			'''
		)
		
		self.background_stacked_widget = QStackedWidget()
		self.background_layout.addWidget(self.background_stacked_widget, stretch=0, alignment=Qt.AlignCenter)
		
		# self.window_layout.addWidget(self.background_group, stretch=0, alignment=Qt.AlignCenter)
		self.main_layout.addWidget(self.background_group, stretch=0, alignment=Qt.AlignCenter)

	def back_button_slot(self):
		self.background_stacked_widget.setCurrentIndex(self.background_stacked_widget.currentIndex() - 1)

	def forward_button_slot(self):
		self.background_stacked_widget.setCurrentIndex(self.background_stacked_widget.currentIndex() + 1)

	def centralWIDGET(self):
		self.central_layout = QVBoxLayout()
		self.central_layout.setContentsMargins(0, 0, 0, 0)
		self.central_layout.setAlignment(Qt.AlignBottom)
		
		self.central_eff = QGraphicsDropShadowEffect()
		self.central_eff.setBlurRadius(11)
		self.central_eff.setOffset(1.2)
		# self.central_eff.setYOffset(-0.2)

		self.header_layout = QVBoxLayout()
		self.header_layout.setContentsMargins(0, 0, 0, 0)
		self.header_layout.setAlignment(Qt.AlignCenter)
		
		import time as t

		days = t.gmtime().tm_wday + 1
		days_list = [
			'Sunday', 'Monday',
			'Tuesday', 'Wednesday',
			'Thursday', 'Friday',
			'Saturday'
		]
		day = days_list[days]
		day = f'{day}\'s'
		mst = 'DiamondRubyQuiz'

		self.quiz_day_label = QLabel(day)
		self.quiz_day_label.setMaximumHeight(60)
		self.quiz_day_label.setStyleSheet(
			'''
			QLabel {
				color: white;
				font-weight: bold;
				font-size: 19px;
				font:Verdana;
			}
			'''
		)
		self.header_layout.addWidget(self.quiz_day_label)

		self.quiz_mst_label = QLabel(mst)
		self.quiz_mst_label.setMaximumHeight(65)
		self.quiz_mst_label.setStyleSheet(
			'''
			QLabel {
				color: white;
				font-weight: bold;
				font-size: 30px;
				font:Verdana;
			}
			'''
		)
		self.header_layout.addWidget(self.quiz_mst_label)

		self.header_group = QGroupBox()
		# self.header_group.setMaximumSize(300, 500)
		self.header_group.setLayout(self.header_layout)
		self.header_group.setStyleSheet(
			'''
			QGroupBox {
				border-radius: 40px;
				background-color: rgb(60, 150, 200);
				padding-left: 20px;
				padding-right: 20px;
			}
			'''
		)

		self.central_layout.addWidget(self.header_group)

		self.mid_width = 600

		self.central_group = QGroupBox()
		self.central_group.setGraphicsEffect(self.central_eff)
		self.central_group.setFixedSize(self.mid_width, 500)
		self.central_group.setLayout(self.central_layout)
		self.central_group.setStyleSheet(
			'''
			QGroupBox {
				border-radius: 50px;
				background-color: rgb(60, 150, 200);
				padding-left: 0px;
				padding-right: 0px;
			}
			'''
		)

		self.central_mid_layout = QVBoxLayout()
		self.central_mid_layout.setContentsMargins(0, 0, 0, 0)
		self.central_mid_layout.setAlignment(Qt.AlignCenter)

		self.quiz_title_layout = QVBoxLayout()
		self.quiz_title_layout.setSpacing(4)
		self.quiz_title_layout.setAlignment(Qt.AlignCenter)

		self.intro_label = QLabel('Today\'s Quiz')
		self.intro_label.setMaximumHeight(50)
		self.intro_label.setStyleSheet(
			'''
			QLabel {
				color: black;
				font-size: 13px;
				font: Verdana;
			}
			'''
		)
		self.quiz_title_layout.addWidget(self.intro_label)

		self.topic = 'General Knowledge'
		self.quiz_topic = QLabel(self.topic)
		self.quiz_topic.setMaximumHeight(60)
		self.quiz_topic.setStyleSheet(
			'''
			QLabel {
				font-weight: bold;
				font-size: 18px;
				color: rgb(60, 150, 200);
			}
			'''
		)
		self.quiz_title_layout.addWidget(self.quiz_topic, stretch=0, alignment=Qt.AlignTop)

		self.warning = QLabel()
		self.warning.setFixedHeight(60)
		self.warning.setStyleSheet(
			'''
			QLabel {
				color: black;
				font-size: 13px;
				font: Verdana;
			}
			'''
		)
		self.quiz_title_layout.addWidget(self.warning)

		self.central_mid_layout.addLayout(self.quiz_title_layout)

		self.clock_layout = QGridLayout()
		self.clock_layout.setVerticalSpacing(3)
		self.clock_layout.setHorizontalSpacing(8)
		self.clock_layout.setAlignment(Qt.AlignCenter)

		clock_size = (40, 40)

		clock_eff1 = QGraphicsDropShadowEffect()
		clock_eff1.setBlurRadius(10)
		clock_eff1.setOffset(3)

		clock_eff2 = QGraphicsDropShadowEffect()
		clock_eff2.setBlurRadius(10)
		clock_eff2.setOffset(3)

		clock_eff3 = QGraphicsDropShadowEffect()
		clock_eff3.setBlurRadius(10)
		clock_eff3.setOffset(3)

		self.hr = 4
		self.min = 30
		self.sd = 46

		self.hour_label = QLabel(str(self.hr))
		self.hour_label.setGraphicsEffect(clock_eff1)
		self.hour_label.setFixedSize(clock_size[0], clock_size[1])
		self.hour_label.setStyleSheet(
			'''
			QLabel {
				font-weight: bold;
				font-size: 20px;
				font: Verdana;
				color: black;
				background-color: rgb(210, 210, 210);
				border-radius: 4px;
				padding: 5px;
				text-align: center;
			}
			'''
		)
		self.clock_layout.addWidget(self.hour_label, 0, 0)

		self.minute_label = QLabel(str(self.min))
		self.minute_label.setGraphicsEffect(clock_eff2)
		self.minute_label.setFixedSize(clock_size[0], clock_size[1])
		self.minute_label.setStyleSheet(
			'''
			QLabel {
				font-weight: bold;
				font-size: 20px;
				font: Verdana;
				color: black;
				background-color: rgb(210, 210, 210);
				border-radius: 4px;
				padding: 5px;
				text-align: center;
			}
			'''
		)
		self.clock_layout.addWidget(self.minute_label, 0, 1)

		self.second_label = QLabel(str(self.sd))
		self.second_label.setGraphicsEffect(clock_eff3)
		self.second_label.setFixedSize(clock_size[0], clock_size[1])
		self.second_label.setStyleSheet(
			'''
			QLabel {
				font-weight: bold;
				font-size: 20px;
				font: Verdana;
				color: black;
				background-color: rgb(210, 210, 210);
				border-radius: 4px;
				padding: 5px;
				text-align: center;
			}
			'''
		)
		self.clock_layout.addWidget(self.second_label, 0, 2)

		self.hr_l = QLabel('Hours')
		self.hr_l.setFixedSize(clock_size[0], clock_size[1] // 3)
		self.hr_l.setStyleSheet(
			'''
			QLabel {
				font-weight: bold;
				font-size: 10px;
				font: Verdana;
				color: black;
				background-color: rgb(210, 210, 210);
				border-radius: 4px;
				padding: 1px;
				text-align: center;
			}
			'''
		)
		self.clock_layout.addWidget(self.hr_l, 1, 0)

		self.mn_l = QLabel('Minutes')
		self.mn_l.setFixedSize(clock_size[0], clock_size[1] // 3)
		self.mn_l.setStyleSheet(
			'''
			QLabel {
				font-weight: bold;
				font-size: 10px;
				font: Verdana;
				color: black;
				background-color: rgb(210, 210, 210);
				border-radius: 4px;
				padding: 1px;
				text-align: center;
			}
			'''
		)
		self.clock_layout.addWidget(self.mn_l, 1, 1)

		self.sd_l = QLabel('Seconds')
		self.sd_l.setFixedSize(clock_size[0], clock_size[1] // 3)
		self.sd_l.setStyleSheet(
			'''
			QLabel {
				font-weight: bold;
				font-size: 10px;
				font: Verdana;
				color: black;
				background-color: rgb(210, 210, 210);
				border-radius: 4px;
				padding: 1px;
				text-align: center;
			}
			'''
		)
		self.clock_layout.addWidget(self.sd_l, 1, 2)

		# self.central_mid_layout.addLayout(self.clock_layout)

		self.button_layout = QHBoxLayout()
		self.button_layout.setSpacing(5)
		self.button_layout.setAlignment(Qt.AlignCenter)

		self.start_quiz_button = Templates.AnimatedButton()
		self.start_quiz_button.setText('Play Quiz Now')
		self.start_quiz_button.clicked.connect(self.start_quiz_slot)
		self.button_layout.addWidget(self.start_quiz_button)

		self.register_button = Templates.AnimatedButton()
		self.register_button.setText('Sign Up')
		self.register_button.clicked.connect(self.register_button_slot)
		self.button_layout.addWidget(self.register_button)

		self.quiz_candidates_button = Templates.AnimatedButton()
		self.quiz_candidates_button.setText('Quiz Candidates')
		self.quiz_candidates_button.clicked.connect(self.quiz_candidates_slot)
		self.button_layout.addWidget(self.quiz_candidates_button)

		self.central_mid_layout.addLayout(self.button_layout)
	
		self.set_quiz_layout = QHBoxLayout()
		self.set_quiz_layout.setSpacing(5)
		self.set_quiz_layout.setAlignment(Qt.AlignCenter)

		self.set_quiz_button = Templates.AnimatedButton('Set Quiz')
		self.set_quiz_button.clicked.connect(self.set_quiz_slot)
		self.set_quiz_layout.addWidget(self.set_quiz_button)

		self.check_quiz_button = Templates.AnimatedButton('Check Quiz')
		self.check_quiz_button.clicked.connect(self.check_quiz_slot)
		self.set_quiz_layout.addWidget(self.check_quiz_button)

		self.quiz_results_button = Templates.AnimatedButton('Quiz Results')
		self.quiz_results_button.clicked.connect(self.quiz_results_slot)
		self.set_quiz_layout.addWidget(self.quiz_results_button)

		self.central_mid_layout.addLayout(self.set_quiz_layout)

		self.central_mid_group = QGroupBox()
		self.central_mid_group.setFixedSize(self.mid_width, 300)
		self.central_mid_group.setLayout(self.central_mid_layout)
		self.central_mid_group.setStyleSheet(
			'''
			QGroupBox {
				border-radius: 40px;
				border: 0px;
				background-color: white;
				padding: 10px;
			}
			'''
		)

		self.central_layout.addWidget(self.central_mid_group, stretch=0, alignment=Qt.AlignCenter)

		self.aid_layout = QVBoxLayout()
		self.aid_layout.addWidget(self.central_group, stretch=0, alignment=Qt.AlignCenter)

		self.aid_group = QGroupBox()
		self.aid_group.setLayout(self.aid_layout)
		self.aid_group.setStyleSheet(
			'''
			QGroupBox {
				border: 0px;
			}
			'''
		)

		self.background_stacked_widget.addWidget(self.aid_group)
		self.background_stacked_widget.setCurrentIndex(0)

		from Projects.DiamondRubyQuiz.Quiz import StartQuiz, QuizRegistration, SetQuiz, CheckQuiz, QuizResults, QuizCandidates

		self.background_stacked_widget.addWidget(StartQuiz.StartQuiz())
		self.background_stacked_widget.addWidget(QuizRegistration.QuizRegister())
		self.background_stacked_widget.addWidget(SetQuiz.SetQuiz(self.background_stacked_widget))
		self.background_stacked_widget.addWidget(CheckQuiz.CheckQuiz(self.background_stacked_widget))
		self.background_stacked_widget.addWidget(QuizResults.QuizResults(self.background_stacked_widget))
		self.background_stacked_widget.addWidget(QuizCandidates.QuizCandidates(self.background_stacked_widget))

	def start_quiz_slot(self):
		try:
			from Projects.DiamondRubyQuiz.Quiz import StartQuiz

			self.background_stacked_widget.setCurrentIndex(1)
		except Exception as e:
			raise e

	def register_button_slot(self):
		try:
			from Projects.DiamondRubyQuiz.Quiz import QuizRegistration
			
			self.background_stacked_widget.setCurrentIndex(2)
		except Exception as e:
			raise e

	def set_quiz_slot(self):
		try:
			from Projects.DiamondRubyQuiz.Quiz import SetQuiz

			self.background_stacked_widget.setCurrentIndex(3)
		except Exception as e:
			raise e

	def check_quiz_slot(self):
		try:
			from Projects.DiamondRubyQuiz.Quiz import CheckQuiz

			self.background_stacked_widget.setCurrentIndex(4)
		except Exception as e:
			raise e

	def quiz_results_slot(self):
		try:
			from Projects.DiamondRubyQuiz.Quiz import QuizResults

			self.background_stacked_widget.setCurrentIndex(5)
		except Exception as e:
			raise e

	def quiz_candidates_slot(self):
		try:
			from Projects.DiamondRubyQuiz.Quiz import QuizCandidates

			self.background_stacked_widget.setCurrentIndex(6)
		except Exception as e:
			raise e


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QuizHome()
	window.show()
	sys.exit(app.exec_())
 