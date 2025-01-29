def sumacplx (x: tuple, y: tuple) -> tuple:
    """ La función calcula la suma de números complejos."""
    return ((x[0] + y[0], x[1] + y[1]))

def restacplx (x: tuple, y: tuple) -> tuple:
    """ La función calcula la resta de números complejos."""
    return ((x[0] - y[0], x[1] - y[1]))

def multcplx (x: tuple, y: tuple) -> tuple:
    """La función calcula la multiplicación de números complejos."""
    return (((x[0] * y[0]) - (x[1] * y[1]), (x[0] * y[1]) + (y[0] * x[1])))

def divcplx (x: tuple, y: tuple) -> tuple:
    """ La función calcula la división de números complejos."""
    leftdiv = ((x[0] * y[0]) + (x[1] * y[1])) / ((y[0]) ** 2 + (y[1]) ** 2)
    rightdiv = ((y[0] * x[1]) - (x[0] * y[1])) / ((y[0]) ** 2 + (y[1]) ** 2)
    return (leftdiv, rightdiv)

def modcplx(x: tuple) -> float:
    """ La función calcula el módulo de un número complejo"""
    return (((x[0]) ** 2 + (x[1]) ** 2) ** (1/2))

def conjcplx(x: tuple) -> tuple:
    """La función calcula el conjuado de un número complejo"""
    lista = list(x)
    lista[1] = lista[1] * -1
    return (tuple(lista))
