from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    pedido_procesado = []
    while not pedidos.empty():
        pedido = pedidos.get()
        pedido_procesado.append({'id':pedido['id'], 'cliente':pedido['cliente'], 'productos':{}, 'precio_total':0, 'estado':'completo'})
        for producto in pedido['productos']:
            if stock_productos[producto] > pedido['productos'][producto]:
                cantidad_vendida = pedido['productos'][producto]
            else:
                cantidad_vendida = stock_productos[producto]
            stock_productos[producto] -= cantidad_vendida
            pedido_procesado[-1]['productos'][producto] = cantidad_vendida
            if cantidad_vendida < pedido['productos'][producto]:
                pedido_procesado[-1]['estado'] = 'incompleto'
            pedido_procesado[-1]['precio_total'] += cantidad_vendida * precios_productos[producto]
    return pedido_procesado


if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input  
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}