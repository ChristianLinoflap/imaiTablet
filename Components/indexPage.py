# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    # Function to call loginOption.py
    def LogInOption (self):
        from loginOption import Ui_MainWindowLogInOption
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowLogInOption()
        self.ui.setupUiLogInOption(self.window)
        self.window.show()

    # Function to Set Up indexPage.py
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setStyleSheet("")
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(470, 420, 300, 50))
        self.startButton.setStyleSheet("#startButton{\n"
"    font-family:Montserrat;\n"
"    font-size:24px;\n"
"    color:#fff;\n"
"    border-radius:25px;\n"
"    background-color:#0000AF;\n"
"}")
        self.startButton.setObjectName("startButton")
        self.labelFrame = QtWidgets.QFrame(self.centralwidget)
        self.labelFrame.setGeometry(QtCore.QRect(400, 580, 421, 80))
        self.labelFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        # To call the function LogInOption to open the page and close the main window
        self.startButton.clicked.connect(self.LogInOption)
        self.startButton.clicked.connect(MainWindow.close)
        self.labelFrame.setObjectName("labelFrame")
        self.productLabel = QtWidgets.QLabel(self.labelFrame)
        self.productLabel.setGeometry(QtCore.QRect(160, 20, 111, 16))
        self.productLabel.setStyleSheet("#productLabel{\n"
"    font-size:20px;\n"
"    font-weight:bold;\n"
"    font-family:Montserrat;\n"
"}")
        self.productLabel.setObjectName("productLabel")
        self.companyLabel = QtWidgets.QLabel(self.labelFrame)
        self.companyLabel.setGeometry(QtCore.QRect(10, 40, 401, 21))
        self.companyLabel.setStyleSheet("#companyLabel{\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"}")
        self.companyLabel.setObjectName("companyLabel")
        self.bgShape = QtWidgets.QFrame(self.centralwidget)
        self.bgShape.setGeometry(QtCore.QRect(470, 90, 300, 300))
        self.bgShape.setStyleSheet("#bgShape{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:150px;\n"
"}")
        self.bgShape.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bgShape.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bgShape.setObjectName("bgShape")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Start Shopping"))
        self.productLabel.setText(_translate("MainWindow", "IM.AI Cart"))
        self.companyLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Powered by </span><span style=\" font-size:12pt; font-weight:600;\">Linoflap Technologies Philippines Inc.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
