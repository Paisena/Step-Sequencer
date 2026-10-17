import numpy as np
import sounddevice as sd
import wave 
import SoundGenerator as sg
from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QTextEdit, QSlider, QProgressBar, QComboBox, QListWidget, QRadioButton
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Step Sequencer")

        menubar = self.menuBar()

        fileMenu = menubar.addMenu("File")
        editMenu = menubar.addMenu("Edit")
        helpMenu = menubar.addMenu("Help")

        submenu = fileMenu.addMenu("submenu")
        aboutAction = submenu.addAction("About")
        exitAction = submenu.addAction("Exit")

        exitAction.triggered.connect(self.close)
        aboutAction.triggered.connect(lambda: print("this is a tutorial GUI app"))

        button = QPushButton("Play Sound")
        button.clicked.connect(self.ask_choices)

        self.setCentralWidget(button)

        # container = QWidget()
        # self.setCentralWidget(container)

        # layout = QVBoxLayout(container)

        # label = QLabel("Hello, world!")
        # label.setAlignment(Qt.AlignCenter)

        # button = QPushButton("Play Sound")
        # button.clicked.connect(lambda: self.do_something())

        # line_edit = QLineEdit()

        # combobox = QComboBox()
        # listwidget = QListWidget()
        # listwidget.addItems(["Item 1", "Item 2", "Item 3"])

        # listwidget.itemClicked.connect(lambda item: print(f"Clicked on {item.text()}"))

        # sldier = QSlider(Qt.Horizontal)

        # radio1 = QRadioButton("Option 1")
        # radio2 = QRadioButton("Option 2")
        # radio3 = QRadioButton("Option 3")

        # for r in (radio1, radio2, radio3):
        #     r.toggled.connect(self.radio_changed)

        # innerContainer = QWidget()
        # innerLayout = QHBoxLayout(innerContainer)

        # layout.addWidget(label)
        # layout.addWidget(button)
        # layout.addWidget(line_edit)
        # layout.addWidget(combobox)
        # layout.addWidget(listwidget)
        # layout.addWidget(sldier)

        # innerLayout.addWidget(radio1)
        # innerLayout.addWidget(radio2)
        # innerLayout.addWidget(radio3)

        # layout.addWidget(innerContainer)

    def do_something(self):
        print("Button clicked!")

    def radio_changed(self):
        r = self.sender()
        if r.isChecked():
            print(f"{r.text()} is selected")

    def ask_yes_no(self):
        if QMessageBox.question(self, "Question", "Do you want to play a sound?") == QMessageBox.Yes:
            print('user likes python')
        else:
            print('user does not like python')

    def ask_choices(self):
        msg = QMessageBox(self)

        msg.setWindowTitle("Choose an option")
        msg.setText("select favorite programming language")
        
        python = msg.addButton("Python", QMessageBox.AcceptRole)
        java = msg.addButton("Java", QMessageBox.AcceptRole)
        cpp = msg.addButton("C++", QMessageBox.AcceptRole)

        msg.exec()

        if msg.clickedButton() == python:
            print("user likes python")
        elif msg.clickedButton() == java:
            print("user likes java")
        elif msg.clickedButton() == cpp:
            print("user likes C++")

app = QApplication()

window = MainWindow()
window.show()
app.exec()



