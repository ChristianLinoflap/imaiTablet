# Third Pary Library Imports
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc

# Module Imports
from config import db_server_name, db_name, db_username, db_password
from config import Config, translations
import config 

# Database Management 
class DatabaseManager:
    # Database Initializations
    def __init__(self, server_name, database_name, username, password):
        self.server_name = server_name
        self.database_name = database_name
        self.username = username
        self.password = password
        
    # Database Connection
    def connect(self):
        driver_name = 'ODBC Driver 17 for SQL Server'
        connection_string = f"DRIVER={{{driver_name}}};SERVER={self.server_name};DATABASE={self.database_name};UID={self.username};PWD={self.password}"

        try:
            with pyodbc.connect(connection_string, timeout=5) as conn:
                return conn
        except pyodbc.OperationalError as e:
            print(f"Error connecting to the database: {e}")
            raise

class Ui_MainWindowCashPaymentOption(object):
    # Initializations
    def __init__(self):
        self.help_window_open = False
        # Database connection setup
        self.db_manager = DatabaseManager(
            server_name=db_server_name,
            database_name=db_name,
            username=db_username,
            password=db_password
        )
        self.conn = self.db_manager.connect()
        self.cursor = self.conn.cursor()

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

    # Function to Call help.py
    def HelpOption(self):
        if not self.help_window_open:
            from help import Ui_MainWindowHelp
            self.window_help = QtWidgets.QMainWindow()
            self.ui_help = Ui_MainWindowHelp()
            self.ui_help.setupUiHelp(self.window_help)
            self.window_help.show()
            # Set the flag to indicate that the window is open
            self.help_window_open = True
        else:
            # Close the window if it's open
            self.window_help.close()
            # Set the flag to indicate that the window is closed
            self.help_window_open = False

    # Function to Set Up cashPaymentOption.py 
    def setupUiCashPaymentOption(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen() 
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.navigationFrame = QtWidgets.QFrame(self.centralwidget)
        self.navigationFrame.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), 150))
        self.navigationFrame.setStyleSheet("#navigationFrame{\n"
"    background-color:#0000AF;\n"
"}")
        self.navigationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigationFrame.setObjectName("navigationFrame")

        self.nameOutput = QtWidgets.QLabel(self.navigationFrame)
        self.nameOutput.setGeometry(QtCore.QRect(50, 50, 900, 35))
        self.nameOutput.setStyleSheet("#nameOutput{\n"
"    font-weight:bold;\n"
"    font-size:42px;\n"
"    color:#fff;\n"
"}")
        self.nameOutput.setObjectName("nameOutput")
        # Translate the welcome message and user's name
        welcome_message = translations[Config.current_language].get('Welcome_User', 'Welcome')
        first_name = config.user_info.get('first_name', '')
        last_name = config.user_info.get('last_name', '')
        translated_welcome_message = f"{welcome_message}, {first_name} {last_name}"
        self.nameOutput.setText(translated_welcome_message)

        self.roleOutput = QtWidgets.QLabel(self.navigationFrame)
        self.roleOutput.setGeometry(QtCore.QRect(50, 100, 75, 16))
        self.roleOutput.setStyleSheet("#roleOutput{\n"
"    font-size:24px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.roleOutput.setObjectName("roleOutput")

        self.helpPushButton = QtWidgets.QPushButton(self.navigationFrame)
        self.helpPushButton.setGeometry(QtCore.QRect(1700, 55, 150, 50))
        self.helpPushButton.setStyleSheet("#helpPushButton{\n"
"    background-color:none;\n"
"    border:none;\n"
"    color:#fff;\n"
"    font-size:24px;\n"
"}")
        self.helpPushButton.setObjectName("helpPushButton")
        self.helpPushButton.clicked.connect(self.HelpOption)

        self.productTable = QtWidgets.QTableWidget(self.centralwidget)
        self.productTable.setGeometry(QtCore.QRect(50, 200, 1000, 650))
        self.productTable.setGridStyle(QtCore.Qt.SolidLine)
        self.productTable.setObjectName("productTable")
        self.productTable.setColumnCount(4)
        self.productTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, item)
        self.productTable.setColumnWidth(0, 400)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, item)
        self.productTable.setColumnWidth(1, 200)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, item)
        self.productTable.setColumnWidth(2, 200) 
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(3, item)
        self.productTable.setColumnWidth(3, 200)
        self.productTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) 
        # Set the table to read-only
        self.productTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        # Make column headers not movable
        self.productTable.horizontalHeader().setSectionsMovable(False)
        # Set column width and row height to be fixed
        self.productTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.productTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        data_font = QtGui.QFont()
        header_font = QtGui.QFont()
        data_font.setPointSize(12)
        header_font.setPointSize(14)

        self.productTable.setFont(data_font)
        header_stylesheet = "QHeaderView::section { font-size: 14px; }"
        self.productTable.horizontalHeader().setStyleSheet(header_stylesheet)
        self.summaryFrame = QtWidgets.QFrame(self.centralwidget)
        self.summaryFrame.setGeometry(QtCore.QRect(50, 870, 740, 115))
        self.summaryFrame.setStyleSheet("#summaryFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:15px;\n"
"}")
        self.summaryFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.summaryFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.summaryFrame.setObjectName("summaryFrame")
        self.summaryLabel = QtWidgets.QLabel(self.summaryFrame)
        self.summaryLabel.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.summaryLabel.setStyleSheet("#summaryLabel{\n"
"    font-size:24px;\n"
"    font-family:Montserrat;\n"
"    font-weight:bold;\n"
"}")
        self.summaryLabel.setObjectName("summaryLabel")

        self.productsLabel = QtWidgets.QLabel(self.summaryFrame)
        self.productsLabel.setGeometry(QtCore.QRect(10, 55, 111, 16))
        self.productsLabel.setStyleSheet("#productsLabel{\n"
"    font-size:16px;\n"
"    color:#A0A0A0;\n"
"}")
        self.productsLabel.setObjectName("productsLabel")

        self.grossLabel = QtWidgets.QLabel(self.summaryFrame)
        self.grossLabel.setGeometry(QtCore.QRect(175, 55, 71, 16))
        self.grossLabel.setStyleSheet("#grossLabel{\n"
"    font-size:16px;\n"
"    color:#A0A0A0;\n"
"}")
        self.grossLabel.setObjectName("grossLabel")

        self.itemsLabel = QtWidgets.QLabel(self.summaryFrame)
        self.itemsLabel.setGeometry(QtCore.QRect(360, 55, 101, 16))
        self.itemsLabel.setStyleSheet("#itemsLabel{\n"
"    font-size:16px;\n"
"    color:#A0A0A0;\n"
"}")
        self.itemsLabel.setObjectName("itemsLabel")

        self.totalLabel = QtWidgets.QLabel(self.summaryFrame)
        self.totalLabel.setGeometry(QtCore.QRect(515, 55, 61, 16))
        self.totalLabel.setStyleSheet("#totalLabel{\n"
"    font-size:16px;\n"
"    color:#A0A0A0;\n"
"}")
        self.totalLabel.setObjectName("totalLabel")

        self.productsOutput = QtWidgets.QLabel(self.summaryFrame)
        self.productsOutput.setGeometry(QtCore.QRect(10, 75, 100, 16))
        self.productsOutput.setStyleSheet("#productsOutput{\n"
"    font-size:16px;\n"
"}")
        self.productsOutput.setObjectName("productsOutput")

        self.grossOutput = QtWidgets.QLabel(self.summaryFrame)
        self.grossOutput.setGeometry(QtCore.QRect(175, 70, 100, 25))
        self.grossOutput.setStyleSheet("#grossOutput{\n"
"    font-size:16px;\n"
"}")
        self.grossOutput.setObjectName("grossOutput")

        self.itemsOutput = QtWidgets.QLabel(self.summaryFrame)
        self.itemsOutput.setGeometry(QtCore.QRect(360, 75, 100, 13))
        self.itemsOutput.setStyleSheet("#itemsOutput{\n"
"    font-size:16px;\n"
"}")
        self.itemsOutput.setObjectName("itemsOutput")

        self.totalOutput = QtWidgets.QLabel(self.summaryFrame)
        self.totalOutput.setGeometry(QtCore.QRect(515, 75, 100, 13))
        self.totalOutput.setStyleSheet("#totalOutput{\n"
"    font-size:16px;\n"
"}")
        self.totalOutput.setObjectName("totalOutput")

        self.PaymentFrame = QtWidgets.QFrame(self.centralwidget)
        self.PaymentFrame.setGeometry(QtCore.QRect(1130, 200, 700, 650))
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
        self.backPushButton.setGeometry(QtCore.QRect(1375, 870, 215, 115))
        self.backPushButton.setStyleSheet("#backPushButton{\n"
"    background-color:none;\n"
"    border:4px solid #0000AF;\n"
"    border-radius:20px;\n"
"    font-family:Montserrat;\n"
"    font-size:20px;\n"
"    color:#fff;\n"
"}")
        self.backPushButton.setObjectName("backPushButton")
         # To call the function PaymentOption to open the page and close the main window
        self.backPushButton.clicked.connect(self.PaymentOption)
        self.backPushButton.clicked.connect(MainWindow.close)

        self.checkOutPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkOutPushButton.setGeometry(QtCore.QRect(1615, 870, 215, 115))
        self.checkOutPushButton.setStyleSheet("#checkOutPushButton{\n"
"    background-color:#0000AF;\n"
"    border-radius:15px;\n"
"    font-size:20px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.checkOutPushButton.setObjectName("checkOutPushButton")
         # To call the function FeedBack to open the page and close the main window
        self.checkOutPushButton.clicked.connect(self.FeedBack)
        self.checkOutPushButton.clicked.connect(MainWindow.close)
        MainWindow.setCentralWidget(self.centralwidget)

        # Call the function to populate the table with scanned products
        self.populateTableWithScannedProducts()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def populateTableWithScannedProducts(self):
        # Get the reference number associated with the logged-in user
        sales_trans = config.transaction_info.get('reference_number')

        # Use the reference number to retrieve scanned products and summary from the database
        query = f"SELECT * FROM dbo.Fn_TransactionReference('{sales_trans}')"
        self.cursor.execute(query)
        scanned_products = self.cursor.fetchall()

        # Retrieve summary information using Fn_TransactionSummary
        summary_data_query = f"SELECT * FROM dbo.Fn_TransactionSummary('{sales_trans}')"
        self.cursor.execute(summary_data_query)

        # Fetch one row, since the summary query is expected to return only one row
        summary_data = self.cursor.fetchone()

        # Check if summary_data is not None before accessing its values
        if summary_data is not None:
            # Update UI elements with summary information
            products_count = summary_data[1]
            total_gross_weight = summary_data[3]
            total_items = summary_data[2]  
            total_price = summary_data[4]  

            # Use a lambda function to update the UI on the main thread
            QtCore.QMetaObject.invokeMethod(self.productsOutput, "setText", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, f"{products_count} Products"))
            QtCore.QMetaObject.invokeMethod(self.grossOutput, "setText", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, f"¥ {total_gross_weight:.2f}"))
            QtCore.QMetaObject.invokeMethod(self.itemsOutput, "setText", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, f"{total_items} Items"))
            QtCore.QMetaObject.invokeMethod(self.totalOutput, "setText", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, f"¥ {total_price:.2f}"))

        # Populate the table with scanned products
        for product in scanned_products:
            product_name = product[7]
            product_weight = product[11]
            product_price = product[12]
            barcode_data = product[13]

            rowPosition = self.productTable.rowCount()
            self.productTable.insertRow(rowPosition)

            item_name = QtWidgets.QTableWidgetItem(product_name)
            item_weight = QtWidgets.QTableWidgetItem(f"{product_weight} grams")
            item_price = QtWidgets.QTableWidgetItem(f"¥ {product_price:.2f}")
            item_barcode = QtWidgets.QTableWidgetItem(barcode_data)

            self.productTable.setItem(rowPosition, 0, item_name)
            self.productTable.setItem(rowPosition, 1, item_weight)
            self.productTable.setItem(rowPosition, 2, item_price)
            self.productTable.setItem(rowPosition, 3, item_barcode)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # Use the stored language from Config
        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

        # Translate texts using the stored language
        self.roleOutput.setText(_translate("MainWindow", translation_dict['Role_Output']))
        self.helpPushButton.setText(_translate("MainWindow", translation_dict['Help_Button']))
        self.checkOutPushButton.setText(_translate("MainWindow", translation_dict['Back_Button']))
        item = self.productTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", translation_dict['Product_Label']))
        item = self.productTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", translation_dict['Detail_Label']))
        item = self.productTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", translation_dict['Price_Label']))
        item = self.productTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", translation_dict['Barcode_Label']))
        self.summaryLabel.setText(_translate("MainWindow", translation_dict['Summary_Label']))
        self.productsLabel.setText(_translate("MainWindow", translation_dict['Total_Products_Label']))
        self.grossLabel.setText(_translate("MainWindow", translation_dict['Total_Gross_Weight']))
        self.itemsLabel.setText(_translate("MainWindow", translation_dict['Total_Items_Label']))
        self.totalLabel.setText(_translate("MainWindow", translation_dict['Total_Price_Label']))
        self.productsOutput.setText(_translate("MainWindow", translation_dict['Total_Products_Output']))
        self.grossOutput.setText(_translate("MainWindow", translation_dict['Total_Gross_Weight_Output']))
        self.itemsOutput.setText(_translate("MainWindow", translation_dict['Total_Items_Output']))
        self.totalOutput.setText(_translate("MainWindow", translation_dict['Total_Price_Output']))
        self.shoppingListLabel.setText(_translate("MainWindow", translation_dict['ShoppingList_Label']))
        self.backPushButton.setText(_translate("MainWindow", translation_dict['Back_Button']))
        self.checkOutPushButton.setText(_translate("MainWindow", translation_dict['Checkout_Button']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowCashPaymentOption()
    ui.setupUiCashPaymentOption(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
