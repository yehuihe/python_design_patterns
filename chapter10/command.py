import os
import time

verbose = True


class RenameFile:

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def execute(self):
        if verbose:
            print(f"[renaming '{self.src}' to '{self.dst}']")
        if not os.path.exists(self.src):
            # TODO: update proper handling
            print(f"No such file or directory: '{self.src}'")
            raise FileNotFoundError()
        else:
            os.rename(self.src, self.dst)

    def undo(self):
        if verbose:
            print(f"[renaming '{self.dst}' back to '{self.src}']")
        os.rename(self.dst, self.src)


class CreateFile:

    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print(f"[creating file '{self.path}']")
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile:

    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print(f"[reading file '{self.path}']")
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


def delete_file(path):
    if verbose:
        print(f"deleting file {path}")
    if not os.path.exists(path):
        # TODO: update proper handling
        print(f"No such file or directory: '{path}'")
        raise FileNotFoundError()
    else:
        os.remove(path)


def main():

    orig_name, new_name = 'file1', 'file2'

    commands = (CreateFile(orig_name),
                ReadFile(orig_name),
                RenameFile(orig_name, new_name))

    [c.execute() for c in commands]

    answer = input('reverse the executed commands? [y/n]')

    if answer not in 'yY':
        print(f"the result is {new_name}")
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            print("Error", str(e))


if __name__ == '__main__':
    main()
