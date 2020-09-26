from CargarArchivo import *
from RegistroSet import *
class ControladorEntrada:
    def createSet(self, nombreSet):
        RegistroSet.registros[nombreSet] = []

    def loadInto(self, espacioSelf, listaArchivo):
        print(espacioSelf)
        cargar = CargarArchivo()
        for archivo in listaArchivo:
            contenido = cargar.cargarArchivo(archivo)
            if contenido != None:
                print(contenido)
                convStr = "".join(contenido)
                self.readAon(convStr, espacioSelf)

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
                    print("inicio")
                    print(RegistroSet.registros.get(espacioSelf))
                    print("final")
                elif entrada[i] == ",":
                    estado = 1
                    #RegistroSet.registros.get(espacioSelf).append(dicDatos)
                    #print(", ---- token coma")