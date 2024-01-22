# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
from config import translations, Config, component_classes
import subprocess

class LanguageManager:
    @classmethod
    def set_language(cls, language):
        Config.set_language(language)

class Ui_MainWindow(object):
    def __init__(self):
        # Reference to the Advertisement Videos process
        self.advertisment_videos_process = None

        # Start the Advertisment Videos when the item view window is opened
        self.startAdvertisementVideos()

    def startAdvertisementVideos(self):
        self.advertisment_videos_process = subprocess.Popen(['python', 'Components\\AdvertisementDownloader.py'])

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
        MainWindow.showFullScreen()
        MainWindow.setStyleSheet("")
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(780, 700, 400, 100))
        self.startButton.setStyleSheet("#startButton{\n"
"    font-family: 'Montserrat', sans-serif;\n"
"    font-size:42px;\n"
"    color:#fff;\n"
"    border-radius:20px;\n"
"    background-color:#0000AF;\n"
"    padding: 5px;\n"
"    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);\n"
"}")
        self.startButton.setObjectName("startButton")
        # To call the function LogInOption to open the page and close the main window
        self.startButton.clicked.connect(self.LogInOption)
        self.startButton.clicked.connect(MainWindow.close)

        self.productLabel = QtWidgets.QLabel(self.centralwidget)
        self.productLabel.setGeometry(QtCore.QRect(780, 915, 400, 50))
        self.productLabel.setStyleSheet("#productLabel{\n"
"    font-size:30px;\n"
"    font-weight:bold;\n"
"    font-family: 'Montserrat', sans-serif;\n"
"}")
        self.productLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.productLabel.setObjectName("productLabel")

        self.companyLabel = QtWidgets.QLabel(self.centralwidget)
        self.companyLabel.setGeometry(QtCore.QRect(660, 965, 600, 30))
        self.companyLabel.setStyleSheet("#companyLabel{\n"
"    font-size:24px;\n"
"    font-family: 'Montserrat', sans-serif;\n"
"}")
        self.companyLabel.setObjectName("companyLabel")
        self.companyLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.bgShape = QtWidgets.QFrame(self.centralwidget)
        self.bgShape.setGeometry(QtCore.QRect(727, 100, 500, 500))
        self.bgShape.setStyleSheet("#bgShape{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:250px;\n"
"}")
        self.bgShape.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bgShape.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bgShape.setObjectName("bgShape")

        self.translationComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.translationComboBox.setGeometry(QtCore.QRect(50, 925, 150, 70))
        self.translationComboBox.setStyleSheet("#translationComboBox {\n"
"    font-family: Montserrat;\n"
"    font-size: 24px;\n"
"    color: #fff;\n"
"    border-radius: 0px;\n"
"    background-color: #0000AF;\n"
"    padding-left:15px;\n"
"}\n"
"\n"
"#translationComboBox QAbstractItemView {\n"
"    border: 1px solid #0000AF;\n"
"    selection-background-color: #000080;\n"
"}\n"
"\n"
"#translationComboBox QAbstractItemView::item {\n"
"    padding: 8px;\n"
"}\n"
"\n"
"#translationComboBox QAbstractItemView::item:selected {\n"
"    background-color: #000080;\n"
"}\n"
"\n"
"#translationComboBox QAbstractItemView::item:hover {\n"
"    background-color: #0000D0;\n"
"}\n"
"")
        self.translationComboBox.setObjectName("translationComboBox")
        self.translationComboBox.addItem("")
        self.translationComboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        # Connect language change signal
        self.translationComboBox.currentIndexChanged.connect(self.change_language)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def change_language(self, index):
        selected_language = self.translationComboBox.itemText(index)
        LanguageManager.set_language(selected_language)
        self.retranslateUi(MainWindow)
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        language = Config.current_language

        translation_dict = translations.get(language, translations['English'])

        MainWindow.setWindowTitle(_translate("MainWindow", translation_dict['MainWindow_Title']))
        self.startButton.setText(_translate("MainWindow", translation_dict['StartShopping_Button']))
        self.productLabel.setText(_translate("MainWindow", translation_dict['ProductLabel_Text']))
        self.companyLabel.setText(_translate("MainWindow", translation_dict['CompanyLabel_Text']))
        self.translationComboBox.setItemText(1, _translate("MainWindow", translation_dict['ComboBox_English']))
        self.translationComboBox.setItemText(0, _translate("MainWindow", translation_dict['ComboBox_Japanese']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())