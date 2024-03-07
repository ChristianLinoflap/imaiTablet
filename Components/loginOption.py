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
        gradient = QtGui.QLinearGradient(0, 0, self.centralwidget.width(), self.centralwidget.height())
        gradient.setColorAt(0, QtGui.QColor("#1D7CBA"))
        gradient.setColorAt(1, QtGui.QColor("#0D3854"))
        self.centralwidget.setStyleSheet("#centralwidget { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #1D7CBA, stop: 1 #0D3854); }")
        self.centralwidget.setObjectName("centralwidget")

        self.backgroundFrameRight = QtWidgets.QFrame(self.centralwidget)
        self.backgroundFrameRight.setGeometry(QtCore.QRect(480, 85, 700, 550))  
        self.backgroundFrameRight.setStyleSheet("#backgroundFrameRight{\n"
"    background-color: #fff; /* Example color */\n"
"    border-top-right-radius: 25px;\n"
"    border-bottom-right-radius: 25px;\n"
"}")
        self.backgroundFrameRight.setObjectName("backgroundFrameRight")

        self.backgroundFrameLeft = QtWidgets.QFrame(self.centralwidget)
        self.backgroundFrameLeft.setGeometry(QtCore.QRect(85, 85, 395, 550))  
        self.backgroundFrameLeft.setStyleSheet("#backgroundFrameLeft{\n"
"    background-color: #0000AF;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"}")
        self.backgroundFrameLeft.setObjectName("backgroundFrameLeft")

        self.bgShape = QtWidgets.QLabel(self.centralwidget)  
        self.bgShape.setGeometry(QtCore.QRect(130, 250, 300, 300))
        self.bgShape.setStyleSheet("#bgShape{\n"
        "    background-color:#FEFCFC;\n"
        "    border-radius:150px;\n"
        "}")
        self.bgShape.setScaledContents(True) 
        self.bgShape.setObjectName("bgShape")

        image_path = "Assets\\loginOptionAsset_1.png" 
        pixmap = QtGui.QPixmap(image_path)
        self.bgShape.setPixmap(pixmap)
        self.bgShape.setAlignment(QtCore.Qt.AlignCenter)

        self.productLabel = QtWidgets.QLabel(self.centralwidget)
        self.productLabel.setGeometry(QtCore.QRect(135, 165, 300, 60))
        self.productLabel.setStyleSheet("#productLabel{\n"
"    font-size:48px;\n"
"    font-weight:bold;\n"
"    font-family: 'Poppins', sans-serif;\n"
"    color:#fff;\n"
"}")
        self.productLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.productLabel.setObjectName("productLabel")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(310, 200, 1050, 65))
        self.titleLabel.setStyleSheet("#titleLabel{\n"
"    font-family:Montserrat;\n"
"    font-size:48px;\n"
"}")
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.memberPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.memberPushButton.setGeometry(QtCore.QRect(500, 290, 300, 220))
        self.memberPushButton.setStyleSheet("#memberPushButton{\n"
"    border-radius:25px;\n"
"    background-color:#0000AF;\n"
"}")
        self.memberPushButton.setText("")
        self.memberPushButton.setObjectName("memberPushButton")
        self.memberPushButton.clicked.connect(self.LogInMember)
        self.memberPushButton.clicked.connect(MainWindow.close)

        self.memberLabel = QtWidgets.QLabel(self.centralwidget)
        self.memberLabel.setGeometry(QtCore.QRect(400, 440, 500, 50))
        self.memberLabel.setStyleSheet("#memberLabel{\n"
"    font-size:20px;\n" 
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.memberLabel.setObjectName("memberLabel")
        self.memberLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.nonMemberLabel = QtWidgets.QLabel(self.centralwidget)
        self.nonMemberLabel.setGeometry(QtCore.QRect(765, 440, 500, 50))
        self.nonMemberLabel.setStyleSheet("#nonMemberLabel{\n"
"    font-size:20px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.nonMemberLabel.setObjectName("nonMemberLabel")
        self.nonMemberLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.nonMemberPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.nonMemberPushButton.setGeometry(QtCore.QRect(860, 290, 300, 220))
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
        self.productLabel.setText(_translate("MainWindow", translation_dict['ProductLabel_Text']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowLogInOption()
    ui.setupUiLogInOption(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
