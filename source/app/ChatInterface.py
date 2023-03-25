# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("font: 700 14pt \"Abyssinica SIL\";")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.stackedWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("background-color:rgb(239, 232, 246)")
        self.stackedWidget.setObjectName("stackedWidget")
        self.chat_widget = QtWidgets.QWidget()
        self.chat_widget.setObjectName("chat_widget")
        self.conversation = QtWidgets.QTextBrowser(self.chat_widget)
        self.conversation.setGeometry(QtCore.QRect(260, 10, 521, 501))
        self.conversation.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.conversation.setStyleSheet("font: 700 14pt \"aakar\";\n"
"background-color:rgb(222, 215, 230);\n"
"color:rgb(97, 53, 131)")
        self.conversation.setLineWidth(2)
        self.conversation.setObjectName("conversation")
        self.type_zone = QtWidgets.QLineEdit(self.chat_widget)
        self.type_zone.setGeometry(QtCore.QRect(262, 530, 521, 51))
        self.type_zone.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.type_zone.setStyleSheet("font: 700 14pt \"aakar\";\n"
"background-color:rgb(222, 215, 230);\n"
"color:rgb(97, 53, 131)")
        self.type_zone.setText("")
        self.type_zone.setObjectName("type_zone")
        self.logout = QtWidgets.QPushButton(self.chat_widget)
        self.logout.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.logout.setStyleSheet("color:rgb(145, 65, 172);\n"
"font: 700 14pt \"aakar\";")
        self.logout.setObjectName("logout")
        self.label = QtWidgets.QLabel(self.chat_widget)
        self.label.setGeometry(QtCore.QRect(10, 60, 231, 31))
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color:rgb(145, 65, 172);\n"
"font: 700 14pt \"aakar\";\n"
"background-color:rgb(222, 215, 230)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.username_text = QtWidgets.QLabel(self.chat_widget)
        self.username_text.setGeometry(QtCore.QRect(70, 10, 171, 31))
        self.username_text.setStyleSheet("font: 700 italic 14pt \"aakar\";\n"
"color:rgb(145, 65, 172);\n"
"background-color:rgb(222, 215, 230)")
        self.username_text.setAlignment(QtCore.Qt.AlignCenter)
        self.username_text.setObjectName("username_text")
        self.chats = QtWidgets.QListWidget(self.chat_widget)
        self.chats.setGeometry(QtCore.QRect(10, 101, 231, 481))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(97, 53, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 215, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 53, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 53, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 215, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 215, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 65, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 53, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 53, 131, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 140, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 53, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 215, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 53, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(97, 53, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 215, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 215, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.chats.setPalette(palette)
        self.chats.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.chats.setStyleSheet("font: 700 14pt \"aakar\";\n"
"background-color:rgb(222, 215, 230);\n"
"color:rgb(97, 53, 131)")
        self.chats.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.chats.setGridSize(QtCore.QSize(0, 60))
        self.chats.setObjectName("chats")
        self.stackedWidget.addWidget(self.chat_widget)
        self.login_widget = QtWidgets.QWidget()
        self.login_widget.setObjectName("login_widget")
        self.login_frame = QtWidgets.QFrame(self.login_widget)
        self.login_frame.setGeometry(QtCore.QRect(270, 200, 249, 251))
        self.login_frame.setStyleSheet("background-color:rgb(222, 215, 230)")
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("login_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.login_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.username = QtWidgets.QLineEdit(self.login_frame)
        self.username.setMouseTracking(False)
        self.username.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username.setAutoFillBackground(False)
        self.username.setStyleSheet("font: 700 14pt \"aakar\";color:rgb(97, 53, 131)")
        self.username.setText("")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.verticalLayout_4.addWidget(self.username)
        self.password = QtWidgets.QLineEdit(self.login_frame)
        self.password.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.password.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password.setAutoFillBackground(False)
        self.password.setStyleSheet("font: 700 14pt \"aakar\";color:rgb(97, 53, 131)")
        self.password.setText("")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.verticalLayout_4.addWidget(self.password)
        self.login_button = QtWidgets.QPushButton(self.login_frame)
        self.login_button.setStyleSheet("font: 700 14pt \"aakar\";color:rgb(192, 97, 203)")
        self.login_button.setObjectName("login_button")
        self.verticalLayout_4.addWidget(self.login_button)
        self.register_button = QtWidgets.QPushButton(self.login_frame)
        self.register_button.setStyleSheet("font: 700 14pt \"aakar\";color:rgb(192, 97, 203)")
        self.register_button.setObjectName("register_button")
        self.verticalLayout_4.addWidget(self.register_button)
        self.login_error = QtWidgets.QLabel(self.login_widget)
        self.login_error.setGeometry(QtCore.QRect(273, 490, 251, 26))
        self.login_error.setText("")
        self.login_error.setAlignment(QtCore.Qt.AlignCenter)
        self.login_error.setObjectName("login_error")
        self.label_2 = QtWidgets.QLabel(self.login_widget)
        self.label_2.setGeometry(QtCore.QRect(270, 25, 251, 71))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 700 26pt \"aakar\";\n"
"color: rgb(145, 65, 172);\n"
"background-color:rgb(222, 215, 230)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.login_widget)
        self.register_wiget = QtWidgets.QWidget()
        self.register_wiget.setObjectName("register_wiget")
        self.register_frame = QtWidgets.QFrame(self.register_wiget)
        self.register_frame.setGeometry(QtCore.QRect(270, 120, 249, 331))
        self.register_frame.setStyleSheet("background-color:rgb(222, 215, 230)")
        self.register_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.register_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_frame.setObjectName("register_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.register_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.email_register = QtWidgets.QLineEdit(self.register_frame)
        self.email_register.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.email_register.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.email_register.setAutoFillBackground(False)
        self.email_register.setStyleSheet("font: 700 14pt \"aakar\";\n"
"color:rgb(97, 53, 131)")
        self.email_register.setText("")
        self.email_register.setAlignment(QtCore.Qt.AlignCenter)
        self.email_register.setObjectName("email_register")
        self.verticalLayout_3.addWidget(self.email_register)
        self.name_register = QtWidgets.QLineEdit(self.register_frame)
        self.name_register.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.name_register.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_register.setAutoFillBackground(False)
        self.name_register.setStyleSheet("font: 700 14pt \"aakar\";\n"
"color:rgb(97, 53, 131)")
        self.name_register.setText("")
        self.name_register.setAlignment(QtCore.Qt.AlignCenter)
        self.name_register.setObjectName("name_register")
        self.verticalLayout_3.addWidget(self.name_register)
        self.username_register = QtWidgets.QLineEdit(self.register_frame)
        self.username_register.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.username_register.setStyleSheet("font: 700 14pt \"aakar\";color:rgb(97, 53, 131)")
        self.username_register.setText("")
        self.username_register.setAlignment(QtCore.Qt.AlignCenter)
        self.username_register.setObjectName("username_register")
        self.verticalLayout_3.addWidget(self.username_register)
        self.pasword_register = QtWidgets.QLineEdit(self.register_frame)
        self.pasword_register.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pasword_register.setStyleSheet("font: 700 14pt \"aakar\";color:rgb(97, 53, 131)")
        self.pasword_register.setText("")
        self.pasword_register.setAlignment(QtCore.Qt.AlignCenter)
        self.pasword_register.setObjectName("pasword_register")
        self.verticalLayout_3.addWidget(self.pasword_register)
        self.register1_button = QtWidgets.QPushButton(self.register_frame)
        self.register1_button.setStyleSheet("font: 700 14pt \"aakar\";\n"
"color:rgb(192, 97, 203)")
        self.register1_button.setObjectName("register1_button")
        self.verticalLayout_3.addWidget(self.register1_button)
        self.back_button = QtWidgets.QPushButton(self.register_frame)
        self.back_button.setStyleSheet("font: 700 14pt \"aakar\";color:rgb(192, 97, 203)")
        self.back_button.setObjectName("back_button")
        self.verticalLayout_3.addWidget(self.back_button)
        self.register_error = QtWidgets.QLabel(self.register_wiget)
        self.register_error.setGeometry(QtCore.QRect(280, 480, 241, 26))
        self.register_error.setText("")
        self.register_error.setAlignment(QtCore.Qt.AlignCenter)
        self.register_error.setObjectName("register_error")
        self.label_3 = QtWidgets.QLabel(self.register_wiget)
        self.label_3.setGeometry(QtCore.QRect(270, 25, 251, 71))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("font: 700 26pt \"aakar\";\n"
"color:rgb(145, 65, 172);\n"
"background-color:rgb(222, 215, 230)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.register_wiget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.conversation.setPlaceholderText(_translate("MainWindow", "Please select a conversation ..."))
        self.type_zone.setPlaceholderText(_translate("MainWindow", "Type a message ..."))
        self.logout.setText(_translate("MainWindow", "X"))
        self.label.setText(_translate("MainWindow", "Chats"))
        self.username_text.setText(_translate("MainWindow", "Username"))
        self.username.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>E-mail</p><p><br/></p></body></html>"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>E-mail</p><p><br/></p></body></html>"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.register_button.setText(_translate("MainWindow", "Register"))
        self.label_2.setText(_translate("MainWindow", "MEPPENGER"))
        self.email_register.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>E-mail</p><p><br/></p></body></html>"))
        self.email_register.setPlaceholderText(_translate("MainWindow", "Email"))
        self.name_register.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>E-mail</p><p><br/></p></body></html>"))
        self.name_register.setPlaceholderText(_translate("MainWindow", "Name"))
        self.username_register.setPlaceholderText(_translate("MainWindow", "Username"))
        self.pasword_register.setPlaceholderText(_translate("MainWindow", "Password"))
        self.register1_button.setText(_translate("MainWindow", "Register"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.label_3.setText(_translate("MainWindow", "MEPPENGER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())