class Plant:  # Superclass
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


class Flower(Plant):  # Subclass - Syntax = Subclass(Superclass)
    def __init__(self, color, petals):
        Plant.__init__(self, color)

        self.__petals = petals

    def get_petals(self):
        return self.__petals

        # petals is specific only to the Flower Class
