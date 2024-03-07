from PyQt5 import QtCore, QtGui, QtWidgets
from config import Config, translations
import config

class Ui_MainWindowFeedback(object):
    def FeedbackQuestions (self):
        from feedbackQuestions import Ui_MainWindowFeedbackQuestions
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowFeedbackQuestions()
        self.ui.setupUiFeedbackQuestions(self.window)
        self.window.show()

    def IndexPage (self):
        # config.user_info.clear()
        # config.transaction_info.clear()
        from indexPage import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    # Function to Set Up feedback.py
    def setupUiFeedback(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        gradient = QtGui.QLinearGradient(0, 0, self.centralwidget.width(), self.centralwidget.height())
        gradient.setColorAt(0, QtGui.QColor("#1D7CBA"))
        gradient.setColorAt(1, QtGui.QColor("#0D3854"))
        self.centralwidget.setStyleSheet("#centralwidget { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #1D7CBA, stop: 1 #0D3854); }")
        self.centralwidget.setObjectName("centralwidget")

        self.navigationFrame = QtWidgets.QFrame(self.centralwidget)
        self.navigationFrame.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), 110))
        self.navigationFrame.setStyleSheet("#navigationFrame{\n"
                                        "    background-color:#0000AF;\n"
                                        "}")
        self.navigationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigationFrame.setObjectName("navigationFrame")

        self.nameOutput = QtWidgets.QLabel(self.navigationFrame)
        self.nameOutput.setGeometry(QtCore.QRect(20, 20, 920, 55))
        self.nameOutput.setStyleSheet("#nameOutput{\n"
                                "    font-weight:bold;\n"
                                "    font-size:42px;\n"
                                "    color:#fff;\n"
                                "}")
        self.nameOutput.setObjectName("nameOutput")
        welcome_message = translations[Config.current_language].get('Welcome_User', 'Welcome')
        first_name = config.user_info.get('first_name', '')
        last_name = config.user_info.get('last_name', '')
        translated_welcome_message = f"{welcome_message}, {first_name} {last_name}"
        self.nameOutput.setText(translated_welcome_message)
        self.roleOutput = QtWidgets.QLabel(self.navigationFrame)
        self.roleOutput.setGeometry(QtCore.QRect(20, 51, 95, 25))
        self.roleOutput.setStyleSheet("#roleOutput{\n"
                                "    font-size:24px;\n"
                                "    font-family:Montserrat;\n"
                                "    color:#fff;\n"
                                "}")
        self.roleOutput.setObjectName("roleOutput")

        self.finishPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishPushButton.setGeometry(QtCore.QRect(700, 515, 275, 100))
        self.finishPushButton.setStyleSheet("#finishPushButton{\n"
                                        "    font-size:20px;\n"
                                        "    font-family:Montserrat;\n"
                                        "    color:#fff;\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #0000AF;\n"
                                        "    background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0.2 #0000AF, stop:0.2 #0000AF, stop:1 #f6f7fa);\n"
                                        "}")
        self.finishPushButton.setObjectName("finishPushButton")
        self.finishPushButton.clicked.connect(self.IndexPage)
        self.finishPushButton.clicked.connect(MainWindow.close)

        self.feedBackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.feedBackPushButton.setGeometry(QtCore.QRect(390, 515, 275, 100))
        self.feedBackPushButton.setStyleSheet("#feedBackPushButton{\n"
                                        "    border-radius:10px;\n"
                                        "    font-family:Montserrat;\n"
                                        "    font-size:20px;\n"
                                        "    color:#000;\n"
                                        "    border: 2px solid #FFD700;\n"
                                        "    border-radius: 9px;\n"
                                        "    background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0.2 #FFD700, stop:0.2 #FFD700, stop:1 #f6f7fa);\n"
                                        "}")
        self.feedBackPushButton.setObjectName("feedBackPushButton")
        # To call the function feedbackQuesitons to open the page and close the main window
        self.feedBackPushButton.clicked.connect(self.FeedbackQuestions)
        self.feedBackPushButton.clicked.connect(MainWindow.close)

        self.qrFrame = QtWidgets.QFrame(self.centralwidget)
        self.qrFrame.setGeometry(QtCore.QRect(280, 190, 760, 300))
        self.qrFrame.setStyleSheet("#qrFrame{\n"
                                "    background-color:#FEFCFC;\n"
                                "    border-radius:25px;\n"
                                "}")
        self.qrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qrFrame.setObjectName("qrFrame")

        self.thankyouLabel = QtWidgets.QLabel(self.qrFrame)
        self.thankyouLabel.setGeometry(QtCore.QRect(0, 60, 760, 41))
        self.thankyouLabel.setStyleSheet("#thankyouLabel{\n"
                                        "    font-family: Montserrat;\n"
                                        "    font-size: 36px;\n"
                                        "}")
        self.thankyouLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.thankyouLabel.setObjectName("thankyouLabel")

        self.feedbackParagraph = QtWidgets.QTextEdit(self.qrFrame)
        self.feedbackParagraph.setGeometry(QtCore.QRect(0, 130, 760, 140))
        self.feedbackParagraph.setStyleSheet("#feedbackParagraph{\n"
                                        "    font-size:24px;\n"
                                        "    font-family:Montserrat;\n"
                                        "    border: none;\n"
                                        "    \n"
                                        "}")
        self.feedbackParagraph.setReadOnly(True)
        self.feedbackParagraph.setObjectName("feedbackParagraph")
        self.feedbackParagraph.setAlignment(QtCore.Qt.AlignCenter)
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
