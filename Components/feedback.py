# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.finishPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishPushButton.setGeometry(QtCore.QRect(610, 440, 231, 51))
        self.finishPushButton.setStyleSheet("#finishPushButton{\n"
"    background-color:none;\n"
"    border:4px solid #0000AF;\n"
"    border-radius:20px;\n"
"    font-family:Montserrat;\n"
"    font-size:16px;\n"
"    font-weight:bold;\n"
"    color:#0000AF;\n"
"}")
        self.finishPushButton.setObjectName("finishPushButton")
        self.feedBackPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.feedBackPushButton.setGeometry(QtCore.QRect(350, 440, 231, 51))
        self.feedBackPushButton.setStyleSheet("#feedBackPushButton{\n"
"    background-color:#0000AF;\n"
"    border-radius:15px;\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.feedBackPushButton.setObjectName("feedBackPushButton")
        # To call the function feedbackQuesitons to open the page and close the main window
        self.feedBackPushButton.clicked.connect(self.FeedbackQuestions)
        self.feedBackPushButton.clicked.connect(MainWindow.close)
        self.qrFrame = QtWidgets.QFrame(self.centralwidget)
        self.qrFrame.setGeometry(QtCore.QRect(210, 150, 760, 275))
        self.qrFrame.setStyleSheet("#qrFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:25px;\n"
"}")
        self.qrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qrFrame.setObjectName("qrFrame")
        self.thankyouLabel = QtWidgets.QLabel(self.qrFrame)
        self.thankyouLabel.setGeometry(QtCore.QRect(180, 60, 411, 41))
        self.thankyouLabel.setStyleSheet("#thankyouLabel{\n"
"    font-family:Montserrat;\n"
"    font-size:36px;\n"
"    \n"
"}")
        self.thankyouLabel.setObjectName("thankyouLabel")
        self.feedbackParagraph = QtWidgets.QTextEdit(self.qrFrame)
        self.feedbackParagraph.setGeometry(QtCore.QRect(90, 130, 611, 91))
        self.feedbackParagraph.setStyleSheet("#feedbackParagraph{\n"
"    font-size:20px;\n"
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
        self.nameOutput.setText(_translate("MainWindow", "Juan Dela Cruz"))
        self.roleOutput.setText(_translate("MainWindow", "Member"))
        self.finishPushButton.setText(_translate("MainWindow", "Finish Shopping"))
        self.feedBackPushButton.setText(_translate("MainWindow", "Give Feedback"))
        self.thankyouLabel.setText(_translate("MainWindow", "Thank you Dear Shopper!"))
        self.feedbackParagraph.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Montserrat\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">We value your experience! Share your thoughts on your </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">recent </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600;\">IM.AI Cart</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\"> journey to help us enhance our services. </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Your feedback is invaluable to us. </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowFeedback()
    ui.setupUiFeedback(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
