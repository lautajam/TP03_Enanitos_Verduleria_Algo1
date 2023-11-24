import sys, csv, os

# Codigos de verduras
TOMATE = "t"
LECHUGA = "l"
ZANAHORIA = "z"
BROCOLI = "b"
verduras = (TOMATE, LECHUGA, ZANAHORIA, BROCOLI)

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
AYUDA = "ayuda"
comandos_validos = (LISTAR_PEDIDOS, AGREGAR_PEDIDOS, ELIMINAR_PEDIDOS, MODIFICAR_PEDIDOS, AYUDA)

# Agregar pedido
CANTIDAD_ARGUMENTOS_AGREGAR = 5
POSICION_CANTIDAD = 2
POSICION_VERDURA = 3
POSICION_CLIENTE = 4

# Archivos
ARCHIVO_PEDIDOS = "verduleria_enanitos.csv"
ARCHIVO_CLIENTES = "clientes.csv"
ARCHIVO_AUXILIAR_PEDIDOS = "auxiliarP.csv"
ARCHIVO_AUXILIAR_CLIENTES = "auxiliarC.csv"

# Modos de apertura de archivos
ESCRIBIR_ARCHIVO = "a"
REESCRIBIR_ARCHIVO = "w"
LEER_ARCHIVO = "r"
CREAR_ARCHIVO = "x"
LEER_ESCRIBIR_ARCHIVO = "r+"

""" --- LISTADO DE PEDIDOS --- """
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

# Pre: pedido es un pedido en formato id;verdura;cantidad
# Post: muestra por consola el pedido
def escribir_pedido(pedido, nombre_cliente): #, nombre_cliente):
    print(f"Pedido número: {pedido[ID_PEDIDO]}")
    print(f"Producto: {pedido[VERDURA].upper()}")
    print(f"Cantidad: {pedido[CANTIDAD]}")
    print(f"Cliente: {nombre_cliente.capitalize() if nombre_cliente != '' else 'No se encontró el cliente'}")

# Pre: numero_pedido es el id del pedido y lectura_clientes es el archivo "clientes.csv" leído
# Post: devuelve el nombre del cliente que hizo el pedido, si no existe el pedido, devuelve un string vacío
def obtener_nombre_cliente(numero_pedido, lectura_clientes):
    for cliente in lectura_clientes:
        if cliente and cliente[ID_PEDIDO] == numero_pedido:
            return cliente[1]
    return ""

# Pre: el numero de pedido puede o no existir en el archivo "verduleria_enanitos.csv"
# Post: si el pedido existe, lo lista, si no existe, muestra un mensaje de error
def listar_pedido_especifico(numero_pedido):
    try:
        archivo_pedidos = open(ARCHIVO_PEDIDOS, LEER_ARCHIVO)
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo de pedidos: {e}")
        return

    try:
        archivo_clientes = open(ARCHIVO_CLIENTES, LEER_ARCHIVO)
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo de clientes: {e}")
        archivo_pedidos.close()
        return
    
    lectura_pedidos = csv.reader(archivo_pedidos, delimiter=';')
    lectura_clientes = csv.reader(archivo_clientes, delimiter=';')

    nombre_cliente = obtener_nombre_cliente(numero_pedido, lectura_clientes)

    if nombre_cliente:
        for pedido in lectura_pedidos:
            if pedido and pedido[ID_PEDIDO] == numero_pedido:
                print("-----------")
                escribir_pedido(pedido, nombre_cliente)
        print("-----------")
    else:
        print(f"No se encontró el pedido con el número {numero_pedido}")

    archivo_pedidos.close()
    archivo_clientes.close()

# Pre: -
# Post: Lista todos los pedidos del archivo "verduleria_enanitos.csv", en caso de que no haya pedidos, 
#       muestra un mensaje de error
def listar_todos_los_pedidos():
    try:
        archivo_pedidos = open(ARCHIVO_PEDIDOS, LEER_ARCHIVO)
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo de pedidos: {e}")
        return

    try:
        archivo_clientes = open(ARCHIVO_CLIENTES, LEER_ARCHIVO)
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo de clientes: {e}")
        archivo_pedidos.close()
        return

    lectura_clientes = list(csv.reader(archivo_clientes, delimiter=';'))
    lectura_pedidos = list(csv.reader(archivo_pedidos, delimiter=';'))

    if lectura_pedidos and lectura_clientes:
        for pedido in lectura_pedidos:
            if pedido and len(pedido) > ID_PEDIDO:
                print("-----------")
                nombre_cliente = obtener_nombre_cliente(pedido[ID_PEDIDO], lectura_clientes)
                escribir_pedido(pedido, nombre_cliente)
        print("-----------")
    else:
        print("No hay pedidos")

    archivo_pedidos.close()
    archivo_clientes.close()

