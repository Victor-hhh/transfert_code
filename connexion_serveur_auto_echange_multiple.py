import socket

HOSTc = '192.168.137.1'
PORT = 12345
HOSTs = '192.168.137.50'
#try except ConnectionRefusedError:

def main():
    try :
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOSTc,PORT))
        while True:
            message = input("msg ? (client)")
            print(f"client : {message}")
            client_socket.send(message.encode("utf-8"))
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"client : {message}")
    except TimeoutError or ConnectionRefusedError:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOSTs, PORT))
        server_socket.listen()
        client_socket, addr = server_socket.accept()
        print(f"Connection from {client_socket},{addr}")
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"client : {message}")
            message = input("msg ? (server)")
            print(f"server : {message}")
            client_socket.send(message.encode("utf-8"))
        client_socket.close()
main()