import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class OnScreenKeyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.shift_pressed = False
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
    
        self.text_input = QLineEdit()
        # layout.addWidget(self.text_input)
        self.keyboard_layout = QVBoxLayout()
        self.update_keyboard_layout() 

        layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addLayout(self.keyboard_layout)
        layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.setLayout(layout)
        
        self.setFixedSize(1280, 230) 
        self.move(0, 490)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def update_keyboard_layout(self):
        # Clear existing layout
        while self.keyboard_layout.count():
            item = self.keyboard_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        lowercase_keys = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '@'],
            ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '.', '⌫'],
            ['-', '_', 'Space', 'Enter']
        ]

        uppercase_keys = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '@'],
            ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '.', '⌫'],
            ['-', '_', 'Space', 'Enter']
        ]

        keys = uppercase_keys if self.shift_pressed else lowercase_keys

        for row in keys:
            row_layout = QHBoxLayout()
            row_layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
            for key in row:
                key_button = QPushButton(key)
                if key == 'Shift':
                    key_button.setFixedHeight(35) 
                    key_button.clicked.connect(self.toggle_shift)
                elif key == 'Enter':
                    key_button.setFixedHeight(35) 
                    key_button.clicked.connect(self.on_enter_pressed)
                elif key == 'Space':
                    key_button.setFixedWidth(500) 
                    key_button.setFixedHeight(35) 
                    key_button.clicked.connect(partial(self.on_key_pressed, ' '))
                elif key == '-' or key == '_':
                    key_button.setFixedWidth(50) 
                    key_button.setFixedHeight(35) 
                    key_button.clicked.connect(partial(self.on_key_pressed, key))
                else:
                    key_button.setFixedHeight(35) 
                    key_button.clicked.connect(partial(self.on_key_pressed, key))
                row_layout.addWidget(key_button)
            row_layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
            self.keyboard_layout.addLayout(row_layout)

    def toggle_shift(self):
        self.shift_pressed = not self.shift_pressed
        self.update_keyboard_layout()

    def on_key_pressed(self, char):
        if char == '⌫':
            self.text_input.backspace()
        else:
            self.text_input.insert(str(char)) 
    
    def on_enter_pressed(self):
        if self.text_input is not None:
            self.text_input.returnPressed.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    keyboard = OnScreenKeyboard()
    keyboard.show()
    sys.exit(app.exec_())
