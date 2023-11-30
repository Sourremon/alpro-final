import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout

class PasswordExample(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create a QLabel for displaying instructions
        label = QLabel("Enter Password:")
        layout.addWidget(label)

        # Create a QLineEdit for password input
        password_input = QLineEdit(self)
        password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_input)

        self.setLayout(layout)

        self.setWindowTitle("Password Example")
        self.setGeometry(300, 300, 300, 150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = PasswordExample()
    example.show()
    sys.exit(app.exec_())
