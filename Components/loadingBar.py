import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QDesktopWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore

class LoadingBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 500, 100)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(30, 30, 500, 40)

        self.progressBar.setRange(0, 0)  
        self.progressBar.setTextVisible(False)

        # Create and start the timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgressBar)
        self.timer.start(50)  

    def updateProgressBar(self):
        value = self.progressBar.value()
        if value == 10000:
            value = 0
        else:
            value += 1
        self.progressBar.setValue(value)
    
    def start(self):
        self.show()
    
    def stop(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingBar()
    window.show()
    sys.exit(app.exec_())