# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QGraphicsDropShadowEffect

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
        self.backPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPushButton.setGeometry(QtCore.QRect(20, 500, 81, 51))
        self.backPushButton.setStyleSheet("#backPushButton{\n"
"    background-color:#ffcc00;\n"
"    border-radius:15px;\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"    color:#000;\n"
"}")
        self.backPushButton.setObjectName("backPushButton")
        # To call the function ItemView to open the page and close the main window
        # self.backPushButton.clicked.connect(self.ItemView)
        self.backPushButton.clicked.connect(MainWindow.close)
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
        self.backPushButton.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowShoppingList()
    ui.setupUiShoppingList(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
