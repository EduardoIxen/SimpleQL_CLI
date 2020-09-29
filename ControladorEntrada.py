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
            #print("lista en uso")
            #print(RegistroSet.listaEnUso)
            #print("fin lista en uso")
        else:
            print(f"El SELF {nombreSet} no existe")

    def selectSimple(self, listaAtributos, atributoComp, valorAtribComp):
        temp = RegistroSet.listaEnUso
        if listaAtributos[0] == "*":
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp:
                    print(registro)
                    print("///////////////////////////////////////////////////////////////////////")

        else:
            for registro in temp:
                if registro.get(atributoComp) == valorAtribComp:
                    for atrib in listaAtributos:
                            print(f"{atrib} : {registro.get(atrib)}")
                    print("///////////////////////////////////////////////////////////////////////")

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