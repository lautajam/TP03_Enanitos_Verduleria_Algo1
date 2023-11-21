import sys
import csv
import os

"""
UN METODO QUE DEVUELVA EL COMANDO ESCRITO NO VALIDO:
"Comando 'elimnar C' no valido, reingrese"
Tengo que tomar la lista de argumentos y ver hacer un string con los argumentos que no son validos
"""

# Codigos de verduras
TOMATE = "t"
LECHUGA = "l"
ZANAHORIA = "z"
BROCOLI = "b"

# Posiciones de los lista_argumentos
POSICION_COMANDO = 1
ID_PEDIDO = 0
VERDURA = 1
CANTIDAD = 2

# Comandos
LISTAR_PEDIDOS = "listar"
AGREGAR_PEDIDOS = "agregar"
ELIMINAR_PEDIDOS = "eliminar"
MODIFICAR_PEDIDOS = "modificar"

# Agregar pedido
CANTIDAD_ARGUMENTOS_AGREGAR = 5
POSICION_CANTIDAD = 2
POSICION_VERDURA = 3
POSICION_CLIENTE = 4

# Archivos
ARCHIVO_PEDIDOS = "verduleria_enanitos.csv"
ARCHIVO_CLIENTES = "clientes.csv"

# Modos de apertura de archivos
ESCRIBIR_ARCHIVO = "a"
REENVIO_ARCHIVO = "w"
LEER_ARCHIVO = "r"
CREAR_ARCHIVO = "x"

# Lista de argumentos
lista_argumentos = sys.argv

# --- LISTADO DE PEDIDOS ---
# Pre: verdura es el código de la verdura
# Post: devuelve por consola el nombre de la verdura
def escribir_verdura(verdura):
    if verdura == TOMATE:
        print("Producto: Tomate")
    elif verdura == LECHUGA:
        print("Producto: Lechuga")
    elif verdura == ZANAHORIA:
        print("Producto: Zanahoria")
    elif verdura == BROCOLI:
        print("Producto: Brócoli")

# Pre: el numero de pedido puede o no existir en el archivo "verduleria_enanitos.csv"
# Post: si el pedido existe, lo lista, si no existe, muestra un mensaje de error
def listar_pedido_especifico(numero_pedido):
        
        with open(ARCHIVO_PEDIDOS, LEER_ARCHIVO) as archivo:

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
    with open(ARCHIVO_PEDIDOS, LEER_ARCHIVO) as archivo:
        
        # Obtén el tamaño del archivo
        tamano_archivo = os.path.getsize(ARCHIVO_PEDIDOS)

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

# Pre: -
# Post: Lista todos los pedidos del archivo "verduleria_enanitos.csv", si 
def listar_pedidos():
    if len(lista_argumentos) == 2:
        listar_todos_los_pedidos()
    elif len(lista_argumentos) == 3 and lista_argumentos[2].isdigit():
        listar_pedido_especifico(lista_argumentos[2])
    else:
        print("Comando no válido")

# --- LISTADO DE PEDIDOS ---

# --- AGREGAR PEDIDO ---

# Pre: verdura es el código de la verdura
# Post: devuelve si la verdura es válida (si está en la lista de verduras)
def verificar_verdura(verdura):
    return verdura.lower() in [TOMATE, LECHUGA, ZANAHORIA, BROCOLI]

# Pre: -
# Post: Devuelve si la longitud de los argumentos es válida
def longitud_argumentos_valida():
    return len(lista_argumentos) == CANTIDAD_ARGUMENTOS_AGREGAR

# Pre: -
# Post: Devuelve si la cantidad es un número
def cantidad_valida(cantidad):
    return cantidad.isdigit()

# Pre: -
# Post: Devuelve si la verdura es un string
def verdura_valida(verdura):
    return verdura.isalpha() and verificar_verdura(verdura)

# Pre: -
# Post: Devuelve si los argumentos son validos para agregar un pedido
def condicion_agregar_pedido():
    return (
        longitud_argumentos_valida() and
        cantidad_valida(lista_argumentos[POSICION_CANTIDAD]) and
        verdura_valida(lista_argumentos[POSICION_VERDURA])
    )

