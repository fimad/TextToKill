
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QGridLayout, QApplication, QMainWindow, QWidget, \
    QFont, QStackedWidget, QLabel, QPushButton, QTabWidget, QLineEdit, QFrame, \
    QTableWidget, QScrollArea, QListWidget, QComboBox

class GUI(object):

    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        # Set size of window
        MainWindow.resize(800, 589)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setWindowTitle("Text to Kill")
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setObjectName("stackedWidget")
        
        font = QFont()
        font.setFamily("Times New Roman")
        
        # Main menu page
        self.menuPage = QWidget()
        self.menuPage.setObjectName("menuPage")
        self.titleLabel = QLabel(self.menuPage)
        self.titleLabel.setGeometry(QtCore.QRect(250, 60, 300, 50))
        font.setPointSize(45)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setText("Text to Kill")
        self.subtitleLabel = QLabel(self.menuPage)
        self.subtitleLabel.setGeometry(QtCore.QRect(100, 140, 600, 40))
        font.setPointSize(25)
        self.subtitleLabel.setFont(font)
        self.subtitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitleLabel.setObjectName("subtitleLabel")
        self.subtitleLabel.setText("The Murder Mystery Automation System")
        self.createButton = QPushButton(self.menuPage)
        self.createButton.setGeometry(QtCore.QRect(310, 260, 180, 60))
        self.createButton.setObjectName("createButton")
        self.createButton.setText("Create Game")
        self.runButton = QPushButton(self.menuPage)
        self.runButton.setGeometry(QtCore.QRect(310, 350, 180, 60))
        self.runButton.setObjectName("runButton")
        self.runButton.setText("Run Game")
        self.stackedWidget.addWidget(self.menuPage)
        
        # Create page
        self.createPage = QWidget()
        self.createPage.setObjectName("createPage")
        self.createTabWidget = QTabWidget(self.createPage)
        self.createTabWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))

        self.createTabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.createTabWidget.setObjectName("createTabWidget")
        
        # Create game tab
        self.createTab = QWidget()
        self.createTab.setObjectName("createTab")
        self.createDoneButton = QPushButton(self.createTab)
        self.createDoneButton.setGeometry(QtCore.QRect(580, 470, 180, 60))
        self.createDoneButton.setObjectName("createDoneButton")
        self.createDoneButton.setText("Done")
        self.gameNameEdit = QLineEdit(self.createTab)
        self.gameNameEdit.setGeometry(QtCore.QRect(140, 20, 160, 30))
        self.gameNameEdit.setObjectName("gameNameEdit")
        self.gameNameLabel = QLabel(self.createTab)
        self.gameNameLabel.setGeometry(QtCore.QRect(20, 25, 110, 20))

        font.setPointSize(15)
        self.gameNameLabel.setFont(font)
        self.gameNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gameNameLabel.setObjectName("gameNameLabel")
        self.gameNameLabel.setText("Game name")
        self.line = QFrame(self.createTab)
        self.line.setGeometry(QtCore.QRect(20, 150, 311, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.addCharLabel = QLabel(self.createTab)
        self.addCharLabel.setGeometry(QtCore.QRect(20, 180, 160, 20))
        
        font.setPointSize(20)
        self.addCharLabel.setFont(font)
        self.addCharLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addCharLabel.setObjectName("addCharLabel")
        self.addCharLabel.setText("Add Character")
        self.charNameLabel = QLabel(self.createTab)
        self.charNameLabel.setGeometry(QtCore.QRect(20, 230, 66, 20))

        font.setPointSize(15)
        self.charNameLabel.setFont(font)
        self.charNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.charNameLabel.setObjectName("charNameLabel")
        self.charNameLabel.setText("Name")
        self.charNameEdit = QLineEdit(self.createTab)
        self.charNameEdit.setGeometry(QtCore.QRect(140, 220, 160, 30))
        self.charNameEdit.setObjectName("charNameEdit")
        self.charAbilScroll = QScrollArea(self.createTab)
        self.charAbilScroll.setGeometry(QtCore.QRect(140, 260, 161, 51))
        self.charAbilScroll.setWidgetResizable(True)
        self.charAbilScroll.setObjectName("charAbilScroll")
        self.charAbilScrollContents = QListWidget()
        self.characterTable = QTableWidget(self.createTab)
        self.characterTable.setGeometry(QtCore.QRect(405, 20, 381, 401))
        self.characterTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.characterTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.characterTable.setRowCount(1)
        self.characterTable.setColumnCount(2)
        self.characterTable.setObjectName("characterTable")
        self.characterTable.horizontalHeader().setVisible(False)
        self.characterTable.horizontalHeader().setCascadingSectionResizes(False)
        self.characterTable.horizontalHeader().setMinimumSectionSize(50)
        self.characterTable.horizontalHeader().setStretchLastSection(True)
        self.characterTable.verticalHeader().setVisible(False)
        self.characterTable.verticalHeader().setDefaultSectionSize(30)
        self.scrollArea = QListWidget(self.createTab)
        self.scrollArea.setGeometry(QtCore.QRect(140, 60, 161, 71))
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setSelectionMode(3)
        self.createSaveButton = QPushButton(self.createTab)
        self.createSaveButton.setGeometry(QtCore.QRect(380, 470, 180, 60))
        self.createSaveButton.setObjectName("createSaveButton")
        self.createSaveButton.setText("Save")
        self.charAbilitiesLabel = QLabel(self.createTab)
        self.charAbilitiesLabel.setGeometry(QtCore.QRect(30, 280, 71, 20))

        font.setPointSize(15)
        self.charAbilitiesLabel.setFont(font)
        self.charAbilitiesLabel.setObjectName("charAbilitiesLabel")
        self.charAbilitiesLabel.setText("Abilities")
        self.abilitiesDropdown = QComboBox(self.createTab)
        self.abilitiesDropdown.setGeometry(QtCore.QRect(140, 330, 151, 25))
        self.abilitiesDropdown.setObjectName("abilitiesDropdown")
        
        self.addCharButton = QPushButton(self.createTab)
        self.addCharButton.setGeometry(QtCore.QRect(30, 370, 98, 27))
        self.addCharButton.setObjectName("addCharButton")
        self.addCharButton.setText("Add")
        self.gameAbilitiesLabel = QLabel(self.createTab)
        self.gameAbilitiesLabel.setGeometry(QtCore.QRect(30, 80, 71, 20))
        
        self.saveCharButton = QPushButton(self.createTab)
        self.saveCharButton.setGeometry(QtCore.QRect(70, 430, 180, 60))
        self.saveCharButton.setObjectName("saveCharButton")
        self.saveCharButton.setText("Save Character")

        font.setPointSize(15)
        self.gameAbilitiesLabel.setFont(font)
        self.gameAbilitiesLabel.setObjectName("gameAbilitiesLabel")
        self.gameAbilitiesLabel.setText("Abilities")
        self.createTabWidget.addTab(self.createTab, "")
        
        # Setup tab widget
        self.setupTab = QWidget()
        self.setupTab.setObjectName("setupTab")
        self.setupDoneButton = QPushButton(self.setupTab)
        self.setupDoneButton.setGeometry(QtCore.QRect(580, 470, 180, 60))
        self.setupDoneButton.setObjectName("setupDoneButton")
        self.setupDoneButton.setText("Done")
        self.setupTable = QTableWidget(self.setupTab)
        self.setupTable.setGeometry(QtCore.QRect(20, 20, 750, 400))
        self.setupTable.setFocusPolicy(QtCore.Qt.TabFocus)
        self.setupTable.setRowCount(1)
        self.setupTable.setColumnCount(3)
        self.setupTable.setObjectName("setupTable")
        self.setupTable.horizontalHeader().setVisible(False)
        self.setupTable.horizontalHeader().setCascadingSectionResizes(False)
        self.setupTable.horizontalHeader().setDefaultSectionSize(187)
        self.setupTable.horizontalHeader().setHighlightSections(False)
        self.setupTable.horizontalHeader().setStretchLastSection(True)
        self.setupTable.verticalHeader().setVisible(False)
        self.setupTable.verticalHeader().setHighlightSections(False)
        self.setupSaveButton = QPushButton(self.setupTab)
        self.setupSaveButton.setGeometry(QtCore.QRect(380, 470, 180, 60))
        self.setupSaveButton.setObjectName("setupSaveButton")
        self.setupSaveButton.setText("Save")
        self.createTabWidget.addTab(self.setupTab, "")
        self.createTabWidget.setTabText(self.createTabWidget.indexOf(self.createTab), "Create New Game")
        self.createTabWidget.setTabText(self.createTabWidget.indexOf(self.setupTab), "Set Up Game")
        self.stackedWidget.addWidget(self.createPage)
        
        # Game page
        self.gamePage = QWidget()
        self.gamePage.setObjectName("gamePage")
        self.gameTabWidget = QTabWidget(self.gamePage)
        self.gameTabWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.gameTabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gameTabWidget.setObjectName("gameTabWidget")
        self.statusTab = QWidget()
        self.statusTab.setObjectName("statusTab")
        self.startGameButton = QPushButton(self.statusTab)
        self.startGameButton.setGeometry(QtCore.QRect(60, 180, 180, 60))
        self.startGameButton.setObjectName("startGameButton")
        self.startGameButton.setText("Start Game")
        self.endGameButton = QPushButton(self.statusTab)
        self.endGameButton.setGeometry(QtCore.QRect(60, 260, 180, 60))
        self.endGameButton.setObjectName("endGameButton")
        self.endGameButton.setText("End Game")
        self.loadGameLabel = QLabel(self.statusTab)
        self.loadGameLabel.setGeometry(QtCore.QRect(20, 65, 101, 21))

        font.setPointSize(15)
        self.loadGameLabel.setFont(font)
        self.loadGameLabel.setObjectName("loadGameLabel")
        self.loadGameLabel.setText("Load Game")
        self.gameTabWidget.addTab(self.statusTab, "")
        self.logTab = QWidget()
        self.logTab.setObjectName("logTab")
        self.logList = QListWidget(self.logTab)
        self.logList.setGeometry(QtCore.QRect(30, 30, 730, 500))
        self.logList.setObjectName("logList")
        self.gameTabWidget.addTab(self.logTab, "")
        self.inputTab = QWidget()
        self.inputTab.setObjectName("inputTab")
        self.gameTabWidget.addTab(self.inputTab, "")
        self.gameTabWidget.setTabText(self.gameTabWidget.indexOf(self.statusTab), "Game Status")
        self.gameTabWidget.setTabText(self.gameTabWidget.indexOf(self.logTab), "Game Log")
        self.gameTabWidget.setTabText(self.gameTabWidget.indexOf(self.inputTab), "Input")
        self.stackedWidget.addWidget(self.gamePage)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.createTabWidget.setCurrentIndex(0)
        self.gameTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

if __name__ == "__main__":
    "For testing"
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = GUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
