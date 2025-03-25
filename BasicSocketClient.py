import socket
import threading

HOST = 'localhost'
PORT = 12345

# Function to receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            #display messages in the group chat
            print(message)
        except:
            print("ʕ0ᴥ0ʔ Disconnected from the server.")
            break

# Start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Start thread to listen for messages
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        #user input
        message = input()
        if message.lower() == "exit":
            print("ʕ0ᴥ0ʔ Leaving the Panda Chat...")
            client_socket.close()
            break
        #send user message to server 
        client_socket.send(message.encode())

if __name__ == "__main__":
    start_client()
