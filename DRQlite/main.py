from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Question(QGroupBox):
	def __init__(self, question_collection, question_num, question, a, b, c, d):
		QGroupBox.__init__(self)

		self.question_collection = question_collection
		self.question_num = question_num
		self.question = question
		self.a = a
		self.b = b
		self.c = c
		self.d = d

		self.group_layout = QVBoxLayout()
		self.group_layout.setSpacing(5)
		self.group_layout.setAlignment(Qt.AlignTop)

		self.setLayout(self.group_layout)

		self.initialization()

	def initialization(self):
		self.question_num_label = QLabel(str(self.question_num))
		self.question_num_label.setMaximumHeight(45)
		self.question_num_label.setStyleSheet(
			'''
			QLabel {
				font-size: 13px;
				font: Verdana;
				font-weight: bold;
				background-color: white;
			}
			'''
		)
		self.group_layout.addWidget(self.question_num_label)

		self.question_label = QTextBrowser()
		self.question_label.setText(self.question)
		self.question_label.setMaximumHeight(300)
		self.question_label.setStyleSheet(
			'''
			QTextBrowser {
				font-size: 15px;
				font: Verdana;
				font-weight: bold;
				background-color: white;
			}
			'''
		)
		self.group_layout.addWidget(self.question_label)

		self.a_label = QCheckBox(str(self.a))
		self.a_label.clicked.connect(self.a_slot)
		self.a_label.setMaximumHeight(300)
		self.a_label.setStyleSheet(
			'''
			QCheckBox {
				font-size: 15px;
				font: Verdana;
				font-weight: bold;
			}
			'''
		)
		self.group_layout.addWidget(self.a_label)

		self.b_label = QCheckBox(str(self.b))
		self.b_label.clicked.connect(self.b_slot)
		self.b_label.setMaximumHeight(300)
		self.b_label.setStyleSheet(
			'''
			QCheckBox {
				font-size: 15px;
				font: Verdana;
				font-weight: bold;
			}
			'''
		)
		self.group_layout.addWidget(self.b_label)

		self.c_label = QCheckBox(str(self.c))
		self.c_label.clicked.connect(self.c_slot)
		self.c_label.setMaximumHeight(300)
		self.c_label.setStyleSheet(
			'''
			QCheckBox {
				font-size: 15px;
				font: Verdana;
				font-weight: bold;
			}
			'''
		)
		self.group_layout.addWidget(self.c_label)

		self.d_label = QCheckBox(str(self.d))
		self.d_label.clicked.connect(self.d_slot)
		self.d_label.setMaximumHeight(300)
		self.d_label.setStyleSheet(
			'''
			QCheckBox {
				font-size: 15px;
				font: Verdana;
				font-weight: bold;
			}
			'''
		)
		self.group_layout.addWidget(self.d_label)

	def a_slot(self):
		self.a_label.setChecked(True)
		self.b_label.setChecked(False)
		self.c_label.setChecked(False)
		self.d_label.setChecked(False)

		self.question_collection[int(self.question_num) - 1] = ('A', self.a_label.text())

	def b_slot(self):
		self.a_label.setChecked(False)
		self.b_label.setChecked(True)
		self.c_label.setChecked(False)
		self.d_label.setChecked(False)

		self.question_collection[int(self.question_num) - 1] = ('B', self.b_label.text())

	def c_slot(self):
		self.a_label.setChecked(False)
		self.b_label.setChecked(False)
		self.c_label.setChecked(True)
		self.d_label.setChecked(False)

		self.question_collection[int(self.question_num) - 1] = ('C', self.c_label.text())

	def d_slot(self):
		self.a_label.setChecked(False)
		self.b_label.setChecked(False)
		self.c_label.setChecked(False)
		self.d_label.setChecked(True)

		self.question_collection[int(self.question_num) - 1] = ('D', self.d_label.text())


