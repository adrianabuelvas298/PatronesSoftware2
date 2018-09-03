# Referencias: https://github.com/jackdbd/design-patterns/blob/master/builder.py

"""
El patrón Builder separa la construcción de un objeto complejo de su
representación para que el mismo proceso de construcción pueda crear diferentes
representaciones.
"""
from abc import ABC, abstractmethod


class IceCream(ABC):
    # Clase abstracta

    @property
    def need_spoon(self):
        return False

    def __str__(self):
        string = self.__class__.__name__
        for key, value in self.__dict__.items():
            string += "\n{}: {}".format(key, value)
        string += "\n"
        return string


class ConeIceCream(IceCream):
    """Concrete Product 1."""

    pass


class CupIceCream(IceCream):
    """Concrete Product 2."""

    @property
    def need_spoon(self):
        return True


class Builder(ABC):
    """
    Especifique la interfaz abstracta que crea todas las partes del producto.
    Esta interfaz abstracta es utilizada por un objeto Director. Todos los métodos excepto
    "get_product" regresa a sí mismo, por lo que esta clase es una "interfaz fluida".
    """

    @abstractmethod
    def __init__(self):
        self.product = None
        self.toppings = None

    def set_flavors(self, flavors):
        self.product.flavors = flavors
        return self

    def set_toppings(self):
        if self.toppings is not None:
            self.product.toppings = self.toppings
        return self

    def add_spoon(self):
        if self.product.need_spoon:
            self.product.spoon = 1
        return self

    def get_product(self):
        return self.product


class ConeIceCreamBuilder(Builder):
    """Concrete Builder 1.
    Esta clase ensambla el producto implementando la interfaz de Builder.
    Define y realiza un seguimiento de la representación que crea.
    """

    def __init__(self):
        # super().__init__()  # ok in Python 3.x, not in 2.x
        super(self.__class__, self).__init__()  # also ok in Python 2.x
        self.product = ConeIceCream()
        self.toppings = "hazelnuts"


class CupIceCreamBuilder(Builder):
    """Concrete Builder 2.
    Esta clase ensambla el producto implementando la interfaz de Builder.
    Define y realiza un seguimiento de la representación que crea.
    """

    def __init__(self):
        # super().__init__()  # ok in Python 3.x, not in 2.x
        super(self.__class__, self).__init__()  # also ok in Python 2.x
        self.product = CupIceCream()
        self.toppings = "chocolate chips"


class Director(object):
    """Construye un objeto usando la interfaz de Builder"""

    def __init__(self, builder):
        self.builder = builder

    def build_product(self, flavors):
        """
        Prepare el producto y finalmente devuélvalo al cliente.
        La clase de Constructor definida anteriormente es una "interfaz fluida", por lo que podemos usar
        método de encadenamiento
        Parámetros
        ----------
        flavors: lista
        return
        -------
        ConeIceCream o CupIceCream
        """
        return (
            self.builder.set_flavors(flavors).set_toppings().add_spoon().get_product()
        )


# Client: crea un objeto Director y lo configura con un objeto Builder.


def main():
    director = Director(ConeIceCreamBuilder())
    product = director.build_product(["chocolate", "vanilla", "banana"])
    print(product)

    director = Director(CupIceCreamBuilder())
    product = director.build_product(["lemon", "strawberry"])
    print(product)

    builder = ConeIceCreamBuilder()
    director = Director(builder)
    builder.toppings = None  # El ConeIceCreamBuilder no tiene más ingredientes!
    product = director.build_product(["chocolate", "vanilla", "banana"])
    print(product)


if __name__ == "__main__":
    main()
