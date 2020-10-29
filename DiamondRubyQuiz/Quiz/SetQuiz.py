from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Tools import Templates
import sys


class QuizQuestion(QGroupBox):
	def __init__(self, number):
		QGroupBox.__init__(self)

		self.number = number

		self.group_layout = QVBoxLayout()
		self.group_layout.setSpacing(5)
		self.group_layout.setAlignment(Qt.AlignTop)

		self.setObjectName(f'page_{number}')
		# self.setTitle(f'Question {number}')
		self.setLayout(self.group_layout)
		self.setStyleSheet(
			'''
			QGroupBox {
				border: 0px;
				padding: 10px;
			}
			'''
		)

		self.initialization()

	def initialization(self):
		self.question_size = (600, 300)

		self.edit_qss = '''
			{
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
		'''

		self.question_title = QLabel(f'Question {self.number}')
		self.question_title.setMaximumSize(300, 40)
		self.question_title.setStyleSheet(f'QLabel {self.edit_qss}')
		self.group_layout.addWidget(self.question_title)

		self.question_box = QTextEdit()
		self.question_box.setPlaceholderText('Question ...')
		self.question_box.setObjectName(f'question_{self.number}')
		self.question_box.setMaximumSize(self.question_size[0], self.question_size[1])
		self.question_box.setStyleSheet(f'QTextEdit {self.edit_qss}')
		self.group_layout.addWidget(self.question_box)

		self.option_size = (400, 40)

		self.option_a = QLineEdit()
		self.option_a.setPlaceholderText('A')
		self.option_a.setObjectName(f'option_{self.number}_a')
		self.option_a.setMaximumSize(self.option_size[0], self.option_size[1])
		self.option_a.setStyleSheet(f'QLineEdit {self.edit_qss}')
		self.group_layout.addWidget(self.option_a)

		self.option_b = QLineEdit()
		self.option_b.setPlaceholderText('B')
		self.option_b.setObjectName(f'option_{self.number}_b')
		self.option_b.setMaximumSize(self.option_size[0], self.option_size[1])
		self.option_b.setStyleSheet(f'QLineEdit {self.edit_qss}')
		self.group_layout.addWidget(self.option_b)

		self.option_c = QLineEdit()
		self.option_c.setPlaceholderText('C')
		self.option_c.setObjectName(f'option_{self.number}_c')
		self.option_c.setMaximumSize(self.option_size[0], self.option_size[1])
		self.option_c.setStyleSheet(f'QLineEdit {self.edit_qss}')
		self.group_layout.addWidget(self.option_c)

		self.option_d = QLineEdit()
		self.option_d.setPlaceholderText('D')
		self.option_d.setObjectName(f'option_{self.number}_d')
		self.option_d.setMaximumSize(self.option_size[0], self.option_size[1])
		self.option_d.setStyleSheet(f'QLineEdit {self.edit_qss}')
		self.group_layout.addWidget(self.option_d)

		self.answer = QLineEdit()
		self.answer.setPlaceholderText('Answer')
		self.answer.setObjectName(f'answer_{self.number}')
		self.answer.setMaximumSize(self.option_size[0], self.option_size[1])
		self.answer.setStyleSheet(f'QLineEdit {self.edit_qss}')
		self.group_layout.addWidget(self.answer)


