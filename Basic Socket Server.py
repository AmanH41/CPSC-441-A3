import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Get local machine name
host = 'localhost'
port = 12345
# Bind to the port
server_socket.bind((host, port))
# Queue up to 5 requests
server_socket.listen(5)

print("Server listening...")

while True:
    # Establish a connection
    client, addr = server_socket.accept()
    print(f"Got a connection from {addr}")
    # Receive data from the client
    data = client.recv(1024).decode()
    print(f"Received '{data}' from the client")
    # Send a reply to the client
    client.send('Thank you for connecting'.encode())
    # Close the connection with the client
    client.close()
    break  # Remove this to keep the server running for multiple connections
