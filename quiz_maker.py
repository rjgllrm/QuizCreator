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
        
        layout = QVBoxLayout()

        gif_label = QLabel()
        movie = QMovie(gif_path)
        gif_label.setMovie(movie)
        movie.start()
        layout.addWidget(gif_label, alignment=Qt.AlignCenter)