# Pre: -
# Post: Lista todos los pedidos del archivo "verduleria_enanitos.csv", si 
def listar_pedidos(argumentos):
    if len(argumentos) == 2:
        listar_todos_los_pedidos()
    elif len(argumentos) == 3 and argumentos[2].isdigit():
        listar_pedido_especifico(argumentos[2])
    else:
        print(f"Comando con parámetros no válidos, escriba '{AYUDA} {LISTAR_PEDIDOS}' para mas información sobre los parámetros")
""" --- LISTADO DE PEDIDOS --- """

""" --- AGREGAR PEDIDO --- """
# Pre: verdura es el código de la verdura
# Post: devuelve si la verdura es válida (si está en la lista de verduras)
def verificar_verdura(verdura):
    return verdura.lower() in [TOMATE, LECHUGA, ZANAHORIA, BROCOLI]

# Pre: -
# Post: Devuelve si la longitud de los argumentos es válida
def longitud_argumentos_valida(argumentos):
    return len(argumentos) == CANTIDAD_ARGUMENTOS_AGREGAR

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
def condicion_agregar_pedido(argumentos):
    return (
        longitud_argumentos_valida(argumentos) and
        cantidad_valida(argumentos[POSICION_CANTIDAD]) and
        verdura_valida(argumentos[POSICION_VERDURA])
    )

# Pre: -
# Post: Devuelve elultimo id del archivo, el cual es el id mas grande
def get_ultimo_id(archivo):
    lectura_archivo = csv.reader(archivo, delimiter=';')

    ultimo_id = 0

    for fila in lectura_archivo:
        if fila and len(fila) > ID_PEDIDO:
            ultimo_id = max(ultimo_id, int(fila[ID_PEDIDO]))

    return ultimo_id

# Pre: archivo_pedidos y archivo_clientes son los archivos csv
# Post: Devuelve el id del pedido que se va a agregar (se busca el id mas grande entre los dos archivos y se le suma 1)
def get_nuevo_id(archivo_pedidos, archivo_clientes):
    ultimo_id_pedidos = get_ultimo_id(archivo_pedidos)
    ultimo_id_clientes = get_ultimo_id(archivo_clientes)

    return max(ultimo_id_pedidos, ultimo_id_clientes) + 1

# Pre: -
# Post: Agrega un pedido al archivo "verduleria_enanitos.csv" (id, verdura, cantidad)
# y al archivo "clientes.csv" (id, cliente)
def agregar_pedido(argumentos):
    if condicion_agregar_pedido(argumentos):

        try:
            archivo_pedidos = open(ARCHIVO_PEDIDOS, LEER_ESCRIBIR_ARCHIVO, newline='\n')
        except Exception as e:
            print(f"Ocurrió un error al abrir el archivo de pedidos: {e}")
            return
        try:
            archivo_clientes = open(ARCHIVO_CLIENTES, LEER_ESCRIBIR_ARCHIVO, newline='\n')
        except Exception as e:
            print(f"Ocurrió un error al abrir el archivo de clientes: {e}")
            archivo_pedidos.close()
            return

        escritor_pedidos = csv.writer(archivo_pedidos, delimiter=';')
        escritor_clientes = csv.writer(archivo_clientes, delimiter=';')

        id_pedido_actual = get_nuevo_id(archivo_pedidos, archivo_clientes)

        pedido_nuevo_pedidos = [str(id_pedido_actual), argumentos[POSICION_VERDURA].upper(), argumentos[POSICION_CANTIDAD]]
        pedido_nuevo_clientes = [str(id_pedido_actual), argumentos[POSICION_CLIENTE].capitalize()]

        escritor_pedidos.writerow(pedido_nuevo_pedidos)
        escritor_clientes.writerow(pedido_nuevo_clientes)

        archivo_pedidos.close()
        archivo_clientes.close()

        print(f"Pedido agregado, su número de pedido es {id_pedido_actual}")

    else:
        print(f"Comando con parámetros no válidos, escriba '{AYUDA} {AGREGAR_PEDIDOS}' para mas información sobre los parámetros")
""" --- AGREGAR PEDIDO --- """

