from Grafica import grafico

from AFD import AFD
from Pila import AFDP

Script = ""
Tokens = []


def cargar():
    ruta = input("Introducir ruta de archivo: ")
    try:
        with open(ruta, 'r') as miarchivo:
            data = miarchivo.read()
            miarchivo.close()
            return data
    except(OSError, IOError):
        print("Archivo -" + ruta + "- no encontrado")
        print("------------------------------------")
        return ""


def inicio(script, tokens):
    print("-------------------------------------------")
    print("              ---Comandos---               ")
    print("1) CARGAR SCRIPT")
    print("2) MANEJO AFD")
    print("3) PILA INTERACTIVA")
    print("4) DIAGRAMA DE BLOQUES")
    print("5) SALIR")
    print("-------------------------------------------")
    print("")
    comando = input("Introducir numero de comando: ")
    if comando == '1':
        print("-------------------------------------------")
        script = ""
        data = cargar()
        if data != "":
            script = data
            print("-------------------------------------------")
            print(script)
        inicio(script, tokens)
    elif comando == '2':
        print("-------------------------------------------")
        if script != "":
            tokens = AFD(script)
            print(tokens)
            inicio(script, tokens)
        else:
            print("----NO HAY SCRIPTS CARGADOS----")
            inicio(script, tokens)
    elif comando == '3':
        print("-------------------------------------------")
        if tokens:
            bandera = AFDP(tokens)
            if bandera:
                print("Correcto")
            else:
                print("Estructura De Archivo Mala")
            print(tokens)
            inicio(script, tokens)
        else:
            print("----NO HAY TOKENS----")
            inicio(script, tokens)
    elif comando == '4':
        print("-------------------------------------------")
        if tokens:
            grafico(tokens)
            print(tokens)
            inicio(script, tokens)
        else:
            print("----NO HAY TOKENS----")
            inicio(script, tokens)
    elif comando == '5':
        print("-------------------------------------------")
        print("Hasta la proxima! :D")
        exit()
    else:
        print("-------------------------------------------")
        print("----Comando Invalido----")
        inicio(script, tokens)


inicio(Script, Tokens)
