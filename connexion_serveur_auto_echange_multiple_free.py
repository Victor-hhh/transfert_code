import socket
import threading

PORT = 12345

def ecoute(host, port):
    while true:
        server_socket.listen()
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        request_d = request.decode("utf-8")
        print(request_d)

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
        #appel de la fc threading
        while True:
            response = input()
            client_socket.sendall(response.encode("utf-8"))
        client_socket.close()  #ça sert à rien ici 
main()