from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from . import Templates, LoopEmit, Database
import sys


class ResultTableDef(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)

        self.group_layout = QHBoxLayout()
        self.group_layout.setAlignment(Qt.AlignLeft)
        self.group_layout.setContentsMargins(0, 0, 0, 0)
        self.group_layout.setSpacing(0)

        self.setLayout(self.group_layout)
        # self.setMaximumHeight(75)
        self.setStyleSheet(
            """
			QGroupBox {
				border: 0px;
				border: 1px solid grey;
			}
			"""
        )

        self.initialization()

    def initialization(self):
        self.number_label = QLabel("S/N")
        self.number_label.setFixedWidth(40)
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.number_label)

        self.quiz_topic_label = QLabel("Quiz Topic")
        self.quiz_topic_label.setFixedWidth(300)
        self.quiz_topic_label.setAlignment(Qt.AlignLeft)
        self.quiz_topic_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_topic_label)

        self.quiz_day_label = QLabel("Quiz Day")
        self.quiz_day_label.setFixedWidth(120)
        self.quiz_day_label.setAlignment(Qt.AlignLeft)
        self.quiz_day_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_day_label)

        self.quiz_master_label = QLabel("Quiz Master")
        self.quiz_master_label.setMaximumWidth(100)
        self.quiz_master_label.setAlignment(Qt.AlignLeft)
        self.quiz_master_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_master_label)

        self.quiz_duration_label = QLabel("Duration")
        self.quiz_duration_label.setMaximumWidth(80)
        self.quiz_duration_label.setAlignment(Qt.AlignLeft)
        self.quiz_duration_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_duration_label)

        self.view_quiz_label = QLabel("View")
        self.view_quiz_label.setMaximumWidth(50)
        self.view_quiz_label.setAlignment(Qt.AlignCenter)
        self.view_quiz_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.view_quiz_label)


class ResultTable(QGroupBox):
    def __init__(
        self, id_, serial_num, quiz_topic, quiz_day, quiz_master, quiz_duration
    ):
        QGroupBox.__init__(self)

        self.id_ = id_
        self.serial_num = serial_num
        self.quiz_topic = quiz_topic
        self.quiz_day = quiz_day
        self.quiz_master = quiz_master
        self.quiz_duration = quiz_duration

        self.group_layout = QHBoxLayout()
        self.group_layout.setAlignment(Qt.AlignTop)
        self.group_layout.setContentsMargins(0, 0, 0, 0)
        self.group_layout.setSpacing(0)

        self.setLayout(self.group_layout)
        # self.setMaximumHeight(75)
        self.setStyleSheet(
            """
			QGroupBox {
				border: 0px;
				border: 1px solid grey;
			}
			"""
        )

        self.initialization()

    def initialization(self):
        self.number_label = QLabel(self.serial_num)
        self.number_label.setFixedWidth(40)
        self.number_label.setAlignment(Qt.AlignLeft)
        self.number_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.number_label)

        self.quiz_topic_label = QLabel(self.quiz_topic)
        self.quiz_topic_label.setFixedWidth(300)
        self.quiz_topic_label.setAlignment(Qt.AlignLeft)
        self.quiz_topic_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_topic_label)

        self.quiz_day_label = QLabel(self.quiz_day)
        self.quiz_day_label.setFixedWidth(120)
        self.quiz_day_label.setAlignment(Qt.AlignLeft)
        self.quiz_day_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_day_label)

        self.quiz_master_label = QLabel(self.quiz_master)
        self.quiz_master_label.setFixedWidth(100)
        self.quiz_master_label.setAlignment(Qt.AlignCenter)
        self.quiz_master_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_master_label)

        self.quiz_duration_label = QLabel(self.quiz_duration)
        self.quiz_duration_label.setFixedWidth(70)
        self.quiz_duration_label.setAlignment(Qt.AlignCenter)
        self.quiz_duration_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_duration_label)

        self.view_quiz_button = QPushButton()
        self.view_quiz_icon = QIcon("Icons/view.png")
        self.view_quiz_button.clicked.connect(self.view_quiz_slot)
        self.view_quiz_button.setIcon(self.view_quiz_icon)
        self.view_quiz_button.setFixedWidth(50)
        self.view_quiz_button.setStyleSheet(
            """
			QPushButton {
				padding: 3px;
				text-align: center;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				background-color: rgb(230, 170, 170);
			}
			QPushButton:hover {
				background-color: rgb(210, 170, 170);
			}
			"""
        )
        self.group_layout.addWidget(self.view_quiz_button)

    def view_quiz_slot(self):
        try:
            self.confirmation = Confirmation(str(self.id_))
            self.confirmation.show()
        except Exception as e:
            raise e


