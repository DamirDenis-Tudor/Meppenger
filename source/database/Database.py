import os
import sqlite3
from collections import namedtuple
from datetime import datetime


class Database:
    User = namedtuple("User", ["Name", "Email", "Username", "Password"])

    CREATE_USER_TABLE_CMD = '''CREATE TABLE IF NOT EXISTS users (
                        Name VARCHAR(100) NOT NULL,
                        Email VARCHAR(100) NOT NULL,
                        Username VARCHAR(100) NOT NULL,
                        Password VARCHAR(100))'''

    INSERT_USER_CMD = '''INSERT INTO users(Name, Email, Username, Password)
                        VALUES (?, ?, ?, ?)'''

    SELECT_BY_USERNAME_CMD = '''SELECT * FROM users WHERE username=?'''
    SELECT_BY_PASSWORD_CMD = '''SELECT * FROM users WHERE password=?'''
    SELECT_BY_USERNAMES_CMD = '''SELECT username FROM users'''

    Message = namedtuple("Message", ["Sender", "Receiver", "Data", "Time"])

    CREATE_MESSAGE_TABLE_CMD = '''CREATE TABLE IF NOT EXISTS messages (
                    Sender VARCHAR(100) NOT NULL,
                    Receiver VARCHAR(100) NOT NULL,
                    Data VARCHAR(100) NOT NULL,
                    Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''

    INSERT_MESSAGE_CMD = '''INSERT INTO messages(Sender ,Receiver ,Data, Time)
                    VALUES (?, ? ,?, ?)'''

    GET_CONVERSATION_CMD = '''SELECT Data, Sender, Receiver, Time
                              FROM Messages
                              WHERE (Sender = ? AND Receiver = ?) OR (Sender = ? AND Receiver = ?)
                  ORDER BY Time ASC'''

    DELETE_USER_CMD = '''DELETE FROM users WHERE Username=?'''
    DELETE_MESSAGES_CMD = '''DELETE FROM messages'''
    DELETE_USERS_CMD = '''DELETE FROM users'''

    CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
    DATABASE_PATH = os.path.join(CURRENT_PATH, 'chatAppDatabase.db')

    def __init__(self):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            # initializam doua tabele unul pentru useri
            # si unul pentru mesaje
            cursor = db.cursor()
            cursor.execute(self.CREATE_USER_TABLE_CMD)
            cursor.execute(self.CREATE_MESSAGE_TABLE_CMD)
            cursor.close()

    def insert_message(self, sender, receiver, message):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.INSERT_MESSAGE_CMD,
                           (sender, receiver, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            cursor.close()

    def insert_user(self, name, email, username, password):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.INSERT_USER_CMD,
                           (name, email, username, password))
            cursor.close()

    def get_messages(self, sender, receiver):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            # mesajele vor fi returnate sub forma unui string
            # astfel backup-ul de conversatie va fi facil
            cursor = db.cursor()
            cursor.execute(self.GET_CONVERSATION_CMD, (sender, receiver, receiver, sender,))
            rows = cursor.fetchall()
            cursor.close()
            data = ""
            for row in rows:
                data += row[1] + f":({row[3]}):" + row[0] + "\n\n"
            return data

    def get_all_users(self):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.SELECT_BY_USERNAMES_CMD)
            rows = cursor.fetchall()
            cursor.close()
            data = ""
            for row in rows:
                data += row[0] + "-?|"
            data = data[:-1]
            return data

    def verify_username(self, username):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.SELECT_BY_USERNAME_CMD, (username,))
            rows = cursor.fetchall()
            cursor.close()
            if [self.User(*row) for row in rows]:
                return True
            return False

    def verify_password(self, password):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.SELECT_BY_PASSWORD_CMD, (password,))
            rows = cursor.fetchall()
            cursor.close()
            if [self.User(*row) for row in rows]:
                return True
            return False

    def delete_user(self, name):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.DELETE_USER_CMD, (name,))
            cursor.close()

    def delete_users(self):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.DELETE_USERS_CMD)
            cursor.close()

    def delete_messages(self):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.DELETE_MESSAGES_CMD)
            cursor.close()


if __name__ == '__main__':
    dataclasses = Database()
    print(dataclasses.get_all_users())
