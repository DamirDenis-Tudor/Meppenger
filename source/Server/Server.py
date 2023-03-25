from multiprocessing import Process, Manager, Value
from multiprocessing.connection import Listener
from Problema2.BONUS.database.Database import Database


class Server:
    def __init__(self):
        # initilizam baza de date
        self.database = Database()

        # adresa propriu-zisa
        self.address = ('localhost', 6000)

        # obiect ce se ocupa cu gestionarea
        # noilor conectiuni
        self.listener = Listener(self.address)

        # obiect ce gestioneaza comunicarea interprocese
        self.manager = Manager()

        # lista proxy interproces ce are clientii logati
        self.clients = self.manager.list()

        # lista cu utilizatori online
        self.usernames = self.manager.list()

        # obiect ce ne ajuta in ne asigura ca la un moment
        # de timp doar un proces aceseaza un segment de cod de exemplu
        # self.lock = self.manager.Lock()

    def wait_for_clients(self):
        # aceasta functie creaza un proces nou pentru fiecare client nou adaugat
        # in acest mod clientii pot face "cereri simultan" nedepinzand de actiunea unui client anume
        # totodata un client poate face o cerere si sa primesca si un raspuns imediat pentru ca
        # se cunoaste cu exactitate conexiunea curenta

        while True:
            # se primeste o conexiune noua
            connection = self.listener.accept()

            # se creaza un proces
            process = Process(target=self.handle_client, args=(connection,))

            # se porneste procesul
            process.start()

            # nota : procesele nu trebuie sincronizate

    def handle_client(self, connection):
        # se retine un numar de ordine al clientilor
        client_id = len(self.clients)

        # adaugam noua conexiune
        self.clients.append(connection)

        # formam vectorul pentru viitoarele citiri de utilizatori
        self.usernames.append("")

        print(f"New client connected: {client_id}")

        while True:
            try:
                # primim un mesaj si il decodam
                msg = str(connection.recv().decode())

                # format mesaj : SPECIFICATOR:CONTINU_1|CONTINUT_2|...|CONTINUT_N
                if msg.split(":")[0] == "REGISTER":
                    name = msg.split(":")[1].split("|")[0]
                    email = msg.split(":")[1].split("|")[1]
                    username = msg.split(":")[1].split("|")[2]
                    password = msg.split(":")[1].split("|")[3]
                    self.database.insert_user(name, email, username, password)
                    connection.send(f"REGISTER SUCCES".encode())
                    for client in self.clients:
                        client.send(f"RELOAD_CHATLIST:".encode())

                elif msg.split(":")[0] == "LOGIN":
                    username = msg.split(":")[1].split("|")[0]
                    password = msg.split(":")[1].split("|")[1]
                    fail = False
                    if self.database.verify_username(username) and \
                            self.database.verify_password(password):
                        for user in self.usernames:
                            if user == username:
                                fail = True
                                break
                    else:
                        fail = True

                    if fail:
                        connection.send(f"LOGIN FAIL".encode())
                    else:
                        self.usernames[client_id] = username
                        connection.send(f"LOGIN SUCCES".encode())
                        for client in self.clients:
                            client.send(f"RELOAD_CHATLIST:".encode())

                elif msg.split(":")[0] == "CHATLIST":
                    chatlist = self.database.get_all_users()
                    print(self.usernames)
                    # verificam care sunt online si care nu
                    for index in range(len(chatlist.split("|"))):
                        user_status = "  offline\n"
                        if chatlist.split("|")[index].split("-")[0] in self.usernames:
                            user_status = "  online\n"
                        chatlist = chatlist.replace("?", user_status, 1)
                    print(chatlist)
                    connection.send(f"CHATS:{chatlist}".encode())

                elif msg.split(":")[0] == "CONVERSATION":
                    sender = msg.split(":")[1].split("|")[0]
                    receiver = msg.split(":")[1].split("|")[1]
                    connection.send(self.database.get_messages(sender, receiver).encode())

                elif msg.split(":")[0] == "LOGOUT":
                    self.usernames[client_id] = ""
                    for client in self.clients:
                        client.send(f"RELOAD_CHATLIST:".encode())

                elif msg.split(":")[0] == "MESSAGE":
                    sender = msg.split(":")[1].split("|")[0]
                    receiver = msg.split(":")[1].split("|")[1]
                    message = msg.split(":")[1].split("|")[2]
                    self.database.insert_message(sender, receiver, message)

                    # trimitem mesajul doar daca clientul este online
                    userIndex = 0
                    for user in self.usernames:
                        if user == receiver:
                            break
                        userIndex += 1
                    if userIndex < len(self.clients):
                        self.clients[userIndex].send(f"MESSAGE:{sender}|{message}".encode())

            except Exception as e:
                print(f"Error receiving message from client {client_id}: {e}")
                break

        self.clients.pop(client_id)
        self.usernames.pop(client_id)

        if not connection.closed:
            connection.close()

        print(f"Client {client_id} disconnected")


if __name__ == '__main__':
    server = Server()
    server.wait_for_clients()