class Confirmation(QDialog):
    def __init__(self, id_):
        QDialog.__init__(self)

        self.id_ = id_

        self.dialog_layout = QVBoxLayout()
        self.dialog_layout.setAlignment(Qt.AlignCenter)
        self.dialog_layout.setSpacing(5)

        self.form_layout = QGridLayout()
        self.form_layout.setSpacing(0)
        self.form_layout.setAlignment(Qt.AlignCenter)

        self.dialog_layout.addLayout(self.form_layout)

        self.setLayout(self.dialog_layout)
        self.setMaximumSize(300, 300)
        self.setWindowTitle("Quiz Checker")

        self.label_qss = """
			QLabel {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
		"""

        self.initialization()

    def initialization(self):
        self.collect_quiz_info()

        self.quiz_topic_label = QLabel("Quiz Topic")
        self.quiz_topic_label.setMaximumSize(120, 40)
        self.quiz_topic_label.setStyleSheet(self.label_qss)
        self.form_layout.addWidget(self.quiz_topic_label, 0, 0)

        self.quiz_topic = QLabel(self.quiz_topic_val)
        self.quiz_topic.setMaximumSize(200, 40)
        self.quiz_topic.setStyleSheet(self.label_qss)
        self.form_layout.addWidget(self.quiz_topic, 0, 1)

        self.quiz_day_label = QLabel("Quiz Day")
        self.quiz_day_label.setMaximumSize(120, 40)
        self.quiz_day_label.setStyleSheet(self.label_qss)
        self.form_layout.addWidget(self.quiz_day_label, 1, 0)

        self.quiz_day = QLabel(self.quiz_day_val)
        self.quiz_day.setMaximumSize(200, 40)
        self.quiz_day.setStyleSheet(self.label_qss)
        self.form_layout.addWidget(self.quiz_day, 1, 1)

        self.quiz_master_label = QLabel("Quiz Master")
        self.quiz_master_label.setMaximumSize(120, 40)
        self.quiz_master_label.setStyleSheet(self.label_qss)
        self.form_layout.addWidget(self.quiz_master_label, 2, 0)

        self.quiz_master = QLabel(self.quiz_master_val)
        self.quiz_master.setMaximumSize(200, 40)
        self.quiz_master.setStyleSheet(self.label_qss)
        self.form_layout.addWidget(self.quiz_master, 2, 1)

        self.quiz_time_label = QLabel("Quiz Time")
        self.quiz_time_label.setMaximumSize(120, 40)
        self.quiz_time_label.setStyleSheet(self.label_qss)
        self.form_layout.addWidget(self.quiz_time_label, 3, 0)

        self.quiz_time = QLabel(self.quiz_time_val)
        self.quiz_time.setMaximumSize(200, 40)
        self.quiz_time.setStyleSheet(self.label_qss)
        self.form_layout.addWidget(self.quiz_time, 3, 1)

        self.quiz_status_label = QLabel("Quiz Status")
        self.quiz_status_label.setMaximumSize(120, 40)
        self.quiz_status_label.setStyleSheet(self.label_qss)
        self.form_layout.addWidget(self.quiz_status_label, 4, 0)

        self.quiz_status = QLabel(self.quiz_status_val)
        self.quiz_status.setMaximumSize(200, 40)
        self.quiz_status.setStyleSheet(self.label_qss)
        self.form_layout.addWidget(self.quiz_status, 4, 1)

        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(5)
        self.button_layout.setAlignment(Qt.AlignCenter)

        # self.button_qss = '''
        # 	QPushButton {

        # 	}
        # 	QPushButton:hover {

        # 	}
        # 	'''

        self.enable_button = QPushButton("Enable")
        self.enable_button.clicked.connect(self.enable_slot)
        self.button_layout.addWidget(self.enable_button)

        self.disable_button = QPushButton("Disable")
        self.disable_button.clicked.connect(self.disable_slot)
        self.button_layout.addWidget(self.disable_button)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_slot)
        self.button_layout.addWidget(self.delete_button)

        self.dialog_layout.addLayout(self.button_layout)

    def enable_slot(self):
        try:
            from Projects.DiamondRubyQuiz.Tools import Database

            Database.update_quiz_check_status(self.id_, "True")
            self.close()
        except Exception as e:
            raise e

    def disable_slot(self):
        try:
            from Projects.DiamondRubyQuiz.Tools import Database

            Database.update_quiz_check_status(self.id_, "False")
            self.close()
        except Exception as e:
            raise e

    def delete_slot(self):
        try:
            from Projects.DiamondRubyQuiz.Tools import Database

            Database.delete_quiz_check(self.id_)
            self.close()
        except Exception as e:
            raise e

    def collect_quiz_info(self):
        try:
            from Projects.DiamondRubyQuiz.Tools import Database

            if Database.get_quiz_check_by_id(self.id_):
                self.quiz_info = Database.get_quiz_check_by_id(self.id_)[0]
                self.quiz_topic_val = self.quiz_info[1]
                self.quiz_day_val = self.quiz_info[2]
                self.quiz_master_val = self.quiz_info[3]
                self.quiz_time_val = self.quiz_info[4]
                self.quiz_status_val = self.quiz_info[5]
            else:
                msg = "Quiz has been deleted."
                message_box = QMessageBox()
                message_box.about(self, "Quiz Manager", msg)
        except Exception as e:
            raise e


