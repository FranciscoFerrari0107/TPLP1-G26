import sys
import csv
from collections import Counter

ruta_code = r"C:\Favaloro\2026\labo_p_1\TP final\Code F"
archivo_csv = r"C:\Favaloro\2026\labo_p_1\TP final\Code F\productos_supermercado_3xcategoria.csv"

sys.path.insert(0, ruta_code)

from Productos.alimentogato import AlimentoGato
from Productos.carne import Carne
from Productos.fiambre import Fiambre
from Productos.fideos import Fideos
from Productos.galletita import Galletita
from Productos.gaseosa import Gaseosa
from Productos.panaderia import Panaderia
from Productos.perfume import Perfume
from Productos.verdura import Verdura

from deposito import Deposito
from inventario import Inventario
from carrito import Carrito
from central import Central
from descuentos import Descuentos

ROJO = "\033[91m"
AZUL = "\033[94m"
RESET = "\033[0m"
NEGRITA = "\033[1m"

def texto(valor):
    if valor is None:
        return ""
    return valor.strip()

def convertir_float(valor):
    valor = texto(valor)

    if valor == "":
        return 0

    try:
        return float(valor)
    except ValueError:
        return 0

def convertir_int(valor):
    valor = texto(valor)

    if valor == "":
        return 0

    try:
        return int(valor)
    except ValueError:
        return 0

def convertir_bool(valor):
    valor = texto(valor).lower()
    return valor == "true"

def mostrar_logo():
    print("\n" + "=" * 60)
    print(f"{NEGRITA}{'SUPERMERCADO FAVALORO':^60}{RESET}")
    print("=" * 60)
    print()
    print(f"{AZUL}{'':>24}█████ {ROJO} █████{RESET}")
    print(f"{AZUL}{'':>22}████  ██{ROJO}██  ████{RESET}")
    print(f"{AZUL}{'':>22}███     {ROJO}     ███{RESET}")
    print(f"{AZUL}{'':>24}███   {ROJO}   ███{RESET}")
    print(f"{AZUL}{'':>26}███ {ROJO} ███{RESET}")
    print(f"{AZUL}{'':>28}██{ROJO}██{RESET}")
    print()

def crear_productos_desde_csv(archivo_csv):
    productos = []

    with open(archivo_csv, "r", encoding="utf-8-sig") as file:
        arch = csv.DictReader(file)

        for datos in arch:
            categoria = texto(datos.get("categoria"))
            codigo = texto(datos.get("codigo"))
            marca = texto(datos.get("marca"))
            nombre = texto(datos.get("nombre"))
            precioB = convertir_float(datos.get("precioB"))
            stockMin = convertir_int(datos.get("stockMin"))
            depMin = convertir_int(datos.get("depMin"))
            ubiGon = texto(datos.get("ubiGon"))
            tipo = texto(datos.get("tipo"))
            sabor = texto(datos.get("sabor"))
            kilos = convertir_float(datos.get("kilos"))
            bandeja = convertir_bool(datos.get("bandeja"))
            tacc = convertir_bool(datos.get("tacc"))
            litros = convertir_float(datos.get("litros"))
            retornable = convertir_bool(datos.get("retornable"))
            uso = texto(datos.get("uso"))
            origen = texto(datos.get("origen"))

            if codigo.startswith("AG"):
                producto = AlimentoGato(
                    codigo,
                    marca,
                    nombre,
                    precioB,
                    stockMin,
                    depMin,
                    ubiGon,
                    tipo,
                    sabor
                )

            elif codigo.startswith("CR"):
                producto = Carne(
                    codigo,
                    marca,
                    nombre,
                    precioB,
                    stockMin,
                    depMin,
                    ubiGon,
                    tipo,
                    kilos)

            elif codigo.startswith("FB"):
                producto = Fiambre(
                    codigo,
                    marca,
                    nombre,
                    precioB,
                    stockMin,
                    depMin,
                    ubiGon,
                    tipo,
                    bandeja)

            elif codigo.startswith("FD"):
                producto = Fideos(
                    codigo,
                    marca,
                    nombre,
                    precioB,
                    stockMin,
                    depMin,
                    ubiGon,
                    tipo,
                    tacc)

            elif codigo.startswith("GL"):
                producto = Galletita(
                    codigo,
                    marca,
                    nombre,
                    precioB,
                    stockMin,
                    depMin,
                    ubiGon,
                    tipo,
                    sabor)

            elif codigo.startswith("GS"):
                producto = Gaseosa(
                    codigo,
                    marca,
                    nombre,
                    precioB,
                    stockMin,
                    depMin,
                    ubiGon,
                    tipo,
                    litros,
                    sabor,
                    retornable)

            elif codigo.startswith("PN"):
                producto = Panaderia(
                    codigo,
                    marca,
                    nombre,
                    precioB,
                    stockMin,
                    depMin,
                    ubiGon,
                    tipo)

            elif codigo.startswith("PF"):
                producto = Perfume(
                    codigo,
                    marca,
                    nombre,
                    precioB,
                    stockMin,
                    depMin,
                    ubiGon,
                    tipo,
                    litros,
                    uso)

            elif codigo.startswith("VR"):
                producto = Verdura(
                    codigo,
                    marca,
                    nombre,
                    precioB,
                    stockMin,
                    depMin,
                    ubiGon,
                    tipo,
                    kilos,
                    origen)

            else:
                print(f"Producto no reconocido: {categoria} - {codigo}")
                continue

            productos.append(producto)

    return productos

