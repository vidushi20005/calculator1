from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Modern Calculator")
        self.setStyleSheet("background-color: #2b2b2b;")

        # Display
        self.display = QLineEdit()
        self.display.setStyleSheet("""
            QLineEdit {
                background: #000;
                color: white;
                font-size: 30px;
                padding: 15px;
                border-radius: 10px;
            }
        """)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        # Layout
        grid = QGridLayout()
        grid.addWidget(self.display, 0, 0, 1, 4)

        buttons = {
            'C': (1, 0), '⌫': (1, 1), '(': (1, 2), ')': (1, 3),
            '7': (2, 0), '8': (2, 1), '9': (2, 2), '/': (2, 3),
            '4': (3, 0), '5': (3, 1), '6': (3, 2), '*': (3, 3),
            '1': (4, 0), '2': (4, 1), '3': (4, 2), '-': (4, 3),
            '0': (5, 0), '.': (5, 1), '=': (5, 2), '+': (5, 3),
        }

        for btn_text, pos in buttons.items():
            btn = QPushButton(btn_text)
            btn.setFixedHeight(70)
            btn.setStyleSheet(self.buttonStyle(btn_text))
            btn.clicked.connect(lambda _, text=btn_text: self.onClick(text))
            grid.addWidget(btn, pos[0], pos[1])

        self.setLayout(grid)
        self.resize(350, 500)
        self.show()

    def buttonStyle(self, text):
        if text.isdigit() or text == ".":
            color = "#4d4d4d"
        elif text == "=":
            color = "#34c759"
        elif text in ["C", "⌫"]:
            color = "#ff3b30"
        else:
            color = "#ff9500"

        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 24px;
            }}
            QPushButton:pressed {{
                background-color: #666666;
            }}
        """

    def onClick(self, text):
        current = self.display.text()

        if text == "C":
            self.display.setText("")
        elif text == "⌫":
            self.display.setText(current[:-1])
        elif text == "=":
            try:
                result = str(eval(current))
                self.display.setText(result)
            except:
                self.display.setText("Error")
        else:
            self.display.setText(current + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())
