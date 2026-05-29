from Productos.producto import Producto

class Gondola:
    def __init__(self, producto: Producto):
        self.producto = producto

    def get_gondola(self):
        ubi_gon = self.producto.get_ubiGon()
        return ubi_gon