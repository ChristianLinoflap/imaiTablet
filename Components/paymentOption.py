from PyQt5 import QtCore, QtGui, QtWidgets
from config import Config, translations
import config 

class Ui_MainWindowPaymentOption(object):
    def __init__(self):
        self.help_window_open = False

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

    def ItemView(self):
        from itemView import Ui_MainWindowItemView
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowItemView()
        self.ui.setupUiItemView(self.window)
        self.window.show() 

    def CardPaymentOption(self):
        from cardPaymentOption import Ui_MainWindowCardPaymentOption
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowCardPaymentOption()
        self.ui.setupUiCardPaymentOption(self.window)
        self.window.show() 

    def EWalletPaymentOption(self):
        from eWalletPaymentOption import Ui_MainWindowEWalletPaymentOption
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowEWalletPaymentOption()
        self.ui.setupUiEWalletPaymentOption(self.window)
        self.window.show() 

    def CashPaymentOption(self):
        from cashPaymentOption import Ui_MainWindowCashPaymentOption
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowCashPaymentOption()
        self.ui.setupUiCashPaymentOption(self.window)
        self.window.show() 
 
    def setupUiPaymentOption(self, MainWindow):
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

        self.checkOutPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkOutPushButton.setGeometry(QtCore.QRect(1035, 615, 215, 75))
        self.checkOutPushButton.setStyleSheet("#checkOutPushButton{\n"
                                        "    font-size:18px;\n"
                                        "    font-family:Montserrat;\n"
                                        "    color:#fff;\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #0000AF;\n"
                                        "    background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0.2 #0000AF, stop:0.2 #0000AF, stop:1 #f6f7fa);\n"
                                        "}")
        self.checkOutPushButton.setObjectName("checkOutPushButton")
        self.checkOutPushButton.clicked.connect(self.ItemView)
        self.checkOutPushButton.clicked.connect(MainWindow.close)

        self.helpViewFrame = QtWidgets.QFrame(self.centralwidget)
        self.helpViewFrame.setGeometry(QtCore.QRect(50, 130, 1200, 475))
        self.helpViewFrame.setStyleSheet("#helpViewFrame{\n"
                                "    background-color:#fff;\n"
                                "    border-radius:15px;\n"
                                "}")
        self.helpViewFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helpViewFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helpViewFrame.setObjectName("helpViewFrame")

        self.paymentLabel = QtWidgets.QLabel(self.helpViewFrame)
        self.paymentLabel.setGeometry(QtCore.QRect(20, 20, 300, 31))
        self.paymentLabel.setStyleSheet("#paymentLabel{\n"
                                "    font-size:24px;\n"
                                "    font-family:Montserrat;\n"
                                "}")
        self.paymentLabel.setObjectName("paymentLabel")
        self.cardPushButton = QtWidgets.QPushButton(self.helpViewFrame)
        self.cardPushButton.setGeometry(QtCore.QRect(20, 60, 310, 175))
        self.cardPushButton.setStyleSheet("#cardPushButton{\n"
                                "    border-radius:15px;\n"
                                "    background-color:#D9D9D9;\n"
                                "}")
        self.cardPushButton.setText("")
        self.cardPushButton.setObjectName("cardPushButton")
        self.cardPushButton.clicked.connect(self.CardPaymentOption)
        self.cardPushButton.clicked.connect(MainWindow.close)
        self.eWalletPushButton = QtWidgets.QPushButton(self.helpViewFrame)
        self.eWalletPushButton.setGeometry(QtCore.QRect(435, 60, 310, 175))
        self.eWalletPushButton.setStyleSheet("#eWalletPushButton{\n"
                                "    border-radius:15px;\n"
                                "    background-color:#D9D9D9;\n"
                                "}")
        self.eWalletPushButton.setText("")
        self.eWalletPushButton.setObjectName("eWalletPushButton")
        self.eWalletPushButton.clicked.connect(self.EWalletPaymentOption)
        self.eWalletPushButton.clicked.connect(MainWindow.close)

        self.cashPushButton = QtWidgets.QPushButton(self.helpViewFrame)
        self.cashPushButton.setGeometry(QtCore.QRect(865, 60, 310, 175))
        self.cashPushButton.setStyleSheet("#cashPushButton{\n"
                                "    border-radius:15px;\n"
                                "    background-color:#D9D9D9;\n"
                                "}")
        self.cashPushButton.setText("")
        self.cashPushButton.setObjectName("cashPushButton")
        self.cashPushButton.clicked.connect(self.CashPaymentOption)
        self.cashPushButton.clicked.connect(MainWindow.close)

        self.cardLabel = QtWidgets.QLabel(self.helpViewFrame)
        self.cardLabel.setGeometry(QtCore.QRect(110, 190, 135, 35))
        self.cardLabel.setStyleSheet("#cardLabel{\n"
                                "    font-size:24px;\n"
                                "    font-family:Montserrat;\n"
                                "}")
        self.cardLabel.setObjectName("cardLabel")

        self.eWalletLabel = QtWidgets.QLabel(self.helpViewFrame)
        self.eWalletLabel.setGeometry(QtCore.QRect(520, 190, 135, 31))
        self.eWalletLabel.setStyleSheet("#cardLabel{\n"
                                "    font-size:24px;\n"
                                "    font-family:Montserrat;\n"
                                "}")
        self.eWalletLabel.setObjectName("eWalletLabel")

        self.cashLabel = QtWidgets.QLabel(self.helpViewFrame)
        self.cashLabel.setGeometry(QtCore.QRect(960, 190, 135, 31))
        self.cashLabel.setStyleSheet("#cardLabel{\n"
                                "    font-size:24px;\n"
                                "    font-family:Montserrat;\n"
                                "}")
        self.cashLabel.setObjectName("cashLabel")

        self.voucherLabel = QtWidgets.QLabel(self.helpViewFrame)
        self.voucherLabel.setGeometry(QtCore.QRect(20, 280, 251, 31))
        self.voucherLabel.setStyleSheet("#voucherLabel{\n"
                                "    font-size:24px;\n"
                                "    font-family:Montserrat;\n"
                                "}")
        self.voucherLabel.setObjectName("voucherLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.roleOutput.raise_()
        self.helpPushButton.raise_()
        self.checkOutPushButton.raise_()
        self.paymentLabel.raise_()
        self.cardLabel.raise_()
        self.eWalletLabel.raise_()
        self.cashLabel.raise_()
        self.voucherLabel.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

        self.roleOutput.setText(_translate("MainWindow", translation_dict['Role_Output']))
        self.helpPushButton.setText(_translate("MainWindow", translation_dict['Help_Button']))
        self.checkOutPushButton.setText(_translate("MainWindow", translation_dict['Back_Button']))
        self.paymentLabel.setText(_translate("MainWindow", translation_dict['Payment_Label']))
        self.cardLabel.setText(_translate("MainWindow", translation_dict['Card_Label']))
        self.eWalletLabel.setText(_translate("MainWindow", translation_dict['E_Wallet_Label']))
        self.cashLabel.setText(_translate("MainWindow", translation_dict['Cash_Label']))
        self.voucherLabel.setText(_translate("MainWindow", translation_dict['Voucher_Label']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowPaymentOption()
    ui.setupUiPaymentOption(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())