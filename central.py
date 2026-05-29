from Productos.producto import Producto
from carrito import Carrito
from inventario import Inventario
from descuentos import Descuentos

class Central():

    def __init__(self, inventario: Inventario, carro: Carrito):
        self.inventario = inventario
        self.carro = carro
        self.descuentos = Descuentos(self.carro)

    def escaneo(self, prod: Producto):
        codigo = prod.get_codigo()
        if self.inventario.decrementar(codigo):
            self.carro.agregar(prod)

    def calcular_precio_final(self):
        return self.descuentos.aplicar_descuentos()
    
    def get_precio_con_descuento(self, prod: Producto):
        return self.descuentos.get_precio_con_descuento(prod)