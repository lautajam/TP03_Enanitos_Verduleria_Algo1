import sys
import csv
import os

# Codigos de verduras
TOMATE = "t"
LECHUGA = "l"
ZANAHORIA = "z"
BROCOLI = "b"

# Posiciones de los argumentos
POSICION_COMANDO = 1
ID_PEDIDO = 0
VERDURA = 1
CANTIDAD = 2

# Comandos
LISTAR_ARCHIVOS = "listar"
AGREGAR_ARCHIVOS = "agregar"
ELIMINAR_ARCHIVOS = "eliminar"
MODIFICAR_ARCHIVOS = "modificar"

# Archivo
ARCHIVO = "verduleria_enanitos.csv"
ESCRIBIR_ARCHIVO = "w"
LEER_ARCHIVO = "r"
CREAR_ARCHIVO = "x"

"""
Pre: verdura es el código de la verdura
Post: devuelve por consola el nombre de la verdura
"""
def escribir_verdura(verdura):
    if verdura == TOMATE:
        print("Producto: Tomate")
    elif verdura == LECHUGA:
        print("Producto: Lechuga")
    elif verdura == ZANAHORIA:
        print("Producto: Zanahoria")
    elif verdura == BROCOLI:
        print("Producto: Brócoli")

"""
Pre: el numero de pedido puede o no existir en el archivo "verduleria_enanitos.csv"
Post: si el pedido existe, lo lista, si no existe, muestra un mensaje de error
"""
def listar_pedido_especifico(numero_pedido):
        
        with open(ARCHIVO, LEER_ARCHIVO) as archivo:

            for fila in csv.reader(archivo):
                pedidos = fila[0].split(";")
    
                if pedidos[0] == numero_pedido:
                    print("Listar pedido específico:")
                    print("Pedido número:", pedidos[ID_PEDIDO])
                    escribir_verdura(pedidos[VERDURA].lower())
                    print("Cantidad:", pedidos[CANTIDAD])
                    print("-----------")
                    return
                
        print("El pedido no existe")

"""
Pre: -
Post: Lista todos los pedidos del archivo "verduleria_enanitos.csv", en caso de que no haya pedidos, 
        muestra un mensaje de error
"""
def listar_todos_los_pedidos():
    with open(ARCHIVO, LEER_ARCHIVO) as archivo:
        
        # Obtén el tamaño del archivo
        tamano_archivo = os.path.getsize(ARCHIVO)

        if tamano_archivo == 0:
            print("No hay pedidos.")
            return

        print("Listar todos los pedidos:")

        for fila in csv.reader(archivo):

            pedidos = fila[0].split(";")

            print("Pedido número:", pedidos[ID_PEDIDO])
            escribir_verdura(pedidos[VERDURA].lower())
            print("Cantidad:", pedidos[CANTIDAD])
            print("-----------")

"""
Pre: -
Post: Lista todos los pedidos del archivo "verduleria_enanitos.csv", si 
"""
def listar():
    if len(sys.argv) == 2:
        listar_todos_los_pedidos()
    elif len(sys.argv) == 3:
        listar_pedido_especifico(sys.argv[2])

"""
Pre: -
Post: Dependiendo del comando ingresado por consola, se ejecuta la función correspondiente:
        listar, para listar todos los pedidos o un pedido específico
        agregar, para agregar un pedido 
        eliminar, para eliminar un pedido
        modificar, para modificar un pedido+
        En caso de que el comando no sea válido, muestra un mensaje de error
"""
def manejar_archivo():
    if sys.argv[POSICION_COMANDO] == LISTAR_ARCHIVOS:
        listar()
    else:
        print("Comando no válido")
"""    elif sys.argv[POSICION_COMANDO] == AGREGAR_ARCHIVOS:
        agregar(archivo)
    elif sys.argv[POSICION_COMANDO] == ELIMINAR_ARCHIVOS:
        eliminar(archivo)
    elif sys.argv[POSICION_COMANDO] == MODIFICAR_ARCHIVOS:
        modificar(archivo)"""

"""
Pre: -
Post: Chequea si el archivo "verduleria_enanitos.csv" existe, si no existe, lo crea
"""
def chequear_archivo():
    if os.path.exists(ARCHIVO):
        pass
    else:
        archivo = open(ARCHIVO, CREAR_ARCHIVO)
        archivo.close()

if __name__ == "__main__":
    
    chequear_archivo()

    manejar_archivo()
    pass
