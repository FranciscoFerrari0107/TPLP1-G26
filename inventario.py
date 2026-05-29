from deposito import Deposito
from proveedor import Proveedor


class Inventario:

    def __init__(self, deposito: Deposito):
        self.stockGondola = {}
        self.deposito = deposito
        self.proveedor = Proveedor()

    def agregarProducto(self, producto, cantGondola, cantDeposito):
        codigo = producto.get_codigo()
        self.stockGondola[codigo] = {
            "producto": producto,
            "cantidad": cantGondola
        }
        self.deposito.agregarProducto(codigo, cantDeposito)

    def decrementar(self, codigo):
        datos = self.stockGondola.get(codigo)

        if not datos:
            print("Producto no encontrado")
            return False

        if datos["cantidad"] <= 0:
            self.reponer(codigo)
            print("No hay stock")
            return False

        datos["cantidad"] -= 1
        self.reponer(codigo)

        return True

    def reponer(self, codigo):
        producto = self.stockGondola[codigo]["producto"]

        stockGondola = self.stockGondola[codigo]["cantidad"]
        stockDeposito = self.deposito.obtenerStock(codigo)

        umbralGondola = producto.get_stockMin()
        umbralDeposito = producto.get_depMin()

        if stockGondola < umbralGondola:
            faltanGondola = umbralGondola - stockGondola
            cantidadMovida = self.deposito.retirar(codigo, faltanGondola)

            self.stockGondola[codigo]["cantidad"] += cantidadMovida
            stockDeposito -= cantidadMovida

        if stockDeposito < umbralDeposito:
            faltanDeposito = umbralDeposito - stockDeposito
            self.genPedido(codigo, 2 * faltanDeposito)

    def genPedido(self, codigo, cantidad):
        producto = self.stockGondola[codigo]["producto"]

        pedido = {
            "codigo": codigo,
            "marca": producto.get_marca(),
            "nombre": producto.get_nombre(),
            "cantidad": cantidad
        }

        self.proveedor.procesarPedido(pedido)
        self.deposito.compra(pedido)