class AvailResultsDef(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)

        self.group_layout = QHBoxLayout()
        self.group_layout.setAlignment(Qt.AlignCenter)
        self.group_layout.setContentsMargins(0, 0, 0, 0)
        self.group_layout.setSpacing(0)

        self.setLayout(self.group_layout)
        # self.setMaximumHeight(75)
        self.setStyleSheet(
            """
			QGroupBox {
				border: 1px solid grey;
			}
			"""
        )

        self.initialization()

    def initialization(self):
        self.number_label = QLabel("S/N")
        self.number_label.setFixedWidth(40)
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.number_label)

        self.quiz_topic_label = QLabel("Quiz Topic")
        self.quiz_topic_label.setFixedWidth(300)
        self.quiz_topic_label.setAlignment(Qt.AlignLeft)
        self.quiz_topic_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_topic_label)

        self.quiz_master_label = QLabel("Quiz Master")
        self.quiz_master_label.setFixedWidth(100)
        self.quiz_master_label.setAlignment(Qt.AlignCenter)
        self.quiz_master_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_master_label)

        self.view_quiz_label = QLabel("View")
        self.view_quiz_label.setFixedWidth(50)
        self.view_quiz_label.setAlignment(Qt.AlignCenter)
        self.view_quiz_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.view_quiz_label)


class AvailResults(QGroupBox):
    def __init__(self, id_, serial_num, quiz_topic, quiz_master):
        QGroupBox.__init__(self)

        self.id_ = id_
        self.serial_num = serial_num
        self.quiz_topic = quiz_topic
        self.quiz_master = quiz_master

        self.group_layout = QHBoxLayout()
        self.group_layout.setAlignment(Qt.AlignTop)
        self.group_layout.setContentsMargins(0, 0, 0, 0)
        self.group_layout.setSpacing(0)

        self.setLayout(self.group_layout)
        # self.setMaximumHeight(75)
        self.setStyleSheet(
            """
			QGroupBox {
				border: 1px solid grey;
			}
			"""
        )

        self.initialization()

    def initialization(self):
        self.number_label = QLabel(str(self.serial_num))
        self.number_label.setFixedWidth(40)
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.number_label)

        self.quiz_topic_label = QLabel(self.quiz_topic)
        self.quiz_topic_label.setFixedWidth(300)
        self.quiz_topic_label.setAlignment(Qt.AlignLeft)
        self.quiz_topic_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_topic_label)

        self.quiz_master_label = QLabel(self.quiz_master)
        self.quiz_master_label.setFixedWidth(100)
        self.quiz_master_label.setAlignment(Qt.AlignCenter)
        self.quiz_master_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.quiz_master_label)

        self.view_quiz_button = QPushButton()
        self.view_quiz_icon = QIcon("Icons/view.png")
        self.view_quiz_button.clicked.connect(self.view_quiz_slot)
        self.view_quiz_button.setIcon(self.view_quiz_icon)
        self.view_quiz_button.setFixedWidth(50)
        self.view_quiz_button.setStyleSheet(
            """
			QPushButton {
				padding: 3px;
				text-align: center;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				background-color: rgb(190, 170, 170);
			}
			QPushButton:hover {
				background-color: rgb(210, 170, 170);
			}
			"""
        )
        self.group_layout.addWidget(self.view_quiz_button)

    def view_quiz_slot(self):
        try:
            from Projects.DiamondRubyQuiz.Tools import Database

            self.display_result = DisplayResult(self.quiz_topic)
            self.display_result.show()
        except Exception as e:
            raise e


