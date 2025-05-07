import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QRadioButton, QPushButton,
    QVBoxLayout, QMessageBox, QButtonGroup, QDialog
)
from PyQt5.QtGui import QPixmap, QPalette, QColor, QMovie
from PyQt5.QtCore import Qt

class ResultDialog(QDialog):
    def __init__(self, message, gif_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Result")
        self.setFixedSize(400, 400)
