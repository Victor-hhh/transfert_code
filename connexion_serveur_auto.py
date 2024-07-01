import socket


PORT = 12345

def main():
    try:
        HOST = '192.168.137.1'
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST,PORT))
        client_port = client_socket.getsockname()[1]
        msg = "hello, world"
        client_socket.send(msg.encode("utf-8"))
        server_info = client_socket.getpeername()
        adr_server=server_info[0]
        port_server=server_info[1]
        print(f"getpeername :  ({adr_server},{port_server})")
        print(f"getsockname : ({HOST},{client_port})")
        response = client_socket.recv(1024)
        response_d =response.decode("utf-8")
        print(f"Received response: temp = {response_d}")
    

    except TimeoutError  or ConnectionRefusedError:
        HOST = '192.168.137.50'
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