import socket
import threading
import colorama
from colorama import Fore

PORT = 5051
SERVER = "192.168.1.101"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client_list = []
names = []

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

nickname = input("\nPlease enter your nickname: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == "NICKNAME":
                client.send(nickname.encode(FORMAT))
            else:
                print(message)
        except:
            print("[SERVER] Thanks for chatting, goodbye!")
            client.close()
            break

def send_message():
    while True:
        message = input()
        if message == DISCONNECT_MESSAGE:
            client.send(f"[MEMBER LEFT] {nickname} has left the chatroom.".encode(FORMAT))
            client.close()
        else:
            message_with_name = f"{nickname}: {message}"
            client.send(message_with_name.encode(FORMAT))

receiving_thread = threading.Thread(target=receive)
receiving_thread.start()

sending_thread = threading.Thread(target=send_message)
sending_thread.start()