""" --- ELIMINAR PEDIDO --- """
# Pre: archivo_a_leer es el archivo csv
# Post: Devuelve una lista con los elementos en el archivo pasado
def leer_archivo(archivo_a_leer):

    # Probablemente haya que eliminar esta función

    with open(archivo_a_leer, LEER_ARCHIVO, newline='') as archivo:
        return list(csv.reader(archivo, delimiter=';'))

# Pre: -
# Post: Devuelve una lista con el elemento eliminado
def eliminar_indicado(lista, elemento_a_eliminar):

    # Probablemente haya que eliminar esta función

    lista_actualizad = []

    for elemento in lista:
        if len(elemento) > ID_PEDIDO:
            if elemento[ID_PEDIDO] != elemento_a_eliminar:
                lista_actualizad.append(elemento)

    return lista_actualizad

# Pre: Lista es una lista de listas y archivo_a_reescribir es el archivo csv que queremos usar
# Post: Reescribe el archivo "archivo_a_reescribir" con los elementos de la lista
def reescribir_archivo(lista, archivo_a_reescribir):

    # Probablemente haya que eliminar esta función

    with open(archivo_a_reescribir, REESCRIBIR_ARCHIVO, newline='') as archivo:
        escritor_csv = csv.writer(archivo, delimiter=';')
        escritor_csv.writerows(lista)

# Pre: -
# Post: Devuelve si la eliminación es válida
def eliminacion_valida(pedido_a_eliminar, argumentos):
    return len(argumentos) == 3 and pedido_a_eliminar.isdigit()

# Pre: pedidos es una lista de listas y pedido_a_eliminar es el pedido que queremos eliminar
# Post: Devuelve si el pedido existe en la lista de pedidos
def pedido_existe(pedidos, pedido_a_eliminar):
    return any(pedido[ID_PEDIDO] == pedido_a_eliminar for pedido in pedidos)

# Pre: pedidos es una lista de listas y pedido_a_eliminar es el pedido que queremos eliminar
# Post: Elimina el pedido del archivo "verduleria_enanitos.csv"
def eliminar_pedido(pedidos, pedido_a_eliminar):

    # Escritura se maneja desde el archivo y un archivo auxiliar
    # El archivo auxiliar se usa para pasar los datos del archivo original al archivo auxiliar
    # Se elimina el archivo original y se renombra el archivo auxiliar
    # Agregar try except a la apertura del archivo

    pedidos_post_eliminacion = eliminar_indicado(pedidos, pedido_a_eliminar)
    reescribir_archivo(pedidos_post_eliminacion, ARCHIVO_PEDIDOS)

# Pre: clientes es una lista de listas y pedido_a_eliminar es el pedido que queremos eliminar
# Post: Elimina el pedido del archivo "clientes.csv"
def eliminar_cliente(clientes, pedido_a_eliminar):

    # Escritura se maneja desde el archivo y un archivo auxiliar
    # El archivo auxiliar se usa para pasar los datos del archivo original al archivo auxiliar
    # Se elimina el archivo original y se renombra el archivo auxiliar
    # Agregar try except a la apertura del archivo

    clientes_post_eliminacion = eliminar_indicado(clientes, pedido_a_eliminar)
    reescribir_archivo(clientes_post_eliminacion, ARCHIVO_CLIENTES)

# Pre: -
# Post: Elimina un pedido del archivo "verduleria_enanitos.csv"
def eliminar(pedido_a_eliminar):

    # Acá tengo que mejorar el manejo de errores

    if eliminacion_valida(pedido_a_eliminar):

        pedidos = leer_archivo(ARCHIVO_PEDIDOS)
        clientes = leer_archivo(ARCHIVO_CLIENTES)

        if pedido_existe(pedidos, pedido_a_eliminar):
            eliminar_pedido(pedidos, pedido_a_eliminar)
            eliminar_cliente(clientes, pedido_a_eliminar)
            print(f"Pedido {pedido_a_eliminar} eliminado")
        else:
            print(f"Error: El pedido {pedido_a_eliminar} no existe.")
    else:
        print("Comando no válido, escriba 'ayuda eliminar' para mas información")
""" --- ELIMINAR PEDIDO --- """

""" --- MODIFICAR PEDIDO --- """
# Pre: pedido es un pedido en formato id;verdura;cantidad, 
#       id_pedido_a_modificar es el id del pedido que queremos modificar,
#       verdura_pedido_a_modificar es la verdura del pedido que queremos modificar y
#       cantidad_pedido_a_modificar es la cantidad del pedido que queremos modificar
# Post: Devuelve si al pedido hay que modificarle solo la cantidad, ya que el id y la verdura son iguales
def modificar_pedido_cantidad(pedido, id_pedido_a_modificar, verdura_pedido_a_modificar):
    return pedido[ID_PEDIDO] == id_pedido_a_modificar and pedido[VERDURA] == verdura_pedido_a_modificar

