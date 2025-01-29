# Librería computación cuantíca números complejos.

Este repositorio contiene una implementación en Python de funciones para realizar operaciones básicas con números complejos representados como tuplas.

## Descripción

Las funciones implementadas permiten realizar las siguientes operaciones con números complejos:

- **Suma** (`sumacplx`)
- **Resta** (`restacplx`)
- **Multiplicación** (`multcplx`)
- **División** (`divcplx`)
- **Cálculo del módulo** (`modcplx`)
- **Cálculo del conjugado** (`conjcplx`)

Cada número complejo se representa como una tupla `(a, b)`, donde `a` es la parte real y `b` es la parte imaginaria.

## Uso

Para utilizar las funciones, simplemente importa el módulo y llama a las funciones con los argumentos adecuados:

```python
# Ejemplo de uso
a = (3, 4)
b = (1, -2)

print(sumacplx(a, b)) 
print(restacplx(a, b))  
print(multcplx(a, b))  
print(divcplx(a, b)) 
print(modcplx(a))  
print(conjcplx(a))
```