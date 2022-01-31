
quotes = (
    'A man is not complete until he is married. Then he is finished.',
    'As I said before, I never repeat myself.',
    'Behind a successful man is an exhausted woman.',
    'Black holes really suck...',
    'Facts are stubborn things.'
)


class QuoteModel:

    @staticmethod
    def get_quote(n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found!'
        return value


class QuoteTerminalView:

    @staticmethod
    def show(quote):
        print(f'And the quote is: "{quote}"')

    @staticmethod
    def error(msg):
        print(f'Error: {msg}')

    @staticmethod
    def select_quote():
        return input('Which quote number would you like to see? ')


class QuoteTerminalController:

    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error(f"Incorrect index '{n}'")
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
