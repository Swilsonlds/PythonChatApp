import socket
import threading

# General information that is used to bind a socket to my local IP address
# and designate which port will be used
PORT = 5051
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client_list = []
client_names = []

# Binding the socket object "server" to my local IP address and identifying 
# the port that will be used
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen(2)

# This function will send a message to all clients in the chatroom except the
# person who sent the message
def broadcast_message_minus_sender(message, conn):
    for client in client_list:
        if conn != client:
            client.send(message)
        else:
            continue

# This function will send a message to all clients connected to the server
def broadcast_message_to_all(message):
    for client in client_list:
        client.send(message)

# This function receives messages from clients, and uses the "broadcast_message_minus_sender"
# function above to send the messages to the appropriate recipients.
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast_message_minus_sender(message, client)
        except:
            index = client_list.index(client)
            client_list.remove(client)
            client.close()
            nickname = client_names[index]
            client_names.remove(nickname)
            break

# This function saves the info of each new client to a list and calls the above functions
# when necessary to make the chatroom function
def start():
    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {str(addr)}")

        conn.send("NICKNAME".encode(FORMAT))
        nickname = conn.recv(1024).decode(FORMAT)
        client_names.append(nickname)
        client_list.append(conn)

        broadcast_message_to_all(f"[NEW MEMBER] {nickname} has joined the server".encode(FORMAT))    

        # The "handle_client" function is running in a separate thread so that the server is always
        # ready to receive messages from any of the clients.
        thread = threading.Thread(target=handle_client, args=(conn,))
        thread.start()

print("Server is up and awaiting clients...")
start()

