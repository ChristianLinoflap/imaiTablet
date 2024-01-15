# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
from config import Config, translations

class Ui_MainWindowLogInOption(object):
    def LogInMember(self):
        from loginMember import Ui_MainWindowLogInMember
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowLogInMember()
        self.ui.setupUiLogInMember(self.window)
        self.window.show()

    def setupUiLogInOption(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(670, 319, 590, 41))
        self.titleLabel.setStyleSheet("#titleLabel{\n"
"    font-family:Montserrat;\n"
"    font-size:35px;\n"
"}")
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.memberPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.memberPushButton.setGeometry(QtCore.QRect(510, 450, 350, 230))
        self.memberPushButton.setStyleSheet("#memberPushButton{\n"
"    border-radius:25px;\n"
"    background-color:#0000AF;\n"
"}")
        self.memberPushButton.setText("")
        self.memberPushButton.setObjectName("memberPushButton")
        self.memberPushButton.clicked.connect(self.LogInMember)
        self.memberPushButton.clicked.connect(MainWindow.close)

        self.memberLabel = QtWidgets.QLabel(self.centralwidget)
        self.memberLabel.setGeometry(QtCore.QRect(530, 630, 310, 31))
        self.memberLabel.setStyleSheet("#memberLabel{\n"
"    font-size:25px;\n" 
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.memberLabel.setObjectName("memberLabel")
        self.memberLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.nonMemberLabel = QtWidgets.QLabel(self.centralwidget)
        self.nonMemberLabel.setGeometry(QtCore.QRect(1045, 630, 310, 31))
        self.nonMemberLabel.setStyleSheet("#nonMemberLabel{\n"
"    font-size:25px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.nonMemberLabel.setObjectName("nonMemberLabel")
        self.nonMemberLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.nonMemberPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.nonMemberPushButton.setGeometry(QtCore.QRect(1025, 450, 350, 230))
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

        # Use the stored language from Config
        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

        # Translate texts using the stored language
        self.titleLabel.setText(_translate("MainWindow", translation_dict['Welcome']))
        self.memberLabel.setText(_translate("MainWindow", translation_dict['Member']))
        self.nonMemberLabel.setText(_translate("MainWindow", translation_dict['Non_Member']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowLogInOption()
    ui.setupUiLogInOption(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
