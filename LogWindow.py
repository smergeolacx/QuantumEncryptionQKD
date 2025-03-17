import sys
from PyQt6 import QtWidgets, QtCore, QtGui

class LogWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Console Log")
        self.setGeometry(100, 100, 550, 700)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.log_text_edit = QtWidgets.QTextEdit(self)
        self.log_text_edit.setReadOnly(True)  # Make it read-only
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.log_text_edit)

    def add_log(self, message):
        self.log_text_edit.append(message)

    def clear_log(self):
        self.log_text_edit.clear()
