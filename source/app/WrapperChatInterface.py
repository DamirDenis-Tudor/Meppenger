import os

from PyQt5.QtWidgets import QMainWindow
from Problema2.BONUS.app.ChatInterface import Ui_MainWindow


# Aceasta clasa este pe post de "clasa tampon", orice modificare
# facuta interfetei propriu-zise, nu va necesita modificari de
# functionabilitate de directe in clasa ChatInterface.
class WrapperChatInterface(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Chat")
        self.stackedWidget.setCurrentWidget(self.login_widget)
        self.register_button.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.register_wiget)
        )
        self.back_button.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.login_widget)
        )
