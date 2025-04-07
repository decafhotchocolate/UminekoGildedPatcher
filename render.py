import webbrowser

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)


def addImage(image_path):
    pixmap = QPixmap(image_path)
    label = QLabel()
    label.setPixmap(pixmap)
    layout.addWidget(label)



app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
window.setWindowTitle("Umineko Gilded Patcher")


layout.addWidget(QPushButton("Select where your Umineko Project is located.\n(this folder contains onscripter-ru.exe)"))

layout.addWidget(QLabel("What spriteset would you like to use?\n(Note, sprites other than PS3 will require a sizable download.)"))

addImage("res/sprites.png")

layout.addWidget(QRadioButton("Ryukishi/OG Sprites"))
layout.addWidget(QRadioButton("Alchemist/PS3 Sprites"))
layout.addWidget(QRadioButton("Panchiko/Mangagamer Sprites"))

layout.addWidget(QLabel("Font scale? (Default is 1.0)\n1.2 is recommended on the Umineko Project website."))
layout.addWidget(QLineEdit('1.0'))

# before uploading this get permission from umipro goat & discord guys
layout.addWidget(QLabel("Discord integration? (Provided by m3t4f1v3 on Github)"))
layout.addWidget(QCheckBox("Discord integration"))

layout.addWidget(QLabel("Enable smallcaps? By default in Umineko Project, BEATRICE will have her name displayed this way.\nIf it matters to you, this was not the case in the original WH/MangaGamer releases.\nHowever, it does emulate the fact BEATRICE's name is origianlly in katakana."))

addImage("res/smallcaps_false.png")
addImage("res/smallcaps_true.png")

layout.addWidget(QCheckBox("Smallcaps for BEATRICE"))

layout.addWidget(QLabel("Would you like your fonts to have a small gradient on them? (Default Umineko Project behavior)"))
addImage("res/gradient_false.png")
layout.addWidget(QCheckBox("Gradient on fonts?"))

layout.addWidget(QLabel("Install Umineko Project GOAT Edition?\nOptional patch by Pteryon on Github.\nContains new logos, replaces PS3 openings with less-spoilery original PC openings, more."))
# # note, UMIPROGOAT only provides ps3fication of og openings, need to add original openings
button = QPushButton("Read more info here!")
button.clicked.connect(lambda: webbrowser.open("https://github.com/Pteryon/umipro-goat"))
layout.addWidget(button)
layout.addWidget(QCheckBox("Install GOAT Edition "))


button = QPushButton("Make it so!")
layout.addWidget(button)



window.setLayout(layout)
window.show()
app.exec()
