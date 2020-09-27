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
    contadorAtributos = 0
    aceptado = False
    for i in range(len(opcion)):
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
                    print("SELECCIONAR")
                    estado = 1
                elif palabraReservada.upper() == "LIST":
                    print("LIST")
                    estado = 1
                elif palabraReservada.upper() == "PRINT":
                    print("PRINT")
                    estado = 1
                elif palabraReservada.upper() == "MAX":
                    print("MAX")
                    estado = 1
                elif palabraReservada.upper() == "MIN":
                    print("MIN")
                    estado = 1
                elif palabraReservada.upper() == "SUM":
                    print("SUM")
                    estado = 1
                elif palabraReservada.upper() == "COUNT":
                    print("COUNT")
                    estado = 1
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
            if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                palabraSegundoNivel = palabraSegundoNivel + opcion[i]
            elif opcion[i] == "," or opcion[i] == " ":
                if palabraSegundoNivel != "" and palabraSegundoNivel.upper().strip() != "WHERE":
                    listaAtributos.append(palabraSegundoNivel.strip())
                    palabraSegundoNivel = ""
                if palabraSegundoNivel.upper() == "WHERE":
                    estado = 19
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

        elif estado == 22:
            if opcion[i] != '"':
                palabraCuartoNivel = palabraCuartoNivel + opcion[i]
            else:
                #print("curto nivel en estado 22",palabraCuartoNivel)
                controlador = ControladorEntrada()
                controlador.selectSimple(listaAtributos, palabraTercerNivel, palabraCuartoNivel)
                palabraCuartoNivel = ""
                listaAtributos = []
                palabraTercerNivel = ""
                aceptado = True
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

    if aceptado == False:
        print("ERROR// COMANDO INVALIDO")
        listaAtributos = []
        palabraSegundoNivel = ""
        palabraTercerNivel = ""
        palabraCuartoNivel = ""
        palabraQuintoNivel = ""