class Quiz(QWidget):
	def __init__(self, question_dictionary):
		QWidget.__init__(self)

		self.question_dictionary = question_dictionary

		self.all_questions = self.question_dictionary['questions']
		self.all_options = self.question_dictionary['options']
		self.all_answers = self.question_dictionary['answers']

		self.window_layout = QVBoxLayout()
		self.window_layout.setAlignment(Qt.AlignTop)
		self.window_layout.setSpacing(4)

		self.setLayout(self.window_layout)
		self.setWindowTitle('Diamond Ruby Quiz')

		self.question_answer_collection = []
		self.score = 0

		self.initialization()

	def initialization(self):
		self.navigation()
		self.stackedWIDGET()
		self.questionPANEL()
		self.bottomLAYER()

	'''
		Navigation
	'''

	def navigation(self):
		self.navigation_layout = QHBoxLayout()
		self.navigation_layout.setSpacing(5)
		self.navigation_layout.setAlignment(Qt.AlignCenter)
		self.window_layout.addLayout(self.navigation_layout)

		self.previous_button = QPushButton('Previous')
		self.previous_button.clicked.connect(self.previous_slot)
		self.previous_button.setMaximumSize(130, 40)
		self.navigation_layout.addWidget(self.previous_button)

		self.next_button = QPushButton('Next')
		self.next_button.clicked.connect(self.next_slot)
		self.next_button.setMaximumSize(130, 40)
		self.navigation_layout.addWidget(self.next_button)

	def stackedWIDGET(self):
		self.stacked_widget_layout = QVBoxLayout()
		self.stacked_widget_layout.setAlignment(Qt.AlignCenter)
		self.stacked_widget_layout.setSpacing(4)
		self.window_layout.addLayout(self.stacked_widget_layout)

		self.stacked_widget = QStackedWidget()
		self.stacked_widget.setStyleSheet(
			'''
			QStackedWidget {
				border: 1px solid black;
			}
			'''
		)
		self.stacked_widget_layout.addWidget(self.stacked_widget)

	def questionPANEL(self):
		'''
			Adding Initial Question Khadija :)
		'''

		self.current_index = 0

		for i in range(len(self.all_questions)):
			self.stacked_widget.addWidget(Question(
				self.question_answer_collection,
				self.current_index + 1,
				self.all_questions[self.current_index],
				self.all_options[self.current_index][0],
				self.all_options[self.current_index][1],
				self.all_options[self.current_index][2],
				self.all_options[self.current_index][3]
				)
			)
			self.question_answer_collection.append(())
			self.current_index += 1
		self.stacked_widget.setCurrentIndex(0)

	def bottomLAYER(self):
		self.bottom_layout = QHBoxLayout()
		self.bottom_layout.setAlignment(Qt.AlignCenter)
		self.bottom_layout.setSpacing(5)
		self.window_layout.addLayout(self.bottom_layout)

		self.submit_button = QPushButton('submit')
		self.submit_button.setMaximumSize(200, 40)
		self.submit_button.clicked.connect(self.submit_slot)
		self.bottom_layout.addWidget(self.submit_button)

	'''
		Slots
	'''

	def previous_slot(self):
		self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() - 1)

	def next_slot(self):
		self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() + 1)

	def submit_slot(self):
		self.dialog_layout = QHBoxLayout()
		self.dialog_layout.setSpacing(5)
		self.dialog_layout.setAlignment(Qt.AlignCenter)

		self.dialog_widget = QDialog()
		self.dialog_widget.setMaximumSize(400, 100)
		self.dialog_widget.setWindowTitle('Confirmation Dialog')
		self.dialog_widget.setLayout(self.dialog_layout)

		self.warning = QLabel('Are you sure you want to submit?')
		self.dialog_layout.addWidget(self.warning)

		self.yes = QPushButton('Yes')
		self.yes.setMaximumSize(100, 40)
		self.yes.clicked.connect(self.yes_slot)
		self.dialog_layout.addWidget(self.yes)

		self.no = QPushButton('No')
		self.no.setMaximumSize(100, 40)
		self.no.clicked.connect(self.no_slot)
		self.dialog_layout.addWidget(self.no)

		self.dialog_widget.show()

	def yes_slot(self):
		for q in range(len(self.all_answers)):
			if self.score >= len(self.all_answers):
				self.score -= len(self.all_answers)
				if len(self.question_answer_collection[q]) != 0:
					if self.all_answers[q] == self.question_answer_collection[q][-1]:
						self.score += 1
			else:
				if len(self.question_answer_collection[q]) != 0:
					if self.all_answers[q] == self.question_answer_collection[q][-1]:
						self.score += 1

		self.dialog_widget.close()

		msg = f'You scored {(round(self.score / len(self.all_answers) * 100, 2))} % of {len(self.all_answers)} Questions.'
		message_box = QMessageBox()
		message_box.about(self, 'Diamond Ruby Quiz', msg)

	def no_slot(self):
		self.dialog_widget.close()


