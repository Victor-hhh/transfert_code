import socket

PORT = 12345

def server():
    HOST = '192.168.1.27'  # Raspberry Pi's IP address
    HOST2 = '192.168.37.1'  # Raspberry Pi's IP address
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on port {PORT}...")
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        request = client_socket.recv(1024)
        request_d = request.decode("utf-8")
        print(f"Received request: {request_d}")
        print("What is the temperature?")
        response = "25.5 °C"
        client_socket.sendall(response.encode("utf-8"))
        client_socket.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    server()
