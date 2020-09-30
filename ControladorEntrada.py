from CargarArchivo import *
from RegistroSet import *
class ControladorEntrada:
    def createSet(self, nombreSet):
        RegistroSet.registros[nombreSet] = []

    def loadInto(self, espacioSelf, listaArchivo):
        #print(espacioSelf)
        if RegistroSet.registros.get(espacioSelf) != None:
            cargar = CargarArchivo()
            for archivo in listaArchivo:
                contenido = cargar.cargarArchivo(archivo)
                if contenido != None:
                    #print(contenido)
                    convStr = "".join(contenido)
                    self.readAon(convStr, espacioSelf)
        else:
            print(f"El SELF {espacioSelf} no existe")
            print("//////////////////////////////////////////////////////////////////////////////////////////////////")

    def readAon(self, entrada, espacioSelf):
        dicDatos = {}
        #print("llego al readAon")
        estado = 0
        nombreAtributo = ""
        comilla = 0
        valorAtribuo = ""
        for i in range(len(entrada)):
            if estado == 0:
                if entrada[i] == "(":
                    estado = 1
                    #print("( ---- token parentesis abierto")
            elif estado == 1:
                if entrada[i] == "<":
                    estado = 2
                    #print("< ---- token menor que")
            elif estado == 2:
                if entrada[i] == "[":
                    estado = 3
                    #print("[ ---- token corchete abierto")
            elif estado == 3:
                if entrada[i].isalpha() or entrada[i].isdigit() or entrada[i] == "_":
                    nombreAtributo = nombreAtributo + entrada[i]
                elif entrada[i] == "]":
                    estado = 4
                    #print(f"{nombreAtributo} ---- token nombre atributo")
                    #print("] ---- token corchete cerrado")
                    #nombreAtributo = ""
            elif estado == 4:
                if entrada[i] == "=":
                    estado = 5
                    #print("= ---- token asignacion")
            elif estado == 5:
                if entrada[i].isdigit() or entrada[i] == "-" or entrada[i] == "+":
                    estado = 6
                    # --i
                elif entrada[i].isalpha():
                    valorAtribuo = valorAtribuo + entrada[i]
                    if valorAtribuo.upper() == "TRUE" or valorAtribuo.upper() == "FALSE":
                        estado = 7
                        if valorAtribuo.upper() == "TRUE":
                            dicDatos[nombreAtributo] = True
                        else:
                            dicDatos[nombreAtributo] = False
                        #print(f"{valorAtribuo} ---- token valor atributo")
                        nombreAtributo = ""
                        valorAtribuo = ""
                elif entrada[i] == '"':
                    estado = 8
                    #print('" ---- token inicio de cadena')
                    continue
            if estado == 6:
                if entrada[i].isdigit() or entrada[i] == "." or entrada[i] == "+" or entrada[i] == "-":
                    valorAtribuo = valorAtribuo + entrada[i]
                elif entrada[i] == ">":
                    estado = 10
                    #print(f"{valorAtribuo} ---- token valor atributo")
                    #print(" > ---- token mayor que")
                    try:
                        dicDatos[nombreAtributo] = int(valorAtribuo)
                    except:
                        dicDatos[nombreAtributo] = float(valorAtribuo)
                    nombreAtributo = ""
                    valorAtribuo = ""
                elif entrada[i] == ",":
                    estado = 2
                    #print(f"{valorAtribuo} ---- token valor atributo")
                    #print(", ---- token coma")
                    try:
                        dicDatos[nombreAtributo] = int(valorAtribuo)
                    except:
                        dicDatos[nombreAtributo] = float(valorAtribuo)
                    nombreAtributo = ""
                    valorAtribuo = ""
            elif estado == 7:
                if entrada[i] == ">":
                    estado = 10
                    #print("> ---- token mayor que")
                elif entrada[i] == ",":
                    estado = 2
                    #RegistroSet.registros.get(espacioSelf).append(dicDatos)
                    #print(", ---- token coma")
            elif estado == 8:
                if entrada[i] != '"':
                    valorAtribuo = valorAtribuo + entrada[i]
                else:
                    estado = 9
                    #print(f"{valorAtribuo} ---- token valor del atributo")
                    #print('" ---- token final cadena')
                    dicDatos[nombreAtributo] = valorAtribuo
                    valorAtribuo = ""
                    nombreAtributo = ""
            elif estado == 9:
                if entrada[i] == ">":
                    estado = 10
                    #print("> ---- token mayor que")
                elif entrada[i] == ",":
                    estado = 2
                    #RegistroSet.registros.get(espacioSelf).append(dicDatos)
                    #print(", ---- token coma")
            elif estado == 10:
                if dicDatos != {}:
                    RegistroSet.registros.get(espacioSelf).append(dicDatos)
                dicDatos = {}

                if entrada[i] == ")":
                    #print(") ---- token parentesis cerrado")
                    #print("inicio")
                    #print(RegistroSet.registros.get(espacioSelf))
                    #print("final")
                    aceptado = True
                elif entrada[i] == ",":
                    estado = 1
                    #RegistroSet.registros.get(espacioSelf).append(dicDatos)
                    #print(", ---- token coma")

    def useSet(self, nombreSet):
        RegistroSet.listaEnUso = []
        if RegistroSet.registros.get(nombreSet) != None:
            RegistroSet.listaEnUso = RegistroSet.registros.get(nombreSet)
            print(f"SET ---{nombreSet}--- EN USO!!!")
            print("//////////////////////////////////////////////////////////////////////////////////////////////////")
            #print("lista en uso")
            #print(RegistroSet.listaEnUso)
            #print("fin lista en uso")
        else:
            print(f"El SELF {nombreSet} no existe")
            print("//////////////////////////////////////////////////////////////////////////////////////////////////")

    def selectSimple(self, listaAtributos, atributoComp, valorAtribComp):
        temp = RegistroSet.listaEnUso
        if listaAtributos[0] == "*":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp:
                    print(registro)
                    print("//////////////////////////////////////////////////////////////////////////////////////////////////")

        else:
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp:
                    for atrib in listaAtributos:
                            print(f"{atrib} : {registro.get(atrib)}")
                    print("//////////////////////////////////////////////////////////////////////////////////////////////////")

    def selectAll(self, listaAtributos):
        temp = RegistroSet.listaEnUso
        if listaAtributos[0] == "*":
            for registro in temp:
                print(registro)
                print("///////////////////////////////////////////////////////////////////////")

    def selectExtend(self, listaAtributos, atributoComp, valorAtribComp, operacionExt, atribEx, operador, valorAtribEx):
        temp = RegistroSet.listaEnUso
        if operacionExt == "AND":
            #print("entro al and")
            if operador == "<":
                #print("entro al menor")
                if listaAtributos[0] == "*":
                    #print("entro al *")
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "and", "<")

                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "and",
                                            "<")
            elif operador == ">":
                if listaAtributos[0] == "*":
                    #print("entro al *")
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "and", ">")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "and",
                                            ">")

            elif operador == "<=":
                if listaAtributos[0] == "*":
                    #print("entro al *")
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "and", "<=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "and",
                                            "<=")
            elif operador == ">=":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "and", ">=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "and",
                                            ">=")
            elif operador == "=":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "and", "=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "and",
                                            "=")
            elif operador == "!=":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "and", "!=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "and",
                                            "!=")
        elif operacionExt == "OR":
            if operador == "<":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "or", "<")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "or",
                                            "<")
            elif operador == ">":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "or", ">")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "or",
                                            ">")
            elif operador == "<=":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "or", "<=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "or",
                                            "<=")
            elif operador == ">=":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "or", ">=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "or",
                                            ">=")
            elif operador == "=":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "or", "=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "or",
                                            "=")
            elif operador == "!=":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "or", "!=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "or",
                                            "!=")
        elif operacionExt == "XOR":
            if operador == "<":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor", "<")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor",
                                            "<")
            elif operador == ">":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor", ">")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor",
                                            ">")
            elif operador == "<=":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor", "<=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor",
                                            "<=")
            elif operador == ">=":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor", ">=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor",
                                            ">=")
            elif operador == "=":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor", "=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor",
                                            "=")
            elif operador == "!=":
                if listaAtributos[0] == "*":
                    self.selectAllExtend(atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor", "!=")
                else:
                    self.selectAtribsExtend(listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, "xor",
                                            "!=")

    def selectAllExtend(self, atributoComp, valorAtribComp, atribEx, valorAtribEx, condicional, operacion):
        temp = RegistroSet.listaEnUso
        if condicional == "and" and operacion == "<":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) < valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "and" and operacion == ">":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) > valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "and" and operacion == "<=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) <= valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "and" and operacion == ">=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) >= valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "and" and operacion == "=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) == valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "and" and operacion == "!=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) != valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == "<":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) < valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == ">":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) > valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == "<=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) <= valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == ">=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) >= valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == "=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) == valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == "!=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) != valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == "<":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) < valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == ">":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) > valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == "<=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) <= valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == ">=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) >= valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == "=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) == valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == "!=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) != valorAtribEx:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

    def selectAtribsExtend(self, listaAtributos, atributoComp, valorAtribComp, atribEx, valorAtribEx, condicional, operacion):
        temp = RegistroSet.listaEnUso
        if condicional == "and" and operacion == "<":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) < valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "and" and operacion == ">":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) > valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "and" and operacion == "<=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) <= valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "and" and operacion == ">=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) >= valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "and" and operacion == "=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) == valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "and" and operacion == "!=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp and registro.get(atribEx) != valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == "<":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) < valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == ">":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) > valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == "<=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) <= valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == ">=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) >= valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == "=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) == valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "or" and operacion == "!=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp or registro.get(atribEx) != valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == "<":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) < valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == ">":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) > valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == "<=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) <= valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == ">=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) >= valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == "=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) == valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

        elif condicional == "xor" and operacion == "!=":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp ^ registro.get(atribEx) != valorAtribEx:
                    for atrib in listaAtributos:
                        print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")


    def listAttributes(self):
        aux = RegistroSet.listaEnUso
        for item in aux:
            keys = item.keys()
            for key in keys:
                if type(item.get(key)) == int:
                    print(f"{key} -- int")
                elif type(item.get(key)) == str:
                    print(f"{key} -- string")
                elif type(item.get(key)) == float:
                    print(f"{key} -- float")
                elif type(item.get(key)) == bool:
                    print(f"{key} -- boolean")
            print("//////////////////////////////////////////////////////////////////////////////////////////////////")

    def addColor(self, color):
        if color == "RED":
            RegistroSet.color = "\u001b[31m"
            #RegistroSet.color = "\033[38:5:196m"
        elif color == "BLUE":
            RegistroSet.color = "\u001b[34m"
        elif color == "GREEN":
            RegistroSet.color = "\033[38:5:28m"
            #RegistroSet.color = "\u001b[32m"
        elif color == "YELLOW":
            RegistroSet.color = "\033[93m"
        elif color == "ORANGE":
            #RegistroSet.color = "\033[33m"
            RegistroSet.color = "\033[38:5:202m"
        elif color == "PINK":
            RegistroSet.color = "\033[38;5;201m"

    def max(self, atributo):
        temp = RegistroSet.listaEnUso
        listaElementosNum = []
        if temp[0].get(atributo) is not None and temp[1].get(atributo) is not None:
            for item in temp:
                if item.get(atributo) != "null" or item.get(atributo) != "NULL" or item.get(atributo) != "Null" or \
                        item.get(atributo) is not None:
                    if type(item.get(atributo)) == int or type(item.get(atributo)) == float:
                        listaElementosNum.append(item.get(atributo))
                    elif type(item.get(atributo)) == str:
                            listaElementosNum.append(item.get(atributo))
                    elif type(item.get(atributo)) == bool:
                        print("-----------------------No se le puede aplicar el maximo-----------------")
                        break
            if listaElementosNum != []:
                print(f"El valor maximo de {atributo} es: {max(listaElementosNum)}")

        else:
            print(f"El atributo {atributo} no existe.")
        print("//////////////////////////////////////////////////////////////////////////////////////////////////")

    def min(self, atributo):
        temp = RegistroSet.listaEnUso
        listaElementosNum = []
        if temp[0].get(atributo) is not None and temp[1].get(atributo) is not None:
            for item in temp:
                if item.get(atributo) != "null" or item.get(atributo) != "NULL" or item.get(atributo) != "Null" or \
                        item.get(atributo) is not None:
                    if type(item.get(atributo)) == int or type(item.get(atributo)) == float:
                        listaElementosNum.append(item.get(atributo))
                    elif type(item.get(atributo)) == str:
                        listaElementosNum.append(item.get(atributo))
                    elif type(item.get(atributo)) == bool:
                        print("-----------------------No se le puede aplicar el minimo-----------------")
                        break
            if listaElementosNum != []:
                print(f"El valor minimo de {atributo} es: {min(listaElementosNum)}")
        else:
            print(f"El atributo {atributo} no existe.")
        print("//////////////////////////////////////////////////////////////////////////////////////////////////")

    def sum(self, listaAtributos):
        temp = RegistroSet.listaEnUso
        listaSum = []
        if listaAtributos[0] == "*":
            atributos = temp[0].keys()
            for key in atributos:
                for item in temp:
                    if type(item.get(key)) == int or type(item.get(key)) == float:
                        listaSum.append(item.get(key))
                if listaSum != []:
                    print(f"La suma de {key} es: {sum(listaSum)}")
                    listaSum = []
        else:
            for atrib in listaAtributos:
                for item in temp:
                    if type(item.get(atrib)) == int or type(item.get(atrib)) == float:
                        listaSum.append(item.get(atrib))
                print(f"La suma de {atrib} es: {sum(listaSum)}")
        print("//////////////////////////////////////////////////////////////////////////////////////////////////")

    def count(self, listaAtributos):
        temp = RegistroSet.listaEnUso
        atributos = temp[0].keys()
        contador = 0
        if listaAtributos[0] == "*":
            for item in temp:
                contador = contador + 1
            print(f"Se cargaron {contador} registros.")
            contador = 0
            for atrib in atributos:
                for item in temp:
                    if item.get(atrib) is not None or item.get(atrib) != "Null" or item.get(atrib) != "NULL" or\
                            item.get(atrib) != "null":
                        contador = contador + 1
                    else:
                        print(f"{atrib} no existe")
                print(f"{atrib}: {contador}")
                contador = 0
        else:
            for atrib in listaAtributos:
                for item in temp:
                    if atrib in item:
                        if item.get(atrib) != "Null" or item.get(atrib) != "NULL" or item.get(atrib) != "null" or \
                                item.get(atrib) is not None:
                            contador = contador + 1
                    else:
                        print(f"{atrib} no existe")
                        contador = 0
                        break
                print(f"{atrib}: {contador} registros guardados")
                contador = 0
        print("//////////////////////////////////////////////////////////////////////////////////////////////////")