class Login(QDialog):
	def __init__(self, question_dictionary, database_dictionary):
		QDialog.__init__(self)

		self.question_dictionary = question_dictionary
		self.database_dictionary = database_dictionary

		self.usernames = self.database_dictionary['usernames']
		self.passwords = self.database_dictionary['passwords']
		self.emails = self.database_dictionary['emails']

		self.username_user = 'jija'
		self.password_user = '1029'
		self.email_user = 'jija@gmail.com'

		self.usernames.append(self.username_user)
		self.passwords.append(self.password_user)
		self.emails.append(self.email_user)

		self.dialog_layout = QVBoxLayout()
		self.dialog_layout.setAlignment(Qt.AlignTop)

		self.setLayout(self.dialog_layout)
		self.setFixedSize(400, 350)
		self.setStyleSheet(
			'''
			QDialog {
				padding: 15px;
			}
			'''
		)
		self.setWindowTitle('Diamond Ruby Quiz Login')

		self.initialization()

	def initialization(self):
		self.dialog_stacked_widget = QStackedWidget()

		self.loginFORM()
		self.registerFORM()

		self.options_layout = QHBoxLayout()
		self.options_layout.setSpacing(5)
		self.options_layout.setAlignment(Qt.AlignTop)

		self.login_button = QPushButton('Login')
		self.login_button.setMaximumSize(200, 25)
		self.login_button.clicked.connect(self.login_slot_page)
		self.options_layout.addWidget(self.login_button)

		self.register_button = QPushButton('Register')
		self.register_button.setMaximumSize(200, 25)
		self.register_button.clicked.connect(self.register_slot_page)
		self.options_layout.addWidget(self.register_button)

		self.dialog_layout.addLayout(self.options_layout)
		self.dialog_layout.addWidget(self.dialog_stacked_widget, stretch=0, alignment=Qt.AlignCenter)

		self.title = QLabel('Diamond Ruby Quiz')
		self.title.setAutoFillBackground(True)
		self.title.autoFillBackground()
		self.title.setStyleSheet(
			'''
			QLabel {
				border: 1px solid black;
			}
			'''
		)
		self.title.setAlignment(Qt.AlignCenter)
		self.dialog_stacked_widget.addWidget(self.title)
		self.dialog_stacked_widget.setCurrentIndex(2)

	def login_slot_page(self):
		self.dialog_stacked_widget.setCurrentIndex(0)

	def register_slot_page(self):
		self.dialog_stacked_widget.setCurrentIndex(1)

	def loginFORM(self):
		self.dialog_stacked_widget.addWidget(
			LoginForm(
				self.question_dictionary,
				self.database_dictionary,
				self.dialog_stacked_widget
				)
			)

	def registerFORM(self):
		self.dialog_stacked_widget.addWidget(
			RegistrationForm(
				self.question_dictionary,
				self.database_dictionary,
				self.dialog_stacked_widget
			)
		)


class LoginForm(QGroupBox):
	def __init__(self, question_dictionary, database_dictionary, dialog_stacked_widget):
		QGroupBox.__init__(self)

		self.question_dictionary = question_dictionary
		self.database_dictionary = database_dictionary
		self.dialog_stacked_widget = dialog_stacked_widget

		self.usernames = self.database_dictionary['usernames']
		self.passwords = self.database_dictionary['passwords']
		self.emails = self.database_dictionary['emails']

		self.login_quiz_layout = QVBoxLayout()
		self.login_quiz_layout.setSpacing(5)
		self.login_quiz_layout.setAlignment(Qt.AlignCenter)

		self.setLayout(self.login_quiz_layout)

		self.title_label = QLabel('Quiz Login')
		self.title_label.setAlignment(Qt.AlignCenter)
		self.title_label.setFixedHeight(60)
		self.login_quiz_layout.addWidget(self.title_label)

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

		self.login_button = QPushButton('Login')
		self.login_button.clicked.connect(self.login_slot)
		self.login_button.setMaximumSize(200, 60)

		self.login_quiz_layout.addWidget(self.login_button)

	def login_slot(self):
		if self.username.text() and self.password.text():
			if self.username.text() in self.usernames:
				id_ = self.usernames.index(self.username.text())
				if self.password.text() == self.passwords[id_]:
					self.username.setText('')
					self.password.setText('')

					msg = 'Login Successful.'
					message_box = QMessageBox()
					message_box.about(self, 'Diamond Ruby Quiz', msg)

					self.loginSUCCESS()
				else:
					msg = 'Incorrect username or password.'
					message_box = QMessageBox()
					message_box.about(self, 'Diamond Ruby Quiz', msg)
			else:
				msg = 'Incorrect username or password.'
				message_box = QMessageBox()
				message_box.about(self, 'Diamond Ruby Quiz', msg)
		else:
			msg = 'Enter a valid username and password.'
			message_box = QMessageBox()
			message_box.about(self, 'Diamond Ruby Quiz', msg)

	def loginSUCCESS(self):
		self.close()

		self.quiz_page = Quiz(self.question_dictionary)
		self.quiz_page.show()