# Pre: pedido es un pedido en formato id;verdura;cantidad,
#       id_pedido_a_modificar es el id del pedido que queremos modificar y
#       verdura_pedido_a_modificar es la verdura del pedido que queremos modificar
# Post: Devuelve si al pedido hay que modificarle la verdura y la cantidad, ya que el id es igual
def modificar_pedido_verdura_cantidad(pedidos, id_pedido_a_modificar, verdura_pedido_a_modificar):
    return verdura_valida(verdura_pedido_a_modificar) and pedido_existe(pedidos, id_pedido_a_modificar)

# Pre: pedidos es una lista de listas, id_pedido_a_modificar es el id del pedido que queremos modificar,
#      verdura_pedido_a_modificar es la verdura del pedido que queremos modificar y
#      cantidad_pedido_a_modificar es la cantidad del pedido que queremos modificar
# Post: Devuelve la lista de pedidos modificada
def modificar_pedido(pedidos, id_pedido_a_modificar, verdura_pedido_a_modificar, cantidad_pedido_a_modificar):

    for pedido in pedidos:
        if modificar_pedido_cantidad(pedido, id_pedido_a_modificar, verdura_pedido_a_modificar):
            pedido[CANTIDAD] = cantidad_pedido_a_modificar
            print(f"Pedido {id_pedido_a_modificar} modificado, cantidad actualizada")
            return pedidos

    if modificar_pedido_verdura_cantidad(pedidos, id_pedido_a_modificar, verdura_pedido_a_modificar):
        pedidos.append([id_pedido_a_modificar, verdura_pedido_a_modificar, cantidad_pedido_a_modificar])
        print(f"Pedido {id_pedido_a_modificar} modificado, verdura y cantidad agregada")
    elif not pedido_existe(pedidos, id_pedido_a_modificar):
        print("El pedido no existe")
    elif not verdura_valida(verdura_pedido_a_modificar):
        print("La verdura no es válida")

    return pedidos

# Pre: id_pedido_a_modificar es el id del pedido que queremos modificar,
#      verdura_pedido_a_modificar es la verdura del pedido que queremos modificar y
#      cantidad_pedido_a_modificar es la cantidad del pedido que queremos modificar
# Post: Devuelve si los argumentos son válidos para modificar un pedido
def validar_modificacion(id_pedido_a_modificar, verdura_pedido_a_modificar, cantidad_pedido_a_modificar):
    return (
        id_pedido_a_modificar.isdigit() and
        cantidad_pedido_a_modificar.isdigit() and
        verdura_pedido_a_modificar.isalpha()
    )

# Pre: -
# Post: Modifica un pedido del archivo "verduleria_enanitos.csv"
def modificar(argumentos):

    # Escritura se maneja desde el archivo y un archivo auxiliar
    # El archivo auxiliar se usa para pasar los datos del archivo original al archivo auxiliar
    # Se elimina el archivo original y se renombra el archivo auxiliar
    # Agregar try except a la apertura del archivo
    # La modificacion deberia ser una inserción ordenada, en caso de que haya que agregar al mismo pedido

    if len(argumentos) == 5:
        pedidos = leer_archivo(ARCHIVO_PEDIDOS)

        id_pedido_a_modificar = argumentos[2]
        verdura_pedido_a_modificar = argumentos[3].upper()
        cantidad_pedido_a_modificar = argumentos[4]

        if validar_modificacion(id_pedido_a_modificar, 
                                verdura_pedido_a_modificar, 
                                cantidad_pedido_a_modificar):
            
            pedidos_modificados = modificar_pedido(pedidos, 
                                                id_pedido_a_modificar, 
                                                verdura_pedido_a_modificar, 
                                                cantidad_pedido_a_modificar)
            
            reescribir_archivo(pedidos_modificados, ARCHIVO_PEDIDOS)
    else:
        print("Ingreso no valido, escriba 'ayuda modificar' para mas información")
""" --- MODIFICAR PEDIDO --- """

