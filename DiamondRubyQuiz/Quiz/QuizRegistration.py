from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Tools import Templates
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


class QuizRegister(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.window_title = "DiamondRubyQuiz"
        self.window_icon = QIcon("Icons/icon.png")

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
            """
			QGroupBox {
				border: 0px;
				padding: 0px;
			}
			"""
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
            """
			QGroupBox {
				border: 0px
				padding: 5px;
			}
			"""
        )

        self.main_layout.addWidget(
            self.background_group, stretch=0, alignment=Qt.AlignCenter
        )

        self.background_stacked_widget = QStackedWidget()
        self.background_stacked_widget.setStyleSheet(
            """
			QStackedWidget {
				padding: 10px;
			}
			"""
        )

        self.background_layout.addWidget(
            self.background_stacked_widget, stretch=0, alignment=Qt.AlignCenter
        )

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
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
        day = days_list[0]
        day = f"{day}'s"
        mst = "DiamondRubyQuiz"

        self.quiz_day_label = QLabel(day)
        self.quiz_day_label.setMaximumHeight(60)
        self.quiz_day_label.setStyleSheet(
            """
			QLabel {
				color: white;
				font-weight: bold;
				font-size: 19px;
				font:Verdana;
			}
			"""
        )
        self.header_layout.addWidget(self.quiz_day_label)

        self.quiz_mst_label = QLabel(mst)
        self.quiz_mst_label.setMaximumHeight(65)
        self.quiz_mst_label.setStyleSheet(
            """
			QLabel {
				color: white;
				font-weight: bold;
				font-size: 30px;
				font:Verdana;
			}
			"""
        )
        self.header_layout.addWidget(self.quiz_mst_label)

        self.header_group = QGroupBox()
        # self.header_group.setMaximumSize(300, 500)
        self.header_group.setLayout(self.header_layout)
        self.header_group.setStyleSheet(
            """
			QGroupBox {
				border-radius: 40px;
				background-color: rgb(60, 150, 200);
				padding: 20px;
			}
			"""
        )

        self.central_layout.addWidget(self.header_group)

        self.mid_width = 600

        self.central_group = QGroupBox()
        self.central_group.setGraphicsEffect(self.central_eff)
        self.central_group.setFixedSize(self.mid_width, 500)
        self.central_group.setLayout(self.central_layout)
        self.central_group.setStyleSheet(
            """
			QGroupBox {
				border-radius: 50px;
				background-color: rgb(60, 150, 200);
				padding-left: 0px;
				padding-right: 0px;
			}
			"""
        )

        self.central_mid_layout = QVBoxLayout()
        self.central_mid_layout.setContentsMargins(0, 0, 0, 0)
        self.central_mid_layout.setAlignment(Qt.AlignCenter)

        self.quiz_title_layout = QVBoxLayout()
        self.quiz_title_layout.setSpacing(4)
        self.quiz_title_layout.setAlignment(Qt.AlignCenter)

        # self.intro_label = QLabel('Today\'s Quiz on')
        # self.intro_label.setMaximumHeight(50)
        # self.intro_label.setStyleSheet(
        # 	'''
        # 	QLabel {
        # 		color: black;
        # 		font-size: 13px;
        # 		font: Verdana;
        # 	}
        # 	'''
        # )
        # self.quiz_title_layout.addWidget(self.intro_label)

        self.topic = "Quiz Registration"
        self.quiz_topic = QLabel(self.topic)
        self.quiz_topic.setMaximumHeight(60)
        self.quiz_topic.setStyleSheet(
            """
			QLabel {
				font-weight: bold;
				font-size: 18px;
				color: rgb(60, 150, 200);
			}
			"""
        )
        self.quiz_title_layout.addWidget(self.quiz_topic)

        self.central_mid_layout.addLayout(self.quiz_title_layout)

        self.clock_layout = QGridLayout()
        self.clock_layout.setVerticalSpacing(3)
        self.clock_layout.setHorizontalSpacing(8)
        self.clock_layout.setAlignment(Qt.AlignCenter)

        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("First name")
        self.first_name.setMaximumSize(200, 60)
        self.first_name.setStyleSheet(
            """
			QLineEdit {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
			"""
        )
        self.clock_layout.addWidget(self.first_name, 0, 0)

        self.middle_name = QLineEdit()
        self.middle_name.setPlaceholderText("Middle name")
        self.middle_name.setMaximumSize(200, 60)
        self.middle_name.setStyleSheet(
            """
			QLineEdit {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
			"""
        )
        self.clock_layout.addWidget(self.middle_name, 1, 0)

        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Last name")
        self.last_name.setMaximumSize(200, 60)
        self.last_name.setStyleSheet(
            """
			QLineEdit {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
			"""
        )
        self.clock_layout.addWidget(self.last_name, 2, 0)

        self.email = QLineEdit()
        self.email.setPlaceholderText("E-Mail")
        self.email.setMaximumSize(200, 60)
        self.email.setStyleSheet(
            """
			QLineEdit {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
			"""
        )
        self.clock_layout.addWidget(self.email, 3, 0)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.username.setMaximumSize(200, 60)
        self.username.setStyleSheet(
            """
			QLineEdit {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
			"""
        )
        self.clock_layout.addWidget(self.username, 4, 0)

        self.new_password = QLineEdit()
        self.new_password.setPlaceholderText("New Password")
        self.new_password.setEchoMode(QLineEdit.Password)
        self.new_password.setMaximumSize(200, 60)
        self.new_password.setStyleSheet(
            """
			QLineEdit {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
			"""
        )
        self.clock_layout.addWidget(self.new_password, 5, 0)

        self.confirm_password = QLineEdit()
        self.confirm_password.setPlaceholderText("Confirm Password")
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.confirm_password.setMaximumSize(200, 60)
        self.confirm_password.setStyleSheet(
            """
			QLineEdit {
				padding: 7px;
				text-align: left;
				font-size: 15px;
				font: Verdana;
				border-radius: 10px;
				border: 1px solid grey;
			}
			"""
        )
        self.clock_layout.addWidget(self.confirm_password, 6, 0)

        self.central_mid_layout.addLayout(self.clock_layout)

        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(0)
        self.button_layout.setAlignment(Qt.AlignCenter)

        self.login_button = Templates.AnimatedButton()
        self.login_button.setText("Sign Up")
        self.login_button.clicked.connect(self.login_button_slot)
        self.button_layout.addWidget(self.login_button)

        self.central_mid_layout.addLayout(self.button_layout)

        self.central_mid_group = QGroupBox()
        self.central_mid_group.setMaximumSize(self.mid_width, 350)
        self.central_mid_group.setLayout(self.central_mid_layout)
        self.central_mid_group.setStyleSheet(
            """
			QGroupBox {
				border-radius: 40px;
				border: 0px;
				background-color: white;
				padding: 10px;
			}
			"""
        )

        self.central_layout.addWidget(self.central_mid_group)

        self.background_stacked_widget.addWidget(self.central_group)
        self.background_stacked_widget.setCurrentIndex(0)

    def login_button_slot(self):
        try:
            from Tools import Database
            from Quiz import StartQuiz

            all_usernames = Database.get_quiz_candidate_by_column("username")

            if self.first_name.text() and self.middle_name.text():
                if (
                    self.username.text()
                    and self.new_password.text()
                    and self.confirm_password.text()
                    and self.email.text()
                ):
                    if self.username.text() not in all_usernames:
                        if self.new_password.text() == self.confirm_password.text():
                            self.background_stacked_widget.addWidget(
                                StartQuiz.StartQuiz()
                            )
                            Database.insert_quiz_candidate(
                                self.first_name.text(),
                                self.middle_name.text(),
                                self.last_name.text(),
                                self.email.text(),
                                self.username.text(),
                                self.new_password.text(),
                            )

                            msg = f"{self.username.text()} has been successfully registered."
                            message_box = QMessageBox()
                            message_box.about(self, "Quiz Manager", msg)

                            self.background_stacked_widget.setCurrentIndex(1)
                        else:
                            msg = "Your passwords don't match."
                            message_box = QMessageBox()
                            message_box.about(self, "Quiz Manager", msg)
                    else:
                        msg = (
                            "Username already exist, please pick a different Username."
                        )
                        message_box = QMessageBox()
                        message_box.about(self, "Quiz Manager", msg)
                else:
                    msg = "Fill in your desired Login Details to continue."
                    message_box = QMessageBox()
                    message_box.about(self, "Quiz Manager", msg)
            else:
                msg = "Fill in your Names to continue."
                message_box = QMessageBox()
                message_box.about(self, "Quiz Manager", msg)
        except Exception as e:
            raise e
