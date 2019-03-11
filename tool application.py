import sys
from PyQt4 import QtGui, QtCore

# app = QtGui.QApplication(sys.argv)

# Create General Window with appropriate title and Icon


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT GUI Tool")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        # Create Action that quits the application

        extractAction = QtGui.QAction("Quit Application", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Close the Application')
        extractAction.triggered.connect(self.close_application)

        # Create Action that changes the font style and Typeface

        extractAction_2 = QtGui.QAction("Change Font Style", self)
        extractAction_2.setShortcut("Ctrl+W")
        extractAction_2.setStatusTip('Change the given Font style / Typeface')
        extractAction_2.triggered.connect(self.font_choice)

        # Create Action that changes the colour scheme used for text

        extractAction_3 = QtGui.QAction("Colour Scheme", self)
        extractAction_3.setStatusTip("Change the background scheme of Widget")
        extractAction_3.triggered.connect(self.colour_picker)

        # Create Action that opens a text editor

        extractAction_4 = QtGui.QAction("Text Editor", self)
        extractAction_4.setShortcut("Ctrl+E")
        extractAction_4.setStatusTip("Opens a text Editor")
        extractAction_4.triggered.connect(self.text_editor)

        # Create Action that opens a writeable file (Mostly Text)

        extractAction_5 = QtGui.QAction("&Open File", self)
        extractAction_5.setShortcut("Ctrl+O")
        extractAction_5.setStatusTip('Open File')
        extractAction_5.triggered.connect(self.file_open)

        # Create Action that lets someone save the text file edited

        extractAction_6 = QtGui.QAction("&Save File", self)
        extractAction_6.setShortcut("Ctrl+S")
        extractAction_6.setStatusTip('Save File')
        extractAction_6.triggered.connect(self.file_save)

        # Create a status bar to show status/info regarding an action chosen

        self.statusBar()

        # Create Menubar to place Menu options - linked to actions above
        # Create a file,font, colour Menu option as well as link to text editor
        # Each Menu option has an action linked to it.

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
        fileMenu.addAction(extractAction_5)
        fileMenu.addAction(extractAction_6)
        fontMenu = mainMenu.addMenu("&Font")
        fontMenu.addAction(extractAction_2)
        colourMenu = mainMenu.addMenu("&Colour Scheme")
        colourMenu.addAction(extractAction_3)
        textEditor = mainMenu.addMenu("&Editor")
        textEditor.addAction(extractAction_4)

        # Refer to body of the windw, refered to as the home

        self.home()

        # A list of all different things to place in the window

    def home(self):

        # Create a button then quits the application if pressed
        # uses the close_application when called
        self.btn = QtGui.QPushButton("Quit", self)
        self.btn.clicked.connect(self.close_application)
        self.btn.resize(self.btn.minimumSizeHint())
        self.btn.move(0, 100)

        # Creates a tool (with an image) which closes the application
        # Uses the close_application when called

        extractTool = QtGui.QAction(QtGui.QIcon("toolbox.png"), "Tools", self)
        extractTool.triggered.connect(self.close_application)

        # Create a tool bar along the top of the body in the window
        # Adds the tool above to the toolbar

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(extractTool)

        # Creates a checkbox that when clicked enlarges the window to some size
        # Refers to the enlarge_window function when called

        checkBox = QtGui.QCheckBox("Enlarge", self)
        checkBox.move(200, 45)
        checkBox.stateChanged.connect(self.enlarge_window)
        # checkBox.toggle()

        # Create a progress bar with a certain geometery

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 200, 300, 30)

        # Creates a download button
        # Calls the download function when called

        self.btn2 = QtGui.QPushButton("Download", self)
        self.btn2.move(200, 250)
        self.btn2.clicked.connect(self.download)

        # Set current syle of Window with a labes placed and moved

        self.styleChoice = QtGui.QLabel("Windows Vista", self)
        self.styleChoice.move(80, 45)

        # Create a list of possible style choices and append to dropdown menu

        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem("motif")
        self.comboBox.addItem("Windows")
        self.comboBox.addItem("cde")
        self.comboBox.addItem("Plastique")
        self.comboBox.addItem("Cleanlooks")
        self.comboBox.addItem("windowsvista")
        self.comboBox.move(150, 100)

        # Create a selection toold for dropdown that links to style_choice
        # When called for that style

        self.comboBox.activated[str].connect(self.style_choice)

        # Add Calendar- if wanted

#        cal = QtGui.QCalendarWidget(self)
#        cal.move(500,200)
#        cal.resize(200,200)

        # Shows all called actions so far onto the window

        self.show()

    # Lets someone save the text document created in the text editor into
    # Local directory

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    # Lets someone open a document that can be converted into text into
    # The the text editor

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')
        self.text_editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    # Creates a text editor tool and sets it to be the central widget
    # Taking up the centre of main window

    def text_editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.progress.resize(0, 0)

    # Creates a function that will change the colour of the widget

    def colour_picker(self):
        colour = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("{colour: %s}" % colour.name())

    # Creates a function that will change the font style of the text

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    # Creates the download function, where for a small step of time will
    # Increase the progress bar with the according scale
    # Currently no file attached

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    # Create a function that takes the different options from the dropdown and
    # and takes the following and string and finds the corresponding style

    def style_choice(self, t):
        self.styleChoice.setText(t)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(t))

    # Creates an enlarged window that resizes the geometry of the window

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 650, 350)
            self.btn.move(10,280)
            self.btn2.move(250,150)
            self.progress.setGeometry(250, 100, 400, 30)
            self.comboBox.move(150, 280)
            self.styleChoice.move(80, 45)

        else:
            self.setGeometry(50, 50, 500, 300)
            self.btn.move(10,100)
            self.btn2.move(200, 250)
            self.progress.setGeometry(200, 200, 300, 30)
            self.comboBox.move(150, 100)
            self.styleChoice.move(80, 45)

    # Creates a seperate dialog box to confirm choice of closing application
    # If yes is chosen then close the application, if not pass back to the
    # System

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Closing Application",
                                                  "Leave the Application?",
                                                   QtGui.QMessageBox.Yes |
                                                   QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Closing Application")
            sys.exit()
        else:
            pass

# Create the application as an argument of the system and define the window
# executes the application to close when the system is meant to exit


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
