from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Projects.DiamondRubyQuiz.Tools import Templates
import sys
import time as t

# days = t.gmtime().tm_wday + 1
# days_list = [
# 	'Sunday', 'Monday',
# 	'Tuesday', 'Wednesday',
# 	'Thursday', 'Friday',
# 	'Saturday'
# ]
# day = day_list[days]

class QuizMasterVerify(QDialog):
	def __init__(self, stacked_widget, credentials):
		QDialog.__init__(self)

		self.stacked_widget = stacked_widget
		self.first_name = credentials[0]
		self.middle_name = credentials[1]
		self.last_name = credentials[2]
		self.username_ = credentials[3]
		self.password_ = credentials[4]
		self.email = credentials[5]

		# print(
		# 	type(self.first_name),
		# 	type(self.last_name),
		# 	type(self.email),
		# 	type(self.username),
		# 	type(self.password)
		# )

		self.window_layout = QVBoxLayout()
		self.window_layout.setContentsMargins(0, 0, 0, 0)
		self.window_layout.setAlignment(Qt.AlignTop)

		self.main_layout = QVBoxLayout()
		self.main_layout.setAlignment(Qt.AlignCenter)

		self.setWindowTitle('Admin Verfication')
		self.setFixedSize(500, 200)
		self.setLayout(self.window_layout)
		self.setStyleSheet(
			'''
			QDialog {
				background-color: white;
				padding-bottom: 10px;
			}
			'''
		)
		
		self.border_design = QLabel()
		self.border_design.setAlignment(Qt.AlignCenter)
		self.border_design.setFixedSize(500, 40)
		self.border_design.setStyleSheet(
			'''
			QLabel {
				background-color: rgb(60, 150, 200);
			}
			'''
		)
		self.window_layout.addWidget(self.border_design, stretch=0, alignment=Qt.AlignTop)

		self.page_title = QLabel()
		self.page_title.setAlignment(Qt.AlignCenter)
		self.page_title.setMaximumSize(200, 40)
		# self.page_title.setStyleSheet(
		# 	'''
		# 	QLabel {
		# 		border: 2px solid rgb(60, 150, 200);
		# 		font-weight: bold;
		# 		font-size: 20px;
		# 		color: rgb(60, 150, 200);
		# 		border-radius: 15px;
		# 	}
		# 	'''
		# )
		self.main_layout.addWidget(self.page_title, stretch=0, alignment=Qt.AlignCenter)

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
		self.main_layout.addWidget(self.username, stretch=0, alignment=Qt.AlignCenter)

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
		self.main_layout.addWidget(self.password, stretch=0, alignment=Qt.AlignCenter)

		self.verify_button = Templates.AnimatedButton()
		self.verify_button.setText('Verify')
		self.verify_button.setMaximumSize(250, 60)
		self.verify_button.clicked.connect(self.verify_button_slot)
		self.main_layout.addWidget(self.verify_button, stretch=0, alignment=Qt.AlignCenter)

		self.window_layout.addLayout(self.main_layout)

		# Diamond Admin credentials

		# Username : DRQ_Admin
		# Password : 246DRQ

		self.username_val = 'DRQ_Admin'
		self.password_val = '246DRQ'

	def verify_button_slot(self):
		try:
			from Projects.DiamondRubyQuiz.Tools import Database
	
			if self.username.text() and self.password.text():
				if (self.username.text() == self.username_val) and (self.password.text() == self.password_val):

					Database.insert_quiz_master(
						self.first_name,
						self.last_name,
						self.email,
						self.username_,
						self.password_
					)

					msg = f'Quiz Master {self.username_} has been successfully registered.'
					message_box = QMessageBox()
					message_box.about(self, 'Quiz Manager', msg)
					
					from Projects.DiamondRubyQuiz.Quiz import SetQuiz

					self.stacked_widget.addWidget(SetQuiz.QuizSheet(self.stacked_widget))
					self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() + 1)

					self.close()
				else:
					msg = 'Invalid credentials. Please check your username or password.'
					message_box = QMessageBox()
					message_box.about(self, 'Quiz Manager', msg)
			else:
				pass
		except Exception as e:
			raise e


