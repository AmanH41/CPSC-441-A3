import socket
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Define the server address and port to connect to
host = 'localhost'
port = 12345
# Connect to the server
client_socket.connect((host, port))
# Send data to the server
message = "Hello from the client!"
client_socket.send(message.encode())
# Receive the server's response
response = client_socket.recv(1024).decode()
print(f"Received from server: {response}")
# Close the connection
client_socket.close()