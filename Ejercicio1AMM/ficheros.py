import os
import shutil

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
    with open("C:/Phyton/fichero1.txt", "r") as archivo:
        for linea in archivo:
            print(linea)
#

def pedir_ruta_fichero_destino():
    print('Introduzca la ruta def fichero de destino: ')

#jgj
def pedir_ruta_directorio():
    print('Introduzca la ruta del directorio: ')


def mostrar_ficheros_directorio(ruta_directorio):
    contenido_directorio = '/Phyton/'
    with os.scandir(contenido_directorio) as ficheros:
        for fichero in ficheros:
            print(fichero.name)

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
            shutil.copy2(ruta, ruta_destino)
            if os.path.isfile(ruta):
                mostrar_contenido_fichero(ruta)
            else:
                print('La ruta de destino no es un fichero')
        elif opcion_menu == 3:
           pedir_ruta_directorio()
           ruta_directorio = leer_ruta()
           if os.path.isdir(ruta_directorio):
               mostrar_ficheros_directorio(ruta_directorio)
           else:
               print('La ruta no es un directorio')
        else:
            opcion_menu == 0
            exit(0)

            
