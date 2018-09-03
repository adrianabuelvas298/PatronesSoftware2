#Referencias: https://github.com/jackdbd/design-patterns/blob/master/prototype.py

import copy
from collections import OrderedDict

"""
Especificamos los tipos de objetos para crear usando una instancia
y crea nuevos objetos copiando ese prototipo.
"""

class Book:
    def __init__(self, name, authors, price, **kwargs):
        #Ejemplos de kwargs: editor, longitud, etiquetas, fecha de publicación
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(kwargs)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append("{}: {}".format(i, ordered[i]))
            if i == "price":
                mylist.append("$")
            mylist.append("\n")
        return "".join(mylist)
    
class Prototype: #Encapsulamos en un Factory
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr): # metodo para clonar
        found = self.objects.get(identifier)
        if not found:
            raise ValueError("Incorrect object identifier: {}".format(identifier))

            obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

def main():
    b1 = Book(
        name="The C Programming Language",
        authors=("Brian W. Kernighan", "Dennis M.Ritchie"),
        price=118,
        publisher="Prentice Hall",
        length=228,
        publication_date="1978-02-22",
        tags=("C", "programming", "algorithms", "data structures"),
    )

    prototype = Prototype()
    cid = "k&r-first"
    prototype.register(cid, b1)
    b2 = prototype.clone(
        cid,
        name="The C Programming Language (ANSI)",
        price=48.99,
        length=274,
        publication_date="1988-04-01",
        edition=2,
    )

    for i in (b1, b2):
        print(i)

    print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))


if __name__ == "__main__":
    main()
