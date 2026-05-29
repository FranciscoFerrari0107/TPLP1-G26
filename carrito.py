from Productos.producto import Producto

class Carrito():

    def __init__(self):
        self.lista = []
        self.totalP = 0

    def agregar(self, prod: Producto):
        self.lista.append(prod)
        self.totalP += prod.get_precioB()

    def get_lista(self):
        return self.lista

    def mostrar_Total(self):
        print(f"Costo total sin descuentos: {self.totalP}")

    def get_totalP(self):
        return self.totalP