import pytest
from carrito_pro import (
    importar_y_validar_orden,
    gestionar_historial_carrito,
    escanear_estanteria_bodega,
    calcular_descuento_cascada,
    ordenar_productos_quicksort,
    buscar_precio_binario
)

# 1. Tests para importar_y_validar_orden
def test_importar_y_validar_orden_valido():
    json_valido = '{"items": ["p1", "p2"], "total": 150.5}'
    res = importar_y_validar_orden(json_valido)
    assert res is not None
    assert res["total"] == 150.5

def test_importar_y_validar_orden_invalido():
    json_corrupto = '{"items": ["p1"]}'  # Falta total
    assert importar_y_validar_orden(json_corrupto) is None
    
    json_negativo = '{"items": ["p1"], "total": -10}'
    assert importar_y_validar_orden(json_negativo) is None

# 2. Tests para gestionar_historial_carrito
def test_gestionar_historial_carrito():
    pila = []
    gestionar_historial_carrito(pila, "AGREGAR", "producto_A")
    gestionar_historial_carrito(pila, "AGREGAR", "producto_B")
    assert pila == ["producto_A", "producto_B"]
    
    removido = gestionar_historial_carrito(pila, "DESHACER")
    assert removido == "producto_B"
    assert pila == ["producto_A"]
    
    gestionar_historial_carrito(pila, "DESHACER")
    assert gestionar_historial_carrito(pila, "DESHACER") is None

# 3. Tests para escanear_estanteria_bodega
def test_escanear_estanteria_bodega():
    matriz = [
        [1, 0, 1],
        [0, 1, 0],
        [0, 0, 1]
    ]
    # Centro perfecto
    assert escanear_estanteria_bodega(matriz, 1, 1) == 4
    # Límites superiores izquierdos (esquina)
    assert escanear_estanteria_bodega(matriz, 0, 0) == 2

# 4. Tests para calcular_descuento_cascada
def test_calcular_descuento_cascada():
    arbol = {
        "cliente_frecuente": True,
        "derecha": {
            "porcentaje_final": 15
        },
        "izquierda": {
            "cliente_frecuente": False,
            "izquierda": {
                "porcentaje_final": 5
            },
            "derecha": None
        }
    }
    assert calcular_descuento_cascada(arbol) == 15

# 5. Tests para ordenar_productos_quicksort
def test_ordenar_productos_quicksort():
    productos = [
        {"nombre": "A", "precio": 50},
        {"nombre": "B", "precio": 10},
        {"nombre": "C", "precio": 30}
    ]
    ordenados = ordenar_productos_quicksort(productos)
    assert ordenados[0]["precio"] == 10
    assert ordenados[1]["precio"] == 30
    assert ordenados[2]["precio"] == 50

# 6. Tests para buscar_precio_binario
def test_buscar_precio_binario():
    lista_ordenada = [
        {"precio": 10},
        {"precio": 30},
        {"precio": 50}
    ]
    assert buscar_precio_binario(lista_ordenada, 30) == 1
    assert buscar_precio_binario(lista_ordenada, 100) == -1