# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowShoppingList(object):
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
        MainWindow.move(1160, 266)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#0000AF;\n"
"}")
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shoppingListFrame = QtWidgets.QFrame(self.centralwidget)
        self.shoppingListFrame.setGeometry(QtCore.QRect(19, 20, 361, 471))
        self.shoppingListFrame.setStyleSheet("#shoppingListFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:25px;\n"
"}")
        self.shoppingListFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shoppingListFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shoppingListFrame.setObjectName("shoppingListFrame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
