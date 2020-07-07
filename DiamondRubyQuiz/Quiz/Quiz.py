from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Projects.DiamondRubyQuiz.Tools import Templates
from Projects.DiamondRubyQuiz.Tools import LoopEmit
import sys
import time as t


class QuizQuestion(QGroupBox):
	def __init__(self, question_collection, id_='', number='1', question='question', a='a', b='b', c='c', d='d'):
		QGroupBox.__init__(self)

		self.question_collection = question_collection
		self.id_ = id_
		self.number = number
		self.question = question
		self.a = a
		self.b = b
		self.c = c
		self.d = d

		self.question_layout = QVBoxLayout()
		self.question_layout.setSpacing(4)
		self.question_layout.setAlignment(Qt.AlignTop)

		self.setLayout(self.question_layout)

		self.setMaximumWidth(400)

		self.initialization()

	def initialization(self):
		self.number_label = QLabel(f'{self.number}.')
		self.number_label.setMaximumSize(100, 40)
		self.number_label.setAlignment(Qt.AlignLeft)
		self.number_label.setStyleSheet(
			'''
			QLabel {
				color: black;
				font: Arial Black;
				font-weight: bold;
				font-size: 14px;
				border: 0px;
				background-color: white;
			}
			'''
		)
		self.question_layout.addWidget(self.number_label)

		self.question_label = QTextBrowser()
		self.question_label.setText(self.question)
		self.question_label.setMaximumSize(400, 400)
		self.question_label.setAlignment(Qt.AlignLeft)
		self.question_label.setStyleSheet(
			'''
			QTextBrowser {
				color: black;
				font: Arial Black;
				font-weight: bold;
				font-size: 13px;
				border: 0px;
				background-color: white;
			}
			'''
		)
		self.question_layout.addWidget(self.question_label)

		self.spacer_label = QLabel()
		self.spacer_label.setMaximumHeight(60)
		self.spacer_label.setStyleSheet(
			'''
			QLabel {
				border: 0px;
				background-color: white;
			}
			'''
		)
		self.question_layout.addWidget(self.spacer_label)

		self.option_size = (700, 60)

		self.option_a = Templates.OptionButton(f'A. {self.a}')
		self.option_a.clicked.connect(self.a_slot)
		self.option_a.setMaximumSize(self.option_size[0], self.option_size[1])
		# self.option_a.setStyleSheet(self.default_sheet)
		self.question_layout.addWidget(self.option_a)

		self.option_b = Templates.OptionButton(f'B. {self.b}')
		self.option_b.clicked.connect(self.b_slot)
		self.option_b.setMaximumSize(self.option_size[0], self.option_size[1])
		# self.option_b.setStyleSheet(self.default_sheet)
		self.question_layout.addWidget(self.option_b)

		self.option_c = Templates.OptionButton(f'C. {self.c}')
		self.option_c.clicked.connect(self.c_slot)
		self.option_c.setMaximumSize(self.option_size[0], self.option_size[1])
		# self.option_c.setStyleSheet(self.default_sheet)
		self.question_layout.addWidget(self.option_c)
		
		self.option_d = Templates.OptionButton(f'D. {self.d}')
		self.option_d.clicked.connect(self.d_slot)
		self.option_d.setMaximumSize(self.option_size[0], self.option_size[1])
		# self.option_d.setStyleSheet(self.default_sheet)
		self.question_layout.addWidget(self.option_d)

	def a_slot(self):
		try:
			self.question_collection[self.number - 1] = ((self.number, 'A', self.a))
		except Exception as e:
			raise e

	def b_slot(self):
		try:
			self.question_collection[self.number - 1] = ((self.number, 'B', self.b))
		except Exception as e:
			raise e

	def c_slot(self):
		try:
			self.question_collection[self.number - 1] = ((self.number, 'C', self.c))
		except Exception as e:
			raise e

	def d_slot(self):
		try:
			self.question_collection[self.number - 1] = ((self.number, 'D', self.d))
		except Exception as e:
			raise e


