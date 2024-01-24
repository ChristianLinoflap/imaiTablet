import config
# Import Python Files
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from config import Config, translations
from databaseManager import DatabaseManager, EnvironmentLoader

class Ui_MainWindowLogInMember(object):
    def __init__(self):
        self.db_manager = DatabaseManager(*EnvironmentLoader.load_env_variables())
        self.conn = self.db_manager.connect()
        self.cursor = self.conn.cursor()
        
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
        MainWindow.showFullScreen()
        # Remove Navigation Tools in Main Window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color:#00C0FF;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(685, 150, 600, 70))
        self.welcomeLabel.setStyleSheet("#welcomeLabel{\n"
"    font-size:60px;\n"
"    font-family:Montserrat;\n"
"    \n"
"}")
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.secondaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.secondaryLabel.setGeometry(QtCore.QRect(730, 250, 500, 70))
        self.secondaryLabel.setStyleSheet("#secondaryLabel{\n"
"    font-size:42px;\n"
"    font-family:Montserrat;\n"
"}")
        self.secondaryLabel.setObjectName("secondaryLabel")
        self.secondaryLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(425, 350, 150, 80))
        self.emailLabel.setStyleSheet("#emailLabel{\n"
"    font-size:36px;\n"
"    font-family:Montserrat;\n"
"}")
        self.emailLabel.setObjectName("emailLabel")

        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(425, 520, 150, 80))
        self.passwordLabel.setStyleSheet("#passwordLabel{\n"
"    font-size:36px;\n"
"    font-family:Montserrat;\n"
"}")
        self.passwordLabel.setObjectName("passwordLabel")

        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLineEdit.setGeometry(QtCore.QRect(420, 425, 450, 80))
        self.emailLineEdit.setStyleSheet("#emailLineEdit{\n"
"    border-radius:10px;\n"
"    font-size:32px;\n"
"    font-family:Montserrat;\n"
"    padding:10px;\n"
"}")
        self.emailLineEdit.setObjectName("emailLineEdit")

        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setGeometry(QtCore.QRect(420, 595, 450, 80))
        self.passwordLineEdit.setStyleSheet("#passwordLineEdit{\n"
"    border-radius:10px;\n"
"    font-size:32px;\n"
"    font-family:Montserrat;\n"
"    padding:10px;\n"
"}")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.loginPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginPushButton.setGeometry(QtCore.QRect(420, 820, 450, 100))
        self.loginPushButton.setStyleSheet("#loginPushButton{\n"
"    background-color:#0000AF;\n"
"    border-radius:35px;\n"
"    font-family:Montserrat;\n"
"    font-size:32px;\n"
"    color:#fff\n"
"}")
        self.loginPushButton.setObjectName("loginPushButton")

        self.backPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPushButton.setGeometry(QtCore.QRect(420, 950, 450, 100))
        self.backPushButton.setStyleSheet("#backPushButton{\n"
"    background-color:none;\n"
"    border:6px solid #0000AF;\n"
"    border-radius:35px;\n"
"    font-family:Montserrat;\n"
"    font-size:32px;\n"
"    color:#fff;\n"
"}")
        self.backPushButton.setObjectName("backPushButton")
        self.backPushButton.clicked.connect(self.LogInOption)
        self.backPushButton.clicked.connect(MainWindow.close)

        self.qrFrame = QtWidgets.QFrame(self.centralwidget)
        self.qrFrame.setGeometry(QtCore.QRect(1000, 360, 500, 500))
        self.qrFrame.setStyleSheet("#qrFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:25px;\n"
"    border: 2px solid black;\n"
"}")
        self.qrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qrFrame.setObjectName("qrFrame")

        self.qrLabel = QtWidgets.QLabel(self.centralwidget)
        self.qrLabel.setGeometry(QtCore.QRect(1025, 860, 480, 85))
        self.qrLabel.setStyleSheet("#qrLabel{\n"
"    font-size:42px;\n"
"    font-family:Montserrat;\n"
"}")
        self.qrLabel.setObjectName("qrLabel")
        self.qrLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.scanLabelFrame = QtWidgets.QFrame(self.centralwidget)
        self.scanLabelFrame.setGeometry(QtCore.QRect(980, 930, 550, 125))
        self.scanLabelFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scanLabelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scanLabelFrame.setObjectName("scanLabelFrame")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scanLabelFrame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scanLabel = QtWidgets.QLabel(self.scanLabelFrame)
        self.scanLabel.setStyleSheet("#scanLabel{\n"
"    font-size:28px;\n"
"    font-family:Montserrat;\n"
"}")
        self.scanLabel.setObjectName("scanLabel")
        self.verticalLayout.addWidget(self.scanLabel)
        self.scanLabel_2 = QtWidgets.QLabel(self.scanLabelFrame)
        self.scanLabel_2.setStyleSheet("#scanLabel_2{\n"
"    font-size:28px;\n"
"    font-family:Montserrat;\n"
"}")
        self.scanLabel_2.setObjectName("scanLabel_2")
        self.verticalLayout.addWidget(self.scanLabel_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.welcomeLabel.raise_()
        self.secondaryLabel.raise_()
        self.emailLabel.raise_()
        self.passwordLabel.raise_()
        self.loginPushButton.raise_()
        self.backPushButton.raise_()
        self.qrLabel.raise_()
        self.scanLabel.raise_()
        self.scanLabel_2.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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

                config.user_info['first_name'] = first_name
                config.user_info['last_name'] = last_name
                config.user_info['user_client_id'] = user_client_id

                reference_number = self.generate_reference_number()
                config.transaction_info['reference_number'] = reference_number
                
                # Insert new transaction
                self.db_manager.insert_transaction(user_client_id, reference_number)
                print("Reference Number:", reference_number)

                # Retrieve TransactionId
                transaction_id = self.db_manager.get_transaction_id(user_client_id, reference_number)
                if transaction_id is not None:
                    config.transaction_info['transaction_id'] = transaction_id

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
        message = translations[Config.current_language]['Invalid_Login_Message']
        title = translations[Config.current_language]['Invalid_Login_Title']
        self.show_alert(message, title)

    def show_input_required_alert(self):
        message = translations[Config.current_language]['Input_Required_Message']
        title = translations[Config.current_language]['Input_Required_Title']
        self.show_alert(message, title)

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

        # Use the stored language from Config
        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

        # Translate texts using the stored language
        self.welcomeLabel.setText(_translate("MainWindow", translation_dict['Welcome_Label']))
        self.secondaryLabel.setText(_translate("MainWindow", translation_dict['Secondary_Label']))
        self.emailLabel.setText(_translate("MainWindow", translation_dict['Email_Label']))
        self.passwordLabel.setText(_translate("MainWindow", translation_dict['Password_Label']))
        self.loginPushButton.setText(_translate("MainWindow", translation_dict['Login_Button']))
        self.backPushButton.setText(_translate("MainWindow", translation_dict['Back_Button']))
        self.qrLabel.setText(_translate("MainWindow", translation_dict['QR_Label']))
        self.scanLabel.setText(_translate("MainWindow", translation_dict['Scan_Label']))
        self.scanLabel_2.setText(_translate("MainWindow", translation_dict['Scan_Label_2']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowLogInMember()
    ui.setupUiLogInMember(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
