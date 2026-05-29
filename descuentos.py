class Descuentos:
    def __init__(self, carrito):
        self.carrito = carrito

    def ordenar_por_precio_menor_a_mayor(self, lista_productos):
        lista_ordenada = []

        for producto in lista_productos:
            lista_ordenada.append(producto)

        for i in range(len(lista_ordenada)):
            for j in range(i + 1, len(lista_ordenada)):
                if lista_ordenada[j].get_precioB() < lista_ordenada[i].get_precioB():
                    aux = lista_ordenada[i]
                    lista_ordenada[i] = lista_ordenada[j]
                    lista_ordenada[j] = aux

        return lista_ordenada

    def aplicar_descuentos(self):
        productos = self.carrito.get_lista()

        total = 0
        descuento = 0

        galletitas = []
        gaseosas = []
        perfumes = []

        for producto in productos:
            total += producto.get_precioB()

            codigo = producto.get_codigo()

            if codigo.startswith("GL"):
                galletitas.append(producto)

            elif codigo.startswith("GS"):
                gaseosas.append(producto)

            elif codigo.startswith("PF"):
                perfumes.append(producto)

        for producto in perfumes:
            descuento += producto.get_precioB() * 0.5

        galletitas_ordenadas = self.ordenar_por_precio_menor_a_mayor(galletitas)
        cantidad_gratis = len(galletitas_ordenadas) // 2

        for i in range(cantidad_gratis):
            descuento += galletitas_ordenadas[i].get_precioB()

        gaseosas_por_marca = {}

        for producto in gaseosas:
            marca = producto.get_marca()

            if marca not in gaseosas_por_marca:
                gaseosas_por_marca[marca] = []

            gaseosas_por_marca[marca].append(producto)

        for marca in gaseosas_por_marca:
            productos_misma_marca = gaseosas_por_marca[marca]
            productos_ordenados = self.ordenar_por_precio_menor_a_mayor(productos_misma_marca)

            cantidad_con_descuento = len(productos_ordenados) // 2

            for i in range(cantidad_con_descuento):
                descuento += productos_ordenados[i].get_precioB() * 0.3

        total_final = total - descuento

        return total_final