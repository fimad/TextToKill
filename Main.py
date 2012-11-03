
from PyQt4.QtGui import QMainWindow
from GUI import GUI
from GameDescription import GameDescription

class Main(QMainWindow):
    """This class provides the graphical interface for the game"""
    
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        
        self.gui = GUI(self)
        self.game = None
        self.gameDescription = None
        self.connectGui()
        
    def connectGui(self):
        """Connect signals for Gui"""
        self.gui.createButton.released.connect(self.goCreate)
        self.gui.runButton.released.connect(self.goRun)
        self.gui.createDoneButton.released.connect(self.goBack)
        self.gui.setupDoneButton.released.connect(self.goBack)
        
    def goCreate(self):
        self.gui.stackedWidget.setCurrentIndex(1)
        self.gameDescription = GameDescription()
        
    def goBack(self):
        self.gui.stackedWidget.setCurrentIndex(0)
        
    def goRun(self):
        self.gui.stackedWidget.setCurrentIndex(2)
