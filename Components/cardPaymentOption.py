# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowCardPaymentOption(object):
    # Function to Call paymentOption.py
    def PaymentOption (self):
        from paymentOption import Ui_MainWindowPaymentOption
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowPaymentOption()
        self.ui.setupUiPaymentOption(self.window)
        self.window.show()

    # Function to Call feedback.py
    def FeedBack (self):
        from feedback import Ui_MainWindowFeedback
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowFeedback()
        self.ui.setupUiFeedback(self.window)
        self.window.show()

    # Function to Set Up cardPaymentOption.py
    def setupUiCardPaymentOption(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.navigationFrame = QtWidgets.QFrame(self.centralwidget)
        self.navigationFrame.setGeometry(QtCore.QRect(0, 0, 1200, 100))
        self.navigationFrame.setStyleSheet("#navigationFrame{\n"
"    background-color:#0000AF;\n"
"}")
        self.navigationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigationFrame.setObjectName("navigationFrame")
        self.nameOutput = QtWidgets.QLabel(self.navigationFrame)
        self.nameOutput.setGeometry(QtCore.QRect(20, 30, 181, 21))
        self.nameOutput.setStyleSheet("#nameOutput{\n"
"    font-weight:bold;\n"
"    font-size:24px;\n"
"    color:#fff;\n"
"}")
        self.nameOutput.setObjectName("nameOutput")
        self.roleOutput = QtWidgets.QLabel(self.navigationFrame)
        self.roleOutput.setGeometry(QtCore.QRect(20, 50, 61, 16))
        self.roleOutput.setStyleSheet("#roleOutput{\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.roleOutput.setObjectName("roleOutput")
        self.helpPushButton = QtWidgets.QPushButton(self.navigationFrame)
        self.helpPushButton.setGeometry(QtCore.QRect(1060, 30, 101, 41))
        self.helpPushButton.setStyleSheet("#helpPushButton{\n"
"    background-color:none;\n"
"    border:none;\n"
"    color:#fff;\n"
"    font-size:16px;\n"
"}")
        self.helpPushButton.setObjectName("helpPushButton")
        self.productTable = QtWidgets.QTableWidget(self.centralwidget)
        self.productTable.setGeometry(QtCore.QRect(10, 110, 691, 481))
        self.productTable.setObjectName("productTable")
        self.productTable.setColumnCount(3)
        self.productTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, item)
        self.summaryFrame = QtWidgets.QFrame(self.centralwidget)
        self.summaryFrame.setGeometry(QtCore.QRect(10, 600, 690, 91))
        self.summaryFrame.setStyleSheet("#summaryFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:15px;\n"
"}")
        self.summaryFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.summaryFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.summaryFrame.setObjectName("summaryFrame")
        self.summaryLabel = QtWidgets.QLabel(self.summaryFrame)
        self.summaryLabel.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.summaryLabel.setStyleSheet("#summaryLabel{\n"
"    font-size:18px;\n"
"    font-family:Montserrat;\n"
"    font-weight:bold;\n"
"}")
        self.summaryLabel.setObjectName("summaryLabel")
        self.productsLabel = QtWidgets.QLabel(self.summaryFrame)
        self.productsLabel.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.productsLabel.setStyleSheet("#productsLabel{\n"
"    font-size:12px;\n"
"    color:#A0A0A0;\n"
"}")
        self.productsLabel.setObjectName("productsLabel")
        self.grossLabel = QtWidgets.QLabel(self.summaryFrame)
        self.grossLabel.setGeometry(QtCore.QRect(210, 40, 71, 16))
        self.grossLabel.setStyleSheet("#grossLabel{\n"
"    font-size:12px;\n"
"    color:#A0A0A0;\n"
"}")
        self.grossLabel.setObjectName("grossLabel")
        self.itemsLabel = QtWidgets.QLabel(self.summaryFrame)
        self.itemsLabel.setGeometry(QtCore.QRect(370, 40, 101, 16))
        self.itemsLabel.setStyleSheet("#itemsLabel{\n"
"    font-size:12px;\n"
"    color:#A0A0A0;\n"
"}")
        self.itemsLabel.setObjectName("itemsLabel")
        self.totalLabel = QtWidgets.QLabel(self.summaryFrame)
        self.totalLabel.setGeometry(QtCore.QRect(540, 40, 61, 16))
        self.totalLabel.setStyleSheet("#totalLabel{\n"
"    font-size:12px;\n"
"    color:#A0A0A0;\n"
"}")
        self.totalLabel.setObjectName("totalLabel")
        self.productsOutput = QtWidgets.QLabel(self.summaryFrame)
        self.productsOutput.setGeometry(QtCore.QRect(10, 55, 51, 16))
        self.productsOutput.setObjectName("productsOutput")
        self.grossOutput = QtWidgets.QLabel(self.summaryFrame)
        self.grossOutput.setGeometry(QtCore.QRect(210, 55, 61, 16))
        self.grossOutput.setObjectName("grossOutput")
        self.itemsOutput = QtWidgets.QLabel(self.summaryFrame)
        self.itemsOutput.setGeometry(QtCore.QRect(370, 55, 47, 13))
        self.itemsOutput.setObjectName("itemsOutput")
        self.totalOutput = QtWidgets.QLabel(self.summaryFrame)
        self.totalOutput.setGeometry(QtCore.QRect(543, 55, 47, 13))
        self.totalOutput.setObjectName("totalOutput")
        self.PaymentFrame = QtWidgets.QFrame(self.centralwidget)
        self.PaymentFrame.setGeometry(QtCore.QRect(720, 110, 461, 481))
        self.PaymentFrame.setStyleSheet("#PaymentFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:15px;\n"
"}")
        self.PaymentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PaymentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PaymentFrame.setObjectName("PaymentFrame")
        self.shoppingListLabel = QtWidgets.QLabel(self.PaymentFrame)
        self.shoppingListLabel.setGeometry(QtCore.QRect(20, 10, 151, 31))
        self.shoppingListLabel.setStyleSheet("#shoppingListLabel{\n"
"    font-size:18px;\n"
"    font-weight:bold;\n"
"    font-family:Montserrat;\n"
"}")
        self.shoppingListLabel.setObjectName("shoppingListLabel")
        self.backPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPushButton.setGeometry(QtCore.QRect(870, 620, 81, 51))
        self.backPushButton.setStyleSheet("#backPushButton{\n"
"    background-color:none;\n"
"    border:4px solid #0000AF;\n"
"    border-radius:20px;\n"
"    font-family:Montserrat;\n"
"    font-size:16px;\n"
"    color:#fff;\n"
"}")
        self.backPushButton.setObjectName("backPushButton")
         # To call the function PaymentOption to open the page and close the main window
        self.backPushButton.clicked.connect(self.PaymentOption)
        self.backPushButton.clicked.connect(MainWindow.close)
        self.checkOutPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkOutPushButton.setGeometry(QtCore.QRect(960, 620, 221, 51))
        self.checkOutPushButton.setStyleSheet("#checkOutPushButton{\n"
"    background-color:#0000AF;\n"
"    border-radius:15px;\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.checkOutPushButton.setObjectName("checkOutPushButton")
         # To call the function FeedBack to open the page and close the main window
        self.checkOutPushButton.clicked.connect(self.FeedBack)
        self.checkOutPushButton.clicked.connect(MainWindow.close)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameOutput.setText(_translate("MainWindow", "Juan Dela Cruz"))
        self.roleOutput.setText(_translate("MainWindow", "Member"))
        self.helpPushButton.setText(_translate("MainWindow", "Help"))
        item = self.productTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Products"))
        item = self.productTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Details"))
        item = self.productTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        self.summaryLabel.setText(_translate("MainWindow", "Summary"))
        self.productsLabel.setText(_translate("MainWindow", "Number of Products"))
        self.grossLabel.setText(_translate("MainWindow", "Gross Weight"))
        self.itemsLabel.setText(_translate("MainWindow", "Number of Items"))
        self.totalLabel.setText(_translate("MainWindow", "Total Price"))
        self.productsOutput.setText(_translate("MainWindow", "4 Products"))
        self.grossOutput.setText(_translate("MainWindow", "5,800 grams"))
        self.itemsOutput.setText(_translate("MainWindow", "9 Items"))
        self.totalOutput.setText(_translate("MainWindow", "¥ 7,900"))
        self.shoppingListLabel.setText(_translate("MainWindow", "Payment Details"))
        self.backPushButton.setText(_translate("MainWindow", "Back"))
        self.checkOutPushButton.setText(_translate("MainWindow", "Proceed to Checkout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowCardPaymentOption()
    ui.setupUiCardPaymentOption(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
