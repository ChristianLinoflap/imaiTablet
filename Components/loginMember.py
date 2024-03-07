import config
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from config import Config, translations
from databaseManager import DatabaseManager, EnvironmentLoader
from onScreenKeyboard import OnScreenKeyboard

class Ui_MainWindowLogInMember(object):
    def __init__(self):
        self.db_manager = DatabaseManager(*EnvironmentLoader.load_env_variables())
        self.conn = self.db_manager.connect()
        self.cursor = self.conn.cursor()
        self.keyboard = OnScreenKeyboard()

    def TutorialMember(self):
        self.hide_keyboard_on_mouse_click(None)
        from tutorialMember import Ui_MainWindowTutorialMember
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowTutorialMember()
        self.ui.setupUiTutorialMember(self.window)
        self.window.show()  

    def LogInOption (self):
        from loginOption import Ui_MainWindowLogInOption
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowLogInOption()
        self.ui.setupUiLogInOption(self.window)
        self.window.show()  

    def setupUiLogInMember(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
       
        MainWindow.mousePressEvent = self.hide_keyboard_on_mouse_click
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        gradient = QtGui.QLinearGradient(0, 0, self.centralwidget.width(), self.centralwidget.height())
        gradient.setColorAt(0, QtGui.QColor("#1D7CBA"))
        gradient.setColorAt(1, QtGui.QColor("#0D3854"))
        self.centralwidget.setStyleSheet("#centralwidget { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #1D7CBA, stop: 1 #0D3854); }")
        self.centralwidget.setObjectName("centralwidget")

        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(345, 50, 600, 70))
        self.welcomeLabel.setStyleSheet("#welcomeLabel{\n"
"    font-size:48px;\n"
"    font-family:Montserrat;\n"
"    color: #fff;\n"
"    \n"
"}")
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.secondaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.secondaryLabel.setGeometry(QtCore.QRect(400, 100, 500, 70))
        self.secondaryLabel.setStyleSheet("#secondaryLabel{\n"
"    font-size:36px;\n"
"    font-family:Montserrat;\n"
"    color: #fff;\n"
"}")
        self.secondaryLabel.setObjectName("secondaryLabel")
        self.secondaryLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(250, 200, 150, 60))
        self.emailLabel.setStyleSheet("#emailLabel{\n"
"    font-size:26px;\n"
"    font-family:Montserrat;\n"
"    color: #fff;\n"
"}")
        self.emailLabel.setObjectName("emailLabel")

        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(250, 340, 150, 60))
        self.passwordLabel.setStyleSheet("#passwordLabel{\n"
"    font-size:26px;\n"
"    font-family:Montserrat;\n"
"    color: #fff;\n"
"}")
        self.passwordLabel.setObjectName("passwordLabel")

        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLineEdit.setGeometry(QtCore.QRect(250, 265, 400, 60))
        self.emailLineEdit.setStyleSheet("#emailLineEdit{\n"
"    border-radius:10px;\n"
"    font-size:26px;\n"
"    font-family:Montserrat;\n"
"    padding:10px;\n"
"}")
        self.emailLineEdit.setObjectName("emailLineEdit")

        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setGeometry(QtCore.QRect(250, 405, 400, 60))
        self.passwordLineEdit.setStyleSheet("#passwordLineEdit{\n"
"    border-radius:10px;\n"
"    font-size:26px;\n"
"    font-family:Montserrat;\n"
"    padding:10px;\n"
"}")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.emailLineEdit.setReadOnly(True)
        self.emailLineEdit.mousePressEvent = self.show_keyboard_for_email

        self.passwordLineEdit.setReadOnly(True)
        self.passwordLineEdit.mousePressEvent = self.show_keyboard_for_password

        self.emailLineEdit.returnPressed.connect(self.move_focus_to_password)
        self.passwordLineEdit.returnPressed.connect(self.click_login_button)
        
        self.loginPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginPushButton.setGeometry(QtCore.QRect(250, 540, 400, 60))
        self.loginPushButton.setStyleSheet("#loginPushButton{\n"
"    font-size:18px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #0000AF;\n"
"    background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0.2 #0000AF, stop:0.2 #0000AF, stop:1 #f6f7fa);\n"
"}")
        self.loginPushButton.setObjectName("loginPushButton")

        self.backPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPushButton.setGeometry(QtCore.QRect(250, 620, 400, 60))
        self.backPushButton.setStyleSheet("#backPushButton{\n"
"    border-radius:10px;\n"
"    font-family:Montserrat;\n"
"    font-size:18px;\n"
"    color:#000;\n"
"    border: 2px solid #FFD700;\n"
"    border-radius: 9px;\n"
"    background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0.2 #FFD700, stop:0.2 #FFD700, stop:1 #f6f7fa);\n"
"}")
        self.backPushButton.setObjectName("backPushButton")
        self.backPushButton.clicked.connect(self.LogInOption)
        self.backPushButton.clicked.connect(MainWindow.close)

        self.qrFrame = QtWidgets.QFrame(self.centralwidget)
        self.qrFrame.setGeometry(QtCore.QRect(750, 280, 300, 300))
        self.qrFrame.setStyleSheet("#qrFrame{\n"
"    background-color:#FEFCFC;\n"
"    border-radius:25px;\n"
"    border: 2px solid black;\n"
"}")
        self.qrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qrFrame.setObjectName("qrFrame")

        self.qrLabel = QtWidgets.QLabel(self.centralwidget)
        self.qrLabel.setGeometry(QtCore.QRect(660, 200, 480, 60))
        self.qrLabel.setStyleSheet("#qrLabel{\n"
"    font-size:36px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.qrLabel.setObjectName("qrLabel")
        self.qrLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.scanLabelFrame = QtWidgets.QFrame(self.centralwidget)
        self.scanLabelFrame.setGeometry(QtCore.QRect(625, 575, 550, 125))
        self.scanLabelFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scanLabelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scanLabelFrame.setObjectName("scanLabelFrame")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scanLabelFrame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scanLabel = QtWidgets.QLabel(self.scanLabelFrame)
        self.scanLabel.setStyleSheet("#scanLabel{\n"
"    font-size:26px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
"}")
        self.scanLabel.setObjectName("scanLabel")
        self.verticalLayout.addWidget(self.scanLabel)
        self.scanLabel_2 = QtWidgets.QLabel(self.scanLabelFrame)
        self.scanLabel_2.setStyleSheet("#scanLabel_2{\n"
"    font-size:26px;\n"
"    font-family:Montserrat;\n"
"    color:#fff;\n"
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

    def show_keyboard_for_email(self, event):
        self.passwordLineEdit.setStyleSheet("""
            #passwordLineEdit {
                border-radius: 10px;
                font-size: 26px;
                font-family: Montserrat;
                padding: 10px;
            }
        """)
        
        self.emailLineEdit.setStyleSheet("""
            #emailLineEdit {
                border: 2px solid #FFD700;
                border-radius: 10px;
                font-size: 26px;
                font-family: Montserrat;
                padding: 10px;
            }
        """)
        self.keyboard.text_input = self.emailLineEdit
        self.keyboard.raise_()
        self.keyboard.show()

    def show_keyboard_for_password(self, event):
        self.emailLineEdit.setStyleSheet("""
            #emailLineEdit {
                border-radius: 10px;
                font-size: 26px;
                font-family: Montserrat;
                padding: 10px;
            }
        """)           
        self.passwordLineEdit.setStyleSheet("""
            #passwordLineEdit {
                border: 2px solid #FFD700;
                border-radius: 10px;
                font-size: 26px;
                font-family: Montserrat;
                padding: 10px;
            }
        """)
        self.keyboard.text_input = self.passwordLineEdit
        self.keyboard.raise_()
        self.keyboard.show()

    def move_focus_to_password(self):
        self.passwordLineEdit.setFocus()
        self.show_keyboard_for_password(None)
    
    def move_focus_to_email(self):
        self.emailLineEdit.setFocus()
        self.show_keyboard_for_email(None)
        
    def click_login_button(self):
        self.loginPushButton.click()
    
    def hide_keyboard_on_mouse_click(self, event):
        if self.keyboard.isVisible():
            self.keyboard.hide()
            self.emailLineEdit.setStyleSheet("""
                #emailLineEdit {
                    border-radius: 10px;
                    font-size: 26px;
                    font-family: Montserrat;
                    padding: 10px;
                }
            """)
            self.passwordLineEdit.setStyleSheet("""
                #passwordLineEdit {
                    border-radius: 10px;
                    font-size: 26px;
                    font-family: Montserrat;
                    padding: 10px;
                }
            """)

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

                reference_number = self.db_manager.generate_reference_number()  
                config.transaction_info['reference_number'] = reference_number
                self.db_manager.insert_transaction(user_client_id, reference_number)

                transaction_id = self.db_manager.get_transaction_id(user_client_id, reference_number)
                if transaction_id is not None:
                    config.transaction_info['transaction_id'] = transaction_id

                self.db_manager.update_transaction(user_client_id, reference_number)

                self.MainWindow.close()
                self.TutorialMember()
            else:
                self.show_invalid_login_alert()
                self.move_focus_to_email()
        else:
            self.show_input_required_alert()
            self.move_focus_to_email()

    def closeEvent(self, event):
        super().closeEvent(event)
        self.cursor.close()
        self.conn.close()

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

        language = Config.current_language
        translation_dict = translations.get(language, translations['English'])

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