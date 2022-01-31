
class Musician:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the musician {self.name}'

    @staticmethod
    def play():
        return 'plays music'


class Dancer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the dancer {self.name}'

    @staticmethod
    def dance():
        return 'does a dance performance'
