# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc

# Module Imports
from config import db_server_name, db_name, db_username, db_password
from config import user_info

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

class Ui_MainWindowShoppingList(object):
     # Initializations
    def __init__(self):
        # Database connection setup
        self.db_manager = DatabaseManager(
            server_name=db_server_name,
            database_name=db_name,
            username=db_username,
            password=db_password
        )
        self.conn = self.db_manager.connect()
        self.cursor = self.conn.cursor()
    
    # Function to populate shopping list items in the listWidget
    def populateShoppingList(self):
        user_client_id = user_info.get('user_client_id')  
        query = f"SELECT Name, Quantity, CartQuantity FROM dbo.vw_ProductShoppingListDetail WHERE UserClientID = {user_client_id}"

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()

            for item in result:
                name, quantity, cart_quantity = item.Name, item.Quantity, item.CartQuantity
                item_widget = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout(item_widget)

                checkbox = QtWidgets.QCheckBox()
                checkbox.setChecked(cart_quantity >= quantity)  # Automatically check if CartQuantity >= Quantity
                checkbox.setDisabled(True)
                layout.addWidget(checkbox)

                label = QtWidgets.QLabel(f"{name} - {quantity}")
                layout.addWidget(label)

                listWidgetItem = QtWidgets.QListWidgetItem()
                listWidgetItem.setSizeHint(item_widget.sizeHint())
                self.listWidget.addItem(listWidgetItem)
                self.listWidget.setItemWidget(listWidgetItem, item_widget)

        except pyodbc.Error as e:
            print(f"Error fetching shopping list items: {e}")

    # Function to Call ItemView.py
    def ItemView(self):
        from itemView import Ui_MainWindowItemView
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowItemView()
        self.ui.setupUiItemView(self.window)
        self.window.show()

    def setupUiShoppingList(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 575)
        MainWindow.move(1520, 150)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#0000AF;\n"
"}")
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shoppingListFrame = QtWidgets.QFrame(self.centralwidget)
        self.shoppingListFrame.setGeometry(QtCore.QRect(20, 30, 361, 471))
        self.shoppingListFrame.setStyleSheet("#shoppingListFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:25px;\n"
"}")
        self.shoppingListFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shoppingListFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shoppingListFrame.setObjectName("shoppingListFrame")
        self.listWidget = QtWidgets.QListWidget(self.shoppingListFrame)
        self.listWidget.setGeometry(QtCore.QRect(25, 11, 311, 441))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Call the function to populate the shopping list items
        self.populateShoppingList()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowShoppingList()
    ui.setupUiShoppingList(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