""" --- AYUDA --- """
# Pre: -
# Post: Muestra por consola los comandos válidos
def ayuda_basica():
    print("Comandos válidos:")
    print("     * listar, para listar todos los pedidos o un pedido específico")
    print("     * agregar, para agregar un pedido")
    print("     * eliminar, para eliminar un pedido")
    print("     * modificar, para modificar un pedido")
    print("     * ayuda, para mostrar los comandos válidos")
    print("Si quieres mas información sobre un comando, escribe 'ayuda' seguido del comando")

# Pre: -
# Post: Muestra por consola los comandos válidos para listar
def ayuda_listar():
    print("Comando 'listar' válido:")
    print("     * listar, para listar todos los pedidos o un pedido específico")
    print("     * listar <id_pedido>, para listar un pedido específico")

# Pre: -
# Post: Muestra por consola los comandos válidos para agregar
def ayuda_agregar():
    print("Comando 'agregar' válido:")
    print("     * agregar <cantidad> <verdura> <cliente>, para agregar un pedido")

# Pre: -
# Post: Muestra por consola los comandos válidos para eliminar
def ayuda_eliminar():
    print("Comando 'eliminar' válido:")
    print("     * eliminar <id_pedido>, para eliminar un pedido")

# Pre: -
# Post: Muestra por consola los comandos válidos para modificar
def ayuda_modificar():
    print("Comando 'modificar' válido:")
    print("     * modificar <id_pedido> <verdura> <cantidad>, para modificar un pedido")

# Pre: -
# Post: Muestra por consola los comandos válidos para ayuda
def ayuda_ayuda():
    print("Comando 'ayuda' válido_")
    print("     * ayuda, para mostrar los comandos válidos")
    print("     * ayuda <comando>, para mostrar información sobre un comando")

# Pre: -
# Post: Muestra por consola los comandos válidos
def ayuda(argumentos):
    if len(argumentos) == 2:
        ayuda_basica()
    elif len(argumentos) == 3:
        comando = argumentos[2]
        if comando == LISTAR_PEDIDOS:
            ayuda_listar()
        elif comando == AGREGAR_PEDIDOS:
            ayuda_agregar()
        elif comando == ELIMINAR_PEDIDOS:
            ayuda_eliminar()
        elif argumentos[2] == MODIFICAR_PEDIDOS:
            ayuda_modificar()
        elif comando == AYUDA:
            ayuda_ayuda()
        else:
            print("Comando de ayuda no válido")
    else:
        print("Comando de ayuda no válido")
""" --- AYUDA --- """

"""
Pre: -
Post: Dependiendo del comando ingresado por consola, se ejecuta la función correspondiente:
        listar, para listar todos los pedidos o un pedido específico
        agregar, para agregar un pedido 
        eliminar, para eliminar un pedido
        modificar, para modificar un pedido
        ayuda, para mostrar los comandos válidos
        En caso de que el comando no sea válido, muestra un mensaje de error
"""
def manejar_archivo():

    # Mejorar el manejo de errores

    argumentos = sys.argv

    if argumentos[POSICION_COMANDO] == LISTAR_PEDIDOS:
        listar_pedidos(argumentos)
    elif argumentos[POSICION_COMANDO] == AGREGAR_PEDIDOS:
        agregar_pedido(argumentos)
    elif argumentos[POSICION_COMANDO] == ELIMINAR_PEDIDOS:
        eliminar(argumentos)
    elif argumentos[POSICION_COMANDO] == MODIFICAR_PEDIDOS:
        modificar(argumentos)
    elif argumentos[POSICION_COMANDO] == AYUDA:
        ayuda(argumentos)

# Pre: -
# Post: Chequea si el archivo "verduleria_enanitos.csv" existe, si no existe, lo crea
def chequear_archivo(archivo):

    # Agregar try except a la creación del archivo

    if not os.path.exists(archivo):
        with open(archivo, CREAR_ARCHIVO):
            pass

# Pre: -
# Post: Chequea si el comando ingresado por consola es válido, si no es válido, muestra un mensaje de error
def chequear_comando():

    # Mejorar el manejo de errores
    argumentos = sys.argv
    if argumentos[POSICION_COMANDO] not in comandos_validos:
        print("Comando no válido, escriba 'ayuda' para mas información")
        return False
    return True

# Pre: -
# Post: Chequea si los archivos "verduleria_enanitos.csv" y "clientes.csv" existen, si no existen, los crea
def chequear_archivos():
    chequear_archivo(ARCHIVO_PEDIDOS)
    chequear_archivo(ARCHIVO_CLIENTES)

if __name__ == "__main__":
    
    chequear_archivos()

    if chequear_comando():
        manejar_archivo()




        