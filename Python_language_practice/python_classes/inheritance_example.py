class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False


class FileStream(Stream):
    @staticmethod
    def read():
        print("Reading data from file.")


class NetworkStream(Stream):
    @staticmethod
    def read():
        print("Reading data from network.")


fs = FileStream()
ns = NetworkStream()

print(fs.opened)
fs.read()

ns.opened = True
print(ns.opened)
ns.read()
