from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowHelp(object):
    # Function to Call loginOption.py
    def HelpOption (self):
        from help import Ui_MainWindowHelp
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowHelp()
        self.ui.setupUiHelp(self.window)
        self.window.show()
    
    # Function to Call ItemView.py
    def ItemView(self):
        from itemView import Ui_MainWindowItemView
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowItemView()
        self.ui.setupUiItemView(self.window)
        self.window.show() 

    # Function to Set Up help.py
    def setupUiHelp(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.navigationFrame = QtWidgets.QFrame(self.centralwidget)
        self.navigationFrame.setGeometry(QtCore.QRect(0, 0, 1200, 100))
        self.navigationFrame.setStyleSheet("#navigationFrame{\n"
"    background-color:#0000AF;\n"
"}")
        self.navigationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigationFrame.setObjectName("navigationFrame")
        self.nameOutput = QtWidgets.QLabel(self.navigationFrame)
        self.nameOutput.setGeometry(QtCore.QRect(20, 30, 181, 21))
        self.nameOutput.setStyleSheet("#nameOutput{\n"
"    font-weight:bold;\n"
"    font-size:24px;\n"
"    color:#fff;\n"
"}")
        self.nameOutput.setObjectName("nameOutput")
        self.roleOutput = QtWidgets.QLabel(self.navigationFrame)
        self.roleOutput.setGeometry(QtCore.QRect(20, 50, 61, 16))
        self.roleOutput.setStyleSheet("#roleOutput{\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.roleOutput.setObjectName("roleOutput")
        self.helpPushButton = QtWidgets.QPushButton(self.navigationFrame)
        self.helpPushButton.setGeometry(QtCore.QRect(1060, 30, 101, 41))
        self.helpPushButton.setStyleSheet("#helpPushButton{\n"
"    background-color:#00C0FF;\n"
"    border:none;\n"
"    border-radius:15px;\n"
"    color:#000;\n"
"    font-size:16px;\n"
"}")
        self.helpPushButton.setObjectName("helpPushButton")
        self.backPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPushButton.setGeometry(QtCore.QRect(20, 620, 90, 51))
        self.backPushButton.setStyleSheet("#backPushButton{\n"
"    background-color:#0000AF;\n"
"    border-radius:15px;\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.backPushButton.setObjectName("backPushButton")
        # To call the function LogInOption to open the page and close the main window
        self.backPushButton.clicked.connect(self.ItemView)
        self.backPushButton.clicked.connect(MainWindow.close)
        self.helpViewFrame = QtWidgets.QFrame(self.centralwidget)
        self.helpViewFrame.setGeometry(QtCore.QRect(20, 120, 1151, 491))
        self.helpViewFrame.setStyleSheet("#helpViewFrame{\n"
"    background-color:#fff;\n"
"    border-radius:15px;\n"
"}")
        self.helpViewFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helpViewFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helpViewFrame.setObjectName("helpViewFrame")
        self.helpLabel = QtWidgets.QLabel(self.helpViewFrame)
        self.helpLabel.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.helpLabel.setStyleSheet("#helpLabel{\n"
"    font-size:20px;\n"
"    font-family:Montserrat;\n"
"}")
        self.helpLabel.setObjectName("helpLabel")
        self.questionOne = QtWidgets.QLabel(self.helpViewFrame)
        self.questionOne.setGeometry(QtCore.QRect(25, 70, 131, 21))
        self.questionOne.setStyleSheet("#questionOne{\n"
"    font-family:Montserrat;\n"
"    font-size:16px;\n"
"}")
        self.questionOne.setObjectName("questionOne")
        self.answerOne = QtWidgets.QTextBrowser(self.helpViewFrame)
        self.answerOne.setGeometry(QtCore.QRect(20, 90, 1101, 61))
        self.answerOne.setStyleSheet("#answerOne{\n"
"    border:none;\n"
"    font-family:Montserrat;\n"
"    font-size:16px;\n"
"}")
        self.answerOne.setObjectName("answerOne")
        self.answerTwo = QtWidgets.QTextBrowser(self.helpViewFrame)
        self.answerTwo.setGeometry(QtCore.QRect(20, 190, 1101, 61))
        self.answerTwo.setStyleSheet("#answerTwo{\n"
"    border:none;\n"
"    font-family:Montserrat;\n"
"    font-size:16px;\n"
"}")
        self.answerTwo.setObjectName("answerTwo")
        self.questionTwo = QtWidgets.QLabel(self.helpViewFrame)
        self.questionTwo.setGeometry(QtCore.QRect(25, 170, 131, 21))
        self.questionTwo.setStyleSheet("#questionTwo{\n"
"    font-family:Montserrat;\n"
"    font-size:16px;\n"
"}")
        self.questionTwo.setObjectName("questionTwo")
        self.questionThree = QtWidgets.QLabel(self.helpViewFrame)
        self.questionThree.setGeometry(QtCore.QRect(25, 280, 131, 21))
        self.questionThree.setStyleSheet("#questionThree{\n"
"    font-family:Montserrat;\n"
"    font-size:16px;\n"
"}")
        self.questionThree.setObjectName("questionThree")
        self.answerThree = QtWidgets.QTextBrowser(self.helpViewFrame)
        self.answerThree.setGeometry(QtCore.QRect(20, 300, 1101, 61))
        self.answerThree.setStyleSheet("#answerThree{\n"
"    border:none;\n"
"    font-family:Montserrat;\n"
"    font-size:16px;\n"
"}")
        self.answerThree.setObjectName("answerThree")
        self.questionFour = QtWidgets.QLabel(self.helpViewFrame)
        self.questionFour.setGeometry(QtCore.QRect(25, 390, 131, 21))
        self.questionFour.setStyleSheet("#questionFour{\n"
"    font-family:Montserrat;\n"
"    font-size:16px;\n"
"}")
        self.questionFour.setObjectName("questionFour")
        self.answerFour = QtWidgets.QTextBrowser(self.helpViewFrame)
        self.answerFour.setGeometry(QtCore.QRect(20, 410, 1101, 61))
        self.answerFour.setStyleSheet("#answerFour{\n"
"    border:none;\n"
"    font-family:Montserrat;\n"
"    font-size:16px;\n"
"}")
        self.answerFour.setObjectName("answerFour")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameOutput.setText(_translate("MainWindow", "Juan Dela Cruz"))
        self.roleOutput.setText(_translate("MainWindow", "Member"))
        self.helpPushButton.setText(_translate("MainWindow", "Help"))
        self.backPushButton.setText(_translate("MainWindow", "Back"))
        self.helpLabel.setText(_translate("MainWindow", "Frequently Asked Questions"))
        self.questionOne.setText(_translate("MainWindow", "Lorem Ipsum"))
        self.answerOne.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et  dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span></p></body></html>"))
        self.answerTwo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et  dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span></p></body></html>"))
        self.questionTwo.setText(_translate("MainWindow", "Lorem Ipsum"))
        self.questionThree.setText(_translate("MainWindow", "Lorem Ipsum"))
        self.answerThree.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et  dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span></p></body></html>"))
        self.questionFour.setText(_translate("MainWindow", "Lorem Ipsum"))
        self.answerFour.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et  dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowHelp()
    ui.setupUiHelp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
