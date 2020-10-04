# SimpleQL_CLI
# Manual de usuario
## Requerimientos
- Tener instalado python en su versión 3
- PyCharm

Para usar SimpleQL primero deberá clonar el repositorio en su computadora para eso deberá abrir su consola en la dirección donde quiera almacenar el repositorio y digitar el siguiente comando.

```sh
git clone https://github.com/EduardoIxen/SimpleQL_CLI.git
```
Después de haber ejecutado el comando, los archivos aparecerán en la dirección seleccionada.
![clone](https://user-images.githubusercontent.com/18478169/95010134-341e1080-05e4-11eb-8829-b7dc70577af8.png)

## Ejecutar el programa

Una vez clonado el repositorio se procede a cargarlo en pycharm donde se seleccionara el archivo principal que en este caso es el **main.py** y presionando click izquierdo sobre el archivo, se mostrará una lista donde se seleccionará **Run 'main'** para ejecutarlo.
Del lado derecho de la imagen se observa que el programa ya se está ejecutando en la consola de Pycharm.

![ejecutar](https://user-images.githubusercontent.com/18478169/95025422-e25aa200-0646-11eb-8893-52d60985092a.png)

Para utilizar el programa necesitaremos de dos tipos de archivos, los que tengan la extencion **.aon** y **.siql**.
Los archivos .aon contendran los datos sobre los cuales se haran las consultas para facilitar la busqueda de ciertos elementos y tendran la siguiente estructura:
```sh
(
    <
        [Atributo3] = 12.3,
        [Atributo2] = True,
        [Atributo1] = "Cadena ejemplo"
    >,
    <
        [Atributo1] = 4,
        [Atributo2] = False,
        [Atributo3] = "Ejemplo 2"
    >
)
```

| Signo | Descripcion |
| --------- | --------- |
| ( | Indica el inicio de una coleccion de datos |
| < | Indica el inicio de un registro dentr de la coleccion |
| [ ] | Delimitan el nombre de un atributo del registro |
| , | Indica que sigue otro registro o atributo|
| = | Asigna un valor al registro|
|valo del registro| El valor del registro puede ser numerico, decimal, booleano o una cadena de texto (que se delimitara con " ") |
| > | Indica el final de un registro |
| ) | Indica el final de una coleccion de datos |

El segundo tipo de archivo es el .siql que tiene la siguiente estructura:

```sh
comando ;
comando2 ;
...
```
| Lexema | Descripcion |
| -------| ----------- |
|comando | Puede ser cualquier comando que acepte el programa, en la funcionalidad se explicará cada uno de ellos |
| ; | Indica el final de un comando para continuar con el siguiente |

## Funcionalidad
- **CREATE SET id:** Este comando permite crear un espacio de memoria sobre el cual podremos cargar datos, el id puede ser un nombre o código.
```sh
CREATE SET prueba
```
![createSet](https://user-images.githubusercontent.com/18478169/95026460-c2c77780-064e-11eb-8878-b3cde4579623.png)

- **LOAD INTO < idSet > FILES < archivo o archivos > :** Este comando permite cargar archivos .aon dentro de un espacio de memoria creado previamente, los archivos deben estar en la carpeta **entradas** del proyecto y para cargar mas de un archivo debe estar separado por una **,**.
```sh
LOAD INTO prueba FILES ejemplo.aon, ejemplo2.aon
```
- **USE SET < idSet >:** Define el set de datos para los siguientes comandos.
```sh
USE SET prueba
```
- **SELECT atributo1, atributo2, ... WHERE < condicion >:** Permite seleccionar uno o mas registros con base a la condicion ingresada, la condicion consiste de operaciones que se le pueden aplicar a cierto atributo y puede ser: 

| Signo | Descripcion |
| ----- | ----------- |
| < | Menor que |
| > | Mayor que |
| <= | Menor o igual|
| >= | Mayor o igual|
|= | Igual |
|!= | Diferente |

```sh
SELECT nombre, edad WHERE edad < 100
```
Otra funcionalidad del comando SELECT es la ampliacion de la condiciones mediante los siguientes operadores logicos:
| Operador | Descripcion |
| -------- | ----------- |
| AND | Las dos condiciones deben cumplirse |
| OR | Una o las dos condiciones pueden cumplirse |
| XOR | Solo una condicion puede cumplirse |

A la ampliacion consiste en aplicarle las mismar operaciones mencionadas anteriormente a otro atributo y operarlos con los operadores lógicos.

```sh
SELECT nombre, edad WHERE nombre = "Tomas" AND edad = 31
```
- **LIST ATTRIBUTES:** Este comando permite listar los atributos de los registros cargados a memoria mediante los archivos .aon.
```sh
LIST ATTRIBUTES
```
- **PRINT IN < color >:** Permite mostrar la salida en consola del color que se le pase como parametro:
| Parametro | Color |
| --------- | ----- |
| BLUE | Azul |
| RED | Rojo |
| GREEN | Verde |
| YELLOW | Amarillo |
| ORANGE | Anaranjado |
| PINK | Rosado |

- **MAX < atributo >:** Permite seleccionar el valor máximo del atributo que se le pase como parametro.
```sh
MAX edad
```
- **MIN < atributo >:** Permite seleccionar el valor mínimo del atributo que se le pase como parametro.
```sh
MIN edad
```
- **SUM < atributo >:** Permite sumar todos los todos los atributos que se le pasen como parametro contenidos dentro del set de datos, solo aplica para atributos numericos.
```sh
SUM edad
```
- **COUNT < atributo >, < atributo2 > ... < atributoN >:** Permite contar el numero de registros o atributos cargados a memoria. Se le puede pasar varios atributos.
```sh
COUNT nombre, edad
```
- **REPORT TO < id > < comando >:** Permite generar un reporte en html con el resultado de cualquier comando mencionado anteriormente, el id que solicita como parametro es para indicarle el nombre que se le colocara al archivo.
```sh
REPORT TO reporte1 SELECT * WHERE nombre = "Tomas"
REPORT TO reporte2 SELECT nombre, edad WHERE edad = 31 AND nombre != "Pedro"
REPORT TO reporte3 LIST ATTRIBUTES
```
- **SCRIPT < archivo.siql >, ... < archivoN.siql >:** Este comando permite cargar scripts con extensión .siql que contienen series de
instrucciones y comandos SimpleQL. Los scripts deben de estar en la carpeta **scriptSIQL** del proyecto. Si desea cargar mas de un script, el nombre debe de ir separado por **,**.
```sh
SCRIPT entrada1.siql, entrada2.siql
```
- **REPORT TOKENS**: Este comando crea un reporte en html que muestra una lista de todos los lexemas encontrados por el AFD.
```SH
REPORT TOKENS
```
