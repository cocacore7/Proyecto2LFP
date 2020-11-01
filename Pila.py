def AFDP(tokens):
    pila = []
    leer = ""
    ingresar = ""
    estado = 0
    i = 0
    contador = len(tokens) - 1
    # NoTerminales = S, INICIAL, SEGUNDO, PARAMETROS, VALORES, VF
    # Terminales = tk_switch,tk_foreach,tk_if,tk_while,tk_valor,tk_iden,tk_,,tk_;,tk_:,tk_(,tk_),tk_{,tk_}
    aux = []
    for u in range(0, len(tokens)):
        aux.append(tokens[contador])
        contador = contador - 1
    while i <= len(tokens):
        if estado == 0:
            aux2 = ""
            contador = len(aux) - 1
            for z in range(0, len(aux)):
                aux2 = aux2 + aux[contador] + " | "
                contador = contador - 1
            print("PILA:        Vacio")
            print("ENTRADA:     " + aux2)
            print("TRANSICION:  (0,€,€,1,#)")
            input("Presione Enter Para Continuar")
            pila.append("#")
            estado = 1
        elif estado == 1:
            if pila[0] == "#":
                aux2 = ""
                contador = len(aux) - 1
                for z in range(0, len(aux)):
                    aux2 = aux2 + aux[contador] + " | "
                    contador = contador - 1
                print("PILA:        #")
                print("ENTRADA:     " + aux2)
                print("TRANSICION:  (1,€,€,2,S)")
                print("")
                pila.append("S")
                estado = 2
        elif estado == 2:
            arriba = pila.pop()
            cima = arriba
            if arriba == "S":
                pila.append("INICIAL")
            elif arriba == "INICIAL" or arriba == "SEGUNDO":
                valor = tokens[i]
                leer = valor
                if valor == "tk_asignacion":
                    pila.append("VF")
                    pila.append("tk_=")
                    pila.append("tk_iden")
                    ingresar = "tk_iden|tk_=|VF"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_case":
                    pila.append("tk_:")
                    pila.append("tk_valor")
                    ingresar = "tk_valor|tk_:"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_}":
                    pila.pop()
                    pila.append("SEGUNDO")
                    ingresar = "SEGUNDO"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_;":
                    aux.pop()
                    i = i + 1
                elif valor == "tk_break":
                    pila.append("tk_;")
                    ingresar = "tk_;"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_default":
                    pila.append("tk_:")
                    ingresar = "tk_:"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_while" or valor == "tk_if":
                    pila.append("tk_}")
                    pila.append("SEGUNDO")
                    pila.append("tk_{")
                    pila.append("tk_)")
                    pila.append("tk_iden")
                    pila.append("tk_(")
                    ingresar = "tk_(|tk_iden|tk_)|tk_{|SEGUNDO|tk_}"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_foreach":
                    pila.append("tk_}")
                    pila.append("SEGUNDO")
                    pila.append("tk_{")
                    pila.append("tk_)")
                    pila.append("tk_iden")
                    pila.append("tk_in")
                    pila.append("tk_iden")
                    pila.append("tk_(")
                    ingresar = "tk_(|tk_iden|tk_in|tk_iden|tk_)|tk_{|SEGUNDO|tk_}"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_switch":
                    pila.append("tk_}")
                    pila.append("tk_:")
                    pila.append("tk_valor")
                    pila.append("tk_case")
                    pila.append("tk_{")
                    pila.append("tk_)")
                    pila.append("tk_valor")
                    pila.append("tk_(")
                    ingresar = "tk_(|tk_valor|tk_)|tk_{|tk_case|tk_valor|tk_:|tk_}"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_iden":
                    pila.append("VALORES")
                    ingresar = "VALORES"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_print":
                    pila.append("VALORES")
                    ingresar = "VALORES"
                    aux.pop()
                    i = i + 1
                else:
                    return False
            elif arriba == "PARAMETROS":
                valor = tokens[i]
                leer = valor
                if valor == "tk_(" or valor == "tk_iden" or valor == "tk_," or "tk_valor":
                    pila.append("PARAMETROS")
                    ingresar = "PARAMETROS"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_)":
                    aux.pop()
                    i = i + 1
                else:
                    return False
            elif arriba == "PARAMETROSF":
                valor = tokens[i]
                leer = valor
                if valor == "tk_(" or valor == "tk_iden" or valor == "tk_,":
                    pila.append("PARAMETROSF")
                    ingresar = "PARAMETROSF"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_)":
                    pila.append("tk_}")
                    pila.append("tk_{")
                    pila.append("tk_=>")
                    ingresar = "tk_=>|tk_{|tk_}"
                    aux.pop()
                    i = i + 1
                else:
                    return False
            elif arriba == "VALORES":
                valor = tokens[i]
                leer = valor
                if valor == "tk_(" or valor == "tk_valor" or valor == "tk_,":
                    pila.append("VALORES")
                    ingresar = "VALORES"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_)":
                    pila.append("tk_;")
                    ingresar = "tk_;"
                    aux.pop()
                    i = i + 1
                else:
                    return False
            elif arriba == "VF":
                valor = tokens[i]
                leer = valor
                if valor == "tk_(":
                    pila.append("PARAMETROSF")
                    ingresar = "PARAMETROSF"
                    aux.pop()
                    i = i + 1
                elif valor == "tk_valor":
                    pila.append("tk_;")
                    ingresar = "tk_;"
                    aux.pop()
                    i = i + 1
                else:
                    return False
            elif arriba == "tk_:":
                valor = tokens[i]
                leer = valor
                if valor == arriba:
                    pila.append("SEGUNDO")
                    ingresar = "SEGUNDO"
                    aux.pop()
                    i = i + 1
                else:
                    return False
            elif arriba == "tk_}":
                valor = tokens[i]
                leer = valor
                if valor == arriba:
                    if contador == 1:
                        pila.append("SEGUNDO")
                        ingresar = "SEGUNDO"
                        aux.pop()
                        i = i + 1
                    else:
                        aux.pop()
                        i = i + 1
                else:
                    return False
            elif arriba == "tk_;":
                valor = tokens[i]
                leer = valor
                if valor == arriba:
                    pila.append("SEGUNDO")
                    ingresar = "SEGUNDO"
                    aux.pop()
                    i = i + 1
                else:
                    return False

            elif arriba == "tk_," or arriba == "tk_=" or arriba == "tk_=>" or arriba == "tk_(" or arriba == "tk_)" or \
                    arriba == "tk_{" or arriba == "tk_valor" or arriba == "tk_iden" or arriba == "tk_case" or \
                    arriba == "tk_in":
                valor = tokens[i]
                leer = valor
                if valor == arriba:
                    aux.pop()
                    i = i + 1
                else:
                    return False
            elif arriba == "#":
                leer = ""
                ingresar = ""
                estado = 3
            else:
                return False
            pil = ""
            aux2 = ""
            contador = len(pila) - 1
            for z in range(0, len(pila)):
                pil = pil + pila[contador] + " | "
                contador = contador - 1
            contador = len(aux) - 1
            for z in range(0, len(aux)):
                aux2 = aux2 + aux[contador] + " | "
                contador = contador - 1
            print("")
            print("PILA:     " + pil)
            print("Entrada:  " + aux2)
            print("TRANSICION:  (2," + leer + "," + cima + ",2," + ingresar + ")")
        elif estado == 3:
            print("PILA:----")
            print("ENTRADA:----")
            print("TRANSICION: ACEPTACION")
            return True
        input("Presione Enter Para Continuar")


