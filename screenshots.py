'''
A GUI based Screenshot application on Python.
(Default location of captured screensshot : project folder.)

1) Create a virtual environment (projects_env)
    > Install pyautogui
    > Install PyQt5

2) Imported required libraries/components.

'''
import time
import pyautogui
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class TitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setParent(parent)
        # self.setStyleSheet('background-color: rgba(100, 100, 255, 150);')
        # self.setFixedHeight(30)
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout(self)

        # Button to capture Screenshot.
        ss_button = QPushButton()
        ss_button.setIcon(QIcon('capture.png'))
        ss_button.setFixedSize(40, 40)
        # custom_button.setStyleSheet('background-color: black; color: white; border: none;')
        ss_button.clicked.connect(self.screenshot)  # Connect the button to screenshot function.
        layout.addWidget(ss_button, alignment=Qt.AlignRight)

        # Button to minimize the widget
        minimize_button = QPushButton()
        minimize_button.setIcon(QIcon('minus.png'))
        minimize_button.setFixedSize(40, 40)
        minimize_button.clicked.connect(self.parent().showMinimized)
        layout.addWidget(minimize_button, alignment=Qt.AlignRight)

        # Button to close the widget
        close_button = QPushButton()
        close_button.setIcon(QIcon('close.png'))
        close_button.setFixedSize(40, 40)
        close_button.clicked.connect(self.parent().close)
        layout.addWidget(close_button, alignment=Qt.AlignRight)

        # layout.addStretch(5)
        self.setLayout(layout)

    def screenshot(self):

        #Screenshot file name generation.
        # --  --  --  --  --  --  --
        # Retrieve the current local time as a struct_time object, which represents the time broken down into its various components.
        date_time = time.localtime()

        # Format a struct_time object or a time tuple into a string representation based on a specified format.
        date_time = time.strftime("%m_%d_%Y_%H_%M_%S", date_time)
        
        ss_name = "SS"+date_time+".png"
        # --  --  --  --  --  --  --

        #minimize app before capture and delay 1sec
        self.parent().showMinimized()
        time.sleep(1)

        #screenshot function allows you to capture screenshots of your computer screen programmatically.
        #Captures the entire screen by default.
        ss = pyautogui.screenshot(ss_name)

        #Display Captured SS
        ss.show()

        #restore minimized window app.
        self.parent().showNormal()



class FloatingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SS App Widget')
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout(self)

        title_bar = TitleBar(self)
        main_layout.addWidget(title_bar)

        # Add some space to hold the widget and move it
        main_layout.addStretch(1)

        # Set the main layout to the widget
        self.setLayout(main_layout)

        # Set the background color for the widget
        self.setStyleSheet('background-color: rgba(0, 0, 0, 150); border: 2px solid #333; border-radius: 8px;')

        # Move the widget to the bottom-center of the screen
        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry(desktop.screenNumber(self))

        x = screen_rect.width() // 2
        y = screen_rect.bottom()
        self.setGeometry(x-50, y-150, 0, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    floating_widget = FloatingWidget()
    floating_widget.show()
    sys.exit(app.exec_())

