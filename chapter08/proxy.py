
class SensitiveInfo:

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        nb = len(self.users)
        print(f"There are {nb} users: {' '.join(self.users)}")

    def add(self, user):
        self.users.append(user)
        print(f'Added user {user}')

    def remove(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f'Removed user {user}')
        else:
            print(f'User {user} cannot be found, please try again...')


class Info:
    """protection proxy to SensitiveInfo"""

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret?')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")

    def remove(self, user):
        sec = input('what is the secret?')
        self.protected.remove(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()

    while True:
        print('1. read list |==| 2. add user |==| 3. remove user |==| 4. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            name = input('choose username: ')
            info.remove(name)
        elif key == '4':
            exit()
        else:
            print(f'unknown option: {key}')


if __name__ == '__main__':
    main()
