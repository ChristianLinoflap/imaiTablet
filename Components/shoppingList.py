# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
from config import user_info
from databaseManager import DatabaseManager, EnvironmentLoader

class Ui_MainWindowShoppingList(object): 
    def populateShoppingList(self):
        user_client_id = user_info.get('user_client_id')

        if not hasattr(self, 'db_manager') or not self.db_manager:
            self.db_manager = DatabaseManager(*EnvironmentLoader.load_env_variables())
            self.conn = self.db_manager.connect()
            self.cursor = self.conn.cursor()

        shopping_list = self.db_manager.populate_shopping_list(self.cursor, user_client_id)

        if shopping_list:
            for item in shopping_list:
                # Extract item details
                name, quantity, cart_quantity = item["name"], item["quantity"], item["cart_quantity"]

                # Create a QWidget for the item
                item_widget = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout(item_widget)
                # Set layout spacing
                layout.setSpacing(10)

                # Create a checkbox for the item
                checkbox = QtWidgets.QCheckBox()
                checkbox.setChecked(cart_quantity >= quantity)
                checkbox.setDisabled(True)
                checkbox.setStyleSheet("QCheckBox { color: #333; }")
                layout.addWidget(checkbox)

                # Create a QLabel for the item name and quantity
                label = QtWidgets.QLabel(f"<b>{name}</b> - {quantity}")
                label.setWordWrap(False)

                # Customize styles based on completion status
                if cart_quantity >= quantity:
                    label.setStyleSheet("QLabel { color: #888; font-size: 14px; }")  # Grayed out for completed items
                else:
                    label.setStyleSheet("QLabel { color: #000; font-size: 14px; }")  # Black for incomplete items

                layout.addWidget(label)

                # Set layout properties
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                item_widget.setLayout(layout)

                # Set minimum height for the item widget
                item_widget.setMinimumHeight(40)

                # Create a QListWidgetItem and add it to the listWidget
                listWidgetItem = QtWidgets.QListWidgetItem()
                listWidgetItem.setSizeHint(item_widget.sizeHint())
                
                # Make items not selectable
                listWidgetItem.setFlags(listWidgetItem.flags() & ~QtCore.Qt.ItemIsSelectable)

                self.listWidget.addItem(listWidgetItem)
                self.listWidget.setItemWidget(listWidgetItem, item_widget)

    # Function to Call ItemView.py
    def ItemView(self):
        from itemView import Ui_MainWindowItemView
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowItemView()
        self.ui.setupUiItemView(self.window)
        self.window.show()

    def setupUiShoppingList(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 450)
        MainWindow.move(880, 110)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#0000AF;\n"
"}")
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shoppingListFrame = QtWidgets.QFrame(self.centralwidget)
        self.shoppingListFrame.setGeometry(QtCore.QRect(25, 25, 350, 400))
        self.shoppingListFrame.setStyleSheet("#shoppingListFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:25px;\n"
"}")
        self.shoppingListFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shoppingListFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shoppingListFrame.setObjectName("shoppingListFrame")
        self.listWidget = QtWidgets.QListWidget(self.shoppingListFrame)
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setGeometry(QtCore.QRect(25, 11, 311, 350))
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
    ui.db_manager = DatabaseManager(*EnvironmentLoader.load_env_variables())
    ui.conn = ui.db_manager.connect()
    ui.cursor = ui.conn.cursor()
    ui.setupUiShoppingList(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
