from LeerComando import *
from CargarArchivo import *
from RegistroSet import *
from ControladorEntrada import *

def principal(op):
    listaAtributos = []
    contadorRep = 0
    while True:
        if op != "a" and contadorRep == 0 and RegistroSet.reporte == True:
            opcion = op
            contadorRep += 1
        else:
            opcion = str(input("Ingrese el comando\n"))
            contadorRep = 0
        estado = 0
        palabraReservada = ""
        palabraSegundoNivel = ""
        palabraTercerNivel = ""
        palabraCuartoNivel = ""
        palabraQuintoNivel = ""
        atributoExtendido = ""
        valAtributoExtendido = ""
        operacionExtendida = ""
        operacion = ""
        contOp = 0
        contadorAtributos = 0
        aceptado = False
        contVacio = 0
        for i in range(len(opcion.strip())):
            if estado == 0:
                if opcion[i].isalpha() or opcion[i] == " ":
                    palabraReservada = palabraReservada + opcion[i]
                    if palabraReservada.upper() == "CREATE":
                        estado = 1
                    elif palabraReservada.upper() == "LOAD":
                        estado = 2
                    elif palabraReservada.upper() == "USE":
                        estado = 3
                    elif palabraReservada.upper() == "SELECT":
                        estado = 4
                    elif palabraReservada.upper() == "SELECCIONAR":
                        estado = 4
                    elif palabraReservada.upper() == "LIST":
                        estado = 6
                        continue
                    elif palabraReservada.upper() == "PRINT":
                        estado = 7
                    elif palabraReservada.upper() == "MAX":
                        estado = 8
                    elif palabraReservada.upper() == "MIN":
                        estado = 9
                    elif palabraReservada.upper() == "SUM":
                        estado = 10
                    elif palabraReservada.upper() == "COUNT":
                        estado = 11
                    elif palabraReservada.upper() == "REPORT ":
                        estado = 12
                        continue
                    elif palabraReservada.upper() == "SCRIPT ":
                        estado = 13
                        continue
            elif estado == 1:
                if opcion[i].isalpha():
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if palabraSegundoNivel.upper() == "SET":
                        estado = 14
            elif estado == 2:
                if opcion[i].isalpha():
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if palabraSegundoNivel.upper() == "INTO":
                        estado = 15
            elif estado == 3:
                if opcion[i].isalpha():
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if palabraSegundoNivel.upper() == "SET":
                        estado = 18
            elif estado == 4: #obtener lista de atributos para seleccionar
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_" or opcion[i] == "*" and i != len(opcion.strip())-1:
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                elif opcion[i] == "," or opcion[i] == " ":
                    if palabraSegundoNivel != "" and palabraSegundoNivel.upper().strip() != "WHERE":
                        listaAtributos.append(palabraSegundoNivel.strip())
                        palabraSegundoNivel = ""
                    if palabraSegundoNivel.upper() == "WHERE":
                        estado = 19
                elif opcion[i] == "*" and i == len(opcion.strip()) - 1:
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    listaAtributos.append(palabraSegundoNivel)
                    controlador = ControladorEntrada()
                    controlador.selectAll(listaAtributos)
                    palabraCuartoNivel = ""
                    listaAtributos = []
                    palabraTercerNivel = ""
                    aceptado = True

            elif estado == 6:
                if opcion[i].isalpha():
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if palabraSegundoNivel.upper() == "ATTRIBUTES":
                        control = ControladorEntrada()
                        control.listAttributes()
                        palabraSegundoNivel = ""
                        aceptado = True

            elif estado == 7:
                if opcion[i].isalpha():
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if palabraSegundoNivel.upper() == "IN":
                        estado = 31
                        continue

            elif estado == 8:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if i == len(opcion.strip()) - 1:
                        controlador = ControladorEntrada()
                        controlador.max(palabraSegundoNivel)
                        palabraSegundoNivel = ""
                        aceptado = True

            elif estado == 9:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if i == len(opcion.strip()) - 1:
                        controlador = ControladorEntrada()
                        controlador.min(palabraSegundoNivel)
                        palabraSegundoNivel = ""
                        aceptado = True

            elif estado == 10:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_" or opcion[i] == "*":
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                if opcion[i] == "," or opcion[i] == " ":
                    if palabraSegundoNivel != "":
                        listaAtributos.append(palabraSegundoNivel.strip())
                        palabraSegundoNivel = ""
                if i == len(opcion.strip()) - 1:
                    if palabraSegundoNivel != " " or palabraSegundoNivel != "":
                        listaAtributos.append(palabraSegundoNivel.strip())
                        control = ControladorEntrada()
                        control.sum(listaAtributos)
                        listaAtributos = []
                        aceptado = True

            elif estado == 11:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_" or opcion[i] == "*":
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                if opcion[i] == "," or opcion[i] == " ":
                    if palabraSegundoNivel != "":
                        listaAtributos.append(palabraSegundoNivel.strip())
                        palabraSegundoNivel = ""
                if i == len(opcion.strip()) - 1:
                    if palabraSegundoNivel != " " or palabraSegundoNivel != "":
                        listaAtributos.append(palabraSegundoNivel.strip())
                        control = ControladorEntrada()
                        control.count(listaAtributos)
                        listaAtributos = []
                        aceptado = True

            elif estado == 12:
                if opcion[i].isalpha():
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                if opcion[i] == " " or i == len(opcion.strip()) - 1:
                    if palabraSegundoNivel.upper() == "TO":
                        estado = 32
                        palabraSegundoNivel = ""
                        RegistroSet.reporte = True
                    elif palabraSegundoNivel.upper() == "TOKENS":
                        print("report tokens")
                        RegistroSet.nombreReporte = "Reporte tokens"
                        control = ControladorEntrada()
                        control.reporteToken()
                        RegistroSet.listaTokens = []
                        aceptado = True
            elif estado == 13:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "." or opcion[i] == "/" or opcion[i] == '\\' \
                        or opcion[i] == ":":
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                elif opcion[i] == ",":
                    if palabraSegundoNivel != "" or palabraSegundoNivel != " ":
                        listaAtributos.append(palabraSegundoNivel)
                        palabraSegundoNivel = ""
                if i == len(opcion.strip()) - 1:
                    listaAtributos.append(palabraSegundoNivel)
                    palabraSegundoNivel = ""
                    #control = ControladorEntrada()
                    #control.loadScript(listaAtributos)
                    leer = LeerComando()
                    leer.cargarArchivo(listaAtributos)
                    listaAtributos = []
                    aceptado = True

            elif estado == 14:
                if i <= len(opcion):
                    if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                        palabraTercerNivel = palabraTercerNivel + opcion[i]
                        if i == len(opcion.strip()) - 1:
                            #print(palabraReservada + " " + palabraSegundoNivel + " " + palabraTercerNivel)
                            create = ControladorEntrada()
                            create.createSet(palabraTercerNivel)
                            items = RegistroSet.registros.items()
                            print(f"SET ---{palabraTercerNivel}--- CREADO CORRECTAMENTE")
                            print("//////////////////////////////////////////////////////////////////////////////////////////////////")
                            print()
                            #print(items)
                            palabraReservada = ""
                            palabraSegundoNivel = ""
                            palabraTercerNivel = ""
                            aceptado = True
            elif estado == 15:
                registro = RegistroSet.registros
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                    palabraTercerNivel = palabraTercerNivel + opcion[i]
                elif opcion[i] == " ":
                    contadorAtributos = contadorAtributos + 1
                    if contadorAtributos == 2:
                        #print(palabraTercerNivel)
                        estado = 16
            elif estado == 16:
                if opcion[i].isalpha():
                    palabraCuartoNivel = palabraCuartoNivel + opcion[i]
                elif opcion[i] == " ":
                    if palabraCuartoNivel.upper() == "FILES":
                        estado = 17
            elif estado == 17: #obtener archivos a cargar por separado
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_" or opcion[i] == ".":
                    if i == len(opcion.strip()) - 1:
                        palabraQuintoNivel = palabraQuintoNivel + opcion[i]
                        #print("Finaaal")
                        listaAtributos.append(palabraQuintoNivel)
                        palabraQuintoNivel = ""
                        #for atributo in listaAtributos:
                            #print("Imprimiendo lista final " + atributo)
                        ctrl = ControladorEntrada()
                        ctrl.loadInto(palabraTercerNivel, listaAtributos)
                        listaAtributos = []
                        aceptado = True
                    else:
                        palabraQuintoNivel = palabraQuintoNivel + opcion[i]
                elif opcion[i] == ",":
                    listaAtributos.append(palabraQuintoNivel)
                    palabraQuintoNivel = ""
            elif estado == 18:
                if i <= len(opcion):
                    if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                        palabraTercerNivel = palabraTercerNivel + opcion[i]
                        if i == len(opcion.strip()) - 1:
                            #print(palabraReservada + " " + palabraSegundoNivel + " " + palabraTercerNivel)
                            use = ControladorEntrada()
                            use.useSet(palabraTercerNivel)
                            aceptado = True
            elif estado == 19:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                    palabraTercerNivel = palabraTercerNivel + opcion[i]
                else:
                    if opcion[i] == "<" or opcion[i] == ">" or opcion[i] == "=" or opcion[i] == "!":
                        operacion = operacion + opcion[i]
                    if contOp == 2:
                        estado = 20
                        contOp = 0
                    else:
                        contOp = contOp + 1


            elif estado == 20:
                if opcion[i].isdigit() or opcion[i] == "-" or opcion[i] == "+":
                    estado = 24
                elif opcion[i].isalpha():
                    palabraCuartoNivel = palabraCuartoNivel + opcion[i]
                    if palabraCuartoNivel.upper() == "TRUE" or palabraCuartoNivel.upper() == "FALSE":
                        estado = 21
                elif opcion[i] == '"':
                    estado = 22
                    continue
            if estado == 21:
                if i == len(opcion.strip())-1:
                    if palabraCuartoNivel.upper() == "TRUE":
                        #print("rs true cuarto nivel en estado 21")
                        controlador = ControladorEntrada()
                        controlador.selectSimple(listaAtributos, palabraTercerNivel, operacion, True)
                        palabraCuartoNivel = ""
                        listaAtributos = []
                        palabraTercerNivel = ""
                        operacion = ""
                        aceptado = True
                    elif palabraCuartoNivel.upper() == "FALSE":
                        #print("es false cuarto nivel en estado 21")
                        controlador = ControladorEntrada()
                        controlador.selectSimple(listaAtributos, palabraTercerNivel, operacion,False)
                        palabraCuartoNivel = ""
                        listaAtributos = []
                        palabraTercerNivel = ""
                        operacion = ""
                        aceptado = True
                else:
                    if palabraCuartoNivel.upper() == "TRUE":
                        palabraCuartoNivel = True
                        estado = 23
                    elif palabraCuartoNivel.upper() == "FALSE":
                        palabraCuartoNivel = False
                        estado = 23

            elif estado == 22:
                if opcion[i] != '"':
                    palabraCuartoNivel = palabraCuartoNivel + opcion[i]
                elif opcion[i] == '"' and i == len(opcion.strip()) - 1:
                    #print("curto nivel en estado 22",palabraCuartoNivel)
                    controlador = ControladorEntrada()
                    controlador.selectSimple(listaAtributos, palabraTercerNivel, operacion,palabraCuartoNivel)
                    palabraCuartoNivel = ""
                    listaAtributos = []
                    palabraTercerNivel = ""
                    operacion = ""
                    aceptado = True
                elif opcion[i] == '"' and i != len(opcion.strip()) - 1:
                    estado = 23
            elif estado == 23:
                if opcion[i].isalpha():
                    palabraQuintoNivel = palabraQuintoNivel + opcion[i]
                if palabraQuintoNivel.upper() == "AND" or palabraQuintoNivel.upper() == "OR" or palabraQuintoNivel.upper() == "XOR":
                    estado = 25
                    continue

            if estado == 24:
                if opcion[i].isdigit() or opcion[i] == "." or opcion[i] == "+" or opcion[i] == "-":
                    palabraCuartoNivel = palabraCuartoNivel + opcion[i]
                    if i == len(opcion.strip()) - 1:
                        if palabraCuartoNivel.isdigit():
                            mandarNumero = int(palabraCuartoNivel)
                            controlador = ControladorEntrada()
                            print(listaAtributos, palabraTercerNivel, operacion, mandarNumero)
                            controlador.selectSimple(listaAtributos, palabraTercerNivel, operacion, mandarNumero)
                            palabraCuartoNivel = ""
                            listaAtributos = []
                            palabraTercerNivel = ""
                            operacion = ""
                            aceptado = True
                        else:
                            mandarNumero = float(palabraCuartoNivel)
                            #print("numero recib cuarto nivel en estado 24" + str(mandarNumero))
                            controlador = ControladorEntrada()
                            controlador.selectSimple(listaAtributos, palabraTercerNivel, operacion, mandarNumero)
                            palabraCuartoNivel = ""
                            listaAtributos = []
                            palabraTercerNivel = ""
                            operacion = ""
                            aceptado = True
                elif opcion[i] == " " and i != len(opcion.strip()) - 1:
                    if palabraCuartoNivel.isdigit():
                        palabraCuartoNivel = int(palabraCuartoNivel)
                        estado = 23
                    else:
                        palabraCuartoNivel = float(palabraCuartoNivel)
                        estado = 23

            elif estado == 25:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                    atributoExtendido = atributoExtendido + opcion[i]
                else:
                    if opcion[i] == "<" or opcion[i] == ">" or opcion[i] == "=" or opcion[i] == "!":
                        operacionExtendida = operacionExtendida + opcion[i]
                    if contOp == 3:
                        estado = 26
                        contOp = 0
                    else:
                        contOp = contOp + 1
            elif estado == 26:
                if opcion[i].isdigit() or opcion[i] == "-" or opcion[i] == "+":
                    estado = 29
                elif opcion[i].isalpha():
                    valAtributoExtendido = valAtributoExtendido + opcion[i]
                    if valAtributoExtendido.upper() == "TRUE" or valAtributoExtendido.upper() == "FALSE":
                        estado = 27
                elif opcion[i] == '"':
                    estado = 28
                    continue
            if estado == 27:
                if i == len(opcion.strip())-1:
                    if valAtributoExtendido.upper() == "TRUE":
                        valAtributoExtendido = True
                        estado = 30
                    elif valAtributoExtendido.upper() == "FALSE":
                        valAtributoExtendido = False
                        estado = 30

            elif estado == 28:
                if opcion[i] != '"':
                    valAtributoExtendido = valAtributoExtendido + opcion[i]
                elif opcion[i] == '"' and i == len(opcion.strip()) - 1:
                    estado = 30
                    #mandar a otro estado para el controlador

            if estado == 29:
                if opcion[i].isdigit() or opcion[i] == "." or opcion[i] == "+" or opcion[i] == "-":
                    valAtributoExtendido = valAtributoExtendido + opcion[i]
                    if i == len(opcion.strip()) - 1:
                        if valAtributoExtendido.isdigit():
                            valAtributoExtendido = int(valAtributoExtendido)
                            estado = 30
                        else:
                            valAtributoExtendido = float(valAtributoExtendido)
                            estado = 30
                            #print("numero recib cuarto nivel en estado 24" + str(mandarNumero))

            if estado == 30:
                #print(listaAtributos)
                #print(palabraTercerNivel, palabraCuartoNivel, palabraQuintoNivel, atributoExtendido, operacionExtendida,
                #      valAtributoExtendido)
                controladorEx = ControladorEntrada()
                controladorEx.selectExtend(listaAtributos, palabraTercerNivel, operacion, palabraCuartoNivel, palabraQuintoNivel,
                                           atributoExtendido, operacionExtendida, valAtributoExtendido)
                listaAtributos = []
                palabraTercerNivel = ""
                palabraCuartoNivel = ""
                palabraQuintoNivel = ""
                atributoExtendido = ""
                operacionExtendida = ""
                valAtributoExtendido = ""
                aceptado = True

            elif estado == 31:
                if opcion[i].isalpha():
                    palabraTercerNivel = palabraTercerNivel + opcion[i]
                    if i == len(opcion.strip()) - 1:
                        control = ControladorEntrada()
                        control.addColor(palabraTercerNivel.upper())
                        print(f"{RegistroSet.color}", end="")
                        aceptado = True

            elif estado == 32:
                if opcion[i].isdigit() or opcion[i].isalpha() or opcion[i] == "_":
                    palabraTercerNivel = palabraTercerNivel + opcion[i]
                if opcion[i] == " ":
                    if contVacio == 1:
                        #print(palabraTercerNivel)
                        RegistroSet.nombreReporte = palabraTercerNivel
                        estado = 33
                    else:
                        contVacio = contVacio + 1

            elif estado == 33:
                palabraCuartoNivel = palabraCuartoNivel + opcion[i]
                if i == len(opcion.strip()) - 1:
                    #print(palabraCuartoNivel)
                    #opcion = palabraCuartoNivel
                    estado = 0
                    #print(palabraCuartoNivel)
                    principal(str(palabraCuartoNivel))


        if aceptado == False:
            print("ERROR// COMANDO INVALIDO")
            listaAtributos = []
            palabraSegundoNivel = ""
            palabraTercerNivel = ""
            palabraCuartoNivel = ""
            palabraQuintoNivel = ""

            #dar formato a los numeros que se manda al metodo ya que todos se mandan como string y eso no se acepta

def principalSinAtrb():
    cadena = "a"
    principal(cadena)
if __name__ == '__main__':
    principalSinAtrb()