class QuizPage(QGroupBox):
	def __init__(self, quiz_topic, username, widget):
		QGroupBox.__init__(self)

		self.quiz_topic = quiz_topic
		self.username = username
		self.widget = widget

		self.window_layout = QVBoxLayout()
		self.window_layout.setAlignment(Qt.AlignTop)
		self.window_layout.setSpacing(5)

		self.stacked_widget = QStackedWidget()

		self.window_layout.addWidget(self.stacked_widget, stretch=0, alignment=Qt.AlignCenter)

		self.setLayout(self.window_layout)
		self.setStyleSheet(
			'''
			QGroupBox {
				padding: 10px;
				padding-bottom: 0px;
			}
			'''
		)

		self.initialization()

	def initialization(self):
		self.topBAR()
		self.navigationPANEL()
		self.questionPANEL()
	
	def topBAR(self):
		self.main_layout = QVBoxLayout()
		self.main_layout.setAlignment(Qt.AlignTop)
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.main_layout.setSpacing(0)

		self.central_eff = QGraphicsDropShadowEffect()
		self.central_eff.setBlurRadius(11)
		self.central_eff.setOffset(1.2)
		# self.central_eff.setYOffset(-0.2)

		self.mid_width = 600

		self.main_group = QGroupBox()
		self.main_group.setGraphicsEffect(self.central_eff)
		self.main_group.setMaximumSize(self.mid_width, 500)
		self.main_group.setLayout(self.main_layout)
		self.main_group.setStyleSheet(
			'''
			QGroupBox {
				background-color: rgb(60, 150, 200);
				border: 0px;
				border-radius: 40px;
				padding: 10px;
				padding-bottom: 0px;
			}
			'''
		)
		self.stacked_widget.addWidget(self.main_group)
		self.stacked_widget.setCurrentIndex(0)

		self.top_widget = QHBoxLayout()
		# self.top_widget.setAlignment(Qt.AlignCenter)
		self.top_widget.setContentsMargins(20, 20, 20, 20)
		self.top_widget.setSpacing(5)

		self.timer = QLabel('00:00')
		self.timer.setFixedSize(100, 35)
		self.timer.setStyleSheet(
			'''
			QLabel {
				color: white;
				font-weight: bold;
				font-size: 14px;
				font: Arial Black;
			}
			'''
		)
		self.top_widget.addWidget(self.timer, stretch=0, alignment=Qt.AlignCenter)

		self.submit = Templates.AnimatedButton('SUBMIT')
		self.submit.clicked.connect(self.submit_slot)
		self.submit.setMaximumSize(240, 35)
		self.top_widget.addWidget(self.submit, stretch=0, alignment=Qt.AlignRight)

		self.main_layout.addLayout(self.top_widget)

	def navigationPANEL(self):
		self.nav_panel_layout = QHBoxLayout()
		self.nav_panel_layout.setSpacing(5)
		self.nav_panel_layout.setAlignment(Qt.AlignCenter)

		self.question_panel_stacked_widget = QStackedWidget()
		# self.question_panel_stacked_widget.setAlignment(Qt.AlignCenter)

		self.question_index = 1
		# self.nav_panel_layout.addWidget(Templates.QuestionButton(self.question_index, self.question_panel_stacked_widget))
		# self.question_index += 1

		# self.question_panel_stacked_widget.addWidget(QuizQuestion())
		# self.question_panel_stacked_widget.setCurrentIndex(0)

		self.nav_panel_group = QGroupBox()
		self.nav_panel_group.setMaximumSize(650, 50)
		self.nav_panel_group.setLayout(self.nav_panel_layout)
		self.nav_panel_group.setStyleSheet(
			'''
			QGroupBox {
				border: 0px;
				background-color: rgb(60, 150, 200);
			}
			'''
		)

		self.nav_panel_scroll = QScrollArea()
		# self.nav_panel_scroll.setMaximumSize(650, 50)
		self.nav_panel_scroll.setWidget(self.nav_panel_group)
		self.nav_panel_scroll.setWidgetResizable(True)
		self.nav_panel_scroll.setStyleSheet(
			'''
			QScrollArea {
				border: 0px;
				background-color: rgb(60, 150, 200);
			}
			'''
		)

		self.main_layout.addWidget(self.nav_panel_scroll)

	def questionPANEL(self):
		self.score = 0
		self.question_answers_collection = []

		self.question_panel_layout = QHBoxLayout()
		self.question_panel_layout.setSpacing(5)

		self.question_panel_layout.addWidget(self.question_panel_stacked_widget, stretch=0, alignment=Qt.AlignCenter)

		self.submitSEQ = LoopEmit.QuestionEmit(30)
		self.submitSEQ.countChanged.connect(self.question_signal)
		self.submitSEQ.run()

		self.question_panel_group = QGroupBox()
		self.question_panel_group.setMaximumSize(self.mid_width, 500)
		self.question_panel_group.setLayout(self.question_panel_layout)

		self.main_layout.addWidget(self.question_panel_group, stretch=0, alignment=Qt.AlignBottom)

	def submit_slot(self):
		self.submit = LoopEmit.QuestionEmit(30)
		self.submit.countChanged.connect(self.submit_confirmation)
		self.submit.run()

	def submit_confirmation(self):
		try:
			self.conf_dialog_layout = QHBoxLayout()
			self.conf_dialog_layout.setSpacing(4)
			self.conf_dialog_layout.setAlignment(Qt.AlignCenter)

			self.warning = QLabel('Are you sure you want to end the quiz?')
			self.conf_dialog_layout.addWidget(self.warning)

			self.yes = QPushButton('Yes')
			self.yes.clicked.connect(self.yes_slot)
			self.yes.setMaximumSize(100, 40)
			self.yes.setStyleSheet(
				'''
				QPushButton {
					background-color: rgb(120, 220, 120);
					border-radius: 5px;
					padding: 5px;
				}
				QPushButton:hover {
					background-color: rgb(120, 240, 120);
				}
				'''
			)
			self.conf_dialog_layout.addWidget(self.yes)

			self.no = QPushButton('No')
			self.no.clicked.connect(self.no_slot)
			self.no.setMaximumSize(100, 40)
			self.no.setStyleSheet(
				'''
				QPushButton {
					background-color: rgb(220, 120, 120);
					border-radius: 5px;
					padding: 5px;
				}
				QPushButton:hover {
					background-color: rgb(240, 120, 120);
				}
				'''
			)
			self.conf_dialog_layout.addWidget(self.no)

			self.conf_dialog = QDialog()
			self.conf_dialog.setMaximumSize(300, 100)
			self.conf_dialog.setLayout(self.conf_dialog_layout)
			self.conf_dialog.setWindowTitle('Quiz Manager')
			self.conf_dialog.show()
		except Exception as e:
			raise e

	def yes_slot(self):
		try:
			from Projects.DiamondRubyQuiz.Tools import Database

			# self.username
			all_usernames = Database.get_quiz_candidate_by_column('username')
			all_ids = Database.get_quiz_candidate_by_column('id')

			id_ = all_ids[all_usernames.index(self.username)]

			self.question_day = Database.get_quiz_all(self.question_topic)
			for i in range(0, len(self.question_answers_collection)):
				if len(self.question_answers_collection[i]) != 0:
					if self.question_day[i][-1] == self.question_answers_collection[i][-1]:
						self.score += 1
						
			Database.insert_quiz_results(
				self.question_topic,
				id_,
				self.username,
				f'{(self.score / len(self.question_answers_collection)) * 100} %'
			)
			self.conf_dialog.close()
			self.widget.setCurrentIndex(0)
		except Exception as e:
			raise e

	def no_slot(self):
		try:
			self.conf_dialog.close()
		except Exception as e:
			raise e

	def question_signal(self):
		try:
			from Projects.DiamondRubyQuiz.Tools import Database

			self.question_topic = ''

			# self.all_question = Database.get_quiz_check_by_column()
			self.all_days = Database.get_quiz_check_by_column('quiz_day')
			self.all_topics = Database.get_quiz_check_by_column('quiz_topic')

			self.date_day = str(QCalendarWidget().selectedDate()).replace('PyQt5.QtCore.QDate', '')		

			for d in self.all_days:
				if d == self.date_day:
					self.quest = self.all_topics[self.all_days.index(self.date_day)]
					self.question_topic  = self.quest
					break
				else:
					msg = 'No quiz available yet'

			self.exam_timer = QTimer()
			self.exam_timer.timeout.connect(self.exam_timer_slot)

			if self.question_topic:
				self.question_day = Database.get_quiz_all(self.question_topic)

				self.quiz_ids = Database.get_quiz_check_by_column('id')
				self.quiz_topics = Database.get_quiz_check_by_column('quiz_topic')
				if len(self.quiz_ids) != 0:
					self.quiz_id_ = self.quiz_ids[self.quiz_topics.index(self.question_topic)]
					self.quiz_time = Database.get_quiz_check_by_id(self.quiz_id_)[0][-2]
					
					# 1000 milliseconds = 1 second

					self.milli_sec = int(self.quiz_time) * 60
					self.milli_sec_dealer = self.milli_sec

					self.exam_timer.start(self.milli_sec)
					for q in self.question_day:
						self.nav_panel_layout.addWidget(Templates.QuestionButton(self.question_index, self.question_panel_stacked_widget))
						self.question_index += 1

						self.question_panel_stacked_widget.addWidget(
							QuizQuestion(
								self.question_answers_collection,
								q[0],
								q[0],
								q[1],
								q[2],
								q[3],
								q[4],
								q[5]
							)
						)
						self.question_answers_collection.append(())
						# self.question_panel_stacked_widget.setCurrentIndex(0)
		except Exception as e:
			raise e

	def exam_timer_slot(self):
		try:
			self.milli_sec_dealer -= 0.05
			self.milli_sec_dealer = round(self.milli_sec_dealer, 2)
			rm = str(self.milli_sec_dealer).split('.')
			self.timer.setText(f'{rm[0]}:{rm[1]}')

			if self.milli_sec_dealer <= 0:
				from Projects.DiamondRubyQuiz.Tools import Database

				# self.username
				all_usernames = Database.get_quiz_candidate_by_column('username')
				all_ids = Database.get_quiz_candidate_by_column('id')

				id_ = all_ids[all_usernames.index(self.username)]

				self.question_day = Database.get_quiz_all(self.question_topic)
				for i in range(0, len(self.question_answers_collection)):
					if len(self.question_answers_collection[i]) != 0:
						if self.question_day[i][-1] == self.question_answers_collection[i][-1]:
							self.score += 1
				Database.insert_quiz_results(
					self.question_topic,
					id_,
					self.username,
					f'{(self.score / len(self.question_answers_collection)) * 100} %'
				)
				
				self.timer.setText('00:00')
				msg = 'You ran out of time. Your exam will be automatically submitted for you.\nGood Luck.'
				message_box = QMessageBox()
				message_box.about(self, 'Quiz Manager', msg)
				
				self.exam_timer.stop()
				self.widget.setCurrentIndex(0)
			elif self.milli_sec_dealer <= 20:
				pass
		except Exception as e:
			raise e
