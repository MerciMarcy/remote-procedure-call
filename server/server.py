import socket
import os
import json

from process import Process


class Server:
    def __init__(self, server_address):
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    def connect(self):
        try:
            os.unlink(self.server_address)
        except FileNotFoundError:
            pass

        self.sock.bind(self.server_address)
        self.sock.listen(1)

    def req_process(self, conn):
        try:
            data = conn.recv(4096)
            data_json = data.decode("utf-8")
            req = json.loads(data_json)
            print(f"Request: {req}")

            method = req["method"]
            params = req["params"]
            id = req["id"]

            process = Process(method, params)
            result = process.execute()

            res = {}
            res["result"] = result
            res["result_type"] = type(result).__name__
            res["id"] = id

            res_json = json.dumps(res)
            conn.sendall(res_json.encode("utf-8"))
        except json.JSONDecodeError as e:
            print(e)

    def start(self):
        self.connect()

        print("Starting up on {}".format(self.server_address))

        while True:
            connection, client_address = self.sock.accept()
            try:
                while True:
                    print("connection from ", client_address)
                    self.req_process(connection)
            finally:
                print("Closing current connection")
                connection.close()


if __name__ == "__main__":
    server_address = "tmp/socket_file"
    server = Server(server_address)
    server.start()
