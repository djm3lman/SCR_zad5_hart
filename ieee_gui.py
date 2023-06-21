import sys, ieee

from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLineEdit, QLabel, QPushButton, QGroupBox, \
    QHBoxLayout


class ConverterWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IEEE 754 Converter")
        self.layout = QVBoxLayout()

        self.radio_group = QGroupBox()
        self.radio_group.setLayout(QHBoxLayout())
        self.radio_internal_to_ieee = QRadioButton("Internal to IEEE 754")
        self.radio_ieee_to_internal = QRadioButton("IEEE 754 to Internal")
        self.radio_group.layout().addWidget(self.radio_internal_to_ieee)
        self.radio_group.layout().addWidget(self.radio_ieee_to_internal)

        self.bin_regexp = QRegularExpression("[0-1]{32}|[0-9A-F]{8}}")
        self.input_field = QLineEdit()
        self.input_field.setValidator(QRegularExpressionValidator(self.bin_regexp))

        self.result_label = QLabel()
        self.result_label.setText("Binary Code: \nHex Code: ")
        self.start_button = QPushButton("START")

        self.layout.addWidget(self.radio_group)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.start_button)

        self.start_button.clicked.connect(self.convert)

        self.setLayout(self.layout)


    def formatResult(self, txt):
        txt = txt.replace(" ", "")
        formatted_text = " ".join(txt[i:i+4] for i in range(0, len(txt), 4))
        return formatted_text


    def convert(self):
        self.result_label.setText("Binary Code: \nHex Code: ")
        input_value = self.input_field.text()
        print("DUPA: ", str(len(self.input_field.text())))
        if len(self.input_field.text()) not in [8, 32]:
            print("DUPA")

        if self.radio_internal_to_ieee.isChecked():
            if self.input_field.text() != '' and len(self.input_field.text()) in [8, 32]:
                binary_code, hex_code = ieee.internal_to_ieee(input_value)
            else:
                self.result_label.setText("Enter the valid binary number (32bit).")
                return
        elif self.radio_ieee_to_internal.isChecked():
            if self.input_field.text() != '' and len(self.input_field.text()) in [8, 32]:
                binary_code, hex_code = ieee.ieee_to_internal(input_value)
            else:
                self.result_label.setText("Enter the valid binary number (32bit).")
                return
        else:
            self.result_label.setText("Select a conversion direction.")
            return
        binary_code = self.formatResult(binary_code)
        hex_code = self.formatResult(hex_code)

        self.result_label.setText(f"Binary Code: {binary_code}\nHex Code: {hex_code}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter_widget = ConverterWidget()
    converter_widget.show()
    sys.exit(app.exec())