def obtener_unidad(producto):
    codigo = producto.get_codigo()

    if codigo.startswith("CR") or codigo.startswith("VR"):
        return "kg"

    elif codigo.startswith("GS"):
        litros = producto.get_litros() if hasattr(producto, "get_litros") else 0 # Verificamos si el método get_litros existe en producto antes de llamarlo con hasattr
        return f"{litros} litros"                                                  # Si no existe, asignamos 0 litros por defecto.

    elif codigo.startswith("PF"):
        litros = producto.get_litros() if hasattr(producto, "get_litros") else 0 # Verificamos si el método get_litros existe en producto antes de llamarlo con hasattr
        return f"{litros} litros"                                                  # Si no existe, asignamos 0 litros por defecto.

    elif codigo.startswith("FB"):
        return "bandeja"

    elif codigo.startswith("FD"):
        return "paquete"

    elif codigo.startswith("PN"):
        return "unidad"

    elif codigo.startswith("AG"):
        return "bolsa"

    else:
        return "unidad"

def mostrar_producto(producto, inventario, numero=None):
    codigo = producto.get_codigo()
    stock = inventario.stockGondola[codigo]["cantidad"]
    unidad = obtener_unidad(producto)

    texto_producto = f"{producto.get_marca()} - {producto.get_nombre()} ({producto.get_tipo()}) - ${producto.get_precioB()} / {unidad} - Stock: {stock}"

    if numero is None:
        print(texto_producto)
    else:
        print(f"{numero}. {texto_producto}")

def agrupar_por_gondola(productos):
    gondolas = {}

    for producto in productos:
        nombre_gondola = producto.get_ubiGon()

        if nombre_gondola not in gondolas:
            gondolas[nombre_gondola] = []

        gondolas[nombre_gondola].append(producto)

    return gondolas

def mostrar_gondolas(gondolas):
    print("\n" + "=" * 60)
    print("GÓNDOLAS DISPONIBLES")
    print("=" * 60)

    nombres_gondolas = list(gondolas.keys())

    for i in range(len(nombres_gondolas)):
        print(f"{i + 1}. {nombres_gondolas[i].capitalize()}")

    print("\nOpciones:")
    print("- Escriba el número de una góndola para ver sus productos")
    print("- Escriba 'ver' para ver el carrito")
    print("- Escriba 'remover' para quitar un producto del carrito")
    print("- Escriba 'fin' para finalizar la compra")

    return nombres_gondolas

def mostrar_productos_de_gondola(nombre_gondola, productos_gondola, inventario):
    print("\n" + "=" * 60)
    print(f"GÓNDOLA: {nombre_gondola.upper()}")
    print("=" * 60)

    for i in range(len(productos_gondola)):
        mostrar_producto(productos_gondola[i], inventario, i + 1)

    print("\nOpciones:")
    print("- Escriba el número del producto que desea comprar")
    print("- Escriba 'volver' para volver al aparatado de góndolas")
    print("- Escriba 'ver' para ver el carrito")
    print("- Escriba 'remover' para quitar un producto del carrito")
    print("- Escriba 'fin' para finalizar la compra")

