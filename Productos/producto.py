from abc import ABC, abstractmethod

class Producto(ABC):

    def __init__(self, codigo, marca, nombre, precioB, stockMin, depMin, ubiGon, tipo):
        self.codigo = codigo
        self.marca = marca
        self.nombre = nombre
        self.precioB = precioB
        self.stockMin = stockMin
        self.depMin = depMin
        self.ubiGon = ubiGon
        self.tipo = tipo

    @abstractmethod
    def get_codigo(self):
        pass

    @abstractmethod
    def get_marca(self):
        pass

    @abstractmethod
    def get_nombre(self):
        pass

    @abstractmethod
    def get_precioB(self):
        pass

    @abstractmethod
    def get_stockMin(self):
        pass

    @abstractmethod
    def get_depMin(self):
        pass

    @abstractmethod
    def get_ubiGon(self):
        pass

    @abstractmethod
    def get_tipo(self):
        pass