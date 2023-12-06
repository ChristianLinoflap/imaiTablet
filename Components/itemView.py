# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from pyzbar.pyzbar import decode
from PyQt5.QtWidgets import QMessageBox
import pyodbc
import threading
import time

# DataBase Management 
class DatabaseManager:
    def __init__(self, server_name, database_name):
        self.server_name = server_name
        self.database_name = database_name

    def connect(self):
        driver_name = 'SQL Server'
        connection_string = f"DRIVER={{{driver_name}}};SERVER={self.server_name};DATABASE={self.database_name};Trusted_Connection=yes;"
        return pyodbc.connect(connection_string)
    
    def get_product_details_by_barcode(self, cursor, barcode):
        query = "SELECT * FROM cart.dbo.Product WHERE Barcode = ?"
        cursor.execute(query, barcode)
        return cursor.fetchone()
    
class Ui_MainWindowItemView(object):
    # Initializations
    def __init__(self):
        self.db_manager = DatabaseManager(server_name='LF-DEV-0001\SQLEXPRESS', database_name='cart')
        self.conn = self.db_manager.connect()
        self.cursor = self.conn.cursor()
        self.scanning_in_progress = False
        self.scanning_thread = None
        self.last_scan_time = 0
        self.scanned_data = []
        self.search_window_open = False
        self.shopping_list_window_open = False
        self.help_window_open = False
        self.logged_in_user_firstname = ""
        self.logged_in_user_lastname = ""

     # Function to update user information after authentication
    def set_logged_in_user_info(self, firstname, lastname):
        self.logged_in_user_firstname = firstname
        self.logged_in_user_lastname = lastname
        self.update_name_output_label()

    # Function to update the nameOutput label with the logged-in user's name
    def update_name_output_label(self):
        full_name = f"{self.logged_in_user_firstname} {self.logged_in_user_lastname}"
        self.nameOutput.setText(full_name)

    # Function to Call help.py
    def SearchProductOption(self):
        # Close other windows if they are open
        self.close_other_windows("search")

        if not self.search_window_open:
            from search import Ui_MainWindowSearchProduct
            self.window_search = QtWidgets.QMainWindow()
            self.ui_search = Ui_MainWindowSearchProduct()
            self.ui_search.setupUiSearchProduct(self.window_search)
            self.window_search.show()
            # Set the flag to indicate that the window is open
            self.search_window_open = True
        else:
            # Close the window if it's open
            self.window_search.close()
            # Set the flag to indicate that the window is closed
            self.search_window_open = False

    # Function to Call shoppingList.py
    def ShoppingList(self):
        # Close other windows if they are open
        self.close_other_windows("shopping_list")

        if not self.shopping_list_window_open:
            from shoppingList import Ui_MainWindowShoppingList
            self.window_shopping_list = QtWidgets.QMainWindow()
            self.ui_shopping_list = Ui_MainWindowShoppingList()
            self.ui_shopping_list.setupUiShoppingList(self.window_shopping_list)
            self.window_shopping_list.show()
            # Set the flag to indicate that the window is open
            self.shopping_list_window_open = True
        else:
            # Close the window if it's open
            self.window_shopping_list.close()
            # Set the flag to indicate that the window is closed
            self.shopping_list_window_open = False

    # Function to Call help.py
    def HelpOption(self):
        # Close other windows if they are open
        self.close_other_windows("help")

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

    def close_other_windows(self, current_window):
        # Close other windows based on the current window
        if current_window != "search" and self.search_window_open:
            self.window_search.close()
            self.search_window_open = False
        if current_window != "shopping_list" and self.shopping_list_window_open:
            self.window_shopping_list.close()
            self.shopping_list_window_open = False
        if current_window != "help" and self.help_window_open:
            self.window_help.close()
            self.help_window_open = False

    # Function to Call paymentOption.py
    def PaymentOption (self):
        from paymentOption import Ui_MainWindowPaymentOption
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowPaymentOption()
        self.ui.setupUiPaymentOption(self.window)
        self.window.show()

    # Function to Set Up itemView.py
    def setupUiItemView(self, MainWindow):
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
        # To call the function HelpOption to open the page and close the main window
        self.helpPushButton.clicked.connect(self.HelpOption)
        self.shoppingListButton = QtWidgets.QPushButton(self.navigationFrame)
        self.shoppingListButton.setGeometry(QtCore.QRect(910, 30, 101, 41))
        self.shoppingListButton.setStyleSheet("#shoppingListButton{\n"
"    background-color:none;\n"
"    border:none;\n"
"    color:#fff;\n"
"    font-size:16px;\n"
"}")
        self.shoppingListButton.setObjectName("shoppingListButton")
        # To call the function PaymentOption to open the page and close the main window
        self.shoppingListButton.clicked.connect(self.ShoppingList)
        self.searchProductsButton = QtWidgets.QPushButton(self.navigationFrame)
        self.searchProductsButton.setGeometry(QtCore.QRect(700, 30, 131, 41))
        self.searchProductsButton.setStyleSheet("#searchProductsButton{\n"
"    background-color:none;\n"
"    border:none;\n"
"    color:#fff;\n"
"    font-size:16px;\n"
"}")
        self.searchProductsButton.setObjectName("searchProductsButton")
        # To call the function PaymentOption to open the page and close the main window
        self.searchProductsButton.clicked.connect(self.SearchProductOption)
        self.productTable = QtWidgets.QTableWidget(self.centralwidget)
        self.productTable.setGeometry(QtCore.QRect(10, 120, 691, 471))
        self.productTable.setGridStyle(QtCore.Qt.SolidLine)
        self.productTable.setObjectName("productTable")
        self.productTable.setColumnCount(3)
        self.productTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, item)
        self.productTable.setColumnWidth(0, 415)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, item)
        self.productTable.setColumnWidth(1, 125)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, item)
        self.productTable.setColumnWidth(2, 125) 
        # Set the table to read-only
        self.productTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        # Make column headers not movable
        self.productTable.horizontalHeader().setSectionsMovable(False)
        # Set column width and row height to be fixed
        self.productTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.productTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.summaryFrame = QtWidgets.QFrame(self.centralwidget)
        self.summaryFrame.setGeometry(QtCore.QRect(10, 600, 511, 91))
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
        self.grossLabel.setGeometry(QtCore.QRect(160, 40, 71, 16))
        self.grossLabel.setStyleSheet("#grossLabel{\n"
"    font-size:12px;\n"
"    color:#A0A0A0;\n"
"}")
        self.grossLabel.setObjectName("grossLabel")
        self.itemsLabel = QtWidgets.QLabel(self.summaryFrame)
        self.itemsLabel.setGeometry(QtCore.QRect(280, 40, 101, 16))
        self.itemsLabel.setStyleSheet("#itemsLabel{\n"
"    font-size:12px;\n"
"    color:#A0A0A0;\n"
"}")
        self.itemsLabel.setObjectName("itemsLabel")
        self.totalLabel = QtWidgets.QLabel(self.summaryFrame)
        self.totalLabel.setGeometry(QtCore.QRect(425, 40, 61, 16))
        self.totalLabel.setStyleSheet("#totalLabel{\n"
"    font-size:12px;\n"
"    color:#A0A0A0;\n"
"}")
        self.totalLabel.setObjectName("totalLabel")
        self.productsOutput = QtWidgets.QLabel(self.summaryFrame)
        self.productsOutput.setGeometry(QtCore.QRect(10, 55, 51, 16))
        self.productsOutput.setObjectName("productsOutput")
        self.grossOutput = QtWidgets.QLabel(self.summaryFrame)
        self.grossOutput.setGeometry(QtCore.QRect(160, 55, 61, 16))
        self.grossOutput.setObjectName("grossOutput")
        self.itemsOutput = QtWidgets.QLabel(self.summaryFrame)
        self.itemsOutput.setGeometry(QtCore.QRect(280, 55, 47, 13))
        self.itemsOutput.setObjectName("itemsOutput")
        self.totalOutput = QtWidgets.QLabel(self.summaryFrame)
        self.totalOutput.setGeometry(QtCore.QRect(425, 55, 47, 13))
        self.totalOutput.setObjectName("totalOutput")
        self.advertisementFrame = QtWidgets.QFrame(self.centralwidget)
        self.advertisementFrame.setGeometry(QtCore.QRect(730, 120, 451, 471))
        self.advertisementFrame.setStyleSheet("#advertisementFrame{\n"
"    background-color:#FEFCFC;\n"
"}")
        self.advertisementFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.advertisementFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.advertisementFrame.setObjectName("advertisementFrame")
        self.checkOutPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkOutPushButton.setGeometry(QtCore.QRect(1010, 600, 171, 91))
        self.checkOutPushButton.setStyleSheet("#checkOutPushButton{\n"
"    background-color:#0000AF;\n"
"    border-radius:15px;\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.checkOutPushButton.setObjectName("checkOutPushButton")
        # To call the function PaymentOption to open the page and close the main window
        self.checkOutPushButton.clicked.connect(self.PaymentOption)
        self.checkOutPushButton.clicked.connect(MainWindow.close)
        self.scanBarcodePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanBarcodePushButton.setGeometry(QtCore.QRect(530, 600, 175, 91))
        self.scanBarcodePushButton.setStyleSheet("#scanBarcodePushButton{\n"
"    background-color:#0000AF;\n"
"    border-radius:15px;\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.scanBarcodePushButton.setObjectName("scanBarcodePushButton")
        # Connect the scanBarcodeButton to the scanBarcode function
        self.scanBarcodePushButton.clicked.connect(self.scanBarcode)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def scanBarcode(self):
        if not hasattr(self, 'cap') or not self.cap.isOpened():
                # Change the text of scanBarcodePushButton to "Close Scanner"
                self.scanBarcodePushButton.setText("Close Barcode Scanner")
                # Show a message to the user
                QMessageBox.information(None, "Scan Barcode", "Please position the barcode in front of the camera. Click again the button to close the scanner.")
                # Open the camera
                self.cap = cv2.VideoCapture(0)
                # Set scanning flag to True to indicate scanning is in progress
                self.scanning_in_progress = True

                # Start the scanning process in a separate thread
                self.scanning_thread = threading.Thread(target=self.scanBarcodeThread)
                self.scanning_thread.start()
        else:
                # Close the camera
                self.cap.release()
                cv2.destroyAllWindows()

                # Change the text of scanBarcodePushButton to "Close Scanner"
                self.scanBarcodePushButton.setText("Open Barcode Scanner")

                # Show a message that scanning is done
                QMessageBox.information(None, "Scanning Done", "Barcode scanning is complete.")
                
                # Toggle camera state for the next button click
                self.cap_opened = not getattr(self, 'cap_opened', False)

    def scanBarcodeThread(self):
        while self.scanning_in_progress:
            ret, frame = self.cap.read()

            if frame is None:
                break

            barcodes = decode(frame)

            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')

                # Check if enough time has passed since the last scan
                current_time = time.time()
                if current_time - self.last_scan_time > 1.5:
                    self.last_scan_time = current_time
                    self.processScannedBarcode(barcode_data)
                

        # Close the camera
        self.cap.release()
        cv2.destroyAllWindows()
    
    def processScannedBarcode(self, barcode_data):
        product_details = self.db_manager.get_product_details_by_barcode(self.cursor, barcode_data)

        if product_details:
                # Extract relevant information from product_details
                product_name = product_details[2]  
                product_weight = product_details[3]  
                product_price = product_details[4]

                # Add the product details to the productTable
                rowPosition = self.productTable.rowCount()
                self.productTable.insertRow(rowPosition)

                # Set values in the corresponding columns
                item_name = QtWidgets.QTableWidgetItem(product_name)
                # Append "grams" to the details column
                item_weight = QtWidgets.QTableWidgetItem(f"{product_weight} grams")       
                # Append yen symbol to the price column
                item_price = QtWidgets.QTableWidgetItem(f"¥ {product_price:.2f}")

                self.productTable.setItem(rowPosition, 0, item_name)  # Products column
                self.productTable.setItem(rowPosition, 1, item_weight)  # Details column
                self.productTable.setItem(rowPosition, 2, item_price)   # Price column

                self.scanned_data.append({
                        'barcode': barcode_data,
                        'product_name': product_name,
                        'product_weight': product_weight,
                        'product_price': product_price
                })

                self.updateSummaryLabels()
                print(f"Product with barcode {barcode_data} found in the database.")
        else:
                print(f"Product with barcode {barcode_data} not found in the database.")

    def updateSummaryLabels(self):
        # Get the number of unique products
        unique_products = set(self.productTable.item(row, 0).text() for row in range(self.productTable.rowCount()))
        products_count = len(unique_products)

        self.productsOutput.setText(f"{products_count} Products")

        # Calculate total gross weight from the details column
        total_gross_weight = sum(float(item.text().split()[0]) for row in range(self.productTable.rowCount()) for item in [self.productTable.item(row, 1)])
        self.grossOutput.setText(f"{total_gross_weight:.2f} grams")

        # Calculate total number of items
        total_items = self.productTable.rowCount()
        self.itemsOutput.setText(f"{total_items} Items")

        # Calculate total price from the price column
        total_price = sum(float(item.text().split()[1]) for row in range(self.productTable.rowCount()) for item in [self.productTable.item(row, 2)])
        self.totalOutput.setText(f"¥ {total_price:.2f}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameOutput.setText(_translate("MainWindow", "Juan Dela Cruz"))
        self.roleOutput.setText(_translate("MainWindow", "Member"))
        self.helpPushButton.setText(_translate("MainWindow", "Help"))
        self.shoppingListButton.setText(_translate("MainWindow", "Shopping List"))
        self.searchProductsButton.setText(_translate("MainWindow", "Search Products"))
        self.productTable.setSortingEnabled(False)
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
        self.productsOutput.setText(_translate("MainWindow", "0 Products"))
        self.grossOutput.setText(_translate("MainWindow", "0 grams"))
        self.itemsOutput.setText(_translate("MainWindow", "0 Items"))
        self.totalOutput.setText(_translate("MainWindow", "¥ 0.00"))
        self.checkOutPushButton.setText(_translate("MainWindow", "Proceed to Payment"))
        self.scanBarcodePushButton.setText(_translate("MainWindow", "Open Barcode Scanner"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowItemView()
    ui.setupUiItemView(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
