from CargarArchivo import *
from RegistroSet import *
from ControladorEntrada import *

# nombreArchivo = input("Agregue el nombre del archivo")
# carga = CargarArchivo()
# contenido = carga.cargarArchivo(nombreArchivo)
# if contenido != None:
#     cadena = "".join(contenido)
#     print(cadena)
# else:
#     print(f"El archivo {nombreArchivo} no existe")
listaAtributos = []
while True:
    opcion = input("Ingrese el comando\n")
    estado = 0
    palabraReservada = ""
    palabraSegundoNivel = ""
    palabraTercerNivel = ""
    palabraCuartoNivel = ""
    palabraQuintoNivel = ""
    atributoExtendido = ""
    valAtributoExtendido = ""
    operacionExtendida = ""
    contOp = 0
    contadorAtributos = 0
    aceptado = False
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
                elif palabraReservada.upper() == "REPORT":
                    print("REPORT")
                    estado = 1
                elif palabraReservada.upper() == "SCRIPT":
                    print("SCRIPT")
                    estado = 1
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
            if opcion[i] == "," or opcion[i] == " " or i == len(opcion.strip()) - 1:
                if palabraSegundoNivel != "":
                    listaAtributos.append(palabraSegundoNivel.strip())
                    control = ControladorEntrada()
                    control.sum(listaAtributos)
                    palabraSegundoNivel = ""
                    listaAtributos = []
                    aceptado = True

        elif estado == 11:
            if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_" or opcion[i] == "*":
                palabraSegundoNivel = palabraSegundoNivel + opcion[i]
            if opcion[i] == "," or opcion[i] == " " or i == len(opcion.strip()) - 1:
                if palabraSegundoNivel != "":
                    listaAtributos.append(palabraSegundoNivel.strip())
                    control = ControladorEntrada()
                    control.count(listaAtributos)
                    palabraSegundoNivel = ""
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
            if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] =="_":
                palabraTercerNivel = palabraTercerNivel + opcion[i]
            elif opcion[i] == "=":
                #print(f"esta es la palabra en el etados 19:{palabraTercerNivel}--")
                estado = 20
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
                    controlador.selectSimple(listaAtributos,palabraTercerNivel,True)
                    palabraCuartoNivel = ""
                    listaAtributos = []
                    palabraTercerNivel = ""
                    aceptado = True
                elif palabraCuartoNivel.upper() == "FALSE":
                    #print("es false cuarto nivel en estado 21")
                    controlador = ControladorEntrada()
                    controlador.selectSimple(listaAtributos, palabraTercerNivel, False)
                    palabraCuartoNivel = ""
                    listaAtributos = []
                    palabraTercerNivel = ""
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
                controlador.selectSimple(listaAtributos, palabraTercerNivel, palabraCuartoNivel)
                palabraCuartoNivel = ""
                listaAtributos = []
                palabraTercerNivel = ""
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
                        controlador.selectSimple(listaAtributos, palabraTercerNivel, mandarNumero)
                        palabraCuartoNivel = ""
                        listaAtributos = []
                        palabraTercerNivel = ""
                        aceptado = True
                    else:
                        mandarNumero = float(palabraCuartoNivel)
                        #print("numero recib cuarto nivel en estado 24" + str(mandarNumero))
                        controlador = ControladorEntrada()
                        controlador.selectSimple(listaAtributos, palabraTercerNivel, mandarNumero)
                        palabraCuartoNivel = ""
                        listaAtributos = []
                        palabraTercerNivel = ""
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
            controladorEx.selectExtend(listaAtributos, palabraTercerNivel, palabraCuartoNivel, palabraQuintoNivel,
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
                if i == len(opcion.strip()) -1:
                    control = ControladorEntrada()
                    control.addColor(palabraTercerNivel.upper())
                    print(f"{RegistroSet.color}",end="")
                    aceptado = True

    if aceptado == False:
        print("ERROR// COMANDO INVALIDO")
        listaAtributos = []
        palabraSegundoNivel = ""
        palabraTercerNivel = ""
        palabraCuartoNivel = ""
        palabraQuintoNivel = ""

        #dar formato a los numeros que se manda al metodo ya que todos se mandan como string y eso no se acepta