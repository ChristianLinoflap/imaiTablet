# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets

# Module Imports
from config import db_server_name, db_name, db_username, db_password
from config import Config, translations
import config

class Ui_MainWindowFeedback(object):
    # Function to Call feedbackQuestions.py
    def FeedbackQuestions (self):
        from feedbackQuestions import Ui_MainWindowFeedbackQuestions
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowFeedbackQuestions()
        self.ui.setupUiFeedbackQuestions(self.window)
        self.window.show()

    # Function to Set Up feedback.py
    def setupUiFeedback(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.navigationFrame = QtWidgets.QFrame(self.centralwidget)
        self.navigationFrame.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), 150))
        self.navigationFrame.setStyleSheet("#navigationFrame{\n"
"    background-color:#0000AF;\n"
"}")
        self.navigationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigationFrame.setObjectName("navigationFrame")

        self.nameOutput = QtWidgets.QLabel(self.navigationFrame)
        self.nameOutput.setGeometry(QtCore.QRect(50, 50, 900, 35))
        self.nameOutput.setStyleSheet("#nameOutput{\n"
"    font-weight:bold;\n"
"    font-size:42px;\n"
"    color:#fff;\n"
"}")
        self.nameOutput.setObjectName("nameOutput")
        # Translate the welcome message and user's name
        welcome_message = translations[Config.current_language].get('Welcome_User', 'Welcome')
        first_name = config.user_info.get('first_name', '')
        last_name = config.user_info.get('last_name', '')
        translated_welcome_message = f"{welcome_message}, {first_name} {last_name}"
        self.nameOutput.setText(translated_welcome_message)
        self.roleOutput = QtWidgets.QLabel(self.navigationFrame)
        self.roleOutput.setGeometry(QtCore.QRect(50, 100, 75, 16))
        self.roleOutput.setStyleSheet("#roleOutput{\n"
"    font-size:24px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.roleOutput.setObjectName("roleOutput")

        self.finishPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishPushButton.setGeometry(QtCore.QRect(1010, 740, 275, 115))
        self.finishPushButton.setStyleSheet("#finishPushButton{\n"
"    background-color:none;\n"
"    border:4px solid #0000AF;\n"
"    border-radius:20px;\n"
"    font-family:Montserrat;\n"
"    font-size:24px;\n"
"    color:#0000AF;\n"
"}")
        self.finishPushButton.setObjectName("finishPushButton")

        self.feedBackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.feedBackPushButton.setGeometry(QtCore.QRect(670, 740, 275, 115))
        self.feedBackPushButton.setStyleSheet("#feedBackPushButton{\n"
"    background-color:#0000AF;\n"
"    border-radius:15px;\n"
"    font-size:24px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.feedBackPushButton.setObjectName("feedBackPushButton")
        # To call the function feedbackQuesitons to open the page and close the main window
        self.feedBackPushButton.clicked.connect(self.FeedbackQuestions)
        self.feedBackPushButton.clicked.connect(MainWindow.close)

        self.qrFrame = QtWidgets.QFrame(self.centralwidget)
        self.qrFrame.setGeometry(QtCore.QRect(600, 400, 760, 300))
        self.qrFrame.setStyleSheet("#qrFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:25px;\n"
"}")
        self.qrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qrFrame.setObjectName("qrFrame")

        self.thankyouLabel = QtWidgets.QLabel(self.qrFrame)
        self.thankyouLabel.setGeometry(QtCore.QRect(90, 60, 600, 41))
        self.thankyouLabel.setStyleSheet("#thankyouLabel{\n"
"    font-family:Montserrat;\n"
"    font-size:36px;\n"
"    \n"
"}")
        self.thankyouLabel.setObjectName("thankyouLabel")

        self.feedbackParagraph = QtWidgets.QTextEdit(self.qrFrame)
        self.feedbackParagraph.setGeometry(QtCore.QRect(90, 130, 611, 110))
        self.feedbackParagraph.setStyleSheet("#feedbackParagraph{\n"
"    font-size:24px;\n"
"    font-family:Montserrat;\n"
"    border:none;\n"
"    \n"
"}")
        self.feedbackParagraph.setReadOnly(True)
        self.feedbackParagraph.setObjectName("feedbackParagraph")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # Use the stored language from Config
        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

        # Translate texts using the stored language
        self.roleOutput.setText(_translate("MainWindow", translation_dict['Role_Output']))
        self.finishPushButton.setText(_translate("MainWindow", translation_dict['Finish_Push_Button']))
        self.feedBackPushButton.setText(_translate("MainWindow", translation_dict['Feedback_Push_Button']))
        self.thankyouLabel.setText(_translate("MainWindow", translation_dict['Thankyou_Label']))
        self.feedbackParagraph.setText(_translate("MainWindow", translation_dict['Feedback_Paragraph']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowFeedback()
    ui.setupUiFeedback(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
