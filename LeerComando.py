from ControladorEntrada import *


class LeerComando:

    def cargarArchivo(self, listaArchivo):
        comando = ""
        for nombreArchivo in listaArchivo:
            if path.exists(f'scriptSIQL/{nombreArchivo}'):
                fichero = open(f'scriptSIQL/{nombreArchivo}', 'r')
                lineasCargadas = fichero.readlines()
                fichero.close()
                cadenaCargada = "".join(lineasCargadas)
                #print(cadenaCargada)
                for i in range(len(cadenaCargada.strip())):
                    if cadenaCargada[i] != ";":
                        comando = comando + cadenaCargada[i]
                    if cadenaCargada[i] == ";":
                        print(comando.strip())
                        self.principalSeg(comando.strip())
                        comando = ""

    def principalSeg(self, op):
        listaAtributos = []
        contadorRep = 0
        opcion = op
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
        dicToken = {}
        for i in range(len(opcion.strip())):
            if estado == 0:
                if opcion[i].isalpha() or opcion[i] == " ":
                    palabraReservada = palabraReservada + opcion[i]
                    if palabraReservada.upper() == "CREATE":
                        estado = 1
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_CREATE"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para crear un set"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                    elif palabraReservada.upper() == "LOAD":
                        estado = 2
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_LOAD"
                        dicToken['Descripcion'] = "Palabra reservada utilizada cargar archivos aon"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                    elif palabraReservada.upper() == "USE":
                        estado = 3
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_USE"
                        dicToken['Descripcion'] = "Palabra reservada utilizada usar un set de memoria"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                    elif palabraReservada.upper() == "SELECT":
                        estado = 4
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_SELECT"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para seleccionar datos en el set en uso"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                    elif palabraReservada.upper() == "SELECCIONAR":
                        estado = 4
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_SELECCIONAR"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para seleccionar datos en el set en uso"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                    elif palabraReservada.upper() == "LIST":
                        estado = 6
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_LIST"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para mostrar una lista"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        continue
                    elif palabraReservada.upper() == "PRINT":
                        estado = 7
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_PRINT"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para agregar color a la salida en consola"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                    elif palabraReservada.upper() == "MAX":
                        estado = 8
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_MAX"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para buscar el valor maximo"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                    elif palabraReservada.upper() == "MIN":
                        estado = 9
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_MIN"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para buscar el valor minimo"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                    elif palabraReservada.upper() == "SUM":
                        estado = 10
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_SUM"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para sumar un conjunto de datos"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                    elif palabraReservada.upper() == "COUNT":
                        estado = 11
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_COUNT"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para contar un conjuto de registros"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                    elif palabraReservada.upper() == "REPORT":
                        estado = 12
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_REPORT"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para generar un reporte"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        continue
                    elif palabraReservada.upper() == "SCRIPT ":
                        estado = 13
                        dicToken['Lexema'] = palabraReservada.upper()
                        dicToken['Token'] = "Tk_SCRIPT"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para cargar archivos siql"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        continue
            elif estado == 1:
                if opcion[i].isalpha():
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if palabraSegundoNivel.upper() == "SET":
                        dicToken['Lexema'] = palabraSegundoNivel.upper()
                        dicToken['Token'] = "Tk_SET"
                        dicToken['Descripcion'] = "Palabra reservada que indica que se utilizara un set de memoria"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 14
            elif estado == 2:
                if opcion[i].isalpha():
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if palabraSegundoNivel.upper() == "INTO":
                        dicToken['Lexema'] = palabraSegundoNivel.upper()
                        dicToken['Token'] = "Tk_INTO"
                        dicToken['Descripcion'] = "Palabra reservada utilizada junto con LOAD para indicar donde se" \
                                                  " cargaran ciertos archivos"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 15
            elif estado == 3:
                if opcion[i].isalpha():
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if palabraSegundoNivel.upper() == "SET":
                        dicToken['Lexema'] = palabraSegundoNivel.upper()
                        dicToken['Token'] = "Tk_SET"
                        dicToken['Descripcion'] = "Palabra reservada que indica que se utilizara un set de memoria"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 18
            elif estado == 4:  # obtener lista de atributos para seleccionar
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_" or opcion[i] == "*" and i != len(
                        opcion.strip()) - 1:
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                elif opcion[i] == "," or opcion[i] == " ":
                    if palabraSegundoNivel != "" and palabraSegundoNivel.upper().strip() != "WHERE":
                        listaAtributos.append(palabraSegundoNivel.strip())
                        dicToken['Lexema'] = palabraSegundoNivel
                        dicToken['Token'] = "Tk_ATRIBUTO"
                        dicToken['Descripcion'] = "Atributo recibido como parametro"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        palabraSegundoNivel = ""
                    if palabraSegundoNivel.upper() == "WHERE":
                        dicToken['Lexema'] = palabraSegundoNivel.upper()
                        dicToken['Token'] = "Tk_WHERE"
                        dicToken['Descripcion'] = "Plabra reservada que indica el inicio de un conjunto de condiciones"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 19
                elif opcion[i] == "*" and i == len(opcion.strip()) - 1:
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    listaAtributos.append(palabraSegundoNivel)
                    controlador = ControladorEntrada()
                    controlador.selectAll(listaAtributos)
                    dicToken['Lexema'] = palabraSegundoNivel
                    dicToken['Token'] = "Tk_ATRIBUTO"
                    dicToken['Descripcion'] = "Selecciona todos los atributos de los datos cargados"
                    RegistroSet.listaTokens.append(dicToken)
                    dicToken = {}
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
                        dicToken['Lexema'] = palabraSegundoNivel.upper()
                        dicToken['Token'] = "Tk_ATTRIBUTES"
                        dicToken['Descripcion'] = "Palabra reservada utilizada junto con LIST indicandole listar los" \
                                                  " atributos de los datos cargados"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        palabraSegundoNivel = ""
                        dicToken['Lexema'] = ";"
                        dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                        dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        aceptado = True

            elif estado == 7:
                if opcion[i].isalpha():
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if palabraSegundoNivel.upper() == "IN":
                        estado = 31
                        dicToken['Lexema'] = palabraSegundoNivel.upper()
                        dicToken['Token'] = "Tk_IN"
                        dicToken['Descripcion'] = "Palabra reservadas que indica el color que utilizara PRINT"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        continue

            elif estado == 8:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if i == len(opcion.strip()) - 1:
                        controlador = ControladorEntrada()
                        controlador.max(palabraSegundoNivel)
                        dicToken['Lexema'] = palabraSegundoNivel
                        dicToken['Token'] = "Tk_ATRIBUTO"
                        dicToken['Descripcion'] = "Atributo recibido como parametro"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        palabraSegundoNivel = ""
                        dicToken['Lexema'] = ";"
                        dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                        dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        aceptado = True

            elif estado == 9:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                    if i == len(opcion.strip()) - 1:
                        controlador = ControladorEntrada()
                        controlador.min(palabraSegundoNivel)
                        dicToken['Lexema'] = palabraSegundoNivel
                        dicToken['Token'] = "Tk_ATRIBUTO"
                        dicToken['Descripcion'] = "Atributo recibido como parametro"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        palabraSegundoNivel = ""
                        dicToken['Lexema'] = ";"
                        dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                        dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        aceptado = True

            elif estado == 10:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_" or opcion[i] == "*":
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                if opcion[i] == "," or opcion[i] == " ":
                    if palabraSegundoNivel != "":
                        listaAtributos.append(palabraSegundoNivel.strip())
                        dicToken['Lexema'] = palabraSegundoNivel
                        dicToken['Token'] = "Tk_ATRIBUTO"
                        dicToken['Descripcion'] = "Atributo recibido como parametro"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        palabraSegundoNivel = ""
                if i == len(opcion.strip()) - 1:
                    if palabraSegundoNivel != " " or palabraSegundoNivel != "":
                        listaAtributos.append(palabraSegundoNivel.strip())
                        control = ControladorEntrada()
                        control.sum(listaAtributos)
                        dicToken['Lexema'] = palabraSegundoNivel
                        dicToken['Token'] = "Tk_ATRIBUTO"
                        dicToken['Descripcion'] = "Atributo recibido como parametro"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        listaAtributos = []
                        dicToken['Lexema'] = ";"
                        dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                        dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        aceptado = True

            elif estado == 11:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_" or opcion[i] == "*":
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                if opcion[i] == "," or opcion[i] == " ":
                    if palabraSegundoNivel != "":
                        listaAtributos.append(palabraSegundoNivel.strip())
                        dicToken['Lexema'] = palabraSegundoNivel
                        dicToken['Token'] = "Tk_ATRIBUTO"
                        dicToken['Descripcion'] = "Atributo recibido como parametro"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        palabraSegundoNivel = ""
                if i == len(opcion.strip()) - 1:
                    if palabraSegundoNivel != " " or palabraSegundoNivel != "":
                        listaAtributos.append(palabraSegundoNivel.strip())
                        control = ControladorEntrada()
                        control.count(listaAtributos)
                        dicToken['Lexema'] = palabraSegundoNivel
                        dicToken['Token'] = "Tk_ATRIBUTO"
                        dicToken['Descripcion'] = "Atributo recibido como parametro"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        listaAtributos = []
                        dicToken['Lexema'] = ";"
                        dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                        dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        aceptado = True

            elif estado == 12:
                if opcion[i].isalpha():
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                if opcion[i] == " " or i == len(opcion.strip()) - 1:
                    if palabraSegundoNivel.upper() == "TO":
                        estado = 32
                        dicToken['Lexema'] = palabraSegundoNivel.upper()
                        dicToken['Token'] = "Tk_TO"
                        dicToken['Descripcion'] = "Palabra reservada utilizada junto con REPORT que indica el nombre " \
                                                  "del reporte"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        palabraSegundoNivel = ""
                        RegistroSet.reporte = True
                    elif palabraSegundoNivel.upper() == "TOKENS":
                        dicToken['Lexema'] = palabraSegundoNivel.upper()
                        dicToken['Token'] = "Tk_TOKENS"
                        dicToken['Descripcion'] = "Palabra reservada utilizada reportar los tokens utilizados"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        #print("report tokens")
                        RegistroSet.nombreReporte = "Reporte tokens"
                        control = ControladorEntrada()
                        control.reporteToken()
                        RegistroSet.listaTokens = []
                        aceptado = True

            elif estado == 13:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "." or opcion[i] == "/" or opcion[
                    i] == '\\' \
                        or opcion[i] == ":":
                    palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                elif opcion[i] == ",":
                    if palabraSegundoNivel != "" or palabraSegundoNivel != " ":
                        listaAtributos.append(palabraSegundoNivel)
                        dicToken['Lexema'] = palabraSegundoNivel
                        dicToken['Token'] = "Tk_NOMBREARCHIVO"
                        dicToken['Descripcion'] = "Atributo recibido que indica el nombre del archivo a buscar"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        palabraSegundoNivel = ""
                if i == len(opcion.strip()) - 1:
                    listaAtributos.append(palabraSegundoNivel)
                    dicToken['Lexema'] = palabraSegundoNivel
                    dicToken['Token'] = "Tk_NOMBREARCHIVO"
                    dicToken['Descripcion'] = "Atributo recibido que indica el nombre del archivo a buscar"
                    RegistroSet.listaTokens.append(dicToken)
                    dicToken = {}
                    palabraSegundoNivel = ""
                    control = ControladorEntrada()
                    control.loadScript(listaAtributos)
                    listaAtributos = []
                    dicToken['Lexema'] = ";"
                    dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                    dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                    RegistroSet.listaTokens.append(dicToken)
                    dicToken = {}
                    aceptado = True

            elif estado == 14:
                if i <= len(opcion):
                    if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                        palabraTercerNivel = palabraTercerNivel + opcion[i]
                        if i == len(opcion.strip()) - 1:
                            # print(palabraReservada + " " + palabraSegundoNivel + " " + palabraTercerNivel)
                            create = ControladorEntrada()
                            create.createSet(palabraTercerNivel)
                            items = RegistroSet.registros.items()
                            dicToken['Lexema'] = palabraTercerNivel
                            dicToken['Token'] = "Tk_NOMBRE_SET"
                            dicToken['Descripcion'] = "Nombre recibido para crear el set"
                            RegistroSet.listaTokens.append(dicToken)
                            dicToken = {}
                            dicToken['Lexema'] = ";"
                            dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                            dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                            RegistroSet.listaTokens.append(dicToken)
                            dicToken = {}
                            print(f"SET ---{palabraTercerNivel}--- CREADO CORRECTAMENTE")
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                            # print(items)
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
                        # print(palabraTercerNivel)
                        dicToken['Lexema'] = palabraTercerNivel
                        dicToken['Token'] = "Tk_NOMBRE_SET"
                        dicToken['Descripcion'] = "Set en el que se cargaran los datos"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 16
            elif estado == 16:
                if opcion[i].isalpha():
                    palabraCuartoNivel = palabraCuartoNivel + opcion[i]
                elif opcion[i] == " ":
                    if palabraCuartoNivel.upper() == "FILES":
                        dicToken['Lexema'] = palabraCuartoNivel.upper()
                        dicToken['Token'] = "Tk_FILES"
                        dicToken['Descripcion'] = "Palabra reservada utilizada para indicar los archivos que se cargaran"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 17
            elif estado == 17:  # obtener archivos a cargar por separado
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_" or opcion[i] == ".":
                    if i == len(opcion.strip()) - 1:
                        palabraQuintoNivel = palabraQuintoNivel + opcion[i]
                        # print("Finaaal")
                        listaAtributos.append(palabraQuintoNivel)
                        dicToken['Lexema'] = palabraQuintoNivel
                        dicToken['Token'] = "Tk_NOMBRE_ARCHIVO"
                        dicToken['Descripcion'] = "Nombre del archivo recibido"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        palabraQuintoNivel = ""
                        # for atributo in listaAtributos:
                        # print("Imprimiendo lista final " + atributo)
                        ctrl = ControladorEntrada()
                        ctrl.loadInto(palabraTercerNivel, listaAtributos)
                        listaAtributos = []
                        dicToken['Lexema'] = ";"
                        dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                        dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        aceptado = True
                    else:
                        palabraQuintoNivel = palabraQuintoNivel + opcion[i]
                elif opcion[i] == ",":
                    listaAtributos.append(palabraQuintoNivel)
                    dicToken['Lexema'] = palabraQuintoNivel
                    dicToken['Token'] = "Tk_NOMBRE_ARCHIVO"
                    dicToken['Descripcion'] = "Nombre del archivo recibido"
                    RegistroSet.listaTokens.append(dicToken)
                    dicToken = {}
                    dicToken['Lexema'] = ","
                    dicToken['Token'] = "Tk_Coma"
                    dicToken['Descripcion'] = "Caracter separador de atributos"
                    RegistroSet.listaTokens.append(dicToken)
                    dicToken = {}
                    palabraQuintoNivel = ""
            elif estado == 18:
                if i <= len(opcion):
                    if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                        palabraTercerNivel = palabraTercerNivel + opcion[i]
                        if i == len(opcion.strip()) - 1:
                            # print(palabraReservada + " " + palabraSegundoNivel + " " + palabraTercerNivel)
                            use = ControladorEntrada()
                            use.useSet(palabraTercerNivel)
                            dicToken['Lexema'] = palabraTercerNivel
                            dicToken['Token'] = "Tk_NOMBRE_SET"
                            dicToken['Descripcion'] = "Nombre recibido del set a usar"
                            RegistroSet.listaTokens.append(dicToken)
                            dicToken = {}
                            dicToken['Lexema'] = ";"
                            dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                            dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                            RegistroSet.listaTokens.append(dicToken)
                            dicToken = {}
                            aceptado = True
            elif estado == 19:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                    palabraTercerNivel = palabraTercerNivel + opcion[i]
                else:
                    if opcion[i] == "<" or opcion[i] == ">" or opcion[i] == "=" or opcion[i] == "!":
                        operacion = operacion + opcion[i]
                        # print(operacion)
                    if contOp == 2:
                        # print(f"{operacion} operacion de primera condicion")
                        estado = 20
                        dicToken['Lexema'] = palabraTercerNivel
                        dicToken['Token'] = "Tk_ATRIBUTO"
                        dicToken['Descripcion'] = "Atributo recibido como parametro"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        dicToken['Lexema'] = operacion
                        dicToken['Token'] = "Tk_OPERACION"
                        dicToken['Descripcion'] = "Operacion de comparacion a realizar"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
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
                if i == len(opcion.strip()) - 1:
                    if palabraCuartoNivel.upper() == "TRUE":
                        # print("rs true cuarto nivel en estado 21")
                        controlador = ControladorEntrada()
                        controlador.selectSimple(listaAtributos, palabraTercerNivel, operacion, True)
                        dicToken['Lexema'] = palabraCuartoNivel
                        dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                        dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        palabraCuartoNivel = ""
                        listaAtributos = []
                        palabraTercerNivel = ""
                        operacion = ""
                        dicToken['Lexema'] = ";"
                        dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                        dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        aceptado = True
                    elif palabraCuartoNivel.upper() == "FALSE":
                        # print("es false cuarto nivel en estado 21")
                        controlador = ControladorEntrada()
                        controlador.selectSimple(listaAtributos, palabraTercerNivel, operacion, False)
                        dicToken['Lexema'] = palabraCuartoNivel
                        dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                        dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        palabraCuartoNivel = ""
                        listaAtributos = []
                        palabraTercerNivel = ""
                        operacion = ""
                        dicToken['Lexema'] = ";"
                        dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                        dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        aceptado = True
                else:
                    if palabraCuartoNivel.upper() == "TRUE":
                        palabraCuartoNivel = True
                        dicToken['Lexema'] = palabraCuartoNivel
                        dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                        dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 23
                    elif palabraCuartoNivel.upper() == "FALSE":
                        palabraCuartoNivel = False
                        dicToken['Lexema'] = palabraCuartoNivel
                        dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                        dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 23

            elif estado == 22:
                if opcion[i] != '"':
                    palabraCuartoNivel = palabraCuartoNivel + opcion[i]
                elif opcion[i] == '"' and i == len(opcion.strip()) - 1:
                    # print("curto nivel en estado 22",palabraCuartoNivel)
                    controlador = ControladorEntrada()
                    controlador.selectSimple(listaAtributos, palabraTercerNivel, operacion, palabraCuartoNivel)
                    dicToken['Lexema'] = palabraCuartoNivel
                    dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                    dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                    RegistroSet.listaTokens.append(dicToken)
                    dicToken = {}
                    palabraCuartoNivel = ""
                    listaAtributos = []
                    palabraTercerNivel = ""
                    operacion = ""
                    dicToken['Lexema'] = ";"
                    dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                    dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                    RegistroSet.listaTokens.append(dicToken)
                    dicToken = {}
                    aceptado = True
                elif opcion[i] == '"' and i != len(opcion.strip()) - 1:
                    estado = 23
            elif estado == 23:
                if opcion[i].isalpha():
                    palabraQuintoNivel = palabraQuintoNivel + opcion[i]
                if palabraQuintoNivel.upper() == "AND" or palabraQuintoNivel.upper() == "OR" or palabraQuintoNivel.upper() == "XOR":
                    dicToken['Lexema'] = palabraQuintoNivel.upper()
                    dicToken['Token'] = "Tk_OPERACION_EXTEND"
                    dicToken['Descripcion'] = "Comapracion que se hara entre el select extendido"
                    RegistroSet.listaTokens.append(dicToken)
                    dicToken = {}
                    estado = 25
                    continue

            if estado == 24:
                if opcion[i].isdigit() or opcion[i] == "." or opcion[i] == "+" or opcion[i] == "-":
                    palabraCuartoNivel = palabraCuartoNivel + opcion[i]
                    if i == len(opcion.strip()) - 1:
                        if palabraCuartoNivel.isdigit():
                            mandarNumero = int(palabraCuartoNivel)
                            controlador = ControladorEntrada()
                            controlador.selectSimple(listaAtributos, palabraTercerNivel, operacion, mandarNumero)
                            dicToken['Lexema'] = palabraCuartoNivel
                            dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                            dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                            RegistroSet.listaTokens.append(dicToken)
                            dicToken = {}
                            palabraCuartoNivel = ""
                            listaAtributos = []
                            palabraTercerNivel = ""
                            operacion = ""
                            dicToken['Lexema'] = ";"
                            dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                            dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                            RegistroSet.listaTokens.append(dicToken)
                            dicToken = {}
                            aceptado = True
                        else:
                            mandarNumero = float(palabraCuartoNivel)
                            # print("numero recib cuarto nivel en estado 24" + str(mandarNumero))
                            controlador = ControladorEntrada()
                            controlador.selectSimple(listaAtributos, palabraTercerNivel, operacion, mandarNumero)
                            dicToken['Lexema'] = palabraCuartoNivel
                            dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                            dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                            RegistroSet.listaTokens.append(dicToken)
                            dicToken = {}
                            palabraCuartoNivel = ""
                            listaAtributos = []
                            palabraTercerNivel = ""
                            operacion = ""
                            dicToken['Lexema'] = ";"
                            dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                            dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                            RegistroSet.listaTokens.append(dicToken)
                            dicToken = {}
                            aceptado = True
                elif opcion[i] == " " and i != len(opcion.strip()) - 1:
                    if palabraCuartoNivel.isdigit():
                        palabraCuartoNivel = int(palabraCuartoNivel)
                        dicToken['Lexema'] = palabraCuartoNivel
                        dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                        dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 23
                    else:
                        palabraCuartoNivel = float(palabraCuartoNivel)
                        dicToken['Lexema'] = palabraCuartoNivel
                        dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                        dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 23

            elif estado == 25:
                if opcion[i].isalpha() or opcion[i].isdigit() or opcion[i] == "_":
                    atributoExtendido = atributoExtendido + opcion[i]
                else:
                    if opcion[i] == "<" or opcion[i] == ">" or opcion[i] == "=" or opcion[i] == "!":
                        operacionExtendida = operacionExtendida + opcion[i]
                    if contOp == 3:
                        estado = 26
                        dicToken['Lexema'] = atributoExtendido
                        dicToken['Token'] = "Tk_ATRIBUTO"
                        dicToken['Descripcion'] = "Atributo de seleccion extendido"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        dicToken['Lexema'] = operacionExtendida
                        dicToken['Token'] = "Tk_OPERACION"
                        dicToken['Descripcion'] = "Operacion a realizarse con los atributos"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
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
                if i == len(opcion.strip()) - 1:
                    if valAtributoExtendido.upper() == "TRUE":
                        valAtributoExtendido = True
                        dicToken['Lexema'] = palabraCuartoNivel
                        dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                        dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 30
                    elif valAtributoExtendido.upper() == "FALSE":
                        valAtributoExtendido = False
                        dicToken['Lexema'] = valAtributoExtendido
                        dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                        dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 30

            elif estado == 28:
                if opcion[i] != '"':
                    valAtributoExtendido = valAtributoExtendido + opcion[i]
                elif opcion[i] == '"' and i == len(opcion.strip()) - 1:
                    estado = 30
                    dicToken['Lexema'] = valAtributoExtendido
                    dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                    dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                    RegistroSet.listaTokens.append(dicToken)
                    dicToken = {}
                    # mandar a otro estado para el controlador

            if estado == 29:
                if opcion[i].isdigit() or opcion[i] == "." or opcion[i] == "+" or opcion[i] == "-":
                    valAtributoExtendido = valAtributoExtendido + opcion[i]
                    if i == len(opcion.strip()) - 1:
                        if valAtributoExtendido.isdigit():
                            valAtributoExtendido = int(valAtributoExtendido)
                            estado = 30
                            dicToken['Lexema'] = valAtributoExtendido
                            dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                            dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                            RegistroSet.listaTokens.append(dicToken)
                            dicToken = {}
                        else:
                            valAtributoExtendido = float(valAtributoExtendido)
                            estado = 30
                            dicToken['Lexema'] = valAtributoExtendido
                            dicToken['Token'] = "Tk_VALOR_ATRIBUTO"
                            dicToken['Descripcion'] = "Valor del atributo para buscar dentro de los datos almacenados"
                            RegistroSet.listaTokens.append(dicToken)
                            dicToken = {}
                            # print("numero recib cuarto nivel en estado 24" + str(mandarNumero))

            if estado == 30:
                # print(listaAtributos)
                # print(palabraTercerNivel, palabraCuartoNivel, palabraQuintoNivel, atributoExtendido, operacionExtendida,
                #      valAtributoExtendido)
                controladorEx = ControladorEntrada()
                controladorEx.selectExtend(listaAtributos, palabraTercerNivel, operacion, palabraCuartoNivel,
                                           palabraQuintoNivel,
                                           atributoExtendido, operacionExtendida, valAtributoExtendido)
                listaAtributos = []
                palabraTercerNivel = ""
                palabraCuartoNivel = ""
                palabraQuintoNivel = ""
                atributoExtendido = ""
                operacionExtendida = ""
                valAtributoExtendido = ""
                aceptado = True
                dicToken['Lexema'] = ";"
                dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                RegistroSet.listaTokens.append(dicToken)
                dicToken = {}

            elif estado == 31:
                if opcion[i].isalpha():
                    palabraTercerNivel = palabraTercerNivel + opcion[i]
                    if i == len(opcion.strip()) - 1:
                        control = ControladorEntrada()
                        control.addColor(palabraTercerNivel.upper())
                        print(f"{RegistroSet.color}", end="")
                        aceptado = True
                        dicToken['Lexema'] = palabraTercerNivel.upper()
                        dicToken['Token'] = "Tk_COLOR"
                        dicToken['Descripcion'] = "Color del que se pitara la consola"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        dicToken['Lexema'] = ";"
                        dicToken['Token'] = "Tk_PUNTO_Y_COMA"
                        dicToken['Descripcion'] = "Caracter de separacion entre las lineas del archivo siql"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}

            elif estado == 32:
                if opcion[i].isdigit() or opcion[i].isalpha() or opcion[i] == "_":
                    palabraTercerNivel = palabraTercerNivel + opcion[i]
                if opcion[i] == " ":
                    if contVacio == 1:
                        # print(palabraTercerNivel)
                        RegistroSet.nombreReporte = palabraTercerNivel
                        dicToken['Lexema'] = palabraTercerNivel
                        dicToken['Token'] = "Tk_NOMBRE_REPORTE"
                        dicToken['Descripcion'] = "Nombre que se le dara al reporte en html"
                        RegistroSet.listaTokens.append(dicToken)
                        dicToken = {}
                        estado = 33
                    else:
                        contVacio = contVacio + 1

            elif estado == 33:
                palabraCuartoNivel = palabraCuartoNivel + opcion[i]
                if i == len(opcion.strip()) - 1:
                    # print(palabraCuartoNivel)
                    # opcion = palabraCuartoNivel
                    estado = 0
                    # print(palabraCuartoNivel)
                    self.principalSeg(str(palabraCuartoNivel))
                    aceptado = True

        if aceptado == False:
            print("ERROR// COMANDO INVALIDO")
            listaAtributos = []
            palabraSegundoNivel = ""
            palabraTercerNivel = ""
            palabraCuartoNivel = ""
            palabraQuintoNivel = ""
