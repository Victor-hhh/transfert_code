import socket
HOST = '192.168.137.1'
PORT = 12345

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on port {PORT}...")
    client_socket, addr = server_socket.accept()
    print(f"Connection from {client_socket},{addr}")
    request = client_socket.recv(1024)
    request_d = request.decode("utf-8")
    print(f"Received request: {request_d}")
    print("What is the temperature ?")
    response = "25.5 °C"
    client_socket.sendall(response.encode("utf-8"))
    client_socket.close()
main()