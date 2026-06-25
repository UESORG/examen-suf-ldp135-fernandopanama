import json

def importar_y_validar_orden(json_orden):
    try:
        data = json.loads(json_orden)
        if "items" not in data or "total" not in data:
            raise KeyError("Faltan llaves obligatorias")
        if data["total"] <= 0:
            raise ValueError("El total debe ser mayor a 0")
        resultado = data
        return resultado
    except (json.JSONDecodeError, KeyError, ValueError):
        return None

def gestionar_historial_carrito(historial_pila, accion, item=None):
    if accion == "AGREGAR":
        historial_pila.append(item)
        return None
    elif accion == "DESHACER":
        if len(historial_pila) > 0:
            item_extraido = historial_pila.pop()
            return item_extraido
        return None
    return None

def escanear_estanteria_bodega(matriz_bodega, fila_centro, col_centro):
    unos_encontrados = 0
    filas = len(matriz_bodega)
    columnas = len(matriz_bodega[0]) if filas > 0 else 0
    
    for i in range(fila_centro - 1, fila_centro + 2):
        for j in range(col_centro - 1, col_centro + 2):
            if 0 <= i < filas and 0 <= j < columnas:
                if matriz_bodega[i][j] == 1:
                    unos_encontrados += 1
                    
    return unos_encontrados

def calcular_descuento_cascada(nodo_descuento):
    if "porcentaje_final" in nodo_descuento:
        res_base = nodo_descuento["porcentaje_final"]
        return res_base
        
    if nodo_descuento.get("cliente_frecuente") is True:
        res_der = calcular_descuento_cascada(nodo_descuento["derecha"])
        return res_der
    else:
        res_izq = calcular_descuento_cascada(nodo_descuento["izquierda"])
        return res_izq

def ordenar_productos_quicksort(lista_items):
    if len(lista_items) <= 1:
        return lista_items
        
    pivote = lista_items[0]
    precio_pivote = pivote["precio"]
    
    menores = [x for x in lista_items[1:] if x["precio"] <= precio_pivote]
    mayores = [x for x in lista_items[1:] if x["precio"] > precio_pivote]
    
    lista_ordenada = ordenar_productos_quicksort(menores) + [pivote] + ordenar_productos_quicksort(mayores)
    return lista_ordenada

def buscar_precio_binario(lista_ordenada, precio_buscado):
    inicio = 0
    fin = len(lista_ordenada) - 1
    indice_resultado = -1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        precio_actual = lista_ordenada[medio]["precio"]
        
        if precio_actual == precio_buscado:
            indice_resultado = medio
            return indice_resultado
        elif precio_actual < precio_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
            
    return indice_resultado