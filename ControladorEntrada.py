from CargarArchivo import *
from RegistroSet import *
from Reporte import *
import os.path

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
            print()
            #print("lista en uso")
            #print(RegistroSet.listaEnUso)
            #print("fin lista en uso")
        else:
            print(f"El SELF {nombreSet} no existe")
            print("//////////////////////////////////////////////////////////////////////////////////////////////////")
            print()

    def selectSimple(self, listaAtributos, atributoComp, operacion,valorAtribComp):
        listaReporte = []
        dicReporte = {}
        print("##########################################SELECT SIMPLE###########################################")
        temp = RegistroSet.listaEnUso
        if operacion == "=":
            if listaAtributos[0] == "*":
                for registro in temp:
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) == valorAtribComp:
                            if RegistroSet.reporte == False:
                                print(registro)
                            listaReporte.append(registro)
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                    else:
                        print("No existe el atributo")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

            else:
                for registro in temp:
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) == valorAtribComp:
                            for atrib in listaAtributos:
                                if RegistroSet.reporte == False:
                                    print(f"{atrib} : {registro.get(atrib)}")
                                dicReporte[atrib] = registro.get(atrib)
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                            listaReporte.append(dicReporte)
                            dicReporte = {}
                    else:
                        print("No existe el atributo")

                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

        elif operacion == "!=":
            if listaAtributos[0] == "*":
                for registro in temp:
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) != valorAtribComp:
                            if RegistroSet.reporte == False:
                                print(registro)
                            listaReporte.append(registro)
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                    else:
                        print("No existe el atributo")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

            else:
                for registro in temp:
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) != valorAtribComp:
                            for atrib in listaAtributos:
                                if RegistroSet.reporte == False:
                                    print(f"{atrib} : {registro.get(atrib)}")
                                dicReporte[atrib] = registro.get(atrib)
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                            listaReporte.append(dicReporte)
                            dicReporte = {}
                    else:
                        print("No exixte el atributo")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

        elif operacion == "<":
            if listaAtributos[0] == "*":
                for registro in temp:
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) < valorAtribComp:
                            if RegistroSet.reporte == False:
                                print(registro)
                            listaReporte.append(registro)
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                    else:
                        print("No exixte el atributo")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

            else:
                for registro in temp:
                    #print(registro.get(atributoComp), type(registro.get(atributoComp)))
                    #print(valorAtribComp, type(registro.get(atributoComp)))
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) < valorAtribComp:
                            for atrib in listaAtributos:
                                if RegistroSet.reporte == False:
                                    print(f"{atrib} : {registro.get(atrib)}")
                                dicReporte[atrib] = registro.get(atrib)
                            print(
                                    "//////////////////////////////////////////////////////////////////////////////////////////////////")
                            listaReporte.append(dicReporte)
                            dicReporte = {}
                    else:
                        print("No existe el atributo")
                    if RegistroSet.reporte == True:
                        reporte = Reporte()
                        reporte.crearHtml(listaReporte)

        elif operacion == "<=":
            if listaAtributos[0] == "*":
                for registro in temp:
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) <= valorAtribComp:
                            if RegistroSet.reporte == False:
                                print(registro)
                            listaReporte.append(registro)
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                    else:
                        print("No existe el atributo")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

            else:
                for registro in temp:
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) <= valorAtribComp:
                            for atrib in listaAtributos:
                                if RegistroSet.reporte == False:
                                    print(f"{atrib} : {registro.get(atrib)}")
                                dicReporte[atrib] = registro.get(atrib)
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                            listaReporte.append(dicReporte)
                            dicReporte = {}
                    else:
                        print("No exixte el atributo")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

        elif operacion == ">":
            if listaAtributos[0] == "*":
                for registro in temp:
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) > valorAtribComp:
                            if RegistroSet.reporte == False:
                                print(registro)
                            listaReporte.append(registro)
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                    else:
                        print("No exixte el atributo")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

            else:
                for registro in temp:
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) > valorAtribComp:
                            for atrib in listaAtributos:
                                if RegistroSet.reporte == False:
                                    print(f"{atrib} : {registro.get(atrib)}")
                                dicReporte[atrib] = registro.get(atrib)
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                            listaReporte.append(dicReporte)
                            dicReporte = {}
                    else:
                        print("No exixte el atributo")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

        elif operacion == ">=":
            if listaAtributos[0] == "*":
                for registro in temp:
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) >= valorAtribComp:
                            if RegistroSet.reporte == False:
                                print(registro)
                            listaReporte.append(registro)
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                    else:
                        print("No existe el atributo")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

            else:
                for registro in temp:
                    if registro.get(atributoComp) != None:
                        if registro.get(atributoComp) >= valorAtribComp:
                            for atrib in listaAtributos:
                                if RegistroSet.reporte == False:
                                    print(f"{atrib} : {registro.get(atrib)}")
                                dicReporte[atrib] = registro.get(atrib)
                            print(
                                "//////////////////////////////////////////////////////////////////////////////////////////////////")
                            listaReporte.append(dicReporte)
                            dicReporte = {}
                    else:
                        print("No existe el atributo")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)
        print("\n")

    def selectAll(self, listaAtributos):
        listaReporte = []
        print("##########################################SELECT ALL###########################################")
        temp = RegistroSet.listaEnUso
        if listaAtributos[0] == "*":
            for registro in temp:
                if RegistroSet.reporte == False:
                    print(registro)
                listaReporte.append(registro)
                print(
                    "//////////////////////////////////////////////////////////////////////////////////////////////////")
            if RegistroSet.reporte == True:
                reporte = Reporte()
                reporte.crearHtml(listaReporte)
        print()

    def selectExtend(self, listaAtributos, atributoComp, primeraOperacion, valorAtribComp, operacionExt, atribEx, operador, valorAtribEx):
        listaReporte = []
        dicReporte = {}
        contador = 0
        print("##########################################SELECT EXTEND###########################################")
        self.firstComp(atributoComp, primeraOperacion, valorAtribComp)
        self.secondComp(atribEx, operador, valorAtribEx)
        temp = RegistroSet.firtsComp
        temp2 = RegistroSet.secondComp
        #print("temp1",temp)
        #print("temp2",temp2)
        if operacionExt == "AND":
            if listaAtributos[0] == "*":
                for item in temp:
                    if item in temp2:
                        if RegistroSet.reporte == False:
                            print(item)
                        listaReporte.append(item)
                RegistroSet.firtsComp = []
                RegistroSet.secondComp = []
                print(
                    "//////////////////////////////////////////////////////////////////////////////////////////////////")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)
            else:
                for registro in temp:
                    if registro in temp2:
                        for atrib in listaAtributos:
                            if RegistroSet.reporte == False:
                                print(f"{atrib}: {registro.get(atrib)}")
                            dicReporte[atrib] = registro.get(atrib)
                        print(
                            "//////////////////////////////////////////////////////////////////////////////////////////////////")
                        listaReporte.append(dicReporte)
                        dicReporte = {}
                RegistroSet.firtsComp = []
                RegistroSet.secondComp = []
                print(
                    "//////////////////////////////////////////////////////////////////////////////////////////////////")
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

        elif operacionExt == "OR":
            resultado = []
            sumaLista = []
            if listaAtributos[0] == "*":
                for item in temp:
                    if item not in temp2:
                        temp2.append(item)

                for item in temp2:
                    if RegistroSet.reporte == False:
                        print(item)
                    listaReporte.append(item)
                    print(
                    "//////////////////////////////////////////////////////////////////////////////////////////////////")
                RegistroSet.firtsComp = []
                RegistroSet.secondComp = []
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)
            else:
                for item in temp:
                    if item not in temp2:
                        temp2.append(item)

                for item in temp2:
                    for atrib in listaAtributos:
                        if RegistroSet.reporte == False:
                            print(f"{atrib}: {item.get(atrib)}")
                        dicReporte[atrib] = item.get(atrib)
                    print(
                    "//////////////////////////////////////////////////////////////////////////////////////////////////")
                    listaReporte.append(dicReporte)
                    dicReporte = {}

                RegistroSet.firtsComp = []
                RegistroSet.secondComp = []
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)

        elif operacionExt == "XOR":
            resultado = []
            if listaAtributos[0] == "*":
                for item in temp:
                    if item not in temp2:
                        resultado.append(item)
                for item2 in temp2:
                    if item2 not in temp:
                        resultado.append(item2)
                for reg in resultado:
                    if RegistroSet.reporte == False:
                        print(reg)
                    listaReporte.append(reg)
                    print(
                        "//////////////////////////////////////////////////////////////////////////////////////////////////")
                RegistroSet.firtsComp = []
                RegistroSet.secondComp = []
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)
            else:
                for item in temp:
                    if item not in temp2:
                        resultado.append(item)
                for item2 in temp2:
                    if item2 not in temp:
                        resultado.append(item2)
                for reg in resultado:
                    for atrib in listaAtributos:
                        if RegistroSet.reporte == False:
                            print(f"{atrib}: {reg.get(atrib)}")
                        dicReporte[atrib] = reg.get(atrib)
                    print(
                        "//////////////////////////////////////////////////////////////////////////////////////////////////")
                    listaReporte.append(dicReporte)
                    dicReporte = {}
                RegistroSet.firtsComp = []
                RegistroSet.secondComp = []
                if RegistroSet.reporte == True:
                    reporte = Reporte()
                    reporte.crearHtml(listaReporte)
        print("\n")

    def firstComp(self, atributoComp, primeraOperacion, valorAtributoComp):
        temp = RegistroSet.listaEnUso
        if primeraOperacion == "=":
            for registro in temp:
                if registro.get(atributoComp) != None:
                    if registro.get(atributoComp) == valorAtributoComp:
                        RegistroSet.firtsComp.append(registro)
                        #print(f"firstComp--->{RegistroSet.firtsComp}")
                else:
                    print("No exixte el atributo")
        elif primeraOperacion == "<":
            for registro in temp:
                if registro.get(atributoComp) != None:
                    if registro.get(atributoComp) < valorAtributoComp:
                        RegistroSet.firtsComp.append(registro)
                        #print(f"firstComp--->{RegistroSet.firtsComp}")
                else:
                    print("No exixte el atributo")
        elif primeraOperacion == ">":
            for registro in temp:
                if registro.get(atributoComp) != None:
                    if registro.get(atributoComp) > valorAtributoComp:
                        RegistroSet.firtsComp.append(registro)
                        #print(f"firstComp--->{RegistroSet.firtsComp}")
                else:
                    print("No existe el atributo")
        elif primeraOperacion == "<=":
            for registro in temp:
                if registro.get(atributoComp) != None:
                    if registro.get(atributoComp) <= valorAtributoComp:
                        RegistroSet.firtsComp.append(registro)
                        #print(f"firstComp--->{RegistroSet.firtsComp}")
                else:
                    print("No exixte el atributo")
        elif primeraOperacion == ">=":
            for registro in temp:
                if registro.get(atributoComp) != None:
                    if registro.get(atributoComp) >= valorAtributoComp:
                        RegistroSet.firtsComp.append(registro)
                        #print(f"firstComp--->{RegistroSet.firtsComp}")
                else:
                    print("No exixte el atributo")
        elif primeraOperacion == "!=":
            for registro in temp:
                if registro.get(atributoComp) != None:
                    if registro.get(atributoComp) != valorAtributoComp:
                        RegistroSet.firtsComp.append(registro)
                        #print(f"firstComp--->{RegistroSet.firtsComp}")
                else:
                    print("No exixte el atributo")

    def secondComp(self, atribEx, operador, valorAtribEx):
        temp = RegistroSet.listaEnUso
        if operador == "=":
            for registro in temp:
                if registro.get(atribEx) != None:
                    if registro.get(atribEx) == valorAtribEx:
                        RegistroSet.secondComp.append(registro)
                        #print("Second Comp", RegistroSet.secondComp)
                else:
                    print("No exixte el atributo")

        elif operador == "<":
            for registro in temp:
                if registro.get(atribEx) != None:
                    if registro.get(atribEx) < valorAtribEx:
                        RegistroSet.secondComp.append(registro)
                        #print("Second Comp", RegistroSet.secondComp)
                else:
                    print("No exixte el atributo")
        elif operador == ">":
            for registro in temp:
                if registro.get(atribEx) != None:
                    if registro.get(atribEx) > valorAtribEx:
                        RegistroSet.secondComp.append(registro)
                        #print("Second Comp", RegistroSet.secondComp)
                else:
                    print("No exixte el atributo")
        elif operador == "<=":
            for registro in temp:
                if registro.get(atribEx) != None:
                    if registro.get(atribEx) <= valorAtribEx:
                        RegistroSet.secondComp.append(registro)
                        #print("Second Comp", RegistroSet.secondComp)
                else:
                    print("No exixte el atributo")
        elif operador == ">=":
            for registro in temp:
                if registro.get(atribEx) != None:
                    if registro.get(atribEx) >= valorAtribEx:
                        RegistroSet.secondComp.append(registro)
                        #print("Second Comp", RegistroSet.secondComp)
                else:
                    print("No exixte el atributo")
        elif operador == "!=":
            for registro in temp:
                if registro.get(atribEx) != None:
                    if registro.get(atribEx) != valorAtribEx:
                        RegistroSet.secondComp.append(registro)
                        #print("Second Comp", RegistroSet.secondComp)
                else:
                    print("No exixte el atributo")

    def listAttributes(self):
        listaReporte = []
        dicReporte = {}
        print("##########################################LIST ATTRIBUTES###########################################")
        aux = RegistroSet.listaEnUso
        for item in aux:
            keys = item.keys()
            for key in keys:
                if type(item.get(key)) == int:
                    if RegistroSet.reporte == False:
                        print(f"{key} -- int")
                    dicReporte["Nombre Atribuo"] = str(key)
                    dicReporte["Tipo"] = "int"
                    listaReporte.append(dicReporte)
                    dicReporte = {}
                elif type(item.get(key)) == str:
                    if RegistroSet.reporte == False:
                        print(f"{key} -- string")
                    dicReporte["Nombre Atribuo"] = str(key)
                    dicReporte["Tipo"] = "String"
                    listaReporte.append(dicReporte)
                    dicReporte = {}
                elif type(item.get(key)) == float:
                    if RegistroSet.reporte == False:
                        print(f"{key} -- float")
                    dicReporte["Nombre Atribuo"] = str(key)
                    dicReporte["Tipo"] = "float"
                    listaReporte.append(dicReporte)
                    dicReporte = {}
                elif type(item.get(key)) == bool:
                    if RegistroSet.reporte == False:
                        print(f"{key} -- boolean")
                    dicReporte["Nombre Atribuo"] = str(key)
                    dicReporte["Tipo"] = "bool"
                    listaReporte.append(dicReporte)
                    dicReporte = {}
            dicReporte["Nombre Atribuo"] = " "
            dicReporte["Tipo"] = " "
            listaReporte.append(dicReporte)
            dicReporte = {}
            print("//////////////////////////////////////////////////////////////////////////////////////////////////")
        if RegistroSet.reporte == True:
            reporte = Reporte()
            reporte.crearHtml(listaReporte)
        print("\n")

    def addColor(self, color):
        print("##########################################ADD COLOR###########################################")
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
        listaReporte = []
        dicReporte = {}
        print("##########################################MAXIMO###########################################")
        temp = RegistroSet.listaEnUso
        listaElementosNum = []
        if temp[0].get(atributo) is not None and temp[1].get(atributo) is not None:
            for item in temp:
                if item.get(atributo) != "null" or item.get(atributo) != "NULL" or item.get(atributo) != "Null" or \
                        item.get(atributo) is not None:
                    if type(item.get(atributo)) == int or type(item.get(atributo)) == float:
                        listaElementosNum.append(item.get(atributo))
                        dicReporte[atributo] = atributo
                        dicReporte["Valor"] = item.get(atributo)
                        listaReporte.append(dicReporte)
                        dicReporte = {}
                    elif type(item.get(atributo)) == str:
                            listaElementosNum.append(item.get(atributo))
                            dicReporte[atributo] = atributo
                            dicReporte["Valor"] = item.get(atributo)
                            listaReporte.append(dicReporte)
                            dicReporte = {}
                    elif type(item.get(atributo)) == bool:
                        print("-----------------------No se le puede aplicar el maximo-----------------")
                        break
            if listaElementosNum != []:
                if RegistroSet.reporte == False:
                    print(f"El valor maximo de {atributo} es: {max(listaElementosNum)}")
                dicReporte[atributo] = f"EL VALOR MAXIMO DE {atributo} ES"
                dicReporte["Valor"] = max(listaElementosNum)
                listaReporte.append(dicReporte)
                dicReporte = {}
            if RegistroSet.reporte == True:
                reporte = Reporte()
                reporte.crearHtml(listaReporte)

        else:
            print(f"El atributo {atributo} no existe.")
        print("//////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\n")

    def min(self, atributo):
        listaReporte = []
        dicReporte = {}
        print("########################################## MINIMO ###########################################")
        temp = RegistroSet.listaEnUso
        listaElementosNum = []
        if temp[0].get(atributo) is not None and temp[1].get(atributo) is not None:
            for item in temp:
                if item.get(atributo) != "null" or item.get(atributo) != "NULL" or item.get(atributo) != "Null" or \
                        item.get(atributo) is not None:
                    if type(item.get(atributo)) == int or type(item.get(atributo)) == float:
                        listaElementosNum.append(item.get(atributo))
                        dicReporte[atributo] = atributo
                        dicReporte["Valor"] = item.get(atributo)
                        listaReporte.append(dicReporte)
                        dicReporte = {}
                    elif type(item.get(atributo)) == str:
                        listaElementosNum.append(item.get(atributo))
                        dicReporte[atributo] = atributo
                        dicReporte["Valor"] = item.get(atributo)
                        listaReporte.append(dicReporte)
                        dicReporte = {}
                    elif type(item.get(atributo)) == bool:
                        print("-----------------------No se le puede aplicar el minimo-----------------")
                        break
            if listaElementosNum != []:
                if RegistroSet.reporte == False:
                    print(f"El valor minimo de {atributo} es: {min(listaElementosNum)}")
                dicReporte[atributo] = f"EL VALOR MINIMO DE {atributo} ES"
                dicReporte["Valor"] = min(listaElementosNum)
                listaReporte.append(dicReporte)
                dicReporte = {}
            if RegistroSet.reporte == True:
                reporte = Reporte()
                reporte.crearHtml(listaReporte)
        else:
            print(f"El atributo {atributo} no existe.")
        print("//////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\n")

    def sum(self, listaAtributos):
        listaReporte = []
        dicReporte = {}
        print("########################################## SUMA ###########################################")
        temp = RegistroSet.listaEnUso
        listaSum = []
        if listaAtributos[0] == "*":
            atributos = temp[0].keys()
            for key in atributos:
                for item in temp:
                    if type(item.get(key)) == int or type(item.get(key)) == float:
                        listaSum.append(item.get(key))
                if listaSum != []:
                    if RegistroSet.reporte == False:
                        print(f"La suma de {key} es: {sum(listaSum)}")
                    sumRepo = sum(listaSum)
                    listaSum = []
                    dicReporte["Atributo"] = f"La suma de {key} es"
                    dicReporte["Valor"] = sumRepo
                    listaReporte.append(dicReporte)
                    dicReporte = {}
            if RegistroSet.reporte == True:
                reporte = Reporte()
                reporte.crearHtml(listaReporte)
                listaReporte = []
        else:
            for atrib in listaAtributos:
                for item in temp:
                    if type(item.get(atrib)) == int or type(item.get(atrib)) == float:
                        listaSum.append(item.get(atrib))
                if RegistroSet.reporte == False:
                    print(f"La suma de {atrib} es: {sum(listaSum)}")
                sumRepo = sum(listaSum)
                listaSum = []
                dicReporte["Atributo"] = f"La suma de {atrib} es"
                dicReporte["Valor"] = sumRepo
                listaReporte.append(dicReporte)
                dicReporte = {}
            if RegistroSet.reporte == True:
                reporte = Reporte()
                reporte.crearHtml(listaReporte)
        print("//////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\n")

    def count(self, listaAtributos):
        listaReporte = []
        dicReporte = {}
        print("########################################## COUNT ###########################################")
        temp = RegistroSet.listaEnUso
        atributos = temp[0].keys()
        contador = 0
        if listaAtributos[0] == "*":
            for item in temp:
                contador = contador + 1
            if RegistroSet.reporte == False:
                print(f"Se cargaron {contador} registros.")
            contador = 0
            for atrib in atributos:
                for item in temp:
                    if item.get(atrib) is not None or item.get(atrib) != "Null" or item.get(atrib) != "NULL" or\
                            item.get(atrib) != "null":
                        contador = contador + 1
                    else:
                        print(f"{atrib} no existe")
                if RegistroSet.reporte == False:
                    print(f"{atrib}: {contador}")
                dicReporte["Atributo"] = atrib
                dicReporte["Registros"] = contador
                listaReporte.append(dicReporte)
                dicReporte = {}
                contador = 0
            if RegistroSet.reporte == True:
                reporte = Reporte()
                reporte.crearHtml(listaReporte)
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
                if RegistroSet.reporte == False:
                    print(f"{atrib}: {contador} registros guardados")
                dicReporte["Atributo"] = atrib
                dicReporte["Registros"] = contador
                listaReporte.append(dicReporte)
                dicReporte = {}
                contador = 0
            if RegistroSet.reporte == True:
                reporte = Reporte()
                reporte.crearHtml(listaReporte)
        print("//////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\n")

    def loadScript(self, listaDirecciones):
        carga = CargarArchivo()
        for item in listaDirecciones:
            carga.cargarScript(item)

    def reporteToken(self):
        repo = Reporte()
        repo.crearHtml(RegistroSet.listaTokens)