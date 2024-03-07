from PyQt5 import QtCore, QtGui, QtWidgets
from config import Config, translations
import config
from databaseManager import DatabaseManager, EnvironmentLoader
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import glob

class Ui_MainWindowEWalletPaymentOption(object):
    def __init__(self):
        self.help_window_open = False
        self.db_manager = DatabaseManager(*EnvironmentLoader.load_env_variables())
        self.conn = self.db_manager.connect()
        self.cursor = self.conn.cursor()
        self.local_videos = self.getLocalVideosFromFolder()

    def PaymentOption (self):
        self.stopVideosAndCheckout()
        from paymentOption import Ui_MainWindowPaymentOption
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowPaymentOption()
        self.ui.setupUiPaymentOption(self.window)
        self.window.show()

    def FeedBack (self):
        self.stopVideosAndCheckout()
        from feedback import Ui_MainWindowFeedback
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowFeedback()
        self.ui.setupUiFeedback(self.window)
        self.window.show()

    def HelpOption(self):
        if not self.help_window_open:
            from help import Ui_MainWindowHelp
            self.window_help = QtWidgets.QMainWindow()
            self.ui_help = Ui_MainWindowHelp()
            self.ui_help.setupUiHelp(self.window_help)
            self.window_help.show()
            self.help_window_open = True
        else:
            self.window_help.close()
            self.help_window_open = False

    def setupUiEWalletPaymentOption(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen() 
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        gradient = QtGui.QLinearGradient(0, 0, self.centralwidget.width(), self.centralwidget.height())
        gradient.setColorAt(0, QtGui.QColor("#1D7CBA"))
        gradient.setColorAt(1, QtGui.QColor("#0D3854"))
        self.centralwidget.setStyleSheet("#centralwidget { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #1D7CBA, stop: 1 #0D3854); }")
        self.centralwidget.setObjectName("centralwidget")

        self.navigationFrame = QtWidgets.QFrame(self.centralwidget)
        self.navigationFrame.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), 110))
        self.navigationFrame.setStyleSheet("#navigationFrame{\n"
"    background-color:#0000AF;\n"
"}")
        self.navigationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigationFrame.setObjectName("navigationFrame")

        self.nameOutput = QtWidgets.QLabel(self.navigationFrame)
        self.nameOutput.setGeometry(QtCore.QRect(20, 20, 920, 55))
        self.nameOutput.setStyleSheet("#nameOutput{\n"
"    font-weight:bold;\n"
"    font-size:28px;\n"
"    color:#fff;\n"
"}")
        self.nameOutput.setObjectName("nameOutput")
        welcome_message = translations[Config.current_language].get('Welcome_User', 'Welcome')
        first_name = config.user_info.get('first_name', '')
        last_name = config.user_info.get('last_name', '')
        translated_welcome_message = f"{welcome_message}, {first_name} {last_name}"
        self.nameOutput.setText(translated_welcome_message)

        self.roleOutput = QtWidgets.QLabel(self.navigationFrame)
        self.roleOutput.setGeometry(QtCore.QRect(20, 51, 95, 25))
        self.roleOutput.setStyleSheet("#roleOutput{\n"
"    font-size:24px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.roleOutput.setObjectName("roleOutput")

        self.helpPushButton = QtWidgets.QPushButton(self.navigationFrame)
        self.helpPushButton.setGeometry(QtCore.QRect(1145, 25, 150, 50))
        self.helpPushButton.setStyleSheet("#helpPushButton{\n"
"    background-color:none;\n"
"    border:none;\n"
"    color:#fff;\n"
"    font-size:24px;\n"
"}")
        self.helpPushButton.setObjectName("helpPushButton")
        self.helpPushButton.clicked.connect(self.HelpOption)

        self.productTable = QtWidgets.QTableWidget(self.centralwidget)
        self.productTable.setGeometry(QtCore.QRect(20, 230, 490, 475))
        self.productTable.setShowGrid(False)
        self.productTable.setObjectName("productTable")
        self.productTable.setColumnCount(2)
        self.productTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, item)
        self.productTable.setColumnWidth(0, 374)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, item)
        self.productTable.setColumnWidth(1, 110)
        self.productTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.productTable.horizontalHeader().setSectionsMovable(False)
        self.productTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.productTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.productTable.verticalHeader().setVisible(False)
        data_font = QtGui.QFont()
        header_font = QtGui.QFont()
        data_font.setPointSize(16)
        header_font.setPointSize(16)
        self.productTable.setFont(data_font)
        header_stylesheet = "QHeaderView::section { color: #0000AF; font-size: 14px;}"
        self.productTable.horizontalHeader().setStyleSheet(header_stylesheet)

        self.summaryFrame = QtWidgets.QFrame(self.centralwidget)
        self.summaryFrame.setGeometry(QtCore.QRect(20, 120, 240, 100))
        self.summaryFrame.setStyleSheet("#summaryFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:15px;\n"
"}")
        self.summaryFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.summaryFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.summaryFrame.setObjectName("summaryFrame")

        self.totalLabel = QtWidgets.QLabel(self.summaryFrame)
        self.totalLabel.setGeometry(QtCore.QRect(10, 5, 200, 35))
        self.totalLabel.setStyleSheet("#totalLabel{\n"
"    font-size:16px;\n"
"    color:#A0A0A0;\n"
"}")
        self.totalLabel.setObjectName("totalLabel")

        self.totalOutput = QtWidgets.QLabel(self.summaryFrame)
        self.totalOutput.setGeometry(QtCore.QRect(10, 45, 175, 25))
        self.totalOutput.setStyleSheet("#totalOutput{\n"
"    font-size:32px;\n"
"}")
        self.totalOutput.setObjectName("totalOutput")

        self.paymentName = QtWidgets.QLabel(self.summaryFrame)
        self.paymentName.setGeometry(QtCore.QRect(10, 70, 200, 25))
        self.paymentName.setStyleSheet("#paymentName{\n"
        "    font-size:12px;\n"
        "    color:#A0A0A0;\n"
        "}")
        self.paymentName.setObjectName("paymentName")

        self.discountFrame = QtWidgets.QFrame(self.centralwidget)
        self.discountFrame.setGeometry(QtCore.QRect(270, 120, 240, 100))
        self.discountFrame.setStyleSheet("#discountFrame{\n"
        "    background-color:#FEFCFC;\n"
        "    border-radius:15px;\n"
        "}")
        self.discountFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.discountFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.discountFrame.setObjectName("discountFrame")

        self.discountLabel = QtWidgets.QLabel(self.discountFrame)
        self.discountLabel.setGeometry(QtCore.QRect(10, 5, 200, 35))
        self.discountLabel.setStyleSheet("#discountLabel{\n"
        "    font-size:16px;\n"
        "    color:#A0A0A0;\n"
        "}")
        self.discountLabel.setObjectName("discountLabel")
        
        self.discountOutput = QtWidgets.QLabel(self.discountFrame)
        self.discountOutput.setGeometry(QtCore.QRect(10, 45, 175, 25))
        self.discountOutput.setStyleSheet("#discountOutput{\n"
        "    font-size:32px;\n"
        "}")
        self.discountOutput.setObjectName("discountOutput")

        self.discountName = QtWidgets.QLabel(self.discountFrame)
        self.discountName.setGeometry(QtCore.QRect(10, 70, 200, 25))
        self.discountName.setStyleSheet("#discountName{\n"
        "    font-size:12px;\n"
        "    color:#A0A0A0;\n"
        "}")
        self.discountName.setObjectName("discountName")

        self.PaymentFrame = QtWidgets.QFrame(self.centralwidget)
        self.PaymentFrame.setGeometry(QtCore.QRect(530, 120, 720, 475))
        self.PaymentFrame.setStyleSheet("#PaymentFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:15px;\n"
"}")
        self.PaymentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PaymentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PaymentFrame.setObjectName("PaymentFrame")
        self.video_player = QMediaPlayer()
        self.video_player.setVolume(10)  
        self.video_frame = QtWidgets.QFrame(self.PaymentFrame)
        self.video_frame.setGeometry(QtCore.QRect(0, 0, 720, 475))
        self.video_widget = QVideoWidget(self.video_frame)
        self.video_widget.setGeometry(QtCore.QRect(0, 0, 720, 475))
        self.video_player.setVideoOutput(self.video_widget)
        self.video_player.mediaStatusChanged.connect(self.handleVideoStateChange)
        self.playNextVideo()
        
        self.backPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPushButton.setGeometry(QtCore.QRect(900, 610, 170, 100))
        self.backPushButton.setStyleSheet("#backPushButton{\n"
"    border-radius:10px;\n"
"    font-family:Montserrat;\n"
"    font-size:20px;\n"
"    color:#000;\n"
"    border: 2px solid #FFD700;\n"
"    border-radius: 9px;\n"
"    background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0.2 #FFD700, stop:0.2 #FFD700, stop:1 #f6f7fa);\n"
"}")
        self.backPushButton.setObjectName("backPushButton")
        self.backPushButton.clicked.connect(self.PaymentOption)
        self.backPushButton.clicked.connect(MainWindow.close)

        self.checkOutPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkOutPushButton.setGeometry(QtCore.QRect(1085, 610, 170, 100))
        self.checkOutPushButton.setStyleSheet("#checkOutPushButton{\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #0000AF;\n"
"    background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0.2 #0000AF, stop:0.2 #0000AF, stop:1 #f6f7fa);\n"
"}")
        self.checkOutPushButton.setObjectName("checkOutPushButton")
        self.checkOutPushButton.clicked.connect(self.FeedBack)
        self.checkOutPushButton.clicked.connect(MainWindow.close)
        MainWindow.setCentralWidget(self.centralwidget)

        self.populateTableWithScannedProducts()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getLocalVideosFromFolder(self):
        try:
            local_videos_path = "Assets\\*.avi"
            local_videos = glob.glob(local_videos_path)
            return local_videos

        except Exception as e:
            error_message = f"An unexpected error occurred while retrieving local videos: {e}"
            print(error_message)
            QtWidgets.QMessageBox.critical(None, "Error", error_message)
            return []

    def playNextVideo(self):
        try:
            if self.local_videos:
                video_url = self.local_videos.pop(0)
                content = QMediaContent(QtCore.QUrl.fromLocalFile(video_url))
                self.video_player.setMedia(content)
                self.video_player.play()
                self.local_videos.append(video_url)
            else:
                print("No videos available.")
        except Exception as e:
            error_message = f"An unexpected error occurred during video playback: {e}"
            print(error_message)
            QtWidgets.QMessageBox.critical(None, "Error", error_message)

    def handleVideoStateChange(self, new_state):
        try:
            if new_state == QMediaPlayer.EndOfMedia:
                self.playNextVideo()
            elif new_state == QMediaPlayer.Error:
                error_message = f"Error during video playback: {self.video_player.errorString()}"
                print(error_message)
                QtWidgets.QMessageBox.critical(None, "Error", error_message)

        except Exception as e:
            error_message = f"An unexpected error occurred while handling video state change: {e}"
            print(error_message)
            QtWidgets.QMessageBox.critical(None, "Error", error_message)
        
    def stopVideosAndCheckout(self):
        self.video_player.stop()
        self.video_player.mediaStatusChanged.disconnect(self.handleVideoStateChange)
        self.video_player.setMedia(QMediaContent())
        self.video_player.setVideoOutput(None)
        self.video_widget.deleteLater()

    def populateTableWithScannedProducts(self):
        sales_trans = config.transaction_info.get('reference_number')

        query = f"SELECT * FROM dbo.Fn_TransactionReference('{sales_trans}')"
        self.cursor.execute(query)
        scanned_products = self.cursor.fetchall()

        summary_data_query = f"SELECT * FROM dbo.Fn_TransactionSummary('{sales_trans}')"
        self.cursor.execute(summary_data_query)

        summary_data = self.cursor.fetchone()

        if summary_data is not None:
            total_price = summary_data[4]  
            QtCore.QMetaObject.invokeMethod(self.totalOutput, "setText", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, f"¥ {total_price:.2f}"))

        for product in scanned_products:
            product_name = product[7]
            product_price = product[12]

            rowPosition = self.productTable.rowCount()
            self.productTable.insertRow(rowPosition)

            item_name = QtWidgets.QTableWidgetItem(product_name)
            item_price = QtWidgets.QTableWidgetItem(f"¥ {product_price:.2f}")

            self.productTable.setItem(rowPosition, 0, item_name)
            self.productTable.setItem(rowPosition, 1, item_price)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

        self.roleOutput.setText(_translate("MainWindow", translation_dict['Role_Output']))
        self.helpPushButton.setText(_translate("MainWindow", translation_dict['Help_Button']))
        self.checkOutPushButton.setText(_translate("MainWindow", translation_dict['Back_Button']))
        item = self.productTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", translation_dict['Product_Label']))
        item = self.productTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", translation_dict['Price_Label']))
        self.totalLabel.setText(_translate("MainWindow", translation_dict['Total_Price_Label']))
        self.totalOutput.setText(_translate("MainWindow", translation_dict['Total_Price_Output']))
        self.paymentName.setText(_translate("MainWindow", translation_dict['E_Wallet_Payment']))
        self.discountLabel.setText(_translate("MainWindow", translation_dict['Discount_Label']))
        self.discountOutput.setText(_translate("MainWindow", translation_dict['Discount_Output']))
        self.discountName.setText(_translate("MainWindow", translation_dict['Discount_Name']))
        self.backPushButton.setText(_translate("MainWindow", translation_dict['Back_Button']))
        self.checkOutPushButton.setText(_translate("MainWindow", translation_dict['Checkout_Button']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowEWalletPaymentOption()
    ui.setupUiEWalletPaymentOption(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())