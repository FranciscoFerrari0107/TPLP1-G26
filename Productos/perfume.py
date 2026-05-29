from Productos.producto import Producto

class Perfume(Producto):

    def __init__(self, codigo, marca, nombre, precioB, stockMin, depMin, ubiGon, tipo, litros, uso):
        super().__init__(codigo, marca, nombre, precioB, stockMin, depMin, ubiGon, tipo)
        self.uso = uso
        self.litros = litros

    def get_codigo(self):
        return self.codigo
    
    def get_marca(self):
        return self.marca
    
    def get_nombre(self):
        return self.nombre
    
    def get_precioB(self):
        return self.precioB
    
    def get_stockMin(self):
        return self.stockMin
    
    def get_depMin(self):
        return self.depMin
    
    def get_ubiGon(self):
        return self.ubiGon
    
    def get_tipo(self):
        return self.tipo
    
    def get_uso(self):
        return self.uso
    
    def get_litros(self):
        return self.litros