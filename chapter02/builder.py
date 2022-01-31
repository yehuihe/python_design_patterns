
from enum import Enum, auto
import time


class PizzaProgress(Enum):
    QUEUED = auto()
    PREPARATION = auto()
    BAKING = auto()
    READY = auto()


class PizzaDough(Enum):
    THIN = auto()
    THICK = auto()


class PizzaSauce(Enum):
    TOMATO = auto()
    CREME_FRAICHE = auto()


class PizzaTopping(Enum):
    MOZZARELLA = auto()
    DOUBLE_MOZZARELLA = auto()
    BACON = auto()
    HAM = auto()
    MUSHROOMS = auto()
    RED_ONION = auto()
    OREGANO = auto()


STEP_DELAY = 3  # in seconds for the sake of the example
# PizzaProgress = Enum('PizzaProgress', 'QUEUED PREPARATION BAKING READY')
# PizzaDough = Enum('PizzaDough', 'THIN THICK')
# PizzaSauce = Enum('PizzaSauce', 'TOMATO CREME_FRAICHE')
# PizzaTopping = Enum('PizzaTopping',
#                     'MOZZARELLA DOUBLE_MOZZARELLA BACON HAM MUSHROOMS RED_ONION OREGANO')
# STEP_DELAY = 3  # in seconds for the sake of the example


class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f'preparing the {self.dough.name} dough of your {self}...')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough')


class MargaritaBuilder:

    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.QUEUED
        self.baking_time = 5  # in seconds for the sake of the example

    def prepare_dough(self):
        self.progress = PizzaProgress.PREPARATION
        self.pizza.prepare_dough(PizzaDough.THIN)

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.TOMATO
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        topping_desc = 'double mozzarella, oregano'
        topping_items = (PizzaTopping.DOUBLE_MOZZARELLA, PizzaTopping.OREGANO)
        print(f'adding the topping ({topping_desc}) to your margarita')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping ({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.BAKING
        print(f'baking your margarita for {self.baking_time} seconds')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.READY
        print('your margarita is ready')


class CreamyBaconBuilder:

    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.QUEUED
        self.baking_time = 7  # in seconds for the sake of the example

    def prepare_dough(self):
        self.progress = PizzaProgress.PREPARATION
        self.pizza.prepare_dough(PizzaDough.THICK)

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.CREME_FRAICHE
        time.sleep(STEP_DELAY)
        print('done with the crème fraîche sauce')

    def add_topping(self):
        topping_desc = 'mozzarella, bacon, ham, mushrooms, red onion, oregano'
        topping_items = (PizzaTopping.MOZZARELLA,
                         PizzaTopping.BACON,
                         PizzaTopping.HAM,
                         PizzaTopping.MUSHROOMS,
                         PizzaTopping.RED_ONION,
                         PizzaTopping.OREGANO)
        print(f'adding the topping ({topping_desc}) to your creamy bacon')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping ({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.BAKING
        print(f'baking your creamy bacon for {self.baking_time} seconds')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.READY
        print('your creamy bacon is ready')


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        steps = (builder.prepare_dough,
                 builder.add_sauce,
                 builder.add_topping,
                 builder.bake)
        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        input_msg = 'What pizza would you like, [m]argarita or [c]reamy bacon? '
        pizza_style = input(input_msg)
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError:
        error_msg = 'Sorry, only margarita (key m) and creamy bacon (key c) are available'
        print(error_msg)
        return False, None
    return True, builder


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f'Enjoy your {pizza}!')


if __name__ == '__main__':
    main()
