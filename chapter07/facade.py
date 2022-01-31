from enum import Enum, auto
from abc import ABCMeta, abstractmethod


class State(Enum):
    NEW = auto()
    RUNNING = auto()
    SLEEPING = auto()
    RESTART = auto()
    ZOMBIE = auto()


class User:
    pass


class Process:
    pass


class File:
    pass


class Server(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):

    def __init__(self):
        """actions required for initializing the file server"""
        self.name = 'FileServer'
        self.state = State.NEW

    def boot(self):
        """actions required for booting the file server"""
        print(f'booting the {self}')
        self.state = State.RUNNING

    def kill(self, restart=True):
        """actions required for killing the file server"""
        print(f'killing {self}')
        self.state = State.RESTART if restart else State.ZOMBIE

    @staticmethod
    def create_file(user, name, permissions):
        """check validity of permissions, user rights, etc."""
        print(f"trying to create the file '{name}' for user '{user}' with permissions {permissions}")


class ProcessServer(Server):

    def __init__(self):
        """actions required for initializing the process server"""
        self.name = 'ProcessServer'
        self.state = State.NEW

    def boot(self):
        """actions required for booting the process server"""
        print(f'booting the {self}')
        self.state = State.RUNNING

    def kill(self, restart=True):
        """actions required for killing the process server"""
        print(f'killing {self}')
        self.state = State.RESTART if restart else State.ZOMBIE

    @staticmethod
    def create_process(user, name):
        """check user rights, generate PID, etc."""
        print(f"trying to create the process '{name}' for user '{user}'")


class WindowServer(Server):

    def __init__(self):
        """actions required for initializing the window server"""
        self.name = 'WindowServer'
        self.state = State.NEW

    def boot(self):
        """actions required for booting the window server"""
        print(f'booting the {self}')
        self.state = State.RUNNING

    def kill(self, restart=True):
        """actions required for killing the window server"""
        print(f'killing {self}')
        self.state = State.RESTART if restart else State.ZOMBIE

    @staticmethod
    def create_window(user, name, window):
        """check user rights, generate a window, etc."""
        print(f"trying to create the window '{name}', for user '{user}' for window '{window}'")


class NetworkServer:
    pass


class OperatingSystem:
    """The Facade"""

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()
        self.ws = WindowServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps, self.ws)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)

    def create_window(self, user, name, window):
        return self.ws.create_window(user, name, window)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')
    os.create_window('foo', 'admin', 'Folder')


if __name__ == '__main__':
    main()
