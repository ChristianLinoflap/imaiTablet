from PyQt5 import QtCore, QtGui, QtWidgets
from config import Config, translations
from PyQt5.QtWidgets import QMessageBox, QStackedWidget
from PyQt5.QtGui import QPixmap

class Ui_MainWindowTutorialMember(object):
    def __init__(self):
        self.tutorial_steps = []
        self.current_step = 1 

    def showTutorialCompletionMessage(self):
        QMessageBox.information(
            None, "Tutorial Completed", "You are now ready to shop!", QMessageBox.Ok
        )

    def handleLoginButtonClick(self):
        print("Current Step:", self.current_step)
        if self.current_step < len(self.tutorial_steps):
            print("Displaying Step:", self.current_step)
            self.stackedWidget.setCurrentIndex(self.current_step)
            self.current_step += 1
        else:
            print("Showing Completion Message")
            self.showTutorialCompletionMessage()
            self.current_step = 0
            self.ItemView()
            
    def setupTutorialSteps(self):
        image_paths = [
            "Assets\\1.png",
            "Assets\\2.png",
            "Assets\\3.png",
            "Assets\\4.png"
        ]

        for image_path in image_paths:
            step_label = QtWidgets.QLabel(self.qrFrame)
            pixmap = QPixmap(image_path)
            step_label.setPixmap(pixmap)
            step_label.setScaledContents(True)
            self.tutorial_steps.append(step_label)

    def ItemView(self):
        from itemView import Ui_MainWindowItemView
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowItemView()
        self.ui.setupUiItemView(self.window)
        self.window.show() 

    def setupUiTutorialMember(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        gradient = QtGui.QLinearGradient(0, 0, self.centralwidget.width(), self.centralwidget.height())
        gradient.setColorAt(0, QtGui.QColor("#1D7CBA"))
        gradient.setColorAt(1, QtGui.QColor("#0D3854"))
        self.centralwidget.setStyleSheet("#centralwidget { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #1D7CBA, stop: 1 #0D3854); }")
        self.centralwidget.setObjectName("centralwidget")

        self.backPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPushButton.setGeometry(QtCore.QRect(655, 570, 200, 100))
        self.backPushButton.setStyleSheet("#backPushButton{\n"
                                            "    border-radius:10px;\n"
                                            "    font-family:Montserrat;\n"
                                            "    font-size:24px;\n"
                                            "    color:#000;\n"
                                            "    border: 2px solid #FFD700;\n"
                                            "    border-radius: 9px;\n"
                                            "    background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0.2 #FFD700, stop:0.2 #FFD700, stop:1 #f6f7fa);\n"
                                        "}")
        self.backPushButton.setObjectName("backPushButton")
        self.backPushButton.clicked.connect(self.ItemView)
        self.backPushButton.clicked.connect(MainWindow.close)

        self.loginPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginPushButton.setGeometry(QtCore.QRect(430, 570, 200, 100))
        self.loginPushButton.setStyleSheet("#loginPushButton{\n"
                                            "    font-size:24px;\n"
                                            "    font-family:Montserrat;\n"
                                            "    color:#fff;\n"
                                            "    border-radius: 10px;\n"
                                            "    border: 2px solid #0000AF;\n"
                                            "    background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0.2 #0000AF, stop:0.2 #0000AF, stop:1 #f6f7fa);\n"
                                        "}")
        self.loginPushButton.setObjectName("loginPushButton")
        self.qrFrame = QtWidgets.QFrame(self.centralwidget)
        self.qrFrame.setGeometry(QtCore.QRect(350, 50, 600, 500))
        self.qrFrame.setStyleSheet("#qrFrame{\n"
                                "    background-color:#FEFCFC;\n"
                                "    border-radius:25px;\n"
                                "}")
        self.stackedWidget = QStackedWidget(self.qrFrame)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 600, 500))

        self.setupTutorialSteps()
        for step in self.tutorial_steps:
            self.stackedWidget.addWidget(step)

        self.loginPushButton.clicked.connect(self.handleLoginButtonClick)
        self.qrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qrFrame.setObjectName("qrFrame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.backPushButton.raise_()
        self.loginPushButton.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

        self.backPushButton.setText(_translate("MainWindow", translation_dict['Skip_Button']))
        self.loginPushButton.setText(_translate("MainWindow", translation_dict['Next_Button']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowTutorialMember()
    ui.setupUiTutorialMember(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())