import socket
import threading
import random

# Server configuration
HOST = 'localhost'
PORT = 12345
clients = []
panda_decorations = ["ʕ•ᴥ•ʔ", "ʕᵔᴥᵔʔ", "ʕ=(o)ᴥ(o)=ʔ", "ʕ0ᴥ0ʔ"]

# Function to broadcast messages to all clients
def broadcast(message, sender=None):
    decorated_message = f"{random.choice(panda_decorations)} {message} {random.choice(panda_decorations)}"
    for client in clients:
        if client != sender:    #Send to all client expect the sender, no duplicate messages.
            try:
                client.send(decorated_message.encode())
            except:
                client.close()
                clients.remove(client)

# function to handle individual client
def handle_client(client, addr):
    client.send("Welcome to the Panda Chat! ʕᵔᴥᵔʔ Please enter your panda name:".encode())
    panda_name = client.recv(1024).decode().strip()
    welcome_message = f"{panda_name} has joined the chat! ʕᵔᴥᵔʔ"
    print(welcome_message)
    #notify chat of new user
    broadcast(welcome_message, client)
    #append user to client list
    clients.append(client)  
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            if message.startswith("@"):
                process_command(client, message)
            else:
                broadcast(f"{panda_name}: {message}", client)
        except:
            break

    print(f"{panda_name} has left the chat.")
    clients.remove(client)
    client.close()
    #notify users of individual leaving chat
    broadcast(f"{panda_name} has left the chat.", None)

# Function to process special panda-themed commands
def process_command(client, message):
    if message.strip() == "@bamboo":
        client.send("ʕ •ᴥ•ʔ Pandas love munching on bamboo! Did you know they eat around 26–84 pounds a day? ʕ•ᴥ• ʔ".encode())
    elif message.strip() == "@grove":
        client.send("ʕ •ᴥ•ʔ Did you know? Pandas spend up to 14 hours a day eating bamboo! Enjoy your stay in the bamboo grove! ʕ•ᴥ• ʔ".encode())
    elif message.strip() == "@leaves":
        client.send("ʕ ᵔᴥᵔʔ Fun fact: Pandas have a special thumb-like bone to grip bamboo leaves better! ʕᵔᴥᵔ ʔ".encode())
    else:
        client.send("ʕ•ᴥ•ʔ Unknown command. Try @bamboo, @grove, or @leaves. ʕ•ᴥ•ʔ".encode())

# Start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("ʕ•ᴥ•ʔ Panda Chat Server is running...")

    while True:
        client, addr = server_socket.accept()
        print(f"New connection from {addr}")
        threading.Thread(target=handle_client, args=(client, addr)).start()

if __name__ == "__main__":
    start_server()
