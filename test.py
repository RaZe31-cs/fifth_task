import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem


class AddEditDatabase(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddEditDatabase()
    ex.show()
    sys.exit(app.exec())
