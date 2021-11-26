import sqlite3
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QMessageBox
import pandas as pd

class Window(QMainWindow):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database Example'


        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Test DB")
        self.setGeometry(50, 50, 800, 800)



        # Showing Ui
        self.show()