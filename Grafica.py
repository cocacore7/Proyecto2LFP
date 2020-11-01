import os


def grafico(tokens):
    estado = 0
    nodo = 1
    temp = ""
    pivote = []
    nodos = []
    variable = False
    ciclo = False
    ciclof = False
    ciclos = False
    casos = False
    llamada = False
    imprimir = False
    with open('grafico.dot', 'w') as arch:
        arch.write('digraph grafica{' + "\n")
        arch.write('rankdir=LR;' + "\n")
        arch.write('node [shape = record, style=filled];' + "\n")
        for i in tokens:
            if estado == 0:
                if i == "tk_asignacion":
                    estado = 1
                    variable = True
                elif i == "tk_if" or i == "tk_while":
                    temp = i
                    estado = 1
                    ciclo = True
                elif i == "tk_foreach":
                    temp = i
                    estado = 1
                    ciclof = True
                elif i == "tk_switch":
                    temp = i
                    estado = 1
                    ciclos = True
                elif i == "tk_case" or i == "tk_break" or i == "tk_default":
                    temp = i
                    casos = True
                    estado = 1
                elif i == "tk_iden":
                    temp = i
                    llamada = True
                    estado = 1
                elif i == "tk_print":
                    temp = i
                    imprimir = True
                    estado = 1
                elif i == "tk_}":
                    nodos.append("}")
            elif estado == 1:
                if variable:
                    if i == "tk_iden":
                        temp = i
                    elif i == "tk_=":
                        estado = 2
                    else:
                        estado = 0
                        temp = ""
                        variable = False
                elif ciclo:
                    if i == "tk_(":
                        arch.write('nodo' + str(nodo) + ' [ label ="Sentencia ' + temp + '",fillcolor=green];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                    elif i == "tk_iden":
                        temp = i
                    elif i == "tk_)":
                        arch.write('nodo' + str(nodo) + ' [ label ="Condicion ' + temp + '"];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                    elif i == "tk_{":
                        nodos.append("{")
                        estado = 0
                        ciclo = False
                        temp = ""
                    else:
                        estado = 0
                        temp = ""
                        ciclo = False
                elif ciclof:
                    if i == "tk_(":
                        arch.write('nodo' + str(nodo) + ' [ label ="Sentencia ' + temp + '",fillcolor=green];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                    elif i == "tk_iden" or i == "tk_in":
                        temp = temp + i
                    elif i == "tk_)":
                        arch.write('nodo' + str(nodo) + ' [ label ="Condicion ' + temp + '"];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                    elif i == "tk_{":
                        nodos.append("{")
                        temp = ""
                        estado = 0
                        ciclof = False
                    else:
                        estado = 0
                        temp = ""
                        ciclof = False
                elif ciclos:
                    if i == "tk_(":
                        arch.write('nodo' + str(nodo) + ' [ label ="Sentencia ' + temp + '",fillcolor=green];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                    elif i == "tk_valor":
                        temp = temp + i
                    elif i == "tk_)":
                        arch.write('nodo' + str(nodo) + ' [ label ="Condicion ' + temp + '"];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                    elif i == "tk_{":
                        nodos.append("{")
                        temp = ""
                        estado = 0
                        ciclos = False
                    else:
                        estado = 0
                        temp = ""
                        ciclos = False
                elif casos:
                    if i == "tk_;" or i == "tk_:":
                        arch.write('nodo' + str(nodo) + ' [ label ="Caso ' + temp + '"];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                        estado = 0
                        casos = False
                    else:
                        estado = 0
                        casos = False
                        temp = ""
                elif llamada:
                    if i == "tk_(":
                        arch.write('nodo' + str(nodo) + ' [ label ="Llamada: ' + temp + '"];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                    elif i == "tk_valor" or i == "tk_,":
                        temp = temp + i
                    elif i == "tk_)":
                        arch.write('nodo' + str(nodo) + ' [ label ="Valores: ' + temp + '"];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                        estado = 0
                        llamada = False
                    else:
                        estado = 0
                        temp = ""
                        llamada = False
                elif imprimir:
                    if i == "tk_(":
                        arch.write('nodo' + str(nodo) + ' [ label ="Llamada: ' + temp + '"];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                    elif i == "tk_valor" or i == "tk_,":
                        temp = temp + i
                    elif i == "tk_)":
                        arch.write('nodo' + str(nodo) + ' [ label ="Valores: ' + temp + '"];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                        estado = 0
                        imprimir = False
                    else:
                        estado = 0
                        temp = ""
                        imprimir = False
            elif estado == 2:
                if variable:
                    if i == "tk_valor":
                        arch.write('nodo' + str(nodo) + ' [ label ="Asignacion: ' + temp + '"];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                    elif i == "tk_;":
                        estado = 0
                        variable = False
                    elif i == "tk_(":
                        arch.write('nodo' + str(nodo) + ' [ label ="Llamada: ' + temp + '"];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                        estado = 3
                    else:
                        estado = 0
                        temp = ""
            elif estado == 3:
                if variable:
                    if i == "tk_iden" or i == "tk_,":
                        temp = temp + i
                    elif i == "tk_)":
                        arch.write('nodo' + str(nodo) + ' [ label ="Parametros: ' + temp + '"];' + "\n")
                        nodos.append("nodo" + str(nodo))
                        nodo = nodo + 1
                        temp = ""
                    elif i == "tk_{":
                        nodos.append("{")
                        temp = ""
                        estado = 0
                        variable = False
                    elif i != "tk_=>":
                        estado = 0
                        temp = ""
        bandera = False
        for z in range(0, len(nodos) - 1):
            if z != 0:
                if nodos[z] == "{":
                    pivote.append(nodos[z - 2])
                elif nodos[z] == "}":
                    if nodos[z + 1] != "}":
                        arch.write(pivote.pop() + '->' + nodos[z + 1] + ";" + "\n")
                        bandera = True
                else:
                    if not bandera:
                        if nodos[z - 1] == "{" or nodos[z - 1] == "}":
                            arch.write(nodos[z - 2] + '->' + nodos[z] + ";" + "\n")
                        else:
                            arch.write(nodos[z - 1] + '->' + nodos[z] + ";" + "\n")
                    else:
                        bandera = False
        arch.write('}')
        arch.close()
        print("Grafo Creado")
        os.system("dot -Tpng grafico.dot -o imagen.png")
        os.system("imagen.png")
