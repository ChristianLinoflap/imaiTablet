# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc

class DatabaseManager:
    def __init__(self, server_name, database_name):
        self.server_name = server_name
        self.database_name = database_name

    def connect(self):
        driver_name = 'SQL Server'
        connection_string = f"DRIVER={{{driver_name}}};SERVER={self.server_name};DATABASE={self.database_name};Trusted_Connection=yes;"
        return pyodbc.connect(connection_string)

    def search_products(self, cursor, keyword):
        query = "SELECT * FROM cart.dbo.Product WHERE ProductName LIKE ?"
        cursor.execute(query, f"%{keyword}%")
        return cursor.fetchall()
    
class Ui_MainWindowSearchProduct(object):
    def __init__(self):
        # Create an instance of DatabaseManager
        self.db_manager = DatabaseManager(server_name='LF-DEV-0001\SQLEXPRESS', database_name='cart')

    # Function to Call ItemView.py
    def ItemView(self):
        from itemView import Ui_MainWindowItemView
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowItemView()
        self.ui.setupUiItemView(self.window)
        self.window.show() 

    # Function to Set Up help.py
    def setupUiSearchProduct(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 350)
        MainWindow.move(360, 266)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#0000AF;\n"
"}")
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLineEdit.setGeometry(QtCore.QRect(20, 20, 351, 41))
        self.searchLineEdit.setStyleSheet("#searchLineEdit{\n"
"    border-radius:15px;\n"
"    padding:10px;\n"
"    font-size:16px;\n"
"}")
        self.searchLineEdit.setObjectName("searchLineEdit")
        # Connect the searchLineEdit to the search function
        self.searchLineEdit.textChanged.connect(self.search_products)
        # Don't forget to close the cursor and connection when you're done
        MainWindow.destroyed.connect(self.close_database_connection)
        self.searchTable = QtWidgets.QTableWidget(self.centralwidget)
        self.searchTable.setGeometry(QtCore.QRect(20, 80, 681, 250))
        self.searchTable.setObjectName("searchTable")
        self.searchTable.setColumnCount(4)
        self.searchTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(0, item)
        self.searchTable.setColumnWidth(0, 300)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(1, item)
        self.searchTable.setColumnWidth(1, 125)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(2, item)
        self.searchTable.setColumnWidth(2, 125)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(3, item)
        self.searchTable.setColumnWidth(3, 125)
        # Set the table to read-only
        self.searchTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        # Make column headers not movable
        self.searchTable.horizontalHeader().setSectionsMovable(False)
        # Set column width and row height to be fixed
        self.searchTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.searchTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.advertisementFrame = QtWidgets.QFrame(self.centralwidget)
        self.advertisementFrame.setGeometry(QtCore.QRect(720, 20, 461, 311))
        self.advertisementFrame.setStyleSheet("#advertisementFrame{\n"
"    background-color:#FEFCFC;\n"
"}")
        self.advertisementFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.advertisementFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.advertisementFrame.setObjectName("advertisementFrame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def search_products(self):
        keyword = self.searchLineEdit.text()
        # Connect to the database
        connection = self.db_manager.connect()
        # Create a cursor for executing queries
        cursor = connection.cursor()
        # Search for products based on the keyword
        search_result = self.db_manager.search_products(cursor, keyword)
        # Populate the search table with the search result
        self.populate_search_table(search_result)
        # Close the cursor and connection
        cursor.close()
        connection.close()
    
    def populate_search_table(self, products):
        self.searchTable.setRowCount(len(products))
        for row, product in enumerate(products):
            _, _, product_name, product_weight, product_price = product

            # Set the product details directly to the searchTable
            self.searchTable.setItem(row, 0, QtWidgets.QTableWidgetItem(product_name))  # Product Name column
            self.searchTable.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{product_weight}"))  # Details column
            self.searchTable.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{product_price}"))   # Price column

    def close_database_connection(self):
        # Close the database connection when the main window is closed
        pass  # You can add code here to close the database connection

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchLineEdit.setPlaceholderText(_translate("MainWindow", "Search Product..."))
        item = self.searchTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.searchTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Details"))
        item = self.searchTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.searchTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowSearchProduct()
    ui.setupUiSearchProduct(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
