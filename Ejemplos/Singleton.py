#Referencias: https://github.com/jackdbd/design-patterns/blob/master/singleton.py

class Singleton(object):

    _instance = None

    def __init__(self, name):# El método __init__ inicializa la instancia.
        self.name = name # El método __init__ reinicia la instancia (la primera).
    # La instancia es la misma, por lo que los efectos del primer __init__ se pierden.
    def __new__(cls, *args):# El método __new__ crea una nueva instancia y la devuelve.
        if getattr(cls, "_instance") is None or cls != cls._instance.__class__:# El método __new__ NO crea una instancia y devuelve la primera.
            cls._instance = object.__new__(cls) # El método __new__ crea una nueva instancia porque es una clase diferente.
        return cls._instance

class Child(Singleton):
    def childmethod(self):
        pass

class GrandChild(Child):
    def grandchildmethod(self):
        pass

def main():
   
    s1 = Singleton("Sam")
    s2 = Singleton("Tom")
    
    c1 = Child("John")
    c2 = Child("Andy")
    g1 = GrandChild("Bob")
    
    print(s1.name, id(s1), s1)
    print(s2.name, id(s2), s2)
    print(c1.name, id(c1), c1)
    print(c2.name, id(c2), c2)
    print(g1.name, id(g1), g1)
    
    print("s1 is s2?")
    print(s1 is s2)
    print("s1 is c1?")
    print(s1 is c1)
    print("c1 is c2?")
    print(c1 is c2)
    print("c1 is g1?")
    print(c1 is g1)

if __name__ == "__main__":
    main()