def mostrar_carrito(productos_comprados, carrito):
    if not productos_comprados:
        print("\nEl carrito está vacío")
        return

    print("\n" + "=" * 60)
    print("CARRITO ACTUAL")
    print("=" * 60)

    for i in range(len(productos_comprados)):
        producto = productos_comprados[i]
        print(f"{i + 1}. {producto.get_marca()} - {producto.get_nombre()} ({producto.get_codigo()}) - ${producto.get_precioB()}")

    calculador_descuentos = Descuentos(carrito)
    total_con_descuentos = calculador_descuentos.aplicar_descuentos()

    print(f"\nTotal parcial sin descuentos: ${carrito.get_totalP()}")

    if total_con_descuentos < carrito.get_totalP():
        ahorro = carrito.get_totalP() - total_con_descuentos
        print(f"Total parcial con descuentos: ${total_con_descuentos}")
        print(f"Ahorro aplicado: ${ahorro}")
    else:
        print("No hay descuentos aplicados")

def reconstruir_carrito(productos_comprados, carrito):
    carrito.lista = []
    carrito.totalP = 0

    for producto in productos_comprados:
        carrito.agregar(producto)

def remover_producto(productos_comprados, carrito, inventario):
    if not productos_comprados:
        print("\nEl carrito está vacío, no hay nada para remover")
        return

    mostrar_carrito(productos_comprados, carrito)

    try:
        num = int(input("\n¿Qué número de producto desea remover?: "))

        if 1 <= num <= len(productos_comprados):
            producto_remover = productos_comprados[num - 1]
            codigo = producto_remover.get_codigo()

            if codigo in inventario.stockGondola:
                inventario.stockGondola[codigo]["cantidad"] += 1

            del productos_comprados[num - 1]
            reconstruir_carrito(productos_comprados, carrito)

            print(f"\nProducto removido: {producto_remover.get_nombre()}")
            print(f"Total actual sin descuentos: ${carrito.get_totalP()}")

            calculador_descuentos = Descuentos(carrito)
            total_con_descuentos = calculador_descuentos.aplicar_descuentos()

            if total_con_descuentos < carrito.get_totalP():
                print(f"Total actual con descuentos: ${total_con_descuentos}")

        else:
            print(f"\nNúmero inválido. Elegí entre 1 y {len(productos_comprados)}")

    except ValueError:
        print("\nEntrada inválida. Tenés que ingresar un número")

def comprar_producto(producto_elegido, central, inventario, productos_comprados):
    codigo = producto_elegido.get_codigo()

    if codigo not in inventario.stockGondola:
        print("\nProducto no encontrado en inventario")
        return

    if inventario.stockGondola[codigo]["cantidad"] <= 0:
        print(f"\nNo hay stock disponible de {producto_elegido.get_nombre()}")
        return

    stock_antes = inventario.stockGondola[codigo]["cantidad"]

    print(f"\nEscaneando: {producto_elegido.get_marca()} - {producto_elegido.get_nombre()} ({codigo})")

    central.escaneo(producto_elegido)
    productos_comprados.append(producto_elegido)

    stock_despues = inventario.stockGondola[codigo]["cantidad"]

    print("Producto agregado al carrito")
    print(f"Stock antes de la compra: {stock_antes}")
    print(f"Stock luego de la compra/reposición: {stock_despues}")

def mostrar_descuentos(carrito):
    calculador_descuentos = Descuentos(carrito)
    total_con_descuentos = calculador_descuentos.aplicar_descuentos()

    print("\n" + "=" * 60)
    print("VERIFICACIÓN DE DESCUENTOS")
    print("=" * 60)

    if total_con_descuentos < carrito.get_totalP():
        ahorro = carrito.get_totalP() - total_con_descuentos
        print("Descuentos aplicados correctamente")
        print(f"Total sin descuentos: ${carrito.get_totalP()}")
        print(f"Total con descuentos: ${total_con_descuentos}")
        print(f"Ahorro total: ${ahorro}")
    else:
        print("No hay descuentos aplicables a los productos del carrito")
        print(f"Total final: ${total_con_descuentos}")

    print("\nDetalle de promociones posibles:")

    productos_vistos = []

    for producto in carrito.get_lista():
        codigo = producto.get_codigo()
        nombre = producto.get_nombre()

        if nombre not in productos_vistos:
            productos_vistos.append(nombre)

            if codigo.startswith("PF"):
                print(f"- {nombre}: 50% de descuento")

            elif codigo.startswith("GL"):
                print(f"- {nombre}: 2x1 en galletitas")

            elif codigo.startswith("GS"):
                print(f"- {nombre}: 30% de descuento en la segunda unidad de la misma marca")

            else:
                print(f"- {nombre}: sin descuento")

    return total_con_descuentos

