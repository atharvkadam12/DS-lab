import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = input("Enter message from Client: ")
client.send(message.encode())

reply = client.recv(1024).decode()
print("Server:", reply)

client.close()