class QuizMasterRegister(QGroupBox):
	def __init__(self):
		QGroupBox.__init__(self)
		
		self.window_title = 'DiamondRubyQuiz'
		self.window_icon = QIcon('Icons/icon.png')

		self.window_layout = QVBoxLayout()
		self.window_layout.setSpacing(0)
		self.window_layout.setContentsMargins(0, 0, 0, 0)
		self.window_layout.setAlignment(Qt.AlignCenter)

		self.main_layout = QVBoxLayout()
		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.main_layout.setAlignment(Qt.AlignCenter)

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

		self.window_layout.addWidget(self.main_group)

		self.setLayout(self.window_layout)
		self.setWindowTitle(self.window_title)
		self.setWindowIcon(self.window_icon)
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
				padding: 5px;
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

		self.topic = 'Quiz Registration'
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

		self.clock_layout = QVBoxLayout()
		self.clock_layout.setSpacing(3)
		self.clock_layout.setAlignment(Qt.AlignCenter)

		self.other_0 = QHBoxLayout()
		self.other_0.setSpacing(5)
		self.other_0.setAlignment(Qt.AlignCenter)

		self.clock_layout.addLayout(self.other_0)

		self.first_name = QLineEdit()
		self.first_name.setPlaceholderText('First name')
		self.first_name.setMaximumSize(200, 60)
		self.first_name.setStyleSheet(
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
		self.other_0.addWidget(self.first_name)

		self.middle_name = QLineEdit()
		self.middle_name.setPlaceholderText('Middle name')
		self.middle_name.setMaximumSize(200, 60)
		self.middle_name.setStyleSheet(
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
		self.other_0.addWidget(self.middle_name)

		self.last_name = QLineEdit()
		self.last_name.setPlaceholderText('Last name')
		self.last_name.setMaximumSize(200, 60)
		self.last_name.setStyleSheet(
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
		self.clock_layout.addWidget(self.last_name, stretch=0, alignment=Qt.AlignCenter)

		self.other_layout = QVBoxLayout()
		self.other_layout.setAlignment(Qt.AlignCenter)
		self.other_layout.setSpacing(3)
		
		self.other_1 = QHBoxLayout()
		self.other_1.setSpacing(5)
		self.other_1.setAlignment(Qt.AlignCenter)

		self.other_2 = QHBoxLayout()
		self.other_2.setSpacing(5)
		self.other_2.setAlignment(Qt.AlignCenter)

		self.email = QLineEdit()
		self.email.setPlaceholderText('E-Mail')
		self.email.setMaximumSize(200, 60)
		self.email.setStyleSheet(
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
		self.other_1.addWidget(self.email)

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
		self.other_1.addWidget(self.username)

		self.new_password = QLineEdit()
		self.new_password.setPlaceholderText('New Password')
		self.new_password.setEchoMode(QLineEdit.Password)
		self.new_password.setMaximumSize(200, 60)
		self.new_password.setStyleSheet(
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
		self.other_2.addWidget(self.new_password)

		self.confirm_password = QLineEdit()
		self.confirm_password.setPlaceholderText('Confirm Password')
		self.confirm_password.setEchoMode(QLineEdit.Password)
		self.confirm_password.setMaximumSize(200, 60)
		self.confirm_password.setStyleSheet(
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
		self.other_2.addWidget(self.confirm_password)

		self.other_layout.addLayout(self.other_1)
		self.other_layout.addLayout(self.other_2)
		self.clock_layout.addLayout(self.other_layout)

		self.central_mid_layout.addLayout(self.clock_layout)

		self.button_layout = QHBoxLayout()
		self.button_layout.setSpacing(0)
		self.button_layout.setAlignment(Qt.AlignCenter)

		self.login_button = Templates.AnimatedButton()
		self.login_button.setText('Sign Up')
		self.login_button.clicked.connect(self.login_button_slot)
		self.button_layout.addWidget(self.login_button)

		self.central_mid_layout.addLayout(self.button_layout)

		self.central_mid_group = QGroupBox()
		self.central_mid_group.setMaximumSize(self.mid_width, 300)
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

		self.central_layout.addWidget(self.central_mid_group)

		self.background_stacked_widget.addWidget(self.central_group)
		self.background_stacked_widget.setCurrentIndex(0)


	def login_button_slot(self):
		try:
			from Projects.DiamondRubyQuiz.Tools import Database
			from Projects.DiamondRubyQuiz.Quiz import StartQuiz

			all_usernames = Database.get_quiz_master_column('username')

			if self.first_name.text() and self.middle_name.text():
				if self.username.text() and self.new_password.text() and self.confirm_password.text() and self.email.text():
					if self.username.text() in all_usernames:
						msg = 'Username already exist, please pick a different Username.'
						message_box = QMessageBox()
						message_box.about(self, 'Quiz Manager', msg)
					else:
						if self.new_password.text() == self.confirm_password.text():
							self.credentials = [
								self.first_name.text(),
								self.middle_name.text(),
								self.last_name.text(),
								self.username.text(),
								self.new_password.text(),
								self.email.text()
							]
							self.admin_verify = QuizMasterVerify(self.background_stacked_widget, self.credentials)
							self.admin_verify.show()

							# self.background_stacked_widget.setCurrentIndex(1)
						else:
							msg = 'Your passwords don\'t match.'
							message_box = QMessageBox()
							message_box.about(self, 'Quiz Manager', msg)
				else:
					msg = 'Fill in your desired Login Details to continue.'
					message_box = QMessageBox()
					message_box.about(self, 'Quiz Manager', msg)
			else:
				msg = 'Fill in your Names to continue.'
				message_box = QMessageBox()
				message_box.about(self, 'Quiz Manager', msg)
		except Exception as e:
			raise e