class ResultGrid(QGridLayout):
    def __init__(self, id_, serial_num, quiz_topic, candidate, score):
        QGridLayout.__init__(self)

        self.setSpacing(0)
        self.setAlignment(Qt.AlignTop)

        self.serial_num_label = QLabel(str(serial_num))
        self.serial_num_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
				}
			"""
        )
        self.serial_num_label.setFixedSize(80, 35)
        self.addWidget(self.serial_num_label, 0, 0)

        self.quiz_topic_label = QLabel(str(quiz_topic))
        self.quiz_topic_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
				}
			"""
        )
        self.quiz_topic_label.setFixedSize(140, 35)
        self.addWidget(self.quiz_topic_label, 0, 1)

        self.candidate_label = QLabel(str(candidate))
        self.candidate_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
				}
			"""
        )
        self.candidate_label.setFixedSize(140, 35)
        self.addWidget(self.candidate_label, 0, 2)

        self.score_label = QLabel(str(score))
        self.score_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
				}
			"""
        )
        self.score_label.setFixedSize(140, 35)
        self.addWidget(self.score_label, 0, 3)


class DisplayResult(QDialog):
    def __init__(self, quiz_topic):
        QDialog.__init__(self)

        self.quiz_topic = quiz_topic

        self.dialog_layout = QVBoxLayout()
        self.dialog_layout.setSpacing(0)
        self.dialog_layout.setAlignment(Qt.AlignTop)
        self.dialog_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.dialog_layout)
        self.setWindowTitle("Quiz Result")
        self.setMaximumWidth(500)
        self.setStyleSheet(
            """
			QDialog {
				padding: 10px;
			}
			"""
        )

        self.initialization()

    def initialization(self):
        self.dialog_group_layout = QVBoxLayout()
        self.dialog_group_layout.setContentsMargins(0, 0, 0, 0)
        self.dialog_group_layout.setAlignment(Qt.AlignTop)
        self.dialog_group_layout.setSpacing(0)

        self.submitSEQ = LoopEmit.QuestionEmit(30)
        self.submitSEQ.countChanged.connect(self.distributeRESULT)
        self.submitSEQ.run()

        self.dialog_group = QGroupBox()
        self.dialog_group.setLayout(self.dialog_group_layout)
        self.dialog_group.setStyleSheet(
            """
			QGroupBox {
				border: 0px;
				background-color: white;
			}
			"""
        )

        self.dialog_scroll = QScrollArea()
        self.dialog_scroll.setWidget(self.dialog_group)
        self.dialog_scroll.setWidgetResizable(True)
        self.dialog_scroll.setStyleSheet(
            """
			QScrollArea {
				border: 0px;
			}
			"""
        )

        self.dialog_layout.addWidget(self.dialog_scroll)

    def distributeRESULT(self):
        try:
            self.dialog_group_layout.addLayout(
                ResultGrid("0", "S/N", "Quiz Topic", "Candidate", "Score")
            )

            number = 1
            self.all_result = Database.get_quiz_results_all(self.quiz_topic)

            for r in self.all_result:
                self.dialog_group_layout.addLayout(
                    ResultGrid(r[0], number, str(r[1]).replace("_", " "), r[2], r[3])
                )
        except Exception as e:
            raise e


