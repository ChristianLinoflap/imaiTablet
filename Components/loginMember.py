# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pyodbc
from config import db_server_name, db_name, db_username, db_password
import logging 
from datetime import datetime, timedelta

# DataBase Management 
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
            logging.error(f"Error connecting to the database: {e}")
            raise

    # Database User Authentication
    def authenticate_user(self, cursor, username, password):
        query = "SELECT UserClientId, FirstName, LastName FROM [dbo].[UserClient] WHERE Email = ? AND Password = ?"
        cursor.execute(query, username, password)
        return cursor.fetchone()
    
    # Insert new transaction
    def insert_transaction(self, user_client_id, reference_number):
        japan_time = datetime.utcnow() + timedelta(hours=9)  # Convert UTC to Japan time
        query = "INSERT INTO [dbo].[Transaction] (UserClientId, CreatedAt, UpdatedAt, TransactionStatus, ReferenceNumber) VALUES (?, ?, ?, 'On-going', ?);"
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, user_client_id, japan_time, japan_time, reference_number)
                conn.commit()

    # Update transaction details
    def update_transaction(self, user_client_id, reference_number):
        japan_time = datetime.utcnow() + timedelta(hours=9)  # Convert UTC to Japan time
        query = "UPDATE [dbo].[Transaction] SET UpdatedAt = ? WHERE UserClientId = ? AND ReferenceNumber = ?;"
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, japan_time, user_client_id, reference_number)
                conn.commit()

class Ui_MainWindowLogInMember(object):
    # Function to Call tutorialMember.py
    def TutorialMember(self):
        from tutorialMember import Ui_MainWindowTutorialMember
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowTutorialMember()
        self.ui.setupUiTutorialMember(self.window)
        self.window.show()  

    # Function to Call loginOption.py
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
        self.db_manager = DatabaseManager(
            server_name=db_server_name,
            database_name=db_name,
            username=db_username,
            password=db_password
        )
        self.conn = self.db_manager.connect()
        self.cursor = self.conn.cursor()

        self.loginPushButton.clicked.connect(self.authenticate_user)
        self.MainWindow = MainWindow

    # User Authentication Function
    def authenticate_user(self):
        entered_username = self.emailLineEdit.text()
        entered_password = self.passwordLineEdit.text()

        if entered_username and entered_password:
            result = self.db_manager.authenticate_user(self.cursor, entered_username, entered_password)

            if result:
                user_client_id, first_name, last_name = result

                # Store first name and last name for later use
                import config
                config.user_info['first_name'] = first_name
                config.user_info['last_name'] = last_name
                
                reference_number = self.generate_reference_number()

                # Insert new transaction
                self.db_manager.insert_transaction(user_client_id, reference_number)
                print("Reference Number:", reference_number)

                # Update transaction details
                self.db_manager.update_transaction(user_client_id, reference_number)

                print("Login successful!")
                self.MainWindow.close()
                self.TutorialMember()
            else:
                print("Invalid username or password.")
                self.show_invalid_login_alert()
        else:
            self.show_input_required_alert()

    def generate_reference_number(self):
        # Generate a unique reference number based on year, month, and a series of numbers
        year_month = QtCore.QDateTime.currentDateTime().toString("yyyyMM")
        query = f"SELECT MAX(CONVERT(INT, SUBSTRING(ReferenceNumber, 9, 6))) FROM [dbo].[Transaction] WHERE ReferenceNumber LIKE '{year_month}%';"
        with self.db_manager.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                max_sequence = cursor.fetchone()[0]
                sequence_number = 1 if max_sequence is None else max_sequence + 1

        reference_number = f"{year_month}{sequence_number:06d}"
        return reference_number

    # Closes the Database Connection
    def closeEvent(self, event):
        super().closeEvent(event)
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
