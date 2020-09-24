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
while True:
    opcion = input("Ingrese el comando\n")
    estado = 0
    palabraReservada = ""
    palabraSegundoNivel = ""
    palabraTercerNivel = ""
    for i in range(len(opcion)):
        if estado == 0:
            if opcion[i].isalpha() or opcion[i] == " ":
                palabraReservada = palabraReservada + opcion[i]
                if palabraReservada.upper() == "CREATE":
                    estado = 1
                elif palabraReservada == "LOAD":
                    print("LOAD")
                    estado = 2
                elif palabraReservada == "USE":
                    print("USE")
                    estado = 1
                elif palabraReservada == "SELECT":
                    print("SELECT")
                    estado = 1
                elif palabraReservada == "SELECCIONAR":
                    print("SELECCIONAR")
                    estado = 1
                elif palabraReservada == "LIST":
                    print("LIST")
                    estado = 1
                elif palabraReservada == "PRINT":
                    print("PRINT")
                    estado = 1
                elif palabraReservada == "MAX":
                    print("MAX")
                    estado = 1
                elif palabraReservada == "MIN":
                    print("MIN")
                    estado = 1
                elif palabraReservada == "SUM":
                    print("SUM")
                    estado = 1
                elif palabraReservada == "COUNT":
                    print("COUNT")
                    estado = 1
                elif palabraReservada == "REPORT":
                    print("REPORT")
                    estado = 1
                elif palabraReservada == "SCRIPT":
                    print("SCRIPT")
                    estado = 1
        elif estado == 1:
            if opcion[i].isalpha():
                palabraSegundoNivel = palabraSegundoNivel + opcion[i]
                if palabraSegundoNivel.upper() == "SET":
                    estado = 14
        elif estado == 14:
            if i <= len(opcion):
                if opcion[i].isalpha() or opcion[i].isdigit():
                    palabraTercerNivel = palabraTercerNivel + opcion[i]
                    if i == len(opcion) - 1:
                        print(palabraReservada + " " + palabraSegundoNivel + " " + palabraTercerNivel)
                        create = ControladorEntrada()
                        create.createSet(palabraTercerNivel)
                        items = RegistroSet.registros.items()
                        print(items)
