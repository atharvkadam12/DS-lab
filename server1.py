import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def handle_client(conn, addr):
    print(f"\nConnected by {addr}")

    # Receive message from client
    client_message = conn.recv(1024).decode()
    print(f"Client {addr}: {client_message}")

    # Server reply
    server_message = input(f"Reply to {addr}: ")
    conn.send(server_message.encode())

    conn.close()
    print(f"Connection closed with {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Multi-client server is running...")

while True:
    conn, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )
    thread.start()