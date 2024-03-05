# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
from databaseManager import DatabaseManager, EnvironmentLoader
from config import Config, translations
from onScreenKeyboard import OnScreenKeyboard

class Ui_MainWindowSearchProduct(object):
    def __init__(self):
        self.db_manager = DatabaseManager(*EnvironmentLoader.load_env_variables())
        self.conn = self.db_manager.connect()
        self.cursor = self.conn.cursor()
        self.keyboard = OnScreenKeyboard()

    # Function to Set Up help.py
    def setupUiSearchProduct(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 380)
        MainWindow.move(0, 110)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#0000AF;\n"
"}")
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLineEdit.setGeometry(QtCore.QRect(20, 20, 351, 60))
        self.searchLineEdit.setStyleSheet("#searchLineEdit{\n"
"    border-radius:15px;\n"
"    padding:10px;\n"
"    font-size:18px;\n"
"}")
        self.searchLineEdit.setObjectName("searchLineEdit")
        # Connect the searchLineEdit to the search function
        self.searchLineEdit.textChanged.connect(self.search_products)
        self.searchLineEdit.setReadOnly(True)
        self.searchLineEdit.mousePressEvent = self.show_keyboard_for_search
        self.searchTable = QtWidgets.QTableWidget(self.centralwidget)
        self.searchTable.setGeometry(QtCore.QRect(20, 100, 750, 260))
        self.searchTable.setObjectName("searchTable")
        self.searchTable.setColumnCount(3)
        self.searchTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(0, item)
        self.searchTable.setColumnWidth(0, 497)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(1, item)
        self.searchTable.setColumnWidth(1, 125)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(2, item)
        self.searchTable.setColumnWidth(2, 125)
        # Set the table to read-only
        self.searchTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        # Make column headers not movable
        self.searchTable.horizontalHeader().setSectionsMovable(False)
        # Set column width and row height to be fixed
        self.searchTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.searchTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.searchTable.verticalHeader().setVisible(False)
        self.advertisementFrame = QtWidgets.QFrame(self.centralwidget)
        self.advertisementFrame.setGeometry(QtCore.QRect(805, 20, 450, 340))
        self.advertisementFrame.setStyleSheet("#advertisementFrame{\n"
"    background-color:#FEFCFC;\n"
"}")
        self.advertisementFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.advertisementFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.advertisementFrame.setObjectName("advertisementFrame")
        data_font = QtGui.QFont()
        header_font = QtGui.QFont()
        data_font.setPointSize(16)
        header_font.setPointSize(16)
        self.searchTable.setFont(data_font)
        header_stylesheet = "QHeaderView::section { font-size: 16px; }"
        self.searchTable.horizontalHeader().setStyleSheet(header_stylesheet)

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.mousePressEvent = self.hide_keyboard_on_mouse_click

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
    
    def show_keyboard_for_search(self, event):
        self.keyboard.text_input = self.searchLineEdit
        self.keyboard.raise_()
        self.keyboard.show()
    
    def hide_keyboard_on_mouse_click(self, event):
        # Hide the keyboard if it's visible
        if self.keyboard.isVisible():
            self.keyboard.close()
    
    def search_products(self):
        search_text = self.searchLineEdit.text()

        if not search_text:
            # If search text is empty, clear the table and return
            self.searchTable.setRowCount(0)
            return

        # If search text is not empty, proceed with searching products
        self.searchTable.setRowCount(0)

        search_results = self.db_manager.search_products(self.cursor, search_text)

        if search_results:
            for row_num, result in enumerate(search_results):
                self.searchTable.insertRow(row_num)
                for col_num, value in enumerate(result):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    if col_num == 0:
                        self.searchTable.setItem(row_num, 0, item)
                    elif col_num == 1:
                        self.searchTable.setItem(row_num, 1, item)
                    elif col_num == 2:
                        item.setText(f"¥ {value}")
                        self.searchTable.setItem(row_num, 2, item)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # Use the stored language from Config
        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

        # Translate texts using the stored language
        self.searchLineEdit.setPlaceholderText(_translate("MainWindow", translation_dict['Search_Line_Edit']))
        self.searchTable.setSortingEnabled(False)
        item = self.searchTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", translation_dict['Product_Label']))
        item = self.searchTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", translation_dict['Detail_Label']))
        item = self.searchTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", translation_dict['Price_Label']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowSearchProduct()
    ui.setupUiSearchProduct(MainWindow)
    MainWindow.close = ui.hide_keyboard_on_mouse_click
    ui.show_keyboard_for_search(None) 
    MainWindow.show()
    sys.exit(app.exec_())
