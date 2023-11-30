# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
import pypyodbc as odbc
from pyzbar.pyzbar import decode

class BarcodeScanner:
    def __init__(self, ui):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)
        self.camera_on = True
        self.scan_barcode()
        self.cursor = None
        self.ui = ui

    def scan_barcode(self):
        success, frame = self.cap.read()
        if success and self.camera_on:
            for code in decode(frame):
                self.cursor.execute(f"SELECT * FROM [cart].[dbo].[Product] WHERE Barcode='{code.data.decode('utf-8')}'")
                rows = self.cursor.fetchall()
                for row in rows:
                    image = row[1]
                    name = row[2]
                    weight = row[3]  
                    price = row[4]  
                    self.ui.add_card(image,name,weight,price)
            if self.camera_on:
                QtCore.QTimer.singleShot(1, self.scan_barcode)
        else:
            self.cap.release()
            cv2.destroyAllWindows()

    def stop_scan(self):
        self.camera_on = False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.scanner = BarcodeScanner(self)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 600)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.card_frames = []
        self.card_counter = 0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.item_frame = QtWidgets.QFrame(self.centralwidget)
        self.item_frame.setStyleSheet("\n"
"background-color: rgb(255, 255, 0);")
        self.item_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.item_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.item_frame.setObjectName("item_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.item_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1010, 481))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.card_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.card_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.card_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card_frame.setObjectName("card1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.card_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.productImage = QtWidgets.QLabel(self.card_frame)
        self.productImage.setMaximumSize(QtCore.QSize(100, 100))
        self.productImage.setText("")
        self.productImage.setPixmap(QtGui.QPixmap("../../milo.png"))
        self.productImage.setScaledContents(True)
        self.productImage.setObjectName("productImage")
        self.horizontalLayout.addWidget(self.productImage)
        self.frame_8 = QtWidgets.QFrame(self.card_frame)
        self.frame_8.setMaximumSize(QtCore.QSize(200, 70))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.product_label = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.product_label.setFont(font)
        self.product_label.setObjectName("product_label")
        self.verticalLayout_2.addWidget(self.product_label)
        self.product_weight = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.product_weight.setFont(font)
        self.product_weight.setObjectName("product_weight")
        self.verticalLayout_2.addWidget(self.product_weight)
        self.horizontalLayout.addWidget(self.frame_8)
        self.price_label = QtWidgets.QLabel(self.card_frame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.price_label.setFont(font)
        self.price_label.setObjectName("price_label")
        self.horizontalLayout.addWidget(self.price_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.quantity_label = QtWidgets.QLabel(self.card_frame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.quantity_label.setFont(font)
        self.quantity_label.setObjectName("quantity_label")
        self.horizontalLayout.addWidget(self.quantity_label, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.quantity_frame = QtWidgets.QFrame(self.card_frame)
        self.quantity_frame.setMaximumSize(QtCore.QSize(50, 50))
        self.quantity_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.quantity_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.quantity_frame.setObjectName("quantity_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.quantity_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.increase_button = QtWidgets.QPushButton(self.quantity_frame)
        self.increase_button.setObjectName("increase_button")
        self.verticalLayout_3.addWidget(self.increase_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.decreas_button = QtWidgets.QPushButton(self.quantity_frame)
        self.decreas_button.setObjectName("decreas_button")
        self.verticalLayout_3.addWidget(self.decreas_button, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.quantity_frame)
        self.removeCart = QtWidgets.QPushButton(self.card_frame)
        self.removeCart.setObjectName("removeCart")
        self.horizontalLayout.addWidget(self.removeCart)
        self.verticalLayout_5.addWidget(self.card_frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_4.addWidget(self.item_frame)
        self.frame_18 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_18.setMaximumSize(QtCore.QSize(100, 100))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_15.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_15.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 0, 0, 1, 1)
        self.pushButton_15.clicked.connect(self.add_card)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_2.setStyleSheet("background-color: rgb(59, 151, 237);")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_18)
        self.verticalLayout.addWidget(self.item_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       

    def add_card(self,product_image,product_name,product_weight,product_price):
        self.card_counter += 1
        card_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        card_frame.setObjectName(f"card_{self.card_counter}")
        card_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        card_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        card_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        card_frame.setObjectName("card_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(card_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.productImage = QtWidgets.QLabel(card_frame)
        self.productImage.setMaximumSize(QtCore.QSize(100, 100))
        self.productImage.setText("")
        self.image_url = f"{product_image}"
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(requests.get(self.image_url).content)
        self.productImage.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.productImage.setScaledContents(True)
        self.productImage.setObjectName("productImage")
        self.horizontalLayout.addWidget(self.productImage)
        self.frame_8 = QtWidgets.QFrame(card_frame)
        self.frame_8.setMaximumSize(QtCore.QSize(200, 70))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.product_label = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.product_label.setFont(font)
        self.product_label.setObjectName("product_label")
        self.verticalLayout_2.addWidget(self.product_label)
        self.product_weight = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.product_weight.setFont(font)
        self.product_weight.setObjectName("product_weight")
        self.verticalLayout_2.addWidget(self.product_weight)
        self.horizontalLayout.addWidget(self.frame_8)
        self.price_label = QtWidgets.QLabel(card_frame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.price_label.setFont(font)
        self.price_label.setObjectName("price_label")
        self.horizontalLayout.addWidget(self.price_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.quantity_label = QtWidgets.QLabel(card_frame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.quantity_label.setFont(font)
        self.quantity_label.setObjectName("quantity_label")
        self.horizontalLayout.addWidget(self.quantity_label, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.quantity_frame = QtWidgets.QFrame(card_frame)
        self.quantity_frame.setMaximumSize(QtCore.QSize(50, 50))
        self.quantity_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.quantity_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.quantity_frame.setObjectName("quantity_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.quantity_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.increase_button = QtWidgets.QPushButton(self.quantity_frame)
        self.increase_button.setObjectName("increase_button")
        self.verticalLayout_3.addWidget(self.increase_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.decreas_button = QtWidgets.QPushButton(self.quantity_frame)
        self.decreas_button.setObjectName("decreas_button")
        self.verticalLayout_3.addWidget(self.decreas_button, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.quantity_frame)
        self.removeCart = QtWidgets.QPushButton(card_frame)
        self.removeCart.setObjectName("removeCart")
        self.card_frames.append(card_frame)
        self.horizontalLayout.addWidget(self.removeCart)
        self.verticalLayout_5.addWidget(card_frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        _translate = QtCore.QCoreApplication.translate
        self.product_label.setText(_translate("MainWindow", f"{product_name}"))
        self.product_weight.setText(_translate("MainWindow", f"netweight: {product_weight}"))
        self.price_label.setText(_translate("MainWindow", f"₱{product_price}"))
        self.quantity_label.setText(_translate("MainWindow", "QTY: 1"))
        self.increase_button.setText(_translate("MainWindow", "^"))
        self.decreas_button.setText(_translate("MainWindow", "v"))
        self.removeCart.setText(_translate("MainWindow", "REMOVE"))
        self.removeCart.clicked.connect(lambda: self.remove_card(card_frame))

    def remove_card(self, card_frame):
        self.verticalLayout_4.removeWidget(card_frame)
        card_frame.deleteLater()
        self.card_frames.remove(card_frame)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_15.setText(_translate("MainWindow", "ADD"))
        self.pushButton_2.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    DRIVER_NAME = 'SQL Server'
    SERVER_NAME = 'LF-DEV-0001\SQLEXPRESS'  # Replace this with your server name
    DATABASE_NAME = 'cart'  # Replace this with your database name
    connection_string = f"DRIVER={{{DRIVER_NAME}}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trusted_Connection=yes;"
    conn = odbc.connect(connection_string)
    ui.scanner.cursor = conn.cursor()

    MainWindow.show()
    sys.exit(app.exec_())
