import os.path as path

class CargarArchivo:
    def cargarArchivo(self, nombreArchivo):
        if path.exists(f'entradas/{nombreArchivo}'):
            fichero = open(f'entradas/{nombreArchivo}', 'r')
            contenido = fichero.readlines()
            fichero.close()
            print(f"Archivo ---{nombreArchivo}--- cargado correctamente")
            print("//////////////////////////////////////////////////////////////////////////////////////////////////")
            print()
            return contenido
        else:
            print(f"El archivo ---{nombreArchivo}--- no existe.")
            print("//////////////////////////////////////////////////////////////////////////////////////////////////")
            print()
            return None
