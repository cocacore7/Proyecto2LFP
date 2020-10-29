import webbrowser


def AFD(script):
    linea = 1
    col = 1
    estado = 0
    palabra = ""
    valor = []
    token = []
    descripcion = []
    fila = []
    columna = []
    valorn = []
    tokenn = []
    descripcionn = []
    filan = []
    columnan = []
    tokens = []
    cadena = False
    comentario = False
    controls = False
    for i in script:
        if estado == 0:
            if i == " ":
                if palabra != "":
                    if palabra == "=>":
                        valor.append(palabra)
                        token.append("tk_" + palabra)
                        descripcion.append("Flecha Funcion")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif palabra == "=":
                        valor.append(palabra)
                        token.append("tk_" + palabra)
                        descripcion.append("Asignacion Valor o Funcion")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif palabra == "in":
                        valor.append(palabra)
                        token.append("tk_" + palabra)
                        descripcion.append("Instancia ForEach")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif numero(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Numerico")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif palabra == "true" or palabra == "false":
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Booleano")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif identificador(palabra):
                        valor.append(palabra)
                        token.append("tk_iden")
                        descripcion.append("Identificador")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    else:
                        valorn.append(palabra)
                        tokenn.append("tk_invalido")
                        descripcionn.append("No Pertenece Al Lenguaje")
                        filan.append(linea)
                        columnan.append(col - len(palabra))
                    palabra = ""
            elif i == '(':
                if palabra != "":
                    if cad(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor String")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif numero(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Numerico")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif palabra == "true" or palabra == "false":
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Booleano")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif identificador(palabra):
                        valor.append(palabra)
                        token.append("tk_iden")
                        descripcion.append("Identificador")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    else:
                        valorn.append(palabra)
                        tokenn.append("tk_invalido")
                        descripcionn.append("No Pertenece Al Lenguaje")
                        filan.append(linea)
                        columnan.append(col - len(palabra))
                palabra = ""
                valor.append(i)
                token.append("tk_" + i)
                descripcion.append("Apertura Valores o Parametros")
                fila.append(linea)
                columna.append(col)
            elif i == ')':
                if palabra != "":
                    if cad(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor String")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif numero(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Numerico")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif palabra == "true" or palabra == "false":
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Booleano")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif identificador(palabra):
                        valor.append(palabra)
                        token.append("tk_iden")
                        descripcion.append("Identificador")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    else:
                        valorn.append(palabra)
                        tokenn.append("tk_invalido")
                        descripcionn.append("No Pertenece Al Lenguaje")
                        filan.append(linea)
                        columnan.append(col - len(palabra))
                palabra = ""
                valor.append(i)
                token.append("tk_" + i)
                descripcion.append("Cerradura Valores o Parametros")
                fila.append(linea)
                columna.append(col)
            elif i == "{":
                if palabra != "":
                    if cad(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor String")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif numero(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Numerico")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif palabra == "true" or palabra == "false":
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Booleano")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif identificador(palabra):
                        valor.append(palabra)
                        token.append("tk_iden")
                        descripcion.append("Identificador")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    else:
                        valorn.append(palabra)
                        tokenn.append("tk_invalido")
                        descripcionn.append("No Pertenece Al Lenguaje")
                        filan.append(linea)
                        columnan.append(col - len(palabra))
                palabra = ""
                valor.append(i)
                token.append("tk_" + i)
                descripcion.append("Apertura Contenido")
                fila.append(linea)
                columna.append(col)
            elif i == '}':
                if palabra != "":
                    if cad(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor String")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif numero(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Numerico")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif palabra == "true" or palabra == "false":
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Booleano")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif identificador(palabra):
                        valor.append(palabra)
                        token.append("tk_iden")
                        descripcion.append("Identificador")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    else:
                        valorn.append(palabra)
                        tokenn.append("tk_invalido")
                        descripcionn.append("No Pertenece Al Lenguaje")
                        filan.append(linea)
                        columnan.append(col - len(palabra))
                palabra = ""
                valor.append(i)
                token.append("tk_" + i)
                descripcion.append("Cerradura Contenido")
                fila.append(linea)
                columna.append(col)
            elif i == ':':
                valor.append(i)
                token.append("tk_" + i)
                descripcion.append("Asigancion Case")
                fila.append(linea)
                columna.append(col)
                palabra = ""
            elif i == ';':
                if palabra != "":
                    if cad(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor String")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif numero(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Numerico")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif palabra == "true" or palabra == "false":
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Booleano")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif identificador(palabra):
                        valor.append(palabra)
                        token.append("tk_iden")
                        descripcion.append("Identificador")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    else:
                        valorn.append(palabra)
                        tokenn.append("tk_invalido")
                        descripcionn.append("No Pertenece Al Lenguaje")
                        filan.append(linea)
                        columnan.append(col - len(palabra))
                palabra = ""
                valor.append(i)
                token.append("tk_" + i)
                descripcion.append("Fin de Instruccion")
                fila.append(linea)
                columna.append(col)
            elif i == ',':
                if palabra != "":
                    if cad(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor String")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif numero(palabra):
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Numerico")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif palabra == "true" or palabra == "false":
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Valor Booleano")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    elif identificador(palabra):
                        valor.append(palabra)
                        token.append("tk_iden")
                        descripcion.append("Identificador")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                    else:
                        valorn.append(palabra)
                        tokenn.append("tk_invalido")
                        descripcionn.append("No Pertenece Al Lenguaje")
                        filan.append(linea)
                        columnan.append(col - len(palabra))
                palabra = ""
                valor.append(i)
                token.append("tk_" + i)
                descripcion.append("Separador")
                fila.append(linea)
                columna.append(col)
            elif i == '"':
                estado = 1
                cadena = True
                palabra = ""
                palabra = palabra + i
            elif i == "\n":
                linea = linea + 1
                col = 0
                palabra = ""
            elif i == '\t':
                palabra = ""
            else:
                palabra = palabra + i
                if palabra == "/*":
                    valor.append(palabra)
                    token.append("tk_" + palabra)
                    descripcion.append("Apertura Comentario")
                    fila.append(linea)
                    columna.append(col - len(palabra))
                    estado = 1
                    comentario = True
                    palabra = ""
                elif palabra == "case":
                    valor.append(palabra)
                    token.append("tk_" + palabra)
                    descripcion.append("Switch" + palabra)
                    fila.append(linea)
                    columna.append(col - len(palabra))
                    estado = 1
                    controls = True
                    palabra = ""
                elif palabra == "break" or palabra == "default":
                    valor.append(palabra)
                    token.append("tk_" + palabra)
                    descripcion.append("Switch" + palabra)
                    fila.append(linea)
                    columna.append(col - len(palabra))
                    palabra = ""
                elif palabra == "switch" or palabra == "foreach" or palabra == "if" or palabra == "while":
                    valor.append(palabra)
                    token.append("tk_" + palabra)
                    descripcion.append("Sentencia Control" + palabra)
                    fila.append(linea)
                    columna.append(col - len(palabra))
                    palabra = ""
                elif palabra == "const" or palabra == "let" or palabra == "var":
                    valor.append(palabra)
                    token.append("tk_asignacion")
                    descripcion.append("Tipo Variable" + palabra)
                    fila.append(linea)
                    columna.append(col - len(palabra))
                    palabra = ""
                elif palabra == "print":
                    valor.append(palabra)
                    token.append("tk_" + palabra)
                    descripcion.append("Imprimir En Pantalla")
                    fila.append(linea)
                    columna.append(col - len(palabra))
                    palabra = ""
        elif estado == 1:
            if i == "\n":
                linea = linea + 1
                col = 0
                palabra = ""
            elif i == '\t':
                palabra = ""
            else:
                if comentario:
                    if i == "*":
                        estado = 2
                    else:
                        palabra = palabra + i
                elif cadena:
                    palabra = palabra + i
                    if i == '"':
                        valor.append(palabra)
                        token.append("tk_valor")
                        descripcion.append("Cadena")
                        fila.append(linea)
                        columna.append(col - len(palabra))
                        palabra = ""
                        estado = 0
                        cadena = False
                elif controls:
                    if i == ':':
                        if palabra != "":
                            if numero(palabra):
                                valor.append(palabra)
                                token.append("tk_valor")
                                descripcion.append("Numero Case")
                                fila.append(linea)
                                columna.append(col)
                        valor.append(i)
                        token.append("tk_" + i)
                        descripcion.append("Asignacion Case")
                        fila.append(linea)
                        columna.append(col)
                        palabra = ""
                        estado = 0
                        controls = False
                    else:
                        palabra = palabra + i
        elif estado == 2:
            if i == "/":
                valor.append(palabra)
                token.append("tk_comentario")
                descripcion.append("Contenido Comentario")
                fila.append(linea)
                columna.append(col - len(palabra))
                valor.append("*/")
                token.append("tk_*/")
                descripcion.append("Cerradura Comentario")
                fila.append(linea)
                columna.append(col)
                estado = 0
                comentario = False
            else:
                palabra = palabra + "*" + i
                estado = 1
        col = col + 1
    reporte("Valido", valor, token, descripcion, fila, columna)
    reporte("NoValido", valorn, tokenn, descripcionn, filan, columnan)
    bandera = False
    for i in range(len(valor)):
        if bandera:
            if token[i] == "tk_*/":
                bandera = False
        else:
            if token[i] == "tk_/*":
                bandera = True
            else:
                tokens.append(token[i])
    return tokens


def reporte(nombre, valor, token, descripcion, fila, columna):
    with open(nombre + '.html', 'w') as arch:
        arch.write('<!DOCTYPE html>' + "\n")
        arch.write('<html lang="en">' + "\n")
        arch.write('<head>' + "\n")
        arch.write('   <meta charset="UTF-8">' + "\n")
        arch.write('   <title>Document</title>' + "\n")
        arch.write('   <style type="text/css">' + "\n")
        arch.write('       body{background: url(fondo.jpg);background-size: 100%;}' + "\n")
        arch.write('h4{width: 400px;height: 40px;line-height: 60px;text-align: center;background: yellow;}'
                   + "\n")
        arch.write('h3{width: 400px;height: 40px;line-height: 60px;text-align: center;background: SkyBlue;}'
                   + "\n")
        arch.write('table{width: 400px;height: 40px;border-collapse: collapse;background: SkyBlue;}'
                   + "\n")
        arch.write('td,th { border: 1px solid black; }'
                   + "\n")
        arch.write('   </style>' + "\n")
        arch.write('</head>' + "\n")
        arch.write('<body>' + "\n")
        arch.write('<center>' + "\n")

        arch.write('<table>')
        arch.write('<tr>')
        arch.write('<td>Valor</td>')
        arch.write('<td>Token</td>')
        arch.write('<td>Descripcion</td>')
        arch.write('<td>Fila</td>')
        arch.write('<td>Columna</td>')
        arch.write('</tr>')

        for i in range(len(valor)):
            arch.write('<tr>')
            arch.write('<td>' + str(valor[i]) + '</td>')
            arch.write('<td>' + str(token[i]) + '</td>')
            arch.write('<td>' + str(descripcion[i]) + '</td>')
            arch.write('<td>' + str(fila[i]) + '</td>')
            arch.write('<td>' + str(columna[i]) + '</td>')
            arch.write('</tr>')
        arch.write('</table>')

        arch.write('</center>' + "\n")
        arch.write('</body>' + "\n")
        arch.write('</html>')
        arch.close()
        print("Reporte Creado")
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(nombre+".html")


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
