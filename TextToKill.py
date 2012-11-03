
from Main import Main
import sys

from PyQt4.QtGui import QMainWindow, QApplication, QCloseEvent

def main():
    """Create an instance of the game"""
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
