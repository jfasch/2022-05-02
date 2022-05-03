import socket
import sys

PORT = int(sys.argv[1])


def incoming_data(port):
    portsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    portsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    portsock.bind(('127.0.0.1', PORT))
    portsock.listen()

    while True:
        connection, addr = portsock.accept()

        while True:
            data = connection.recv(10)
            if len(data) == 0:   # End-Of-File (EOF)
                break

            yield data

for data in incoming_data(PORT):
    print(data)

# POINT IS: decoupling of data prodiction and data consumption enables
# to test data consumption IN ISOLATION ...

# data_for_testing = [
#     b'seas oida\n',
#     b'hallo\n',
#     b'hello\n',
# ]
# for data in data_for_testing:
#     print(data)

    