"""
	Candidates Table
"""


class CandidatesDef(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)

        self.group_layout = QHBoxLayout()
        self.group_layout.setAlignment(Qt.AlignLeft)
        self.group_layout.setContentsMargins(0, 0, 0, 0)
        self.group_layout.setSpacing(0)

        self.setLayout(self.group_layout)
        # self.setMaximumHeight(75)
        self.setStyleSheet(
            """
			QGroupBox {
				border: 0px;
				border: 1px solid grey;
			}
			"""
        )

        self.initialization()

    def initialization(self):
        self.number_label = QLabel("S/N")
        self.number_label.setFixedWidth(40)
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.number_label)

        self.first_name_label = QLabel("First Name")
        self.first_name_label.setFixedWidth(200)
        self.first_name_label.setAlignment(Qt.AlignLeft)
        self.first_name_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.first_name_label)

        self.middle_name_label = QLabel("Middle Name")
        self.middle_name_label.setFixedWidth(200)
        self.middle_name_label.setAlignment(Qt.AlignLeft)
        self.middle_name_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.middle_name_label)

        self.last_name_label = QLabel("Last Name")
        self.last_name_label.setFixedWidth(200)
        self.last_name_label.setAlignment(Qt.AlignLeft)
        self.last_name_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.last_name_label)

        self.username_label = QLabel("Username")
        self.username_label.setFixedWidth(120)
        self.username_label.setAlignment(Qt.AlignLeft)
        self.username_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.username_label)

        self.view_candidates_label = QLabel("View")
        self.view_candidates_label.setMaximumWidth(50)
        self.view_candidates_label.setAlignment(Qt.AlignCenter)
        self.view_candidates_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.view_candidates_label)


