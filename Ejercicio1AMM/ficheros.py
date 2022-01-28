import os


def elegir_opcion_menu():
    print('''
        FICHEROS
        1. Leer fichero de texto
        2. Copiar fichero
        3. Listar archivos de directorio
        0. Salir''')


def leer_entero(texto):
    try:
        return int(input(texto))
    except ValueError:
        return None


def pedir_ruta_fichero():
    print('Escriba la ruta del fichero: ')

# aqui leo el string de la ruta
def leer_ruta():
    return input()


def mostrar_contenido_fichero(ruta):
    print(f'La ruta es {ruta}')


def pedir_ruta_fichero_destino():
    print('Introduzca la ruta def fichero de destino: ')

#jgj
if __name__ == '__main__':
    while True:
        elegir_opcion_menu()
        opcion_menu = leer_entero('Escoja una opción: ')
        if opcion_menu == 1:
            pedir_ruta_fichero()
            ruta = leer_ruta()
            if os.path.isfile(ruta):
                mostrar_contenido_fichero(ruta)
            else:
                print('La ruta no es un fichero')
        elif opcion_menu == 2:
            pedir_ruta_fichero()
            ruta = leer_ruta()
            pedir_ruta_fichero_destino()
            ruta_destino = leer_ruta()



            
