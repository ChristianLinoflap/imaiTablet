# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowLogInOption(object):
    # Function to call loginMember.py
    def LogInMember(self):
        from loginMember import Ui_MainWindowLogInMember
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowLogInMember()
        self.ui.setupUiLogInMember(self.window)
        self.window.show()

    # Function to Set Up loginOption.py
    def setupUiLogInOption(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(340, 140, 591, 41))
        self.titleLabel.setStyleSheet("#titleLabel{\n"
"    font-family:Montserrat;\n"
"    font-size:35px;\n"
"}")
        self.titleLabel.setObjectName("titleLabel")
        self.memberPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.memberPushButton.setGeometry(QtCore.QRect(240, 250, 350, 230))
        self.memberPushButton.setStyleSheet("#memberPushButton{\n"
"    border-radius:25px;\n"
"    background-color:#0000AF;\n"
"}")
        self.memberPushButton.setText("")
        self.memberPushButton.setObjectName("memberPushButton")
        # To call the function LogInmember to open the page and close the main window
        self.memberPushButton.clicked.connect(self.LogInMember)
        self.memberPushButton.clicked.connect(MainWindow.close)
        self.memberLabel = QtWidgets.QLabel(self.centralwidget)
        self.memberLabel.setGeometry(QtCore.QRect(300, 420, 231, 31))
        self.memberLabel.setStyleSheet("#memberLabel{\n"
"    font-size:25px;\n" 
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.memberLabel.setObjectName("memberLabel")
        self.nonMemberLabel = QtWidgets.QLabel(self.centralwidget)
        self.nonMemberLabel.setGeometry(QtCore.QRect(730, 420, 271, 31))
        self.nonMemberLabel.setStyleSheet("#nonMemberLabel{\n"
"    font-size:25px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.nonMemberLabel.setObjectName("nonMemberLabel")
        self.nonMemberPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.nonMemberPushButton.setGeometry(QtCore.QRect(680, 250, 350, 230))
        self.nonMemberPushButton.setStyleSheet("#nonMemberPushButton{\n"
"    border-radius:25px;\n"
"    background-color:#0000AF;\n"
"}")
        self.nonMemberPushButton.setText("")
        self.nonMemberPushButton.setObjectName("nonMemberPushButton")
        self.titleLabel.raise_()
        self.memberPushButton.raise_()
        self.memberLabel.raise_()
        self.nonMemberPushButton.raise_()
        self.nonMemberLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Welcome! Are you already a member?"))
        self.memberLabel.setText(_translate("MainWindow", "Yes, I am a member"))
        self.nonMemberLabel.setText(_translate("MainWindow", "No, I am not a member"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowLogInOption()
    ui.setupUiLogInOption(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
