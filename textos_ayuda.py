from utiles import *

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

""" --- AYUDA --- """
# Pre: -
# Post: Muestra por consola los comandos válidos
def ayuda_basica():
    print( "Comandos válidos:")
    for comando in comandos_validos:
        print( "     *", comando + ", " + diccionario_comandos_basico[comando] + ".")
    print(f"Si quieres mas información sobre un comando, o especificaciones de sus argumentos, escribe '{AYUDA}' <comando>.")

# Pre: -
# Post: Muestra por consola los comandos válidos para listar
def ayuda_listar():
    print(f"Comando '{LISTAR_PEDIDOS}' válido:")
    print( "     *", LISTAR_PEDIDOS + ", " + diccionario_comandos_basico[LISTAR_PEDIDOS], "(sin argumentos).")
    print( "     *", LISTAR_PEDIDOS, diccionario_comandos_completo[LISTAR_PEDIDOS] + ".")

# Pre: -
# Post: Muestra por consola los comandos válidos para agregar
def ayuda_agregar():
    print(f"Comando '{AGREGAR_PEDIDOS}' válido:")
    print( "     *", AGREGAR_PEDIDOS, diccionario_comandos_completo[AGREGAR_PEDIDOS] + ".")

# Pre: -
# Post: Muestra por consola los comandos válidos para eliminar
def ayuda_eliminar():
    print(f"Comando '{ELIMINAR_PEDIDOS}' válido:")
    print( "     *", ELIMINAR_PEDIDOS, diccionario_comandos_completo[ELIMINAR_PEDIDOS] + ".")

# Pre: -
# Post: Muestra por consola los comandos válidos para modificar
def ayuda_modificar():
    print(f"Comando '{MODIFICAR_PEDIDOS}' válido:")
    print( "     *", MODIFICAR_PEDIDOS, diccionario_comandos_completo[MODIFICAR_PEDIDOS] + ".")

# Pre: -
# Post: Muestra por consola los comandos válidos para ayuda
def ayuda_ayuda():
    print(f"Comando '{AYUDA}' válido:")
    print( "     *", AYUDA + ", " + diccionario_comandos_basico[AYUDA], "(sin argumentos).")
    print( "     *", AYUDA, diccionario_comandos_completo[AYUDA] + ".")

# Pre: -
# Post: Muestra por consola los comandos válidos
def ayuda(argumentos):
    if len(argumentos) == 2:
        ayuda_basica()
        return
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
            print(f"Comando con argumentos no válidos, escriba '{AYUDA} {AYUDA}' para mas información sobre los argumentos.")
    else:
        print(f"Comando con argumentos no válidos, escriba '{AYUDA} {AYUDA}' para mas información sobre los argumentos.")
""" --- AYUDA --- """