class RegistrationForm(QGroupBox):
	def __init__(self, question_dictionary, database_dictionary, dialog_stacked_widget):
		QGroupBox.__init__(self)

		self.question_dictionary = question_dictionary
		self.database_dictionary = database_dictionary
		self.dialog_stacked_widget = dialog_stacked_widget

		self.usernames = self.database_dictionary['usernames']
		self.passwords = self.database_dictionary['passwords']
		self.emails = self.database_dictionary['emails']

		self.register_quiz_layout = QVBoxLayout()
		self.register_quiz_layout.setSpacing(5)
		self.register_quiz_layout.setAlignment(Qt.AlignCenter)

		self.setLayout(self.register_quiz_layout)

		self.title_label = QLabel('Quiz Registration')
		self.title_label.setAlignment(Qt.AlignCenter)
		self.title_label.setFixedHeight(60)
		self.register_quiz_layout.addWidget(self.title_label)

		self.reg_username = QLineEdit()
		self.reg_username.setPlaceholderText('Username')
		self.reg_username.setMaximumSize(200, 60)
		self.reg_username.setStyleSheet(
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
		self.register_quiz_layout.addWidget(self.reg_username)

		self.reg_email = QLineEdit()
		self.reg_email.setPlaceholderText('Email')
		self.reg_email.setMaximumSize(200, 60)
		self.reg_email.setStyleSheet(
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
		self.register_quiz_layout.addWidget(self.reg_email)

		self.new_password = QLineEdit()
		self.new_password.setPlaceholderText('New password')
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
		self.register_quiz_layout.addWidget(self.new_password)

		self.confirm_password = QLineEdit()
		self.confirm_password.setPlaceholderText('Confirm password')
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
		self.register_quiz_layout.addWidget(self.confirm_password)

		self.register_button = QPushButton('Register')
		self.register_button.clicked.connect(self.register_slot)
		self.register_button.setMaximumSize(200, 60)

		self.register_quiz_layout.addWidget(self.register_button)

	def register_slot(self):
		if (self.reg_username.text() and
			self.reg_email.text() and
			self.new_password.text() and
			self.confirm_password.text()
			):
			if self.reg_username.text() not in self.usernames:
				if self.new_password.text() == self.confirm_password.text():
					self.usernames.append(self.reg_username.text())
					self.passwords.append(self.new_password.text())
					self.emails.append(self.reg_email.text())

					self.reg_username.setText('')
					self.reg_email.setText('')
					self.new_password.setText('')
					self.confirm_password.setText('')

					msg = 'Registration Successful.'
					message_box = QMessageBox()
					message_box.about(self, 'Quiz Manager', msg)

					self.dialog_stacked_widget.setCurrentIndex(0)
				else:
					msg = 'Incorrect password.\nPasswords mismatch !!!'
					message_box = QMessageBox()
					message_box.about(self, 'Quiz Manager', msg)
			else:
				msg = 'User name already exists.\nPlease choose a different username.'
				message_box = QMessageBox()
				message_box.about(self, 'Quiz Manager', msg)
		else:
			msg = 'Please fill all fields to continue.'
			message_box = QMessageBox()
			message_box.about(self, 'Quiz Manager', msg)


question_dictionary = {
	'questions':
	[
		'What is the longest that an elephant has lived? (That we know of)',
		'How many rings are on the olympic flag?',
		'What is a tarsier?',
		'How did Spider-Man yet his powers?',
		'In darts, what\'s the most points you can get with a single throw?'
	],
	'options':
	[
		['17 years', '49 years', '86 years', '142 years'],
		['None', '4', '5', '7'],
		['A primate', 'A rodent', 'A lizard', 'A bird'],
		['Military experiment gone awry', 'Born with them', 'Woke up with them after a strange dream', 'Bitten by a radioactive Spider'],
		['20', '50', '60', '100']
	],
	'answers':
	[
		'86 years',
		'5',
		'A primate',
		'Bitten by a radioactive Spider',
		'60'
	]
}


database_dictionary = {
	'usernames': [],
	'passwords': [],
	'emails': []
}


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Login(question_dictionary, database_dictionary)
	window.show()
	sys.exit(app.exec_())
