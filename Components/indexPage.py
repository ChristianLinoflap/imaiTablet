from PyQt5 import QtCore, QtGui, QtWidgets
from config import translations, Config
from AdvertisementDownloader import AdvertisementDownloader

class LanguageManager:
    @classmethod
    def set_language(cls, language):
        Config.set_language(language)

class AdvertisementThread(QtCore.QThread):
    def __init__(self, parent=None):
        super(AdvertisementThread, self).__init__(parent)
        self.advertisement_downloader = AdvertisementDownloader()

    def run(self):
        self.advertisement_downloader.start_download()

class Ui_MainWindow(object):
    # def __init__(self):
    #     self.advertisement_thread = AdvertisementThread()
    #     self.startAdvertisementThread()

    # def startAdvertisementThread(self):
    #     self.advertisement_thread.start()

    def LogInOption (self):
        from loginOption import Ui_MainWindowLogInOption
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowLogInOption()
        self.ui.setupUiLogInOption(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        MainWindow.setStyleSheet("")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        gradient = QtGui.QLinearGradient(0, 0, self.centralwidget.width(), self.centralwidget.height())
        gradient.setColorAt(0, QtGui.QColor("#1D7CBA"))
        gradient.setColorAt(1, QtGui.QColor("#0D3854"))
        self.centralwidget.setStyleSheet("#centralwidget { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #1D7CBA, stop: 1 #0D3854); }")
        self.centralwidget.setObjectName("centralwidget")

        self.imageFrame = QtWidgets.QLabel(self.centralwidget)
        self.imageFrame.setGeometry(QtCore.QRect(655, 145, 550, 450))
        self.imageFrame.setStyleSheet("#imageFrame{\n"
                                    "    background-color: #FEFCFC;\n"
                                    "    border-radius: 15px;\n"
                                    "}\n")
        self.imageFrame.setObjectName("imageFrame")
        self.imageFrame.setScaledContents(True)

        image_path = "Assets\\indexPageAsset_2.jpg" 
        pixmap = QtGui.QPixmap(image_path)
        target_size = QtCore.QSize(900, 600)
        pixmap_resized = pixmap.scaled(target_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        mask = QtGui.QBitmap(pixmap_resized.size())
        mask.fill(QtCore.Qt.white)
        painter = QtGui.QPainter(mask)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtGui.QColor(QtCore.Qt.black))
        painter.drawRoundedRect(mask.rect(), 15, 15)
        painter.end()
        pixmap_resized.setMask(mask)
        self.imageFrame.setPixmap(pixmap_resized)
        self.imageFrame.setAlignment(QtCore.Qt.AlignCenter)
    
        self.welcomeTitle = QtWidgets.QLabel(self.centralwidget)
        self.welcomeTitle.setGeometry(QtCore.QRect(100, 310, 300, 50))
        self.welcomeTitle.setStyleSheet("#welcomeTitle{\n"
                                    "    font-size: 48px;\n"
                                    "    font-weight: bold;\n"
                                    "    color: #fff;\n"
                                    "}\n")
        self.welcomeTitle.setObjectName("welcomeTitle")

        self.welcomeMessage = QtWidgets.QLabel(self.centralwidget)
        self.welcomeMessage.setGeometry(QtCore.QRect(100, 360, 400, 50))
        self.welcomeMessage.setStyleSheet("#welcomeMessage{\n"
                                        "    font-size: 18px;\n"
                                        "    color: #fff;\n"
                                        "}\n")
        self.welcomeMessage.setObjectName("welcomeMessage")

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(100, 470, 255, 100))
        self.startButton.setStyleSheet("#startButton{\n"
                                        "    font-size: 24px;\n"
                                        "    font-family: Montserrat;\n"
                                        "    color: #fff;\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #0000AF;\n"
                                        "    background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0.2 #0000AF, stop:0.2 #0000AF, stop:1 #f6f7fa);\n"
                                        "}")
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.LogInOption)
        self.startButton.clicked.connect(MainWindow.close)


        self.productLabel = QtWidgets.QLabel(self.centralwidget)
        self.productLabel.setGeometry(QtCore.QRect(195, 185, 300, 60))
        self.productLabel.setStyleSheet("#productLabel{\n"
                                        "    font-size:48px;\n"
                                        "    font-weight:bold;\n"
                                        "    font-family: 'Poppins', sans-serif;\n"
                                        "    color:#fff;\n"
                                        "}")
        self.productLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.productLabel.setObjectName("productLabel")

        self.companyLabel = QtWidgets.QLabel(self.centralwidget)
        self.companyLabel.setGeometry(QtCore.QRect(100, 605, 405, 30))
        self.companyLabel.setStyleSheet("#companyLabel{\n"
                                        "    font-size:24px;\n"
                                        "    font-family: 'Montserrat', sans-serif;\n"
                                        "    font-family: 'Poppins', sans-serif;\n"
                                        "    color:#fff;\n"
                                        "}")
        self.companyLabel.setObjectName("companyLabel")
        
        self.bgShape = QtWidgets.QLabel(self.centralwidget)  
        self.bgShape.setGeometry(QtCore.QRect(100, 160, 106, 106))
        self.bgShape.setStyleSheet("#bgShape{\n"
                                    "    background-color:#FEFCFC;\n"
                                    "    border-radius:53px;\n"
                                    "}")
        self.bgShape.setScaledContents(True) 
        self.bgShape.setObjectName("bgShape")

        image_path = "Assets\\indexPageAsset_1.png" 
        pixmap = QtGui.QPixmap(image_path)
        self.bgShape.setPixmap(pixmap)

        self.translationComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.translationComboBox.setGeometry(QtCore.QRect(1055, 40, 150, 75))
        self.translationComboBox.setStyleSheet("#translationComboBox {\n"
                                                "    font-family: Montserrat;\n"
                                                "    font-size: 20px;\n"
                                                "    color: #fff;\n"
                                                "    border-radius: 10px;\n"
                                                "    background-color: #0000AF;\n"
                                                "    padding-left: 15px;\n"
                                                "}\n"
                                                "\n"
                                                "#translationComboBox QAbstractItemView {\n"
                                                "    border: 1px solid #0000AF;\n"
                                                "    selection-background-color: #0000AF;\n"
                                                "}\n"
                                                "\n"
                                                "#translationComboBox QAbstractItemView::item {\n"
                                                "    padding: 24px;\n"
                                                "}\n"
                                                "\n"
                                                "#translationComboBox QAbstractItemView::item:selected {\n"
                                                "    background-color: #0000AF;\n"
                                                "}\n"
                                                "\n"
                                                "#translationComboBox::drop-down {\n"
                                                "    border-top-right-radius: 10px;\n"
                                                "    border-bottom-right-radius: 10px;\n"
                                                "    background-color: #fff; \n"
                                                "    subcontrol-origin: padding;\n"
                                                "    subcontrol-position: right center;\n"
                                                "    width: 30px; /* Adjust the width as needed */\n"
                                                "    height: 75px; /* Adjust the height as needed */\n"
                                                "}\n"
                                                "")
        self.translationComboBox.setObjectName("translationComboBox")
        self.translationComboBox.addItem("")
        self.translationComboBox.addItem("")

        MainWindow.setCentralWidget(self.centralwidget)

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
        self.welcomeMessage.setText(_translate("MainWindow", translation_dict['Welcome_Message']))      
        self.welcomeTitle.setText(_translate("MainWindow", translation_dict['Welcome_Title']))  
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