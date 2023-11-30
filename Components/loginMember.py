# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pyodbc

# DataBase Management 
class DatabaseManager:
    def __init__(self, server_name, database_name):
        self.server_name = server_name
        self.database_name = database_name

    def connect(self):
        driver_name = 'SQL Server'
        connection_string = f"DRIVER={{{driver_name}}};SERVER={self.server_name};DATABASE={self.database_name};Trusted_Connection=yes;"
        return pyodbc.connect(connection_string)

    def authenticate_user(self, cursor, username, password):
        query = "SELECT * FROM users.Login WHERE user_name = ? AND password = ?"
        cursor.execute(query, username, password)
        return cursor.fetchone()

class Ui_MainWindowLogInMember(object):
    # Function to Call tutorialMember.py
    def TutorialMember(self):
        from tutorialMember import Ui_MainWindowTutorialMember
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowTutorialMember()
        self.ui.setupUiTutorialMember(self.window)
        self.window.show()  

    # Function to Call tutorialMember.py
    def LogInOption (self):
        from loginOption import Ui_MainWindowLogInOption
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowLogInOption()
        self.ui.setupUiLogInOption(self.window)
        self.window.show()  

    # Function to Set Up loginMember.py
    def setupUiLogInMember(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(170, 110, 301, 41))
        self.welcomeLabel.setStyleSheet("#welcomeLabel{\n"
"    font-size:36px;\n"
"    font-family:Montserrat;\n"
"    \n"
"}")
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.secondaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.secondaryLabel.setGeometry(QtCore.QRect(240, 150, 151, 31))
        self.secondaryLabel.setStyleSheet("#secondaryLabel{\n"
"    font-size:20px;\n"
"    font-family:Montserrat;\n"
"}")
        self.secondaryLabel.setObjectName("secondaryLabel")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(150, 230, 61, 16))
        self.emailLabel.setStyleSheet("#emailLabel{\n"
"    font-size:20px;\n"
"    font-family:Montserrat;\n"
"}")
        self.emailLabel.setObjectName("emailLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(150, 350, 91, 16))
        self.passwordLabel.setStyleSheet("#passwordLabel{\n"
"    font-size:20px;\n"
"    font-family:Montserrat;\n"
"}")
        self.passwordLabel.setObjectName("passwordLabel")
        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLineEdit.setGeometry(QtCore.QRect(140, 260, 350, 45))
        self.emailLineEdit.setStyleSheet("#emailLineEdit{\n"
"    border-radius:10px;\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"    padding:10px;\n"
"}")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setGeometry(QtCore.QRect(140, 380, 350, 45))
        self.passwordLineEdit.setStyleSheet("#passwordLineEdit{\n"
"    border-radius:10px;\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"    padding:10px;\n"
"}")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginPushButton.setGeometry(QtCore.QRect(140, 490, 350, 45))
        self.loginPushButton.setStyleSheet("#loginPushButton{\n"
"    background-color:#0000AF;\n"
"    border-radius:20px;\n"
"    font-family:Montserrat;\n"
"    font-size:20px;\n"
"    color:#fff\n"
"}")
        self.loginPushButton.setObjectName("loginPushButton")
        self.backPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPushButton.setGeometry(QtCore.QRect(140, 550, 350, 45))
        self.backPushButton.setStyleSheet("#backPushButton{\n"
"    background-color:none;\n"
"    border:4px solid #0000AF;\n"
"    border-radius:20px;\n"
"    font-family:Montserrat;\n"
"    font-size:20px;\n"
"    color:#fff;\n"
"}")
        self.backPushButton.setObjectName("backPushButton")
        self.backPushButton.clicked.connect(self.LogInOption)
        self.backPushButton.clicked.connect(MainWindow.close)
        self.qrFrame = QtWidgets.QFrame(self.centralwidget)
        self.qrFrame.setGeometry(QtCore.QRect(730, 160, 300, 300))
        self.qrFrame.setStyleSheet("#qrFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:25px;\n"
"}")
        self.qrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qrFrame.setObjectName("qrFrame")
        self.qrLabel = QtWidgets.QLabel(self.centralwidget)
        self.qrLabel.setGeometry(QtCore.QRect(720, 490, 331, 51))
        self.qrLabel.setStyleSheet("#qrLabel{\n"
"    font-size:36px;\n"
"    font-family:Montserrat;\n"
"}")
        self.qrLabel.setObjectName("qrLabel")
        self.scanLabelFrame = QtWidgets.QFrame(self.centralwidget)
        self.scanLabelFrame.setGeometry(QtCore.QRect(760, 540, 241, 64))
        self.scanLabelFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scanLabelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scanLabelFrame.setObjectName("scanLabelFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scanLabelFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scanLabel = QtWidgets.QLabel(self.scanLabelFrame)
        self.scanLabel.setStyleSheet("#scanLabel{\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"}")
        self.scanLabel.setObjectName("scanLabel")
        self.verticalLayout.addWidget(self.scanLabel)
        self.scanLabel_2 = QtWidgets.QLabel(self.scanLabelFrame)
        self.scanLabel_2.setStyleSheet("#scanLabel_2{\n"
"    font-size:16px;\n"
"    font-family:Montserrat;\n"
"}")
        self.scanLabel_2.setObjectName("scanLabel_2")
        self.verticalLayout.addWidget(self.scanLabel_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Database connection setup
        self.db_manager = DatabaseManager(server_name='LF-DEV-0001\SQLEXPRESS', database_name='cart')
        self.conn = self.db_manager.connect()
        self.cursor = self.conn.cursor()

        self.loginPushButton.clicked.connect(self.authenticate_user)

    # User Authentication Function
    def authenticate_user(self):
        entered_username = self.emailLineEdit.text()
        entered_password = self.passwordLineEdit.text()

        if not entered_username or not entered_password:
            self.show_input_required_alert()
            return

        result = self.db_manager.authenticate_user(self.cursor, entered_username, entered_password)
        
        if result:
            print("Login successful!")
            self.TutorialMember()
            
        else:
            print("Invalid username or password.")
            self.show_invalid_login_alert()

    # Closes the Database Connection
    def closeEvent(self, event):
        self.cursor.close()
        self.conn.close()

    # Error Validation
    def show_invalid_login_alert(self):
        self.show_alert("Invalid username or password.", "Login Failed")

    def show_input_required_alert(self):
        self.show_alert("Please enter username and password.", "Input Required")

    def show_alert(self, message, title):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.handle_alert_response)
        msg.exec_()

    def handle_alert_response(self, button):
        if button.text() == "OK":
            self.emailLineEdit.clear()
            self.passwordLineEdit.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcomeLabel.setText(_translate("MainWindow", "Welcome Shopper!"))
        self.secondaryLabel.setText(_translate("MainWindow", "Good to see you!"))
        self.emailLabel.setText(_translate("MainWindow", "E-Mail:"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.loginPushButton.setText(_translate("MainWindow", "Login"))
        self.backPushButton.setText(_translate("MainWindow", "Back"))
        self.qrLabel.setText(_translate("MainWindow", "Log in with QR Code"))
        self.scanLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Scan this with the Supermarket </span></p></body></html>"))
        self.scanLabel_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">mobile app to log in instantly.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowLogInMember()
    ui.setupUiLogInMember(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
