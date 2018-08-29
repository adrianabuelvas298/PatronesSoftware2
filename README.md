# Patrones de diseño

## Introducción

Cada patrón describe un problema que ocurre una y otra vez en nuestro entorno y describe también el núcleo de 
la solución al problema, de forma que puede utilizarse un millón de veces sin tener que hacer dos veces lo mismo.

El diseño OO es difícil y el diseño de software orientado a objetos reutilizable lo es aún más.

Los diseñadores expertos no resuelven los problemas desde sus principios; reutilizan soluciones que han funcionado en el pasado.

* Se encuentran patrones de clases y objetos de comunicación recurrentes en muchos sistemas orientados a objetos.

* Estos patrones resuelven problemas de diseño específicos y hacen el diseño flexible y reusable.

## Clasificación de los patrones

**Según su propósito:**

* **De creación:** Conciernen al proceso de creación de objetos.

* **De estructura:** Tratan la composición de clases y/o objetos.

* **De comportamiento:** Caracterizan las formas en las que interactúan y reparten responsabilidades las distintas clases u objetos.

![imagen](/Imagenes/imagen1.PNG)

# Singleton

Utilizaremos el patrón Singleton cuando por alguna razón necesitemos que exista sólo una instancia **(un objeto)** de una determinada Clase.

Dicha clase se creará de forma que tenga una propiedad estática y un constructor privado, así como un método público estático que será el encargado de crear la instancia **(cuando no exista)** y guardar una referencia a la misma en la propiedad estática **(devolviendo ésta)**


![imagen](/Imagenes/imagen2.png)

[Ejemplo](Ejemplos/Singleton.py)


# Builder

**Problema y Contexto:**

Un único proceso de construcción debe ser capaz de construir distintos objetos complejos, abstrayéndonos de los detalles particulares de cada uno de los tipos.

**Se aplica cuando:**

* Nuestro sistema trata con objetos complejos (compuestos por muchos atributos) pero el número de configuraciones es limitada.
* El algoritmo de creación del objeto complejo puede independizarse de las partes que lo componen y del ensamblado de las mismas.

![imagen](/Imagenes/imagen3.png)

[Ejemplo](Ejemplos/builder.py)

# Factory

**Problema y Contexto:**

Crear diferentes familias de objetos abstrayéndonos de los detalles de su creación.

**Se aplica cuando:**

* Hay previsión de que se incluirán nuevas familias de objetos.
* Existe dependencia (teórica) entre los tipos de objetos

![imagen](/Imagenes/imagen4.png)

[Ejemplo](Ejemplos/factory.py)

# Prototype

El patrón prototype tiene un objetivo muy sencillo: crear a partir de un modelo.Permite crear objetos prediseñados sin conocer detalles de cómo crearlos. Esto lo logra especificando los prototipos de objetos a crear. Los nuevos objetos que se crearán de los prototipos, en realidad, son clonados. Vale decir, tiene como finalidad crear nuevos objetos duplicándolos, clonando una instancia creada previamente.

## Cuando utilizar este patrón:

* Aplica en un escenario donde sea necesario la creación de objetos parametrizados como "recién salidos de fábrica" ya listos para utilizarse, con la gran ventaja de la mejora de la performance: clonar objetos es más rápido que crearlos y luego setear cada valor en particular.

* Este patrón debe ser utilizado cuando un sistema posea objetos con datos repetitivos, en cuanto a sus atributos: por ejemplo, si una biblioteca posee una gran cantidad de libros de una misma editorial, mismo idioma, etc. Hay que pensar en este patrón como si fuese un fábrica que tiene ciertas plantillas de ejemplos de sus prodcutos y, a partir de estos prototipos, puede crear una gran cantidad de productos con esas características.

![imagen](/Imagenes/imagen5.png)

[Ejemplo](Ejemplos/prototype.py)

# Bibliografía

* https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
* https://gist.github.com/pazdera/1122366
* https://programacion.net/articulo/patrones_de_diseno_iii_patrones_de_creacion_builder_1002
* https://gist.github.com/pazdera/1121157
* https://informaticapc.com/patrones-de-diseno/singleton.php
* https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
