from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Projects.DiamondRubyQuiz.Tools import Templates
import sys


class Login(QDialog):
	def __init__(self, widget, next_page):
		QDialog.__init__(self)

		self.widget = widget
		self.next_page = next_page

		self.dialog_layout = QVBoxLayout()
		self.dialog_layout.setSpacing(5)
		self.dialog_layout.setAlignment(Qt.AlignTop)

		self.setLayout(self.dialog_layout)
		self.setStyleSheet(
			'''
			QDialog {
				padding: 20px;
				border: 0px;
			}
			'''
		)

		self.initialization()

	def initialization(self):
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
		self.dialog_layout.addWidget(self.username)

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
		self.dialog_layout.addWidget(self.password)

		self.login_button = Templates.AnimatedButton('Login')
		self.login_button.clicked.connect(self.login_button_slot)
		self.dialog_layout.addWidget(self.login_button)

	def login_button_slot(self):
		try:
			from Projects.DiamondRubyQuiz.Tools import Database

			self.all_usernames = Database.get_quiz_master_column('username')
			self.all_passwords = Database.get_quiz_master_column('password')

			if username.text() in self.all_usernames:
				if password.text() == self.all_passwords[self.all_usernames.index(self.username.text())]:
					msg = 'Login successful.'
					message_box = QMessageBox()
					message_box.about(self, 'Quiz Manager', msg)

					self.widget.addWidget(self.next_page)
					self.widget.setCurrentIndex(self.currentIndex() + 1)
				else:
					msg = 'Invalid credentials.\nPlease check your username and password to continue.'
					message_box = QMessageBox()
					message_box.about(self, 'Quiz Manager', msg)
			else:
				msg = 'Invalid credentials.\nPlease check your username and password to continue.'
				message_box = QMessageBox()
				message_box.about(self, 'Quiz Manager', msg)
		except Exception as e:
			raise e


class CheckQuiz(QGroupBox):
	def __init__(self, widget):
		QGroupBox.__init__(self)

		self.widget = widget

		self.main_layout = QVBoxLayout()
		self.main_layout.setSpacing(0)

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

		day = 'Monday'
		day = f'{day}\'s'
		mst = 'DiamondRubyQuiz'

		self.quiz_day_label = QLabel('Available Quiz')
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
		self.header_group.setMaximumHeight(200)
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
		self.central_mid_layout.setSpacing(0)
		self.central_mid_layout.setContentsMargins(0, 0, 0, 0)
		self.central_mid_layout.setAlignment(Qt.AlignTop)

		self.central_mid_group = QGroupBox()
		self.central_mid_group.setFixedWidth(self.mid_width - 100)
		self.central_mid_group.setMaximumHeight(400)
		self.central_mid_group.setLayout(self.central_mid_layout)
		self.central_mid_group.setStyleSheet(
			'''
			QGroupBox {
				border-radius: 40px;
				border: 0px;
				background-color: white;
				padding: 12px;
			}
			'''
		)
		
		'''
			Quiz Table
		'''
		
		self.quizTABLE()
		self.central_mid_scroll = QScrollArea()
		self.central_mid_scroll.setWidget(self.central_mid_group)
		self.central_mid_scroll.setWidgetResizable(True)
		self.central_mid_scroll.setStyleSheet(
			'''
			QScrollArea {
				border-radius: 40px;
				border: 0px;
				background-color: white;
				padding: 12px;
			}
			'''
		)
		self.central_layout.addWidget(self.central_mid_scroll)

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

	def quizTABLE(self):
		try:
			from Projects.DiamondRubyQuiz.Tools import TableTools, LoopEmit

			self.central_mid_layout.addWidget(TableTools.ResultTableDef())

			self.table_index = 1
			
			self.submitSEQ = LoopEmit.QuestionEmit(30)
			self.submitSEQ.countChanged.connect(self.distributeTABLE)
			self.submitSEQ.run()
		except Exception as e:
			raise e

	def distributeTABLE(self):
		try:
			from Projects.DiamondRubyQuiz.Tools import Database, TableTools

			self.all_questions = Database.get_quiz_check_all()
			# self.id_ = id_
			# self.serial_num = serial_num
			# self.quiz_topic = quiz_topic
			# self.quiz_day = quiz_day
			# self.quiz_master = quiz_master
			# self.quiz_duration = quiz_duration
			for i in self.all_questions:
				self.central_mid_layout.addWidget(
					TableTools.ResultTable(
						str(i[0]),
						str(self.table_index),
						str(i[1]),
						str(i[2]),
						str(i[3]),
						str(i[4])
					)
				)
				self.table_index += 1
		except Exception as e:
			raise e

	def check_quiz_slot(self):
		try:
			pass
		except Exception as e:
			raise e