def numero(palabra):
    bandera = False
    estado = 0
    for i in palabra:
        if estado == 0:
            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or \
                    i == "8" or i == "9":
                bandera = True
            elif i == ".":
                bandera = False
                estado = 1
            else:
                return False
        if estado == 1:
            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or \
                    i == "8" or i == "9":
                bandera = True
            else:
                return False
    return bandera


def cad(palabra):
    bandera = False
    estado = 0
    for i in palabra:
        if estado == 0:
            if i == '"':
                estado = 1
                bandera = True
            else:
                return False
        if estado == 1:
            if i == '"':
                bandera = True
            else:
                bandera = False
    return bandera


def identificador(palabra):
    estado = 0
    for i in palabra:
        if estado == 0:
            if i == "_" or i == "a" or i == "A" or i == "b" or i == "B" or i == "c" or i == "C" or i == "d" or i == "D"\
                    or i == "e" or i == "E" or i == "f" or i == "F" or i == "g" or i == "G" or i == "h" or i == "H" or \
                    i == "i" or i == "I" or i == "j" or i == "J" or i == "k" or i == "K" or i == "l" or i == "L" or \
                    i == "m" or i == "M" or i == "n" or i == "N" or i == "o" or i == "O" or i == "p" or i == "P" or \
                    i == "q" or i == "Q" or i == "r" or i == "R" or i == "s" or i == "S" or i == "t" or i == "T" or \
                    i == "u" or i == "U" or i == "v" or i == "V" or i == "w" or i == "W" or i == "x" or i == "X" or \
                    i == "y" or i == "Y" or i == "z" or i == "Z":
                return True
            else:
                return False
