import socket

# initilize parameter
BACK_LOG = 5
BUFFER_SIZE = 4096

# get hostname and port
host = socket.gethostname()
port = 4002

# print host IP address
hostIP = socket.gethostbyname(host)
print("Prison tcp server, version 0.0.1")
print("Listening on port: " + str(port))

# init tcp server
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket object
tcpServer.bind((host, port))  # bind port number
tcpServer.listen(BACK_LOG)  # set max connect number, if timeout aline


class Connection:
    name = ''
    type = ''
    ip = ''
    port = 0
    online = 0
    max_online = 0

    is_online = True

    def __init__(self, d):
        print(d)
        self.name = d[0]
        self.type = d[1]
        self.ip = d[2]
        self.port = d[3]
        self.max_online = d[4]
        self.online = d[5]

    def get_server_name(self):
        return self.name


connections = {}

while True:
    for c in connections:
        print(connections[c].online)

    try:
        conn, addr = tcpServer.accept()
    except KeyboardInterrupt:
        print('Closing Server...')
        tcpServer.close()
        break

    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    data = conn.recv(BUFFER_SIZE).decode('utf-8')

    # send encoded data to client
    conn.send(data.encode('utf-8'))
    # splitting data
    split = data.split(":")
    # create connection with decoded data
    connections[split[0]] = Connection(split)
    # close connection, why not tho..
    conn.close()
