import sqlite3
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QMessageBox
import pandas as pd

class Window(QMainWindow):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Labels
        self.title = 'Database Example'

        self.studentID_Label = QLabel(self)

        self.studentID = QLineEdit(self)

        self.test_button = QPushButton(self)

        # Pop ups
        self.id_error = QMessageBox(self)
        self.id_error.setWindowTitle("ID Error")
        self.id_error.setText("The ID you have entered is invalid. Please enter a valid ID")

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Test DB")
        self.setGeometry(50, 50, 800, 800)

        self.studentID_Label.setText("Enter Student ID")
        self.studentID_Label.resize(180, 30)
        self.studentID_Label.move(50, 20)

        self.studentID.move(50, 50)
        self.studentID.resize(180, 30)

        self.test_button.resize(180, 30)
        self.test_button.move(50, 90)
        self.test_button.setText('Select Information')
        self.test_button.clicked.connect(self.test_button_connection)


        # Showing Ui
        self.show()

    def test_button_connection(self):
        table = 'enrollments'
        studentID = self.studentID.text()
        query = f"""SELECT EXISTS(SELECT 1 FROM Enrollments WHERE studentID = '{studentID}')"""
        flag = self.cursor.execute(query).fetchall()[0][0]
        if flag == 1:
            query = f"""SELECT Enrollments.studentID, student_name, sectionID, course_desc, flags FROM
                    Enrollments INNER JOIN Student S on S.studentID = Enrollments.studentID
                    INNER JOIN Section Sec on sec.course_sectionID = sectionID
                    INNER JOIN Course C on Sec.courseID = C.courseID WHERE Enrollments.studentID = '{studentID}'"""
            self.cursor.execute(query)

            df = pd.DataFrame.from_records(self.cursor.fetchall())

            print(df)
        else:
            self.id_error.exec()
