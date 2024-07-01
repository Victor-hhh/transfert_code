import socket

HOST = '192.168.137.1'
PORT = 12345

def main():
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
main()