# Pre: -
# Post: Devuelve el último id del archivo "verduleria_enanitos.csv"
def get_ultimo_id():
    with open(ARCHIVO_PEDIDOS, LEER_ARCHIVO) as archivo:
        pedidos = csv.reader(archivo)
        return len(list(pedidos))

# Pre: -
# Post: Agrega un pedido al archivo "verduleria_enanitos.csv"
def agregar_pedido():
    if condicion_agregar_pedido():

        id_pedido_actual = str(get_ultimo_id())

        with open(ARCHIVO_PEDIDOS, ESCRIBIR_ARCHIVO) as archivo_pedidos:
            pedido = f"{id_pedido_actual};{lista_argumentos[POSICION_VERDURA]};{lista_argumentos[POSICION_CANTIDAD]}\n"
            archivo_pedidos.write(pedido)

        with open(ARCHIVO_CLIENTES, ESCRIBIR_ARCHIVO) as archivo_clientes:
            pedido_cliente = f"{id_pedido_actual};{lista_argumentos[POSICION_CLIENTE]}\n"
            archivo_clientes.write(pedido_cliente)

        print("Pedido agregado")
    else:
        print("Comando no válido, reingrese")

# --- AGREGAR PEDIDO ---

# --- ELIMINAR PEDIDO ---

# Pre: -
# Post: Devuelve una lista con los pedidos del archivo "verduleria_enanitos.csv
def leer_archivo():
    with open(ARCHIVO_PEDIDOS, LEER_ARCHIVO, newline='') as archivo:
        return list(csv.reader(archivo, delimiter=';'))

"""
Pre: Pedidos es una lista con los pedidos del archivo "verduleria_enanitos.csv" 
        y pedido_a_eliminar es el id del pedido a eliminar
Post: Devuelve una lista con los pedidos del archivo "verduleria_enanitos.csv" sin el pedido a eliminar
"""
def eliminar_pedido_indicado(pedidos, pedido_a_eliminar):
    pedidos_actualizados = []

    for pedido in pedidos:
        if len(pedido) > ID_PEDIDO:
            if pedido[ID_PEDIDO] != pedido_a_eliminar:
                pedidos_actualizados.append(pedido)

    return pedidos_actualizados

# Pre: Pedidos es una lista con los pedidos del archivo "verduleria_enanitos.csv"
# Post: Reescribe el archivo "verduleria_enanitos.csv" con los pedidos de la lista pedidos
def reescribir_archivo(pedidos):
    with open(ARCHIVO_PEDIDOS, REENVIO_ARCHIVO, newline='') as archivo:
        escritor_csv = csv.writer(archivo, delimiter=';')
        escritor_csv.writerows(pedidos)

# Pre: -
# Post: Devuelve si la eliminación es válida
def eliminacion_valida():
    return len(lista_argumentos) == 3 and lista_argumentos[2].isdigit()

# Pre: -
# Post: Elimina un pedido del archivo "verduleria_enanitos.csv"
def eliminar_pedido():
    if eliminacion_valida():
        pedidos = leer_archivo()
        pedidos_post_eliminacion = eliminar_pedido_indicado(pedidos, lista_argumentos[2])
        reescribir_archivo(pedidos_post_eliminacion)
        print(f"Pedido {lista_argumentos[2]} eliminado")
    else:
        print("Comando no válido")

# --- ELIMINAR PEDIDO ---

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
    if lista_argumentos[POSICION_COMANDO] == LISTAR_PEDIDOS:
        listar_pedidos()
    elif lista_argumentos[POSICION_COMANDO] == AGREGAR_PEDIDOS:
        agregar_pedido()
    elif lista_argumentos[POSICION_COMANDO] == ELIMINAR_PEDIDOS:
        eliminar_pedido()
    else:
        print("Comando no válido")
"""
    elif lista_argumentos[POSICION_COMANDO] == MODIFICAR_PEDIDOS:
        modificar()"""

# Pre: -
# Post: Chequea si el archivo "verduleria_enanitos.csv" existe, si no existe, lo crea
def chequear_archivo(archivo):
    if not os.path.exists(archivo):
        with open(archivo, CREAR_ARCHIVO):
            pass

if __name__ == "__main__":
    
    chequear_archivo(ARCHIVO_PEDIDOS)
    chequear_archivo(ARCHIVO_CLIENTES)

    manejar_archivo()