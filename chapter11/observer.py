
class Publisher:

    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print(f'Failed to add: {observer}')

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print(f'Failed to remove: {observer}')

    def notify(self):
        [o.notify(self) for o in self.observers]


class DefaultFormatter(Publisher):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self._data = 0

    def __str__(self):
        return f"{type(self).__name__}: '{self.name}' has data = {self._data}"

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        try:
            self._data = int(value)
        except ValueError as e:
            print(f'Error: {e}')
        else:
            self.notify()


class HexFormatterObs:
    def notify(self, publisher):
        value = hex(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now hex data = {value}")


class BinaryFormatterObs:
    def notify(self, publisher):
        value = bin(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now bin data = {value}")


class OctFormatterObs:
    def notify(self, publisher):
        value = oct(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now oct data = {value}")


def validate_format(observers):
    try:
        input_msg = 'What format for would you like, [h]exFormatterObs, [b]inaryFormatterObs, or [o]ctFormatterObs?'
        observer_format = input(input_msg)
        observer = observers[observer_format]()
        valid_input = True
    except KeyError:
        error_msg = 'Sorry, only hexadecimal (key h), binary (key b) and octal (key o) are available'
        print(error_msg)
        return False, None
    return True, observer


def validate_input():
    try:
        input_msg = 'What data for would you like to display? '
        data = int(input(input_msg))
        valid_input = True
    except ValueError:
        error_msg = 'Sorry, only integer are acceptable'
        print(error_msg)
        return False, None
    return True, data


def validate_opt(operations):
    try:
        input_msg = 'What operation for would you like, [a]dd, or [r]emove?'
        opt = input(input_msg)
        operation = operations[opt]
        valid_input = True
    except KeyError:
        error_msg = 'Sorry, only add (key a), and remove (key r) are available'
        print(error_msg)
        return False, None
    return True, operation


def main():
    # df = DefaultFormatter('test1')
    # print(df)
    #
    # print()
    # hf = HexFormatterObs()
    # df.add(hf)
    # df.data = 3
    # print(df)
    #
    # print()
    # bf = BinaryFormatterObs()
    # df.add(bf)
    # df.data = 21
    # print(df)
    #
    # print()
    # df.remove(hf)
    # df.data = 40
    # print(df)
    #
    # print()
    # df.remove(hf)
    # df.add(bf)
    #
    # df.data = 'hello'
    # print(df)
    #
    # print()
    # df.data = 15.8
    # print(df)

    # df = DefaultFormatter('test1')
    # print(df)
    #
    # print()
    # observers = dict(h=HexFormatterObs, b=BinaryFormatterObs, o=OctFormatterObs)
    # valid_input = False
    # while not valid_input:
    #     valid_input, observer = validate_format(observers)
    # print()
    #
    # operations = dict(a=df.add, r=df.remove)
    # valid_input = False
    # while not valid_input:
    #     valid_input, operation = validate_opt(operations)
    # operation(observer)
    # print()
    #
    # valid_input = False
    # while not valid_input:
    #     valid_input, data = validate_input()
    # df.data = data
    # print(df)

    OPERATION_IN_DESC = 'What operation for would you like, [a]ttach / [d]etach an observer, ' \
                        'or [m]odify the value? (type "quit" to exit) '

    OBSERVERS_IN_DESC = 'What format for would you like, [h]exFormatterObs, [b]inaryFormatterObs, ' \
                        'or [o]ctFormatterObs? '

    df = DefaultFormatter('test1')
    print(df)

    # TODO: Errors in menu flow
    while True:
        operation_picked = None
        operations = dict(a=df.add, d=df.remove)
        while not operation_picked:
            operation_picked = input(OPERATION_IN_DESC)

            if operation_picked == 'quit':
                print('bye')
                return

            observers_picked = None
            observers = dict(h=HexFormatterObs, b=BinaryFormatterObs, o=OctFormatterObs)
            while observers_picked not in observers.keys():
                observers_picked = input(OBSERVERS_IN_DESC)

                try:
                    observer = observers[observers_picked]()
                    if operation_picked in operations.keys():
                        operations[operation_picked](observer)
                    elif operation_picked == 'm':
                        valid_input = False
                        while not valid_input:
                            valid_input, data = validate_input()
                        df.data = data
                    print(df)
                except KeyError as err:
                    print(f'Incorrect option: {observers_picked}')


if __name__ == '__main__':
    main()
