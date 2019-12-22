import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
clients = []


def start_server(port):
    host = socket.gethostname()
    sock.bind((host, int(port)))
    print("Server start\t")
    sock.listen(5)
    print("Listen\t")
    return port


start_server(12345)

while True:
    conn, addr = sock.accept()
    print("адрес подключения", addr)
    conn.send("You are connect".encode("utf-8"))
    data = conn.recv(2048)
    print("msg from client: " + str(data))

    if addr != clients:
        clients.append(addr)
        print(clients)

    for client in clients:
        if client != addr:
            conn.sendto(data, addr)
        else:
            print("данные else", data.decode("utf-8"))

    if str(data) == "Stop":
        print("Connection Close")
        break
