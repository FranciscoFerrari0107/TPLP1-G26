class Deposito:

    def __init__(self):
        self.stock = {}

    def agregarProducto(self, codigo, cantidad):
        self.stock[codigo] = cantidad

    def obtenerStock(self, codigo):
        return self.stock.get(codigo)

    def retirar(self, codigo, cantidad):
        disponible = self.obtenerStock(codigo)
        retirado = min(disponible, cantidad)
        self.stock[codigo] -= retirado
        return retirado

    def actualizarStock(self, codigo, cantidad):
        self.stock[codigo] = self.obtenerStock(codigo) + cantidad

    def compra(self, pedido):
        self.actualizarStock(pedido["codigo"], pedido["cantidad"])