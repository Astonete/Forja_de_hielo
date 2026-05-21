# Forja_de_hielo
- Crear desde cero un juego en Python centrado en POO:
    El objetivo es desarrollar un videojuego desde cero utilizando Python y Programación Orientada a Objetos (POO).
    
    Con:
        -> Clases bien diseñadas:
            - estructurar un proyecto de forma escalable: "capaz de crecer"
            - ordenada: (ciclo principal de ejecución game loop)
            - mantenible: crecer sin romper su estructura.
        -> Herencia
        -> Polimorfismo
        -> Encapsulamiento: Proteger el estado interno y la lógica
        -> Abstraccion: al menos una clase abstracta que funcione como contrato del sistema
        -> Y un game loop modular y extensible

El objetivo evaluar la capacidad de diseñar sistemas mediante clases, más que la temática del juego en sí.

El proyecto debe implementar los pilares fundamentales de la POO: abstracción, herencia, polimorfismo y encapsulamiento. También debe incluir un ciclo principal de ejecución controlado por una clase central encargada de coordinar el funcionamiento del juego.

El código debe estar organizado de forma modular, separando entidades, lógica y consola, evitando estructuras desordenadas o lógica fuera de las clases. Además, se valora que el sistema sea escalable y fácil de extender.

1. Clase Game o motor principal

    - Debe existir una clase encargada de:
        - Inicializar el juego.
        - Controlar el ciclo principal de ejecución.
        - Coordinar las interacciones entre objetos.
        - Determinar cuándo termina la partida.
    La lógica principal no debe quedar dispersa fuera de esta clase.

2. Organización y modularización

    - El proyecto debe dividirse en tres áreas principales:

Dominio

    - Contiene entidades, reglas y lógica del juego.

3.Motor

    - Incluye la clase Game y la coordinación general del sistema.

4.Interfaz de consola

    -Se encarga de mostrar información al usuario y leer entradas.

4.Prácticas prohibidas
    - Colocar todo el código en un único archivo desorganizado.
    - Dejar reglas importantes dentro del main mediante condicionales aislados.
    - Acceder directamente a atributos internos desde fuera de las clases.