def mostrar_resumen_final(productos_comprados, carrito):
    print("\nCompra finalizada")

    if not productos_comprados:
        print("\nNo se compraron productos")
        return

    total_con_descuentos = mostrar_descuentos(carrito)

    print("\n" + "=" * 60)
    print("RESUMEN FINAL DE LA COMPRA")
    print("=" * 60)

    contador_productos = Counter(producto.get_nombre() for producto in productos_comprados)

    print("\nProductos comprados:")

    for nombre, cantidad in contador_productos.items():
        producto_original = next(producto for producto in productos_comprados if producto.get_nombre() == nombre)
        subtotal = producto_original.get_precioB() * cantidad
        unidad = obtener_unidad(producto_original)

        print(f"- {nombre}: {cantidad} x {unidad} - ${subtotal}")

    print(f"\nTotal de unidades compradas: {len(productos_comprados)}")
    print(f"Monto total sin descuentos: ${carrito.get_totalP()}")
    print(f"Monto total a pagar con descuentos: ${total_con_descuentos}")

def main():
    print("=" * 60)
    print("SUPERMERCADO - SISTEMA INTERACTIVO")
    print("=" * 60)

    deposito = Deposito()
    inventario = Inventario(deposito)
    carrito = Carrito()
    central = Central(inventario, carrito)

    print("\nCargando productos desde CSV...")

    try:
        productos = crear_productos_desde_csv(archivo_csv)

        for producto in productos:
            stock_inicial_gondola = producto.get_stockMin() + 5
            stock_inicial_deposito = producto.get_depMin() + 10

            inventario.agregarProducto(producto, stock_inicial_gondola, stock_inicial_deposito)

        print(f"Productos cargados correctamente: {len(productos)}")

    except FileNotFoundError:
        print("No se encontró el archivo CSV")
        return

    except Exception as e:
        print(f"Error al cargar productos: {e}")
        return

    mostrar_logo()

    gondolas = agrupar_por_gondola(productos)
    productos_comprados = []
    compra_finalizada = False

    while not compra_finalizada:
        nombres_gondolas = mostrar_gondolas(gondolas)
        opcion_gondola = input("\n¿Qué góndola desea ver?: ").strip().lower()

        if opcion_gondola == "fin":
            compra_finalizada = True

        elif opcion_gondola == "ver":
            mostrar_carrito(productos_comprados, carrito)

        elif opcion_gondola == "remover":
            remover_producto(productos_comprados, carrito, inventario)

        else:
            try:
                num_gondola = int(opcion_gondola)

                if 1 <= num_gondola <= len(nombres_gondolas):
                    nombre_gondola = nombres_gondolas[num_gondola - 1]
                    productos_gondola = gondolas[nombre_gondola]
                    volver_a_gondolas = False

                    while not volver_a_gondolas and not compra_finalizada:
                        mostrar_productos_de_gondola(nombre_gondola, productos_gondola, inventario)
                        opcion_producto = input("\n¿Qué producto desea comprar?: ").strip().lower()

                        if opcion_producto == "volver":
                            volver_a_gondolas = True

                        elif opcion_producto == "fin":
                            compra_finalizada = True

                        elif opcion_producto == "ver":
                            mostrar_carrito(productos_comprados, carrito)

                        elif opcion_producto == "remover":
                            remover_producto(productos_comprados, carrito, inventario)

                        else:
                            try:
                                num_producto = int(opcion_producto)

                                if 1 <= num_producto <= len(productos_gondola):
                                    producto_elegido = productos_gondola[num_producto - 1]
                                    comprar_producto(producto_elegido, central, inventario, productos_comprados)

                                else:
                                    print(f"\nNúmero inválido. Elegí entre 1 y {len(productos_gondola)}")

                            except ValueError:
                                print("\nEntrada inválida. Ingresá un número, 'volver', 'ver', 'remover' o 'fin'")

                else:
                    print(f"\nNúmero inválido. Elegí entre 1 y {len(nombres_gondolas)}")

            except ValueError:
                print("\nEntrada inválida. Ingresá un número, 'ver', 'remover' o 'fin'")

    mostrar_resumen_final(productos_comprados, carrito)