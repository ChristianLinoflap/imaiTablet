import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel


from design import Ui_Form


class MyForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        self.duplicateButton.clicked.connect(self.duplicate_widget)

    def duplicate_widget(self):
        new_widget = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Duplicated Widget")
        layout.addWidget(label)
        new_widget.setLayout(layout)
        self.verticalLayout.addWidget(new_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
