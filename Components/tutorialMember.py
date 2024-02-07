# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
from config import Config, translations
from PyQt5.QtWidgets import QMessageBox, QStackedWidget, QDialog, QVBoxLayout, QLabel, QProgressBar
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

class Ui_MainWindowTutorialMember(object):
    def __init__(self):
        self.tutorial_steps = []
        self.current_step = 0 
        self.loading_titles = ["Initializing assets. . .", "Loading configurations. . .", "Preparing user interface. . ."]
        self.title_index = 0

    def startProgressBar(self):
        # Create and set up the progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setMinimumWidth(310) 
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)

        self.loading_dialog = QDialog()
        self.loading_dialog.setWindowTitle(self.loading_titles[self.title_index])
        self.loading_dialog.setFixedSize(300, 70)
        self.loading_dialog.setLayout(layout)
        self.loading_dialog.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.loading_dialog.setWindowFlags(self.loading_dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.loading_dialog.show()

        # Create a timer to update the title every two seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTitle)
        self.timer.start(2500)

    def updateTitle(self):
        # Increment the title index
        self.title_index = (self.title_index + 1) % len(self.loading_titles)
        # Update the title of the loading dialog
        self.loading_dialog.setWindowTitle(self.loading_titles[self.title_index])

    def stopProgressBar(self):
        if hasattr(self, 'loading_dialog'):
            self.loading_dialog.close()

    def showTutorialCompletionMessage(self):
        QMessageBox.information(
            None, "Tutorial Completed", "You are now ready to shop!", QMessageBox.Ok
        )

    def handleLoginButtonClick(self, MainWindow):
        if self.current_step < len(self.tutorial_steps):
            self.stackedWidget.setCurrentIndex(self.current_step)
            self.current_step += 1
        else:
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

    # Function to Call ItemView.py
    def ItemView(self):
        self.startProgressBar()
        QTimer.singleShot(2000, lambda: self.showItemView())

    def showItemView(self):
        from itemView import Ui_MainWindowItemView
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowItemView()
        self.ui.setupUiItemView(self.window)
        self.stopProgressBar()
        self.window.show() 
        MainWindow.close()

    # Function to Set Up tutorialMember.py
    def setupUiTutorialMember(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPushButton.setGeometry(QtCore.QRect(655, 600, 200, 60))
        self.backPushButton.setStyleSheet("#backPushButton{\n"
"    background-color:none;\n"
"    border:4px solid #0000AF;\n"
"    border-radius:24px;\n"
"    font-family:Montserrat;\n"
"    font-size:24px;\n"
"    color:#fff;\n"
"}")
        self.backPushButton.setObjectName("backPushButton")
        # To call the function ItemView to open the page and close the main window
        self.backPushButton.clicked.connect(self.ItemView)
        # self.backPushButton.clicked.connect(MainWindow.close)
        self.loginPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginPushButton.setGeometry(QtCore.QRect(430, 600, 200, 60))
        self.loginPushButton.setStyleSheet("#loginPushButton{\n"
"    background-color:#0000AF;\n"
"    border-radius:24px;\n"
"    font-family:Montserrat;\n"
"    font-size:24px;\n"
"    color:#fff\n"
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

        # Use the stored language from Config
        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

        # Translate texts using the stored language
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