class Candidates(QGroupBox):
    def __init__(self, id_, serial_num, first_name, middle_name, last_name, username):
        QGroupBox.__init__(self)

        self.id_ = id_
        self.serial_num = serial_num
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.username = username

        self.group_layout = QHBoxLayout()
        self.group_layout.setAlignment(Qt.AlignTop)
        self.group_layout.setContentsMargins(0, 0, 0, 0)
        self.group_layout.setSpacing(0)

        self.setLayout(self.group_layout)
        # self.setMaximumHeight(75)
        self.setStyleSheet(
            """
			QGroupBox {
				border: 0px;
				border: 1px solid grey;
			}
			"""
        )

        self.initialization()

    def initialization(self):
        self.number_label = QLabel(str(self.serial_num))
        self.number_label.setFixedWidth(40)
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.number_label)

        self.first_name_label = QLabel(self.first_name)
        self.first_name_label.setFixedWidth(200)
        self.first_name_label.setAlignment(Qt.AlignLeft)
        self.first_name_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.first_name_label)

        self.middle_name_label = QLabel(self.middle_name)
        self.middle_name_label.setFixedWidth(200)
        self.middle_name_label.setAlignment(Qt.AlignLeft)
        self.middle_name_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.middle_name_label)

        self.last_name_label = QLabel(self.last_name)
        self.last_name_label.setFixedWidth(200)
        self.last_name_label.setAlignment(Qt.AlignLeft)
        self.last_name_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.last_name_label)

        self.username_label = QLabel(self.username)
        self.username_label.setFixedWidth(120)
        self.username_label.setAlignment(Qt.AlignLeft)
        self.username_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
			}
			"""
        )
        self.group_layout.addWidget(self.username_label)

        self.view_quiz_button = QPushButton()
        self.view_quiz_icon = QIcon("Icons/view.png")
        self.view_quiz_button.clicked.connect(self.view_quiz_slot)
        self.view_quiz_button.setIcon(self.view_quiz_icon)
        self.view_quiz_button.setFixedWidth(50)
        self.view_quiz_button.setStyleSheet(
            """
			QPushButton {
				padding: 3px;
				text-align: center;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				background-color: rgb(230, 170, 170);
			}
			QPushButton:hover {
				background-color: rgb(210, 170, 170);
			}
			"""
        )
        self.group_layout.addWidget(self.view_quiz_button)

    def view_quiz_slot(self):
        try:
            self.dialog = CandidateData(str(self.id_))
            self.dialog.show()
        except Exception as e:
            raise e


class CandidateData(QDialog):
    def __init__(self, id_):
        QDialog.__init__(self)

        self.id_ = id_

        self.dialog_layout = QGridLayout()
        self.dialog_layout.setSpacing(0)
        self.dialog_layout.setAlignment(Qt.AlignCenter)

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.main_layout.setSpacing(4)

        self.main_layout.addLayout(self.dialog_layout)

        self.setLayout(self.main_layout)
        self.setFixedSize(300, 300)
        self.setWindowTitle("Quiz Candidate Information")
        self.setStyleSheet(
            """
			QDialog {
				padding: 10px;
				background-color: white;
			}
			"""
        )

        self.initialization()

    def initialization(self):
        self.fetch_student()

        self.f_name_title = QLabel("First Name")
        self.f_name_title.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.f_name_title.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.f_name_title, 0, 0)

        self.f_name_label = QLabel(self.f_name)
        self.f_name_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.f_name_label.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.f_name_label, 0, 1)

        self.m_name_title = QLabel("Middle Name")
        self.m_name_title.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.m_name_title.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.m_name_title, 1, 0)

        self.m_name_label = QLabel(self.m_name)
        self.m_name_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.m_name_label.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.m_name_label, 1, 1)

        self.l_name_title = QLabel("Last Name")
        self.l_name_title.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.l_name_title.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.l_name_title, 2, 0)

        self.l_name_label = QLabel(self.l_name)
        self.l_name_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.l_name_label.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.l_name_label, 2, 1)

        self.e_mail_title = QLabel("E-Mail")
        self.e_mail_title.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.e_mail_title.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.e_mail_title, 3, 0)

        self.e_mail_label = QLabel(self.e_mail)
        self.e_mail_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.e_mail_label.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.e_mail_label, 3, 1)

        self.u_name_title = QLabel("Username")
        self.u_name_title.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.u_name_title.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.u_name_title, 4, 0)

        self.u_name_label = QLabel(self.u_name)
        self.u_name_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.u_name_label.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.u_name_label, 4, 1)

        self.p_word_title = QLabel("Password")
        # self.p_word_title.setEnabled(False)
        self.p_word_title.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.p_word_title.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.p_word_title, 5, 0)

        self.p_word_label = QLabel(self.p_word)
        # self.p_word_label.setEnabled(False)
        self.p_word_label.setStyleSheet(
            """
			QLabel {
				padding: 3px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border: 1px solid grey;
			}
			"""
        )
        self.p_word_label.setMaximumSize(230, 40)
        self.dialog_layout.addWidget(self.p_word_label, 5, 1)

        self.delete_result_button = QPushButton()
        self.delete_result_button.clicked.connect(self.delete_slot)
        self.delete_icon = QIcon("Icons/delete.png")
        self.delete_result_button.setIcon(self.delete_icon)
        self.delete_result_button.setStyleSheet(
            """
			QPushButton {
				background-color: rgb(230, 90, 90);
				border-radius: 10px;
				padding: 6px;
			}
			QPushButton:hover {
				background-color: rgb(200, 90, 90);
			}
			"""
        )
        self.main_layout.addWidget(self.delete_result_button)

    def fetch_student(self):
        try:
            self.student_info = Database.get_quiz_candidate_by_id(str(self.id_))
            if len(self.student_info) != 0:
                self.f_name = self.student_info[0][1]
                self.m_name = self.student_info[0][2]
                self.l_name = self.student_info[0][3]
                self.e_mail = self.student_info[0][4]
                self.u_name = self.student_info[0][5]
                self.p_word = self.student_info[0][6]
            else:
                msg = "Information for this student is currently not available."
                message_box = QMessageBox()
                message_box.about(self, "Quiz Manager", msg)
        except Exception as e:
            raise e

    def delete_slot(self):
        try:
            Database.delete_quiz_candidate(self.id_)

            msg = "Candidate has been successfully deleted."
            message_box = QMessageBox()
            message_box.about(self, "Quiz Manager", msg)

            self.close()
        except Exception as e:
            raise e
