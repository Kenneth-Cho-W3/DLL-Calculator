# calculator_gui.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

# Load the Rust DLL
from ctypes import CDLL

calc_lib = CDLL("./target/release/calculator_core.dll")

# Rust functions
add = calc_lib.add
subtract = calc_lib.subtract
multiply = calc_lib.multiply
divide = calc_lib.divide

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.entry_a = QLineEdit(self)
        self.entry_b = QLineEdit(self)
        self.result_label = QLabel("Result:", self)

        # Create buttons
        add_button = QPushButton("Add", self)
        subtract_button = QPushButton("Subtract", self)
        multiply_button = QPushButton("Multiply", self)
        divide_button = QPushButton("Divide", self)

        # Connect buttons to functions
        add_button.clicked.connect(self.perform_addition)
        subtract_button.clicked.connect(self.perform_subtraction)
        multiply_button.clicked.connect(self.perform_multiplication)
        divide_button.clicked.connect(self.perform_division)

        # Layout setup
        vbox = QVBoxLayout()
        vbox.addWidget(self.entry_a)
        vbox.addWidget(self.entry_b)
        vbox.addWidget(self.result_label)

        hbox = QHBoxLayout()
        hbox.addWidget(add_button)
        hbox.addWidget(subtract_button)
        hbox.addWidget(multiply_button)
        hbox.addWidget(divide_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.show()

    def get_values(self):
        try:
            a = int(self.entry_a.text())
            b = int(self.entry_b.text())
            return a, b
        except ValueError:
            self.result_label.setText("Invalid input")

    def perform_addition(self):
        a, b = self.get_values()
        result = add(a, b)
        self.result_label.setText(f"Result: {result}")

    def perform_subtraction(self):
        a, b = self.get_values()
        result = subtract(a, b)
        self.result_label.setText(f"Result: {result}")

    def perform_multiplication(self):
        a, b = self.get_values()
        result = multiply(a, b)
        self.result_label.setText(f"Result: {result}")

    def perform_division(self):
        a, b = self.get_values()
        if b != 0:
            result = divide(a, b)
            self.result_label.setText(f"Result: {result}")
        else:
            self.result_label.setText("Cannot divide by zero")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc_app = CalculatorApp()
    sys.exit(app.exec())
    