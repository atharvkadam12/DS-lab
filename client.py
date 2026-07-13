import socket

HOST = '127.0.0.1'   # Server IP
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Client sends message first
client_message = input("Enter message from Client: ")
client.send(client_message.encode())

# Receive reply from server
server_message = client.recv(1024).decode()
print("Server:", server_message)

client.close()