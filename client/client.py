import socket
import sys

from file import File


class Client:
    def __init__(self, server_address):
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.sock.connect(self.server_address)
        except socket.error as e:
            print(e)
            sys.exit(1)

    def start(self):
        self.connect()

        try:
            self.sock.settimeout(2)
            try:
                default = True
                while default:
                    data = File.readData("data/data1.json")
                    self.sock.sendall(data.encode("utf-8"))

                    res = self.sock.recv(4096)
                    print(res)
                    res_json = res.decode("utf-8")

                    if res_json:
                        default = False
                        print("Server response: " + res_json)
                    else:
                        break

            except TimeoutError:
                print("Socket timeout, ending listening for server messages")

        finally:
            print("closing socket")
            self.sock.close()


if __name__ == "__main__":
    server_address = "tmp/socket_file"
    client = Client(server_address)
    client.start()
