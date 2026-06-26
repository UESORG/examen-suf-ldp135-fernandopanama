[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/66UDLJ0P)
# Examen_Suficiencia_LDP2026
 E-Commerce Pro Backend - Complementario LDP

Este proyecto implementa las funciones del backend transaccional de un sistema de E-Commerce utilizando estructuras lógicas puras en Python y control estricto de sintaxis (AST).

## Descripción de Archivos

### 1. `carrito_pro.py`
Contiene las 6 funciones núcleo del sistema:
* **`importar_y_validar_orden`**: Decodificación segura de JSON controlando excepciones léxicas y lógicas de montos monetarios.
* **`gestionar_historial_carrito`**: Implementación de una estructura de datos tipo Pila (LIFO) usando mutación de listas por referencia.
* **`escanear_estanteria_bodega`**: Algoritmo de visión/mapeo matricial bidimensional 3x3 que respeta estrictamente los bordes físicos de la matriz.
* **`calcular_descuento_cascada`**: Algoritmo recursivo en árbol de decisión binario.
* **`ordenar_productos_quicksort`**: Algoritmo de ordenamiento QuickSort basado en pivotes y listas por comprensión.
* **`buscar_precio_binario`**: Algoritmo de búsqueda logarítmica de alta eficiencia temporal sobre colecciones previamente ordenadas.

### 2. `test_carrito_pro.py`
Conjunto de pruebas automatizadas con `pytest` que evalúan el comportamiento correcto de la lógica de negocio frente a flujos idóneos, entradas corruptas, estructuras vacías y colisiones en límites de índices.

## Cómo ejecutar las pruebas
Asegúrate de tener instalado el modulo `pytest`. En tu terminal ejecuta de la siguiente manera:
```bash
pytest test_carrito_pro.py
