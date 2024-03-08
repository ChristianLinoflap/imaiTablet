from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowHelp(object):
    def setupUiHelp(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 450)
        MainWindow.move(0, 110)
        MainWindow.setStyleSheet("#centralwidget{\n"
                                "    background-color:#0000AF;\n"
                                "}")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.helpViewFrame = QtWidgets.QFrame(self.centralwidget)
        self.helpViewFrame.setGeometry(QtCore.QRect(20, 20, 1240, 400))
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
        self.questionOne.setGeometry(QtCore.QRect(25, 70, 1100, 21))
        self.questionOne.setStyleSheet("#questionOne{\n"
                                "    font-family:Montserrat;\n"
                                "    font-size:16px;\n"
                                "}")
        self.questionOne.setObjectName("questionOne")

        self.answerOne = QtWidgets.QTextBrowser(self.helpViewFrame)
        self.answerOne.setGeometry(QtCore.QRect(20, 90, 1200, 75))
        self.answerOne.setStyleSheet("#answerOne{\n"
                                "    border:none;\n"
                                "}")
        self.answerOne.setObjectName("answerOne")

        self.answerTwo = QtWidgets.QTextBrowser(self.helpViewFrame)
        self.answerTwo.setGeometry(QtCore.QRect(20, 190, 1200, 75))
        self.answerTwo.setStyleSheet("#answerTwo{\n"
                                "    border:none;\n"
                                "}")
        self.answerTwo.setObjectName("answerTwo")

        self.questionTwo = QtWidgets.QLabel(self.helpViewFrame)
        self.questionTwo.setGeometry(QtCore.QRect(25, 170, 1200, 21))
        self.questionTwo.setStyleSheet("#questionTwo{\n"
                                "    font-family:Montserrat;\n"
                                "    font-size:16px;\n"
                                "}")
        self.questionTwo.setObjectName("questionTwo")

        self.questionThree = QtWidgets.QLabel(self.helpViewFrame)
        self.questionThree.setGeometry(QtCore.QRect(25, 280, 1200, 21))
        self.questionThree.setStyleSheet("#questionThree{\n"
                                "    font-family:Montserrat;\n"
                                "    font-size:16px;\n"
                                "}")
        self.questionThree.setObjectName("questionThree")

        self.answerThree = QtWidgets.QTextBrowser(self.helpViewFrame)
        self.answerThree.setGeometry(QtCore.QRect(20, 300, 1200, 75))
        self.answerThree.setStyleSheet("#answerThree{\n"
                                "    border:none;\n"
                                "}")
        self.answerThree.setObjectName("answerThree")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowHelp()
    ui.setupUiHelp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())