class QuizSheet(QGroupBox):
	def __init__(self, background_stacked_widget):
		QGroupBox.__init__(self)

		self.background_stacked_widget = background_stacked_widget

		self.group_layout = QVBoxLayout()
		self.group_layout.setSpacing(5)
		self.group_layout.setAlignment(Qt.AlignTop)

		self.setLayout(self.group_layout)
		# self.setMaximumSize(500, 300)

		self.intitialization()

	def intitialization(self):
		self.mid_width = 600
		self.mid_height = 500

		self.topBAR()
		self.questionLAYOUT()

	def topBAR(self):
		self.submit_button = Templates.SwitchButton('SUBMIT')
		self.submit_button.clicked.connect(self.submit_slot)
		self.group_layout.addWidget(self.submit_button)

		self.top_bar_layout = QHBoxLayout()
		self.top_bar_layout.setSpacing(5)
		self.top_bar_layout.setAlignment(Qt.AlignLeft)

		self.total_question = 1
		self.btn_size = (35, 40)

		file_name = 'plus.png'
		self.add_question = Templates.SwitchButton()
		self.add_question_icon = QIcon(f'Icons/{file_name}')
		self.add_question.setIcon(self.add_question_icon)
		self.add_question.clicked.connect(self.add_question_slot)
		self.add_question.setMaximumSize(self.btn_size[0], self.btn_size[1])
		self.top_bar_layout.addWidget(self.add_question, stretch=0, alignment=Qt.AlignLeft)

		self.top_group = QGroupBox()
		self.top_group.setMaximumHeight(45)
		self.top_group.setLayout(self.top_bar_layout)
		self.top_group.setStyleSheet(
			'''
			QGroupBox {
				border-radius: 15px;
				background-color: rgb(60, 150, 200);
			}
			'''
		)

		self.top_scroll = QScrollArea()
		self.top_scroll.setWidget(self.top_group)
		self.top_scroll.setWidgetResizable(True)
		self.top_scroll.setStyleSheet(
			'''
			QScrollArea {
				border: 0px;
			}
			'''
		)
		self.group_layout.addWidget(self.top_scroll)


	def questionLAYOUT(self):
		self.current_number = 1

		self.question_layout = QVBoxLayout()
		self.question_layout.setSpacing(5)
		self.question_layout.setAlignment(Qt.AlignTop)

		self.question_stacked_widget = QStackedWidget()
		self.question_layout.addWidget(self.question_stacked_widget)

		self.question_stacked_widget.addWidget(QuizQuestion(self.current_number))
		self.question_stacked_widget.setCurrentIndex(0)

		self.question_group = QGroupBox()
		self.question_group.setLayout(self.question_layout)
		self.question_group.setStyleSheet(
			'''
			QGroupBox {
				border: 0px;
			}
			'''
		)
		self.group_layout.addWidget(self.question_group)

		self.init_question = Templates.QuestionButton(str(self.current_number), self.question_stacked_widget)
		self.init_question.setMaximumSize(self.btn_size[0], self.btn_size[1])
		self.top_bar_layout.addWidget(self.init_question, stretch=0, alignment=Qt.AlignRight)

		self.current_number += 1

	def add_question_slot(self):
		try:
			self.question_stacked_widget.addWidget(QuizQuestion(self.current_number))
			self.question_stacked_widget.setCurrentIndex(self.current_number - 1)

			# self.new_question.clicked.connect(self.question_slot)
			# self.new_question.setObjectName()
			# self.new_question.setMaximumSize(self.btn_size[0], self.btn_size[1])
			self.top_bar_layout.addWidget(
				Templates.QuestionButton(
					str(self.current_number),
					self.question_stacked_widget
					),
				stretch=0, alignment=Qt.AlignRight
			)
			self.current_number += 1
		except Exception as e:
			raise e

	def question_slot(self):
		try:
			# self.page_num = self.findChild(QGroupBox, f'page_{self.current_number}').title()[-1]
			# self.page_num = self.new_question.text()
			# print(self.page_num)
			self.question_stacked_widget.setCurrentIndex(1)
		except Exception as e:
			raise e

	def submit_slot(self):
		self.confirmation_dialog_layout = QVBoxLayout()
		self.confirmation_dialog_layout.setSpacing(5)
		self.confirmation_dialog_layout.setAlignment(Qt.AlignCenter)

		self.quiz_title = QLineEdit()
		self.quiz_title.setPlaceholderText('Quiz Title')
		self.quiz_title.setMaximumSize(200, 40)
		self.quiz_title.setStyleSheet(
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
		self.confirmation_dialog_layout.addWidget(self.quiz_title)

		self.quiz_day = QCalendarWidget()
		# self.quiz_day.setPlaceholderText('Quiz Day')
		# self.quiz_day.setMaximumSize(200, 60)
		self.quiz_day.setStyleSheet(
			'''
			QCalendarWidget {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
			'''
		)
		self.confirmation_dialog_layout.addWidget(self.quiz_day)

		self.quiz_time = QSpinBox()
		# self.quiz_time.setPlaceholderText('Quiz Title')
		self.quiz_time.setMaximumSize(200, 40)
		self.quiz_time.setStyleSheet(
			'''
			QSpinBox {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
			'''
		)
		self.confirmation_dialog_layout.addWidget(self.quiz_time)

		self.username = QLineEdit()
		self.username.setPlaceholderText('Username')
		self.username.setMaximumSize(200, 40)
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
		self.confirmation_dialog_layout.addWidget(self.username)

		self.password = QLineEdit()
		self.password.setPlaceholderText('Password')
		self.password.setEchoMode(QLineEdit.Password)
		self.password.setMaximumSize(200, 40)
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
		self.confirmation_dialog_layout.addWidget(self.password)

		self.confirm_button = Templates.AnimatedButton('Confirm')
		self.confirm_button.clicked.connect(self.confirm_button_slot)
		self.confirmation_dialog_layout.addWidget(self.confirm_button)

		self.confirmation_dialog = QDialog()
		self.confirmation_dialog.setWindowTitle('Quiz Confirmation')
		self.confirmation_dialog.setLayout(self.confirmation_dialog_layout)
		self.confirmation_dialog.show()

	def confirm_button_slot(self):
		try:
			from Tools import Database

			self.all_usernames = Database.get_quiz_master_column('username')
			self.all_passwords = Database.get_quiz_master_column('password')
			if self.quiz_title.text():
				if self.username.text() and self.password.text():
					if self.username.text() in self.all_usernames:
						if self.password.text() == self.all_passwords[self.all_usernames.index(self.username.text())]:
							self.submit_slot_conf()
						else:
							msg = 'Invalid credentials.\nCheck your username and password, then try again.'
							message_box = QMessageBox()
							message_box.about(self, 'Quiz Manager', msg)
					else:
						msg = 'Invalid credentials.\nCheck your username and password, then try again.'
						message_box = QMessageBox()
						message_box.about(self, 'Quiz Manager', msg)
				else:
					msg = 'You must enter your password and username to continue.'
					message_box = QMessageBox()
					message_box.about(self, 'Quiz Manager', msg)
			else:
				msg = 'Enter the quiz title to continue.'
				message_box = QMessageBox()
				message_box.about(self, 'Quiz Manager', msg)
		except Exception as e:
			raise e

	def submit_slot_conf(self):
		try:
			from Tools import LoopEmit

			self.submitSEQ = LoopEmit.QuestionEmit(self.current_number)
			self.submitSEQ.countChanged.connect(self.submit_slot_helper)
			self.submitSEQ.run()
		except Exception as e:
			raise e

	def submit_slot_helper(self):
		try:
			from Tools import Database


			Database.create_quiz(self.quiz_title.text())
			for i in range(1, self.current_number):
				self.get_question = self.findChild(QTextEdit, f'question_{i}').toPlainText()
				self.get_a = self.findChild(QLineEdit, f'option_{i}_a').text()
				self.get_b = self.findChild(QLineEdit, f'option_{i}_b').text()
				self.get_c = self.findChild(QLineEdit, f'option_{i}_c').text()
				self.get_d = self.findChild(QLineEdit, f'option_{i}_d').text()
				self.get_answer = self.findChild(QLineEdit, f'answer_{i}').text()

				if (self.quiz_title.text() and
					i and
					self.get_question and
					self.get_a and
					self.get_b and
					self.get_c and
					self.get_d and
					self.get_answer):
					Database.insert_quiz(
						self.quiz_title.text(),
						i,
						self.get_question,
						self.get_a,
						self.get_b,
						self.get_c,
						self.get_d,
						self.get_answer
					)
			
			Database.insert_quiz_check(
				self.quiz_title.text(),
				str(self.quiz_day.selectedDate()).replace('PyQt5.QtCore.QDate', ''),
				self.username.text(),
				self.quiz_time.text(),
				'False'
			)
			self.confirmation_dialog.close()

			msg = 'Your questions have been successfully uploaded.'
			message_box = QMessageBox()
			message_box.about(self, 'Quiz Manager', msg)

			self.background_stacked_widget.setCurrentIndex(0)
		except Exception as e:
			raise e


class SetQuiz(QGroupBox):
	def __init__(self, background_stacked_widget):
		QGroupBox.__init__(self)

		self.background_stacked_widget = background_stacked_widget

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
		
		self.background_stacked_widget = QStackedWidget()
		self.background_layout.addWidget(self.background_stacked_widget, stretch=0, alignment=Qt.AlignCenter)
		
		# self.window_layout.addWidget(self.background_group, stretch=0, alignment=Qt.AlignCenter)
		self.main_layout.addWidget(self.background_group, stretch=0, alignment=Qt.AlignCenter)

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
	
		self.login_quiz_layout = QVBoxLayout()
		self.login_quiz_layout.setSpacing(5)
		self.login_quiz_layout.setAlignment(Qt.AlignCenter)

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
		self.login_quiz_layout.addWidget(self.username)

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
		self.login_quiz_layout.addWidget(self.password)

		self.register_quiz_button = Templates.AnimatedButton('Login')
		self.register_quiz_button.clicked.connect(self.register_quiz_slot)
		self.login_quiz_layout.addWidget(self.register_quiz_button)

		self.central_mid_layout.addLayout(self.login_quiz_layout)

		self.register_quiz_master_button = QPushButton('sign up')
		self.register_quiz_master_button.setStyleSheet(
			'''
			QPushButton {
				background-color: white;
				color: rgb(60, 150, 200);
				font-size: 12px;
				font: Verdana;
				border: 0px;
			}
			QPushButton:hover {
				color: rgb(40, 110, 170);
			}
			'''
		)
		self.register_quiz_master_button.clicked.connect(self.sign_up_slot)
		self.register_quiz_master_button.setMaximumSize(100, 30)

		self.central_mid_layout.addWidget(self.register_quiz_master_button, stretch=0, alignment=Qt.AlignBottom | Qt.AlignCenter)

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

		from Quiz import QuizMasterRegistration

		self.background_stacked_widget.addWidget(self.aid_group)
		self.background_stacked_widget.addWidget(QuizMasterRegistration.QuizMasterRegister())
		self.background_stacked_widget.addWidget(QuizSheet(self.background_stacked_widget))
		self.background_stacked_widget.setCurrentIndex(0)


	def register_quiz_slot(self):
		try:
			from Tools import Database

			self.all_usernames = Database.get_quiz_master_column('username')
			self.all_passwords = Database.get_quiz_master_column('password')

			if self.username.text() and self.password.text():
				if self.username.text() in self.all_usernames:
					if self.password.text() == self.all_passwords[self.all_usernames.index(self.username.text())]:
						self.background_stacked_widget.setCurrentIndex(2)

						msg = f'Login successfull.\nWelcome {self.username.text()}'
						message_box = QMessageBox()
						message_box.about(self, 'Quiz manager', msg)
					else:
						msg = 'Invalid credentials.\nCheck your password and username, and try again.'
						message_box = QMessageBox()
						message_box.about(self, 'Quiz manager', msg)
				else:
					msg = 'Invalid credentials.\nCheck your password and username, and try again.'
					message_box = QMessageBox()
					message_box.about(self, 'Quiz manager', msg)
			else:
				msg = 'Please enter your usename and password to login.'
				message_box = QMessageBox()
				message_box.about(self, 'Quiz manager', msg)
		except Exception as e:
			raise e

	def sign_up_slot(self):
		try:
			self.background_stacked_widget.setCurrentIndex(1)
		except Exception as e:
			raise e
