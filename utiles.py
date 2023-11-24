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

# Lisa de comandos válidos con una breve descripción
diccionario_comandos_basico = {
    LISTAR_PEDIDOS: "para listar un pedido específico",
    AGREGAR_PEDIDOS: "para agregar un pedido",
    ELIMINAR_PEDIDOS: "para eliminar un pedido",
    MODIFICAR_PEDIDOS: "para modificar un pedido",
    AYUDA: "para mostrar los comandos válidos"
}

# Lista de comandos válidos con una descripción detallada, con sus argumentos
diccionario_comandos_completo = {
    LISTAR_PEDIDOS: "<id_pedido>, para listar un pedido específico (id_pedido = numero, sin los '<' y '>')",
    AGREGAR_PEDIDOS: "<cantidad> <verdura> <cliente>, para agregar un pedido (cantidad = numero, verdura = letra," +
                        " cliente = nombre, sin los '<' y '>')",
    ELIMINAR_PEDIDOS: "<id_pedido>, para eliminar un pedido (id_pedido = numero, sin los '<' y '>')",
    MODIFICAR_PEDIDOS: "<id_pedido> <verdura> <cantidad>, para modificar un pedido (id_pedido = numero, verdura = letra," + 
                        " cantidad = numero, sin los '<' y '>')",
    AYUDA: "<comando>, para mostrar información sobre un comando (comando = cualquier comando válido, sin los '<' y '>')"
}