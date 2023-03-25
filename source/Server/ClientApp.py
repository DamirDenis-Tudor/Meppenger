import sys
from datetime import datetime
from multiprocessing import Process, Manager

from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication
from multiprocessing.connection import Client

from Problema2.BONUS.app.WrapperChatInterface import WrapperChatInterface

class ChatApp:
    def __init__(self):
        # initializam adresa de conexiune si
        # obiectul de tip client(conexiunea la server)
        self.address = ('localhost', 6000)
        self.client = Client(self.address)

        # adaugam cele 2 procese principale ale aplicatiei
        self.processes = [
            Process(target=self.display_interface),
            Process(target=self.communicate_with_server)
        ]

        # initializam coada de mesaje pentru
        # comunicarea interproces
        self.message_queue = Manager().Queue()

    def communicate_with_server(self):
        # preluam toate mesajele primite de la
        # server si le incarcam in coada de mesaje
        while True:
            msg = self.client.recv().decode()
            self.message_queue.put(msg)

    def display_interface(self):
        # prin apelul functiei show()
        # se initiaza un process ce are ca scop
        # rularea interfetei grafice
        app = QApplication(sys.argv)
        window = WrapperChatInterface()
        cursor = QTextCursor(window.conversation.document())
        window.show()

        # acum in timpul rularii aplicatiei pot
        # aparea o serie de evenimente

        # eventul de inregistrare a unui client
        window.register1_button.clicked.connect(lambda: self.register_client(window))

        # eventul de login
        window.login_button.clicked.connect(lambda: self.login(window))

        # eventul de logout
        window.logout.clicked.connect(lambda: self.logout(window))

        # evenimentul de trimitere de mesaj
        window.type_zone.returnPressed.connect(lambda: self.send_message(window, cursor))

        # evenimentul de reinprospatare conversatie
        window.chats.currentItemChanged.connect(lambda: self.load_conversations(window, cursor))

        # daca nu sunt event-uri principala functie
        # este cea de a afisa mesajele primite de la server
        self.receiveve_message(app, window, cursor)

        # evetul de inchidere a aplicatiei
        sys.exit(app.exec_())

    def register_client(self, window):
        # datele user-ului
        username = window.username_register.text()
        name = window.name_register.text()
        email = window.email_register.text()
        password = window.pasword_register.text()

        fail = False
        if username != "" and name != "" and \
                email != "" and password != "":

            # trimitem formularul de inregistrare
            self.client.send(f"REGISTER:{name}|{email}|{username}|{password}".encode())
            while True:
                msg = self.message_queue.get()
                # asteptam sa fim notificati de server
                # legat de statusul inregistrarii
                if msg == "REGISTER SUCCES":
                    window.username_text.setText(username)
                    window.stackedWidget.setCurrentWidget(window.login_widget)
                    window.register_error.setText("")
                    break
                elif msg == "REGISTER FAIL":
                    fail = True
                    break
        else:
            fail = True

        window.login_error.setText("")
        window.name_register.clear()
        window.username_register.clear()
        window.pasword_register.clear()
        window.email_register.clear()

        if fail:
            window.register_error.setText("Invalid data")

    def login(self, window):
        # datele user-ului
        username = window.username.text()
        password = window.password.text()
        fail = False
        if username != "" and password != "":
            # trimitem datele de login la server
            # pentru a fi validate
            self.client.send(f"LOGIN:{username}|{password}".encode())
            while True:
                msg = self.message_queue.get()
                print(msg)
                if msg == "LOGIN SUCCES":
                    window.username_text.setText(username)
                    window.stackedWidget.setCurrentWidget(window.chat_widget)
                    window.login_error.setText("")
                    break
                elif msg == "LOGIN FAIL":
                    fail = True
                    break
        else:
            fail = True

        window.username.clear()
        window.password.clear()
        if fail:
            window.login_error.setText("Invalid data")

    def logout(self, window):
        window.stackedWidget.setCurrentWidget(window.login_widget)
        window.chats.clear()
        window.conversation.clear()
        self.client.send("LOGOUT:".encode())

    def load_chat_list(self, window):
        window.chats.clear()
        # facem cerere catre server
        self.client.send(f"CHATLIST:".encode())
        while True:
            msg = str(self.message_queue.get())
            if msg.split(":")[0] == "CHATS":
                # mesajul este intr-un anumit format
                # => trebuie "despachetat"
                for user in msg.split(":")[1].split("|"):
                    if user.split("-")[0] != window.username_text.text():
                        window.chats.addItem(user)
            break

    def load_conversations(self, window, cursor):
        if window.stackedWidget.currentWidget() == window.chat_widget:
            if window.chats.currentItem() is not None :
                # facem cerere la server
                conversation_with = str(window.chats.currentItem().text()).split("-")[0]
                self.client.send(f"CONVERSATION:{window.username_text.text()}|{conversation_with}".encode())
                while True:
                    msg = str(self.message_queue.get())
                    if msg is not None:
                        window.conversation.clear()
                        cursor.insertText(msg.replace(window.username_text.text(), "You"))
                    break

    def send_message(self, window, cursor):
        if window.chats.currentItem() is not None:
            message = window.type_zone.text()
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.insertText(f"You({date}): \n\t{message}\n\n")
            conversation_with = str(window.chats.currentItem().text()).split("-")[0]
            self.client.send(
                f"MESSAGE:{window.username_text.text()}|{conversation_with}|\n\t{message}\n".encode()
            )
            window.type_zone.clear()

    def receiveve_message(self, app, window, cursor):
        while True:
            # apelul functiei processEvents() precum si
            # verificarea continutului cozii de mesaje
            # ofera posibilitatea de a se ocupa de eventurile
            # din aplicatie, prioritate mica avand afisarea mesajelor
            app.processEvents()
            if not self.message_queue.empty():
                message = self.message_queue.get()
                # in caz de un user se logeaza sau
                # delogheaza vom actualiza chatlistul
                if str(message).split(":")[0] == "RELOAD_CHATLIST":
                    previous_active = None
                    if window.chats.currentItem() is not None:
                        previous_active = window.chats.currentRow()
                    self.load_chat_list(window)
                    if previous_active is not None:
                        window.chats.setCurrentItem(window.chats.item(previous_active))
                    continue

                if window.chats.currentItem() is not None:
                    # totusi functia ruland in procesul de
                    # display_interface, exista posibilitatea
                    # sa primesca niste mesaje care sunt
                    # destinate altor procese
                    if str(message).split(":")[0] != "MESSAGE":
                        # punem inapoi in coada
                        self.message_queue.put(message)
                        continue
                    if window.chats.currentItem().text().split("-")[0] == str(message).split(":")[1].split("|")[0]:
                        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        cursor.insertText(
                            str(message).split(":")[1].split("|")[0] + f"({date})" + ":" +
                            str(message).split(":")[1].split("|")[1] + "\n")

    def run(self):
        for proces in self.processes:
            proces.start()
        for proces in self.processes:
            proces.join()


if __name__ == '__main__':
    chatApp = ChatApp()
    chatApp.run()
