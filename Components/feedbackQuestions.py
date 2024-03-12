from PyQt5 import QtCore, QtGui, QtWidgets
import config 
from config import Config, translations
from databaseManager import DatabaseManager, EnvironmentLoader
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindowFeedbackQuestions(object):
    def __init__(self):
        self.db_manager = DatabaseManager(*EnvironmentLoader.load_env_variables())
        self.conn = self.db_manager.connect()
        self.cursor = self.conn.cursor()
        self.answer_one = None
        self.answer_two = None
        self.answer_three = None
        self.answer_four = None
        self.answer_five = None
        self.window = None
        
    # def IndexPage (self):
    #     # config.user_info.clear()
    #     # config.transaction_info.clear() 
    #     if all([self.answer_one is not None,
    #         self.answer_two is not None,
    #         self.answer_three is not None,
    #         self.answer_four is not None,
    #         self.answer_five is not None]):
    #         user_client_id = config.user_info.get('user_client_id')
    #         reference_number = config.transaction_info.get('reference_number')
    #         config.user_info.get('user_client_id')

    #         self.tallyAnswers(user_client_id)
    #         latest_status = self.db_manager.get_latest_transaction_status(user_client_id)
    #         if latest_status == 'On-Going':
    #             self.db_manager.update_transaction_status(user_client_id, reference_number)
            
    #         self.finishPushButton.clicked.connect(MainWindow.close)
            
    #         from indexPage import Ui_MainWindow
    #         self.window = QtWidgets.QMainWindow()
    #         self.ui = Ui_MainWindow()
    #         self.ui.setupUi(self.window)
    #         self.window.show()
    #     else:
    #         message_box = QMessageBox()
    #         message_box.setWindowTitle("Warning!")
    #         message_box.setText("Please complete all answers before proceeding.")
    #         message_box.setStandardButtons(QMessageBox.Ok)
    #         message_box.exec_()

    def IndexPage(self):
        if all([self.answer_one, self.answer_two, self.answer_three, self.answer_four, self.answer_five]):
            user_client_id = config.user_info.get('user_client_id')
            reference_number = config.transaction_info.get('reference_number')

            self.tallyAnswers(user_client_id)
            latest_status = self.db_manager.get_latest_transaction_status(user_client_id)
            if latest_status == 'On-Going':
                self.db_manager.update_transaction_status(user_client_id, reference_number)

            self.finishPushButton.clicked.connect(MainWindow.close)

            from indexPage import Ui_MainWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            message_box = QMessageBox()
            message_box.setWindowTitle("Warning!")
            message_box.setText("Please complete all answers before proceeding.")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec_()

    def setupUiFeedbackQuestions(self, MainWindow):
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
        self.navigationFrame.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), 100))
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
                                    "    font-size:24px;\n"
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
        self.finishPushButton.setGeometry(QtCore.QRect(1030, 600, 231, 100))
        self.finishPushButton.setStyleSheet("#finishPushButton{\n"
                                        "    font-size:16px;\n"
                                        "    font-family:Montserrat;\n"
                                        "    color:#fff;\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #0000AF;\n"
                                        "    background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0.2 #0000AF, stop:0.2 #0000AF, stop:1 #f6f7fa);\n"
                                        "}")
        self.finishPushButton.setObjectName("finishPushButton")
        self.finishPushButton.clicked.connect(self.IndexPage)
        # self.finishPushButton.clicked.connect(lambda: self.tallyAnswers(config.user_info.get('user_client_id')))
        
        self.surveyFrame = QtWidgets.QFrame(self.centralwidget)
        self.surveyFrame.setGeometry(QtCore.QRect(20, 115, 1240, 471))
        self.surveyFrame.setStyleSheet("#surveyFrame{\n"
                                    "    background-color:#FEFCFC;\n"
                                    "    border-radius:15px;\n"
                                    "}")
        self.surveyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.surveyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.surveyFrame.setObjectName("surveyFrame")
        self.surveyOne = QtWidgets.QLabel(self.surveyFrame)
        self.surveyOne.setGeometry(QtCore.QRect(20, 20, 500, 21))
        self.surveyOne.setStyleSheet("#surveyOne{\n"
                                    "    font-style:Montserrat;\n"
                                    "    font-size:14px;\n"
                                    "}")    
        self.surveyOne.setObjectName("surveyOne")
        self.surveyTwo = QtWidgets.QLabel(self.surveyFrame)
        self.surveyTwo.setGeometry(QtCore.QRect(20, 210, 481, 21))
        self.surveyTwo.setStyleSheet("#surveyTwo{\n"
                                    "    font-style:Montserrat;\n"
                                    "    font-size:14px;\n"
                                    "}")
        self.surveyTwo.setObjectName("surveyTwo")
        self.surveyFour = QtWidgets.QLabel(self.surveyFrame)
        self.surveyFour.setGeometry(QtCore.QRect(590, 20, 521, 21))
        self.surveyFour.setStyleSheet("#surveyFour{\n"
                                    "    font-style:Montserrat;\n"
                                    "    font-size:14px;\n"
                                    "}")
        self.surveyFour.setObjectName("surveyFour")
        self.surveyThree = QtWidgets.QLabel(self.surveyFrame)
        self.surveyThree.setGeometry(QtCore.QRect(20, 390, 481, 21))
        self.surveyThree.setStyleSheet("#surveyThree{\n"
                                    "    font-style:Montserrat;\n"
                                    "    font-size:14px;\n"
                                    "}")
        self.surveyThree.setObjectName("surveyThree")
        self.surveyFive = QtWidgets.QLabel(self.surveyFrame)
        self.surveyFive.setGeometry(QtCore.QRect(590, 210, 551, 21))
        self.surveyFive.setStyleSheet("#surveyFive{\n"
                                    "    font-style:Montserrat;\n"
                                    "    font-size:14px;\n"
                                    "}")
        self.surveyFive.setObjectName("surveyFive")
        self.surveyOneFrame = QtWidgets.QFrame(self.surveyFrame)
        self.surveyOneFrame.setGeometry(QtCore.QRect(20, 50, 120, 151))
        self.surveyOneFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.surveyOneFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.surveyOneFrame.setObjectName("surveyOneFrame")
        self.surveyOneExcellent = QtWidgets.QRadioButton(self.surveyOneFrame)
        self.surveyOneExcellent.setGeometry(QtCore.QRect(0, 120, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyOneExcellent.setFont(font)
        self.surveyOneExcellent.setObjectName("surveyOneExcellent")
        self.surveyOneVeryPoor = QtWidgets.QRadioButton(self.surveyOneFrame)
        self.surveyOneVeryPoor.setGeometry(QtCore.QRect(0, 0, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyOneVeryPoor.setFont(font)
        self.surveyOneVeryPoor.setObjectName("surveyOneVeryPoor")
        self.surveyOneGood = QtWidgets.QRadioButton(self.surveyOneFrame)
        self.surveyOneGood.setGeometry(QtCore.QRect(0, 90, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyOneGood.setFont(font)
        self.surveyOneGood.setObjectName("surveyOneGood")
        self.surveyOnePoor = QtWidgets.QRadioButton(self.surveyOneFrame)
        self.surveyOnePoor.setGeometry(QtCore.QRect(0, 30, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyOnePoor.setFont(font)
        self.surveyOnePoor.setObjectName("surveyOnePoor")
        self.surveyOneNeutral = QtWidgets.QRadioButton(self.surveyOneFrame)
        self.surveyOneNeutral.setGeometry(QtCore.QRect(0, 60, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyOneNeutral.setFont(font)
        self.surveyOneNeutral.setObjectName("surveyOneNeutral")
        self.surveyTwoFrame = QtWidgets.QFrame(self.surveyFrame)
        self.surveyTwoFrame.setGeometry(QtCore.QRect(20, 230, 201, 151))
        self.surveyTwoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.surveyTwoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.surveyTwoFrame.setObjectName("surveyTwoFrame")
        self.surveyTwoExtreme = QtWidgets.QRadioButton(self.surveyTwoFrame)
        self.surveyTwoExtreme.setGeometry(QtCore.QRect(0, 130, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyTwoExtreme.setFont(font)
        self.surveyTwoExtreme.setObjectName("surveyTwoExtreme")
        self.surveyTwoNotAtAll = QtWidgets.QRadioButton(self.surveyTwoFrame)
        self.surveyTwoNotAtAll.setGeometry(QtCore.QRect(0, 10, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyTwoNotAtAll.setFont(font)
        self.surveyTwoNotAtAll.setObjectName("surveyTwoNotAtAll")
        self.surveyTwoVery = QtWidgets.QRadioButton(self.surveyTwoFrame)
        self.surveyTwoVery.setGeometry(QtCore.QRect(0, 100, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyTwoVery.setFont(font)
        self.surveyTwoVery.setObjectName("surveyTwoVery")
        self.surveyTwoSlightly = QtWidgets.QRadioButton(self.surveyTwoFrame)
        self.surveyTwoSlightly.setGeometry(QtCore.QRect(0, 40, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyTwoSlightly.setFont(font)
        self.surveyTwoSlightly.setObjectName("surveyTwoSlightly")
        self.surveyTwoModerate = QtWidgets.QRadioButton(self.surveyTwoFrame)
        self.surveyTwoModerate.setGeometry(QtCore.QRect(0, 70, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyTwoModerate.setFont(font)
        self.surveyTwoModerate.setObjectName("surveyTwoModerate")
        self.surveyThreeFrame = QtWidgets.QFrame(self.surveyFrame)
        self.surveyThreeFrame.setGeometry(QtCore.QRect(20, 410, 120, 51))
        self.surveyThreeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.surveyThreeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.surveyThreeFrame.setObjectName("surveyThreeFrame")
        self.surveyThreeNo = QtWidgets.QRadioButton(self.surveyThreeFrame)
        self.surveyThreeNo.setGeometry(QtCore.QRect(0, 30, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyThreeNo.setFont(font)
        self.surveyThreeNo.setObjectName("surveyThreeNo")
        self.surveyThreeYes = QtWidgets.QRadioButton(self.surveyThreeFrame)
        self.surveyThreeYes.setGeometry(QtCore.QRect(0, 5, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyThreeYes.setFont(font)
        self.surveyThreeYes.setObjectName("surveyThreeYes")
        self.surveyFourFrame = QtWidgets.QFrame(self.surveyFrame)
        self.surveyFourFrame.setGeometry(QtCore.QRect(590, 50, 141, 141))
        self.surveyFourFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.surveyFourFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.surveyFourFrame.setObjectName("surveyFourFrame")
        self.surveyFourVerySat = QtWidgets.QRadioButton(self.surveyFourFrame)
        self.surveyFourVerySat.setGeometry(QtCore.QRect(0, 120, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyFourVerySat.setFont(font)
        self.surveyFourVerySat.setObjectName("surveyFourVerySat")
        self.surveyFourDis = QtWidgets.QRadioButton(self.surveyFourFrame)
        self.surveyFourDis.setGeometry(QtCore.QRect(0, 30, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyFourDis.setFont(font)
        self.surveyFourDis.setObjectName("surveyFourDis")
        self.surveyFourVeryDis = QtWidgets.QRadioButton(self.surveyFourFrame)
        self.surveyFourVeryDis.setGeometry(QtCore.QRect(0, 0, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyFourVeryDis.setFont(font)
        self.surveyFourVeryDis.setObjectName("surveyFourVeryDis")
        self.surveyFourSatisfied = QtWidgets.QRadioButton(self.surveyFourFrame)
        self.surveyFourSatisfied.setGeometry(QtCore.QRect(0, 90, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyFourSatisfied.setFont(font)
        self.surveyFourSatisfied.setObjectName("surveyFourSatisfied")
        self.surveyFourNeutral = QtWidgets.QRadioButton(self.surveyFourFrame)
        self.surveyFourNeutral.setGeometry(QtCore.QRect(0, 60, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyFourNeutral.setFont(font)
        self.surveyFourNeutral.setObjectName("surveyFourNeutral")
        self.surveyFiveFrame = QtWidgets.QFrame(self.surveyFrame)
        self.surveyFiveFrame.setGeometry(QtCore.QRect(590, 230, 201, 151))
        self.surveyFiveFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.surveyFiveFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.surveyFiveFrame.setObjectName("surveyFiveFrame")
        self.surveyFourVeryDis_6 = QtWidgets.QRadioButton(self.surveyFiveFrame)
        self.surveyFourVeryDis_6.setGeometry(QtCore.QRect(0, 130, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyFourVeryDis_6.setFont(font)
        self.surveyFourVeryDis_6.setObjectName("surveyFourVeryDis_6")
        self.surveyFourVeryDis_4 = QtWidgets.QRadioButton(self.surveyFiveFrame)
        self.surveyFourVeryDis_4.setGeometry(QtCore.QRect(0, 70, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyFourVeryDis_4.setFont(font)
        self.surveyFourVeryDis_4.setObjectName("surveyFourVeryDis_4")
        self.surveyFourVeryDis_3 = QtWidgets.QRadioButton(self.surveyFiveFrame)
        self.surveyFourVeryDis_3.setGeometry(QtCore.QRect(0, 40, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyFourVeryDis_3.setFont(font)
        self.surveyFourVeryDis_3.setObjectName("surveyFourVeryDis_3")
        self.surveyFourVeryDis_2 = QtWidgets.QRadioButton(self.surveyFiveFrame)
        self.surveyFourVeryDis_2.setGeometry(QtCore.QRect(0, 10, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyFourVeryDis_2.setFont(font)
        self.surveyFourVeryDis_2.setObjectName("surveyFourVeryDis_2")
        self.surveyFourVeryDis_5 = QtWidgets.QRadioButton(self.surveyFiveFrame)
        self.surveyFourVeryDis_5.setGeometry(QtCore.QRect(0, 100, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.surveyFourVeryDis_5.setFont(font)
        self.surveyFourVeryDis_5.setObjectName("surveyFourVeryDis_5")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def answerOne(self):
        if self.surveyOneExcellent.isChecked():
            self.answer_one = "Excellent"
            print('Excellent')
        elif self.surveyOneVeryPoor.isChecked():
            self.answer_one = "Very Poor"
        elif self.surveyOneGood.isChecked():
            self.answer_one = "Good"
        elif self.surveyOnePoor.isChecked():
            self.answer_one = "Poor"
        elif self.surveyOneNeutral.isChecked():
            self.answer_one = "Neutral"

    def answerTwo(self):
        if self.surveyTwoExtreme.isChecked():
            self.answer_two = "Extremely user-friendly"
        elif self.surveyTwoNotAtAll.isChecked():
            self.answer_two = "Not at all user-friendly"
        elif self.surveyTwoVery.isChecked():
            self.answer_two = "Very user-friendly"
        elif self.surveyTwoSlightly.isChecked():
            self.answer_two = "Slightly user-friendly"
        elif self.surveyTwoModerate.isChecked():
            self.answer_two = "Moderately user-friendly"

    def answerThree(self):
        if self.surveyThreeYes.isChecked():
            self.answer_three = "Yes"  
        elif self.surveyThreeNo.isChecked():
            self.answer_three = "No"
        
    def answerFour(self):
        if self.surveyFourVerySat.isChecked():
            self.answer_four = "Very satisfied" 
        elif self.surveyFourDis.isChecked():
            self.answer_four = "Dissatisfied"
        elif self.surveyFourVeryDis.isChecked():
            self.answer_four = "Extremely dissatisfied"
        elif self.surveyFourSatisfied.isChecked():
            self.answer_four = "Satisfied"      
        elif self.surveyFourNeutral.isChecked():
            self.answer_four = "Neutral"

    def answerFive(self):
        if self.surveyFourVeryDis_6.isChecked():
            self.answer_five = "Extremely Likely"
        elif self.surveyFourVeryDis_4.isChecked():
            self.answer_five = "Neutral"
        elif self.surveyFourVeryDis_3.isChecked():
            self.answer_five = "Slightly likely" 
        elif self.surveyFourVeryDis_2.isChecked():
            self.answer_five = "Not likely at all"
        elif self.surveyFourVeryDis_5.isChecked():
            self.answer_five = "Very likely"

    def tallyAnswers(self, user_client_id):
        self.answerOne()
        self.answerTwo()
        self.answerThree()
        self.answerFour()
        self.answerFive()

        answer_one = self.answer_one
        answer_two = self.answer_two
        answer_three = self.answer_three
        answer_four = self.answer_four
        answer_five = self.answer_five

        self.db_manager.insert_feedback_answers(user_client_id, answer_one, answer_two, answer_three, answer_four, answer_five) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

        self.roleOutput.setText(_translate("MainWindow", "Member"))
        self.finishPushButton.setText(_translate("MainWindow", translation_dict['Finish_Button']))
        self.surveyOne.setText(_translate("MainWindow", translation_dict['Question_1']))
        self.surveyTwo.setText(_translate("MainWindow", translation_dict['Question_2']))
        self.surveyFour.setText(_translate("MainWindow", translation_dict['Question_3']))
        self.surveyThree.setText(_translate("MainWindow", translation_dict['Question_4']))
        self.surveyFive.setText(_translate("MainWindow", translation_dict['Question_5']))
        self.surveyOneExcellent.setText(_translate("MainWindow", translation_dict['Q1_Answer_1']))
        self.surveyOneVeryPoor.setText(_translate("MainWindow", translation_dict['Q1_Answer_2']))
        self.surveyOneGood.setText(_translate("MainWindow", translation_dict['Q1_Answer_3']))
        self.surveyOnePoor.setText(_translate("MainWindow", translation_dict['Q1_Answer_4']))
        self.surveyOneNeutral.setText(_translate("MainWindow", translation_dict['Q1_Answer_5']))

        self.surveyTwoExtreme.setText(_translate("MainWindow", translation_dict['Q2_Answer_1']))
        self.surveyTwoNotAtAll.setText(_translate("MainWindow", translation_dict['Q2_Answer_2']))
        self.surveyTwoVery.setText(_translate("MainWindow", translation_dict['Q2_Answer_3']))
        self.surveyTwoSlightly.setText(_translate("MainWindow", translation_dict['Q2_Answer_4']))
        self.surveyTwoModerate.setText(_translate("MainWindow", translation_dict['Q2_Answer_5']))

        self.surveyThreeNo.setText(_translate("MainWindow", translation_dict['Q3_Answer_1']))
        self.surveyThreeYes.setText(_translate("MainWindow", translation_dict['Q3_Answer_2']))

        self.surveyFourVerySat.setText(_translate("MainWindow", translation_dict['Q4_Answer_1']))
        self.surveyFourDis.setText(_translate("MainWindow", translation_dict['Q4_Answer_2']))
        self.surveyFourVeryDis.setText(_translate("MainWindow", translation_dict['Q4_Answer_3']))
        self.surveyFourSatisfied.setText(_translate("MainWindow", translation_dict['Q4_Answer_4']))
        self.surveyFourNeutral.setText(_translate("MainWindow", translation_dict['Q4_Answer_5']))

        self.surveyFourVeryDis_6.setText(_translate("MainWindow", translation_dict['Q5_Answer_1']))
        self.surveyFourVeryDis_4.setText(_translate("MainWindow", translation_dict['Q5_Answer_2']))
        self.surveyFourVeryDis_3.setText(_translate("MainWindow", translation_dict['Q5_Answer_3']))
        self.surveyFourVeryDis_2.setText(_translate("MainWindow", translation_dict['Q5_Answer_4']))
        self.surveyFourVeryDis_5.setText(_translate("MainWindow", translation_dict['Q5_Answer_5']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowFeedbackQuestions()
    ui.setupUiFeedbackQuestions(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())