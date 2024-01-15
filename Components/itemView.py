# Standard Python Library Imports
import threading
import subprocess
import os
import time

# Third Party Library Imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import cv2
from pyzbar.pyzbar import decode
from PyQt5.QtWidgets import QMessageBox
import pyodbc
import pygame

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

    # Select Query for Product
    def get_product_details_by_barcode(self, cursor, barcode):
        try:
            query = """
                SELECT * FROM Fn_Products_BranchProducts (?)
            """
            cursor.execute(query, barcode)
            return cursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
            return None

# UI Mainwindow Management
class Ui_MainWindowItemView(object):
    # Initializations
    def __init__(self):
        self.scanning_in_progress = False
        self.scanning_thread = None
        self.last_scan_time = 0
        self.search_window_open = False
        self.shopping_list_window_open = False
        self.help_window_open = False
        pygame.mixer.init()
        self.scan_sound = pygame.mixer.Sound("Assets\\bgSound.mp3")
        # Database connection setup
        self.db_manager = DatabaseManager(
            server_name=db_server_name,
            database_name=db_name,
            username=db_username,
            password=db_password, 
        )
        self.conn = self.db_manager.connect()
        self.cursor = self.conn.cursor()

        # Reference to the classifier process
        self.classifier_process = None

        # Start the classifier when the item view window is opened
        self.startClassifier()

        # Check every 1000 milliseconds (1 second)
        self.predicted_class_timer = QTimer()
        self.predicted_class_timer.timeout.connect(self.checkPredictedClass)
        self.predicted_class_timer.start(1000)  

    def checkPredictedClass(self):
        # Check if the predicted class file exists
        if os.path.exists("predicted_class.txt"):
            # Read the content of the file
            with open("predicted_class.txt", "r") as file:
                predicted_class = file.read().strip()

            # Process the predicted class (barcode) and update the table
            if predicted_class:
                self.processScannedBarcode(predicted_class)

            # Update the file with new details
            with open("predicted_class.txt", "w") as file:
                file.write("new_details")
            
            # Remove the file to avoid reprocessing the same class
            os.remove("predicted_class.txt")

    # Start the classifier process
    def startClassifier(self):
        self.classifier_process = subprocess.Popen(['python', r'Components\classifier.py'])
        
    # Stop the classifier process if running
    def stopClassifier(self):
        if self.classifier_process and self.classifier_process.poll() is None:
            self.classifier_process.terminate()
            self.classifier_process.wait()

    # Function to Call help.py
    def SearchProductOption(self):
        self.close_other_windows("search")

        if not self.search_window_open:
            from search import Ui_MainWindowSearchProduct
            self.window_search = QtWidgets.QMainWindow()
            self.ui_search = Ui_MainWindowSearchProduct()
            self.ui_search.setupUiSearchProduct(self.window_search)
            self.window_search.show()
            self.search_window_open = True
        else:
            self.window_search.close()
            self.search_window_open = False

    # Function to Call shoppingList.py
    def ShoppingList(self):
        self.close_other_windows("shopping_list")

        if not self.shopping_list_window_open:
            from shoppingList import Ui_MainWindowShoppingList
            self.window_shopping_list = QtWidgets.QMainWindow()
            self.ui_shopping_list = Ui_MainWindowShoppingList()
            self.ui_shopping_list.setupUiShoppingList(self.window_shopping_list)
            self.window_shopping_list.show()
            self.shopping_list_window_open = True
        else:
            self.window_shopping_list.close()
            self.shopping_list_window_open = False

    # Function to Call help.py
    def HelpOption(self):
        self.close_other_windows("help")

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

    # Close other windows based on the current window
    def close_other_windows(self, current_window):
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
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
            cv2.destroyAllWindows()
        from paymentOption import Ui_MainWindowPaymentOption
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowPaymentOption()
        self.ui.setupUiPaymentOption(self.window)
        self.window.show()

    # Function to Set Up itemView.py
    def setupUiItemView(self, MainWindow):
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
        # To call the function HelpOption to open the page and close the main window
        self.helpPushButton.clicked.connect(self.HelpOption)

        self.shoppingListButton = QtWidgets.QPushButton(self.navigationFrame)
        self.shoppingListButton.setGeometry(QtCore.QRect(1425, 55, 150, 50))
        self.shoppingListButton.setStyleSheet("#shoppingListButton{\n"
"    background-color:none;\n"
"    border:none;\n"
"    color:#fff;\n"
"    font-size:24px;\n"
"}")
        self.shoppingListButton.setObjectName("shoppingListButton")
        # To call the function PaymentOption to open the page and close the main window
        self.shoppingListButton.clicked.connect(self.ShoppingList)

        self.searchProductsButton = QtWidgets.QPushButton(self.navigationFrame)
        self.searchProductsButton.setGeometry(QtCore.QRect(1125, 55, 150, 50))
        self.searchProductsButton.setStyleSheet("#searchProductsButton{\n"
"    background-color:none;\n"
"    border:none;\n"
"    color:#fff;\n"
"    font-size:24px;\n"
"}")
        self.searchProductsButton.setObjectName("searchProductsButton")
        # To call the function PaymentOption to open the page and close the main window
        self.searchProductsButton.clicked.connect(self.SearchProductOption)

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

        self.advertisementFrame = QtWidgets.QFrame(self.centralwidget)
        self.advertisementFrame.setGeometry(QtCore.QRect(1130, 200, 700, 650))
        self.advertisementFrame.setStyleSheet("#advertisementFrame{\n"
"    background-color:#FEFCFC;\n"
"}")
        self.advertisementFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.advertisementFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.advertisementFrame.setObjectName("advertisementFrame")

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
        # To call the function PaymentOption to open the page and close the main window
        self.checkOutPushButton.clicked.connect(self.PaymentOption)
        self.checkOutPushButton.clicked.connect(MainWindow.close)

        self.scanBarcodePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanBarcodePushButton.setGeometry(QtCore.QRect(840, 870, 215, 115))
        self.scanBarcodePushButton.setStyleSheet("#scanBarcodePushButton{\n"
"    background-color:#F4C430;\n"
"    border-radius:5px;\n"
"    font-size:20px;\n"
"    font-family:Montserrat;\n"
"    color:#000;\n"
"}")
        self.scanBarcodePushButton.setObjectName("scanBarcodePushButton")
        # Connect the scanBarcodeButton to the scanBarcode function
        self.scanBarcodePushButton.clicked.connect(self.scanBarcode)
        MainWindow.setCentralWidget(self.centralwidget)

        self.scan_timer = QTimer()
        self.scan_timer.timeout.connect(self.closeScanner)
        self.scan_timeout = 30000  

        # Call the function to populate the table with scanned products
        self.populateTableWithScannedProducts()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    # Scan Barcode Process
    def scanBarcode(self):
        if not hasattr(self, 'cap') or not self.cap.isOpened():
            # Stop the classifier when the barcode scanner is opened
            self.stopClassifier()
            self.scanBarcodePushButton.setText(translations[Config.current_language]['Close_Barcode_Scanner'])
            QMessageBox.information(None, translations[Config.current_language]['Scan_Barcode_Title'],
                        translations[Config.current_language]['Scan_Barcode_Message'])
            self.cap = cv2.VideoCapture(0)
            self.scanning_in_progress = True
            self.scan_timer.start(self.scan_timeout)
            self.scanning_thread = threading.Thread(target=self.scanBarcodeThread)
            self.scanning_thread.start()
        else:
            self.cap.release()
            cv2.destroyAllWindows()
            self.scanBarcodePushButton.setText(translations[Config.current_language]['Scan_Barcode_Push_Button'])
            if self.scanning_in_progress:
                QMessageBox.information(None, translations[Config.current_language]['Scanning_Done_Title'],
                        translations[Config.current_language]['Scanning_Done_Message'])
            self.scan_timer.stop()
            self.scanning_in_progress = False
            # Start the classifier when the barcode scanner is closed
            self.startClassifier()  

    # Decode Barcode 
    def scanBarcodeThread(self):
        try:
            while self.scanning_in_progress:
                ret, frame = self.cap.read()
                if frame is None:
                    break
                barcodes = decode(frame)
                for barcode in barcodes:
                    barcode_data = barcode.data.decode('utf-8')
                    current_time = time.time()
                    if current_time - self.last_scan_time > 1:
                        self.last_scan_time = current_time
                        self.processScannedBarcode(barcode_data)
                        
            self.cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"An unexpected error occurred during barcode scanning: {e}")
            self.cap.release()
            cv2.destroyAllWindows()

    # Proccess Decoded Barcode
    def processScannedBarcode(self, barcode_data):
        product_details = self.db_manager.get_product_details_by_barcode(self.cursor, barcode_data)
        if product_details:
                # Extract relevant information from product_details
                product_id = product_details[0]
                product_name = product_details[1]  
                product_weight = product_details[7]  
                product_price = product_details[-1] 

                existing_product = self.checkProductInShoppingList(product_id)
                if existing_product:
                    # Product exists in the ShoppingListDetail table, update CartQuantity
                    self.updateCartQuantity(product_id)
                    print(f"CartQuantity updated for ProductId {product_id}.")
                else:
                    # Product not in the ShoppingListDetail table, perform other actions if needed
                    print(f"Product with ProductId {product_id} not found in the ShoppingListDetail table.")

                # Add the product details to the productTable
                rowPosition = self.productTable.rowCount()
                self.productTable.insertRow(rowPosition)

                # Set values in the corresponding columns
                item_name = QtWidgets.QTableWidgetItem(product_name)
                # Append "grams" to the details column
                item_weight = QtWidgets.QTableWidgetItem(f"{product_weight} grams")       
                # Append yen symbol to the price column
                item_price = QtWidgets.QTableWidgetItem(f"¥ {product_price:.2f}")
                # Set barcode data to the barcode column
                item_barcode = QtWidgets.QTableWidgetItem(barcode_data)

                sales_trans = config.transaction_info.get('reference_number')
                self.saveTransactionDetail(product_name, product_weight, product_price, barcode_data, sales_trans)
            
                self.productTable.setItem(rowPosition, 0, item_name)  
                self.productTable.setItem(rowPosition, 1, item_weight)
                self.productTable.setItem(rowPosition, 2, item_price) 
                self.productTable.setItem(rowPosition, 3, item_barcode) 

                self.scan_sound.play()
                self.updateSummaryLabels()

                print(f"Product with barcode {barcode_data} found in the database.")
        else:
                print(f"Product with barcode {barcode_data} not found in the database.")
    
    # Check if the product exists in the ShoppingListDetail table
    def checkProductInShoppingList(self, product_id):
        query = "SELECT TOP 1 * FROM ShoppingListDetail WHERE ProductId = ?"
        self.cursor.execute(query, product_id)
        return self.cursor.fetchone()

    def updateCartQuantity(self, product_id):
        # Get the current CartQuantity from ShoppingListDetail
        query_select = "SELECT CartQuantity FROM ShoppingListDetail WHERE ProductId = ?"
        self.cursor.execute(query_select, product_id)
        current_cart_quantity = self.cursor.fetchone()[0]

        # Call the stored procedure to update CartQuantity
        query_update = "UPDATE ShoppingListDetail SET CartQuantity = ? WHERE ProductId = ?"
        new_cart_quantity = current_cart_quantity + 1  # Update CartQuantity as needed
        self.cursor.execute(query_update, new_cart_quantity, product_id)
        self.conn.commit()

    def saveTransactionDetail(self, item_name, item_weight, item_price, item_barcode, sales_trans):
        try:
            # Call the stored procedure using the pyodbc connection
            self.cursor.execute(
                "{CALL sp_SaveTransDetail (?, ?, ?, ?, ?)}",
                item_name, item_weight, item_price, item_barcode, sales_trans
            )
            self.conn.commit()
            print(f"Transaction details for {item_name} saved successfully.")
        except pyodbc.Error as e:
            print(f"Error executing the stored procedure: {e}")
            self.conn.rollback()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            self.conn.rollback()

    def closeScanner(self):
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
            cv2.destroyAllWindows()
            self.scanBarcodePushButton.setText(translations[Config.current_language]['Scan_Barcode_Push_Button'])
            if self.scanning_in_progress:
                QMessageBox.information(None, translations[Config.current_language]['Scanner_Closed_Title'],
                        translations[Config.current_language]['Scanner_Closed_Message'])
            self.scanning_in_progress = False
            self.scan_timer.stop()
    
    def populateTableWithScannedProducts(self):
        # Retrieve Reference Number
        sales_trans = config.transaction_info.get('reference_number')

        # Retrive Transaction Reference
        query = f"SELECT * FROM dbo.Fn_TransactionReference('{sales_trans}')"
        self.cursor.execute(query)
        scanned_products = self.cursor.fetchall()

        # Retrieve Transaction Sumamry
        summary_data_query = f"SELECT * FROM dbo.Fn_TransactionSummary('{sales_trans}')"
        self.cursor.execute(summary_data_query)

        # Fetch one row, expected to return one row
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

        # Use the stored language from Config
        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

        # Translate texts using the stored language
        self.roleOutput.setText(_translate("MainWindow", translation_dict['Role_Output']))
        self.helpPushButton.setText(_translate("MainWindow", translation_dict['Help_Button']))
        self.shoppingListButton.setText(_translate("MainWindow", translation_dict['Shopping_List_Button']))
        self.searchProductsButton.setText(_translate("MainWindow", translation_dict['Search_Products_Button']))
        self.productTable.setSortingEnabled(False)
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
        self.checkOutPushButton.setText(_translate("MainWindow", translation_dict['Checkout_Button']))
        self.checkOutPushButton.setText(_translate("MainWindow", translation_dict['Payment_Button']))
        self.scanBarcodePushButton.setText(_translate("MainWindow", translation_dict['Scan_Barcode_Push_Button']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowItemView()
    ui.setupUiItemView(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
