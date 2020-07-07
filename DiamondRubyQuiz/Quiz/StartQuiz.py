from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Projects.DiamondRubyQuiz.Tools import Templates, Database, LoopEmit
import sys
import time as t


class StartQuiz(QGroupBox):
	def __init__(self):
		QGroupBox.__init__(self)
		
		self.window_layout = QVBoxLayout()
		self.window_layout.setSpacing(0)
		# self.window_layout.setContentsMargins(0, 0, 0, 0)
		# self.window_layout.setAlignment(Qt.AlignCenter)

		self.main_layout = QVBoxLayout()
		self.main_layout.setSpacing(0)
		# self.main_layout.setContentsMargins(0, 0, 0, 0)
		# self.main_layout.setAlignment(Qt.AlignCenter)

		self.main_group = QGroupBox()
		self.main_group.setAlignment(Qt.AlignCenter)
		self.main_group.setLayout(self.main_layout)
		self.main_group.setStyleSheet(
			'''
			QGroupBox {
				border: 0px;
				padding: 0px;
			}
			'''
		)

		self.window_layout.addWidget(self.main_group, stretch=0, alignment=Qt.AlignCenter)

		self.setLayout(self.window_layout)
		# self.setMinimumSize(600, 500)
		# self.showMaximized()
		
		self.intitialization()

	def intitialization(self):
		self.background()
		self.centralWIDGET()

	def background(self):
		self.background_layout = QVBoxLayout()
		self.background_layout.setAlignment(Qt.AlignCenter)
		# self.background_layout.setContentsMargins(0, 0, 0, 0)

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
		
		self.main_layout.addWidget(self.background_group, stretch=0, alignment=Qt.AlignCenter)

		self.background_stacked_widget = QStackedWidget()
		self.background_stacked_widget.setStyleSheet(
			'''
			QStackedWidget {
				padding: 10px;
			}
			'''
		)
		
		self.background_layout.addWidget(self.background_stacked_widget, stretch=0, alignment=Qt.AlignCenter)

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
				padding: 20px;
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

		self.intro_label = QLabel('Today\'s Quiz on')
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
		self.quiz_title_layout.addWidget(self.quiz_topic)

		self.central_mid_layout.addLayout(self.quiz_title_layout)

		self.clock_layout = QGridLayout()
		self.clock_layout.setVerticalSpacing(3)
		self.clock_layout.setHorizontalSpacing(8)
		self.clock_layout.setAlignment(Qt.AlignCenter)

		self.username = QLineEdit()
		self.username.setPlaceholderText('Username')
		self.username.setMaximumSize(200, 60)
		self.username.setStyleSheet(
			'''
			QLineEdit {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
			'''
		)
		self.clock_layout.addWidget(self.username, 0, 0)

		self.password = QLineEdit()
		self.password.setPlaceholderText('Password')
		self.password.setEchoMode(QLineEdit.Password)
		self.password.setMaximumSize(200, 60)
		self.password.setStyleSheet(
			'''
			QLineEdit {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
			'''
		)
		self.clock_layout.addWidget(self.password, 1, 0)

		self.central_mid_layout.addLayout(self.clock_layout)

		self.button_layout = QHBoxLayout()
		self.button_layout.setSpacing(0)
		self.button_layout.setAlignment(Qt.AlignCenter)

		self.login_button = Templates.AnimatedButton()
		self.login_button.setText('Login')
		self.login_button.clicked.connect(self.login_button_slot)
		self.button_layout.addWidget(self.login_button)

		self.central_mid_layout.addLayout(self.button_layout)

		self.central_mid_group = QGroupBox()
		self.central_mid_group.setFixedSize(self.mid_width, 300)
		self.central_mid_group.setLayout(self.central_mid_layout)
		self.central_mid_group.setStyleSheet(
			'''
			QGroupBox {
				border-radius: 40px;
				border: 0px;
				background-color: white;
				padding: 20px;
			}
			'''
		)

		self.central_layout.addWidget(self.central_mid_group)

		self.background_stacked_widget.addWidget(self.central_group)
		self.background_stacked_widget.setCurrentIndex(0)

		from Projects.DiamondRubyQuiz.Quiz import Quiz

	def login_button_slot(self):
		try:
			from Projects.DiamondRubyQuiz.Tools import Database

			if self.username.text():
				if self.password.text():
					all_usernames = Database.get_quiz_candidate_by_column('username')
					all_passwords = Database.get_quiz_candidate_by_column('password')

					if self.username.text() in all_usernames:
						index = all_usernames.index(self.username.text())
						db_password = all_passwords[index]
						if self.password.text() == db_password:
							self.loginSUCCESS()
						else:
							msg = 'Invalid credentials. Check your username and password.'
							message_box = QMessageBox()
							message_box.about(self, 'Quiz Manager', msg)
					else:
						msg = 'Invalid credentials. Check your username and password.'
						message_box = QMessageBox()
						message_box.about(self, 'Quiz Manager', msg)
				else:
					msg = 'Please enter a valid Username and Password.'
					message_box = QMessageBox()
					message_box.about(self, 'Quiz Manager', msg)
			else:
				msg = 'Please enter a valid Username and Password.'
				message_box = QMessageBox()
				message_box.about(self, 'Quiz Manager', msg)
		except Exception as e:
			raise e

	def loginSUCCESS(self):
		try:
			self.submitSEQ = LoopEmit.QuestionEmit(10)
			self.submitSEQ.countChanged.connect(self.go_signal)
			self.submitSEQ.run()
		except Exception as e:
			raise e

	def go_signal(self):
		try:
			from Projects.DiamondRubyQuiz.Quiz import Quiz

			self.current_date = str(QCalendarWidget().selectedDate()).replace('PyQt5.QtCore.QDate', '')

			self.all_dates = Database.get_quiz_check_by_column('quiz_day')
			self.all_topics = Database.get_quiz_check_by_column('quiz_topic')

			if len(self.all_dates) != 0:
				for d in self.all_dates:
					if d == self.current_date:
						self.fetched_topic = self.all_topics[self.all_dates.index(d)]
						
						msg = 'Login Successul.\nYour Quiz will commence immediately.\nPress "Ok" to continue.'
						message_box = QMessageBox()
						message_box.about(self, 'Quiz Manager', msg)

						self.background_stacked_widget.addWidget(Quiz.QuizPage(
							self.fetched_topic,
							self.username.text(),
							self.background_stacked_widget
							)
						)
						self.background_stacked_widget.setCurrentIndex(1)

						break
					else:
						msg = 'Quiz is not available right now, check back later.'
						message_box = QMessageBox()
						message_box.about(self, 'Quiz Manager', msg)

						break
			else:
				msg = 'Quiz is not available right now, check back later.'
				message_box = QMessageBox()
				message_box.about(self, 'Quiz Manager', msg)
		except Exception as e:
			raise e
