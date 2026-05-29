class Proveedor:

    def __init__(self):
        pass

    def procesarPedido(self, pedido):
        print("\nPedido enviado al proveedor")
        print(f"Código: {pedido['codigo']}")
        print(f"Marca: {pedido['marca']}")
        print(f"Producto: {pedido['nombre']}")
        print(f"Cantidad solicitada: {pedido['cantidad']}")