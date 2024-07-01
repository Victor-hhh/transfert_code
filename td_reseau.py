import socket

#question1
"""
host='192.168.158.174'
port=8081
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #configure a socket for TCP communication
s.bind((host, port)) # define the address
s.listen() #waiting for a request from a client
print(f"Server started, listening on {host}:{port}")
conn, addr = s.accept()
print(f"Connected by client : {addr}")
data = conn.recv(1024) # receiving client request
print(f"Received data: {data.decode()}")
conn.close()
s.close()
"""

#question2
"""
HOST = 'localhost'#127.0.0.1
PORT = 8080

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on port {PORT}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request:\n{request}")

        response = "HTTP/1.1 200 OK\nContent-Type: text/plain\nContent-Length: 12\n\nHello, World!"
        client_socket.sendall(response.encode('utf-8'))

        print("Hello message sent to the client")

        client_socket.close()
main()
"""
#question3 serveur client sur ce pc
import threading

HOST = '127.0.0.1'
PORT = 8080

def handle_client(client_socket, addr):
    print(f"Connection from {addr}")
    request = client_socket.recv(1024)
    request_d = request.decode("utf-8")
    print(f"Received request: {request_d}")
    print("What is the temperature ?")
    response = "25.5 °C"
    client_socket.sendall(response.encode("utf-8"))

    request2 = client_socket.recv(1024)
    request2_d = request2.decode("utf-8")
    print(f"c est qui: {request2_d}")
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on port {PORT}...")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST,PORT))
    client_port = client_socket.getsockname()[1]
    msg = "hello, world"
    client_socket.send(msg.encode("utf-8"))

    server_thread = threading.Thread(target=server_thread_func, args=(server_socket,))
    client_thread = threading.Thread(target=client_thread_func, args=(client_socket,))

    server_thread.start()
    client_thread.start()

def server_thread_func(server_socket):
    while True:
        client_socket, addr = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

def client_thread_func(client_socket):
    server_info = client_socket.getpeername()
    adr_server=server_info[0]
    port_server=server_info[1]
    print(f"getpeername :  ({adr_server},{port_server})")
    client_port = client_socket.getsockname()[1]
    print(f"getsockname : ({HOST},{client_port})")
    response = client_socket.recv(1024)
    response_d =response.decode("utf-8")
    print(f"Received response: temp = {response_d}")
    msg2 = "dudule"
    client_socket.send(msg2.encode("utf-8"))

if __name__ == "__main__":
    main()
