# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowTutorialMember(object):
    # Function to Call ItemView.py
    def ItemView(self):
        from itemView import Ui_MainWindowItemView
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowItemView()
        self.ui.setupUiItemView(self.window)
        self.window.show() 

    # Function to Set Up tutorialMember.py
    def setupUiTutorialMember(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPushButton.setGeometry(QtCore.QRect(450, 540, 350, 45))
        self.backPushButton.setStyleSheet("#backPushButton{\n"
"    background-color:none;\n"
"    border:4px solid #0000AF;\n"
"    border-radius:20px;\n"
"    font-family:Montserrat;\n"
"    font-size:20px;\n"
"    color:#fff;\n"
"}")
        self.backPushButton.setObjectName("backPushButton")
        # To call the function ItemView to open the page and close the main window
        self.backPushButton.clicked.connect(self.ItemView)
        self.backPushButton.clicked.connect(MainWindow.close)
        self.loginPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginPushButton.setGeometry(QtCore.QRect(450, 480, 350, 45))
        self.loginPushButton.setStyleSheet("#loginPushButton{\n"
"    background-color:#0000AF;\n"
"    border-radius:20px;\n"
"    font-family:Montserrat;\n"
"    font-size:20px;\n"
"    color:#fff\n"
"}")
        self.loginPushButton.setObjectName("loginPushButton")
        self.qrFrame = QtWidgets.QFrame(self.centralwidget)
        self.qrFrame.setGeometry(QtCore.QRect(210, 50, 825, 390))
        self.qrFrame.setStyleSheet("#qrFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:25px;\n"
"}")
        self.qrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qrFrame.setObjectName("qrFrame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backPushButton.setText(_translate("MainWindow", "Skip"))
        self.loginPushButton.setText(_translate("MainWindow", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowTutorialMember()
    ui.setupUiTutorialMember(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
