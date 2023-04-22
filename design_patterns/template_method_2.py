from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Class Abstract """

    def prepare(self):
        """ Template Method """
        self.hook_before_add_ingredients()  # Hook no obligatory
        self.add_ingredients()  # Abstract
        self.hook_after_add_ingredients()  # Hook no obligatory
        self.cook()  # Abstract
        self.cut()  # Concretos
        self.server()  # Concretos

    def hook_before_add_ingredients(self): pass
    def hook_after_add_ingredients(self): pass

    def cut(self):
        print('Cutting the pizza')

    def server(self):
        print('Serving the pizza')

    @abstractmethod
    def add_ingredients(self): pass

    @abstractmethod
    def cook(self): pass


class StylishPizza(Pizza):
    def add_ingredients(self):
        print('StylishPizza - adding ingredients: ham, cheese, tomato')

    def cook(self):
        print('StylishPizza - cook for 45min in a wood oven')


class VeganPizza(Pizza):
    def hook_before_add_ingredients(self):
        print('VeganPizza - washing ingredients')

    def add_ingredients(self):
        print('VeganPizza - adding ingredients: broccoli, green-corn, tomato')

    def cook(self):
        print('VeganPizza - cook for 5min in a common oven')


if __name__ == "__main__":
    stylish_pizza = StylishPizza()
    stylish_pizza.prepare()

    print()

    vegan_pizza = VeganPizza()
    vegan_pizza.prepare()
