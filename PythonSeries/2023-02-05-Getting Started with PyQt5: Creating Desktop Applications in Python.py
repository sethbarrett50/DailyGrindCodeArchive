# PyQt5 is a powerful library for creating desktop applications in Python.
# To get started with PyQt5, you'll need to install the library. 
# You can do this using pip: 
# pip install PyQt5 > In terminal

# Once you have PyQt5 installed, you can start creating your application. 
# The first step is to import the necessary modules from the library: 
from PyQt5.QtWidgets import QApplication, QLabel

# The QApplication class is the main event loop for a PyQt5 application, and the QLabel class is a widget for displaying text.
# Next, we'll create an instance of the QApplication class and a label widget:
app = QApplication([])
label = QLabel("Hello, PyQt5!")

# We can then show the label on the screen by calling the show() method:
label.show()

# Finally, we'll start the event loop by calling the exec_() method of the QApplication class:
app.exec_()

# The above example is a basic PyQt5 application, it creates a window with a label that displays text "Hello, PyQt5!". 
# But PyQt5 provides many more widgets such as Buttons, LineEdit, ComboBox, ListView, etc.
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton

app = QApplication([])
label = QLabel("Please enter your name:")
line_edit = QLineEdit()
button = QPushButton("Submit")

label.show()
line_edit.show()
button.show()

app.exec_()


# PyQt5 also provides a powerful layout system that allows you to control the position and size of widgets. 
# The basic layout classes are QHBoxLayout, QVBoxLayout, and QGridLayout. 
# These classes allow you to arrange widgets in a horizontal, vertical, or grid pattern.
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout

app = QApplication([])

label = QLabel("Please enter your name:")
line_edit = QLineEdit()
button = QPushButton("Submit")

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(line_edit)
layout.addWidget(button)

widget = QWidget()
widget.setLayout(layout)
widget.show()

app.exec_()


# PyQt5 also allows you to handle signals and slots, which is a mechanism for communication between objects. 
# Signals are emitted by widgets when an event occurs, such as a button being clicked. 
# Slots are methods that are called when a signal is emitted.
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout

app = QApplication([])

label = QLabel("Please enter your name:")
line_edit = QLineEdit()
button = QPushButton("Submit")

def on_button_clicked():
    name = line_edit.text()
    label.setText("Hello, " + name + "!")

button.clicked.connect(on_button_clicked)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(line_edit)
layout.addWidget(button)

widget = QWidget()
widget.setLayout(layout)
widget.show()

app.exec_()