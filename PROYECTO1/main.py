# This proyect was programmed by Christa Itzel Martinez Barrios & Lorena Ruelas Gaytan

import os
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

# Importa las matrices de los crucigramas
from matrices_crucigramas import matriz_animales, matriz_pantalla_animales, matriz_comida, matriz_pantalla_comida, matriz_marvel, matriz_pantalla_marvel, matriz_paises, matriz_pantalla_paises
matriz_a_mostrar = {1:[matriz_animales,matriz_pantalla_animales],2:[matriz_comida,matriz_pantalla_comida],
                        3:[matriz_marvel,matriz_pantalla_marvel],4:[matriz_paises, matriz_pantalla_paises]}

puntaje_jugador = 0
lista_usuario = []
lista_puntaje = []

#Estructurar y organizar el proyecto

#Funciones###############################################################################################################

def compruebaNombreDeUsario():
    #Se necesita resolver el problema de que pide 2 veces el nombre de usuario, YA ESTÁ
    while True:
        nom_usuario=input("\nIngrese su nombre(min. 3 caracteres):") 
        if (len(nom_usuario)) >=3:
          break
        print("Error")
    #Return nombre de usuario
    return nom_usuario
    

def validarOpciones(opciones,opcionseleccionada):
    # Valida si la opción seleccionada está en la lista correspondiente
    return opcionseleccionada in opciones

def mostrarSelecciónDeMenu2(opcion): #Menu 2: Menu de instrucciones y preguntas frecuentes
    if opcion==1:
        print("\n ¿Cómo jugar?")
        texto=leerTexto("Instrucciones.txt")
        print(texto)
    elif opcion == 2:
        print("\nPreguntas frecuentes:")
        print("""P1.¿Cómo sé que la palabra escrita es la correcta?
                        Se sustituye la palabra en el lugar en el crucigrama, de lo
                        contrario se seguirá pidiendo la palabra """) #extraer a un archivo aparte
    

def leerTexto(nombre_archivo):
    m_archivo=open(nombre_archivo,"r",encoding="utf-8")
    texto=m_archivo.read()
    #Cerrar archivo (para que no ocupe "espacio") 
    m_archivo.close() 
    return texto

def mostrarCrucigramaCapturarRespuesta(opcion): #
    global matriz_a_mostrar
    # Indica que matriz será la que se muestra dependiendo de la opción que se selccionó
    matriz_pantalla_mostrar = matriz_a_mostrar[opcion][1]
    print ("\nCompleta el crucigrama: \n")

    # Imprime la matriz en bonito
    ImprimirMatriz(matriz_pantalla_mostrar)
    return matriz_pantalla_mostrar

def ImprimirMatriz(matriz_pantalla_mostrar):
    for row in matriz_pantalla_mostrar:
        for item in row:
            print ("{:5}".format(item),end="")
        print()

def mostrarmenuycapturaropcion (menu,opciones):
    print(menu)
    opc = input()
    # Validar que sea entero
    if opc.isdigit():
        opc = int(opc)
    # Validar opción
    if (validarOpciones(opciones,opc)):
        return True,opc
    else:
        return False,opc


def MostrarDefiniciones(opcion,nom_usuario):
    # = nombre del archivo - dsp hago el bloc de notas para cada crucigrama con sus definiciones
    # Entre corchetes va el nombre del archivo
    # Se mete a la llave que corresponde  ala opción seleccionada
    dic_definiciones = {1:["animales_def.txt"],2:["comida_def.txt"],3:["marvel_def.txt"],4:["paises_def.txt"]}
    archivo_def = dic_definiciones[opcion][0]
    m_archivo=open(archivo_def,"r",encoding="utf-8")
    texto = m_archivo.read()
    print()
    print (texto)
    m_archivo.close()

    #Seleccionar definición
    posibles_def_selec = [1,2,3,4,9]
    def_selec = input("\nIndique la definición que guste: \n")
    if def_selec=="9":
        finalDeCrucigrama(nom_usuario,puntaje_jugador)
        sys.exit()
    #Validación de definición seleccionada (def_selec)
    valid = def_selec.isdigit()
    while valid == False and def_selec not in posibles_def_selec:
        def_selec = input("\nIndique la definición que guste:\n ")
        valid = def_selec.isdigit()
    # a.close() - no sé si en algún punto tengamos que cerrar los archivos
    return def_selec



def InteraccionCrucigrama(opcion, matriz_pantalla, nom_usuario): # en los parámetros le vamos a pasar la config del crucigrama selecionado & la matriz y matriz_pantalla de acuerdo al crucigrama
    # Usar variables globales
    global matriz_a_mostrar
    global puntaje_jugador
    matriz_original = matriz_a_mostrar[opcion][0]
    # Lista de la configuración de las palabras de los crucigramas (llave = def_selec)(llave indica la definición seleccionada)
    # Crucigrma Animales - 1 / Crucigrama Comida - 0 / Crucigrama Marvel - 2 / Crucigrama Países - 3
    lista_config = [{1:["perro","horizontal",0,2], 2:["pescado","vertical",0,2], 3:["vaca","horizontal",3,0], 4:["oveja","vertical",2,0]},
                    {1:["pasta","horizontal",0,0], 2:["pastel","vertical",0,0], 3:["salmon","vertical",0,2], 4:["tamales","horizontal",3,0]},
                    {1:["vision","vertical",0,2], 2:["thor","horizontal",4,0], 3:["hulk","horizontal",7,0], 4:["rocket","vertical",4,3]},
                    {1:["mexico","horizontal",0,0], 2:["china","vertical",0,4], 3:["italia","horizontal",2,0], 4:["tibet","vertical",2,1]}
                    ]
                    #número de definición, respuesta, orientación, fila, columna
    # Se decide con que diccionario se va a interactuar dependiendo del crucigrama seleccionado (opcion)
    
    if opcion == 1:
        diccionario = lista_config[0]
    elif opcion ==2:
        diccionario = lista_config[1]
    elif opcion ==3:
        diccionario = lista_config[2]
    else:
        diccionario = lista_config[3]
    
    while True: #controla si el crucigrma se termina o no
        def_selec = MostrarDefiniciones(opcion,nom_usuario)
        # Cambia la variable a int para que se pueda ingresar al diccionario
        def_selec = int(def_selec)
        # Pide al usuario la palabra y lo combierte a minúsculas para que dsp se pueda comparar correctamente
        palabra_usuario = input("\nIngrese la palabra: ").lower()
        if palabra_usuario== 9:
            finalDeCrucigrama(nom_usuario,puntaje_jugador)

        # Se asignó una variable para faciliar el ingreso a cada posición del diccionario
        # La variable indica qué está en esa posición del diccionario (configuración aplica para cualquier diccionario en el programa)
        palabra = diccionario[def_selec][0]
        orientacion = diccionario[def_selec][1]
        x_matriz = diccionario[def_selec][2]
        y_posicion = diccionario[def_selec][3]

    
        # Comprueba si la palabra ingresada es correcta con la palabra correspondiente 
        if palabra_usuario == 9:
            finalDeCrucigrama(nom_usuario)
        else:
            while palabra_usuario != palabra and palabra_usuario != 9:
                # Si es incorrecta la volverá a pedir
                palabra_usuario = input("\nIncorrecta, ingrese nuevamente la palabra: ").lower()
        

        # Si es correcta entonces procederá a cambiar los números por la palabra
        # Los índices donde se encuentran los números de las palabras se irán modificando en base a la palabra y orientación correspondiente 
        # Selecciona la posición correspondiente = lo iguala a la letra de la palabra dada por "i" (letra 0, letra 1, ...)
            #HORIZONTAL
            if orientacion == "horizontal":
                for i in range (len(palabra)):
                    matriz_pantalla[x_matriz][y_posicion+i] = matriz_original[x_matriz][y_posicion+i]
                    # En caso de ser hosrizontal la matriz será fija, pero la posición sí irá cambiando
                    
            # VERTICAL
            if orientacion == "vertical":
                for i in range (len(palabra)):
                    matriz_pantalla[x_matriz+i][y_posicion] = matriz_original[x_matriz+i][y_posicion]
                    # En caso de ser vertical la posición será fija, pero la matriz sí irá cambiando
                
            ImprimirMatriz(matriz_pantalla)
            puntaje_jugador += 5

            if matriz_pantalla == matriz_original:
                print ("¡FELIICIDADES! Ha completa el crucigrama")
                break


def finalDeCrucigrama(nom_usuario,puntaje_jugador):
    print ("GRACIAS POR JUGAR\n")
    m = AcumuladorPuntaje(nom_usuario,puntaje_jugador)
    #Grafica(nom_usuario,puntaje_jugador,m)

def AcumuladorPuntaje(nom_usuario, puntaje_jugador):
    
    archivo = open("puntajes.csv","r",encoding="utf-8")
    # leer el archivo de la matriz, convertirla a dato núemrico y regresarla
    m = []
    cadena_1 = ""
    # lectura de todas las líneas del archivo
    
    for linea in archivo:
        cadena_1 = cadena_1 + linea
    
    #for item in cadena_1:
     #   print ("item", item,end="/")
    if "," in cadena_1:
        m = cadena_1.split(",")
        # for i in range(len(lista)):
        #    lista[i] = int(lista[i]) 
        # construcción de matriz
        # print ("lista: items", lista)        
    
    # 1ra Impresión
    print ("PUNTAJE DE ESTA PARTIDA...")
    print ("Jugador: ",nom_usuario," Puntaje: ",puntaje_jugador, "\n")

    archivo=open("puntajes.csv","w",encoding="utf-8")
    # El índice donde está el usuario será el mismo donde estará el puntaje de tal ususario pero en la lista_puntaje
    # Si no está el usuario, se agregará

    if nom_usuario not in m:
        m.append(nom_usuario)
        m.append(str(puntaje_jugador))
    # Si sí existe el usuario se va al indice del usuario y se va a la lista de punatje en el mismo índice y modifica el puntaje
    else:
        indice = m.index(nom_usuario)
    # + 1 para que sea la siguiente posición a la que está el usuario
        suma_puntaje = int(m[indice+1]) + int(puntaje_jugador)
        m[indice+1] = str(suma_puntaje)

    # 2nda Impresión (Opcional)
        print ("PUNTAJE TOTAL DEL JUGADOR...")
        print ("Jugador: ",nom_usuario," Puntaje: ",suma_puntaje , "\n")

    cadena = ""

    for j in range (len(m)):
            if j == (len(m)-1):
                # para que en la ultima linea no imprima ","
                cadena = cadena + str(m[j]) 
            else:
                cadena = cadena + str(m[j]) + ","
    #cadena = cadena + "\n"

    archivo.write(cadena)  

    # 3ra Impresión 

    print ("RESTO DE JUGADORES...")
    indice_jugador = 0
    mitad_m = int (len(m)/2)
    if len(m) > 2:
        for i in range (mitad_m):
            if m[indice_jugador] != nom_usuario:
                print ("Jugador: ",m[indice_jugador], "Puntaje: ",m[indice_jugador + 1])
            indice_jugador += 2
    else:
        print ("No existen todavía")


    archivo.close() 
    return m

def Grafica(nom_usuario,puntaje_jugador,m):
    usuarios = []
    puntajes = []
    numeros = []
    index = 0
    topValue =int(len(m)/2)
    for i in range (topValue):
        user = m[index]
        score = m[index+1]
        usuarios.append(user)
        puntajes.append(score)
        index += 2
        numeros.append(i+1)

    fig, ax = plt.subplots()
    ax.bar(numeros,puntajes)
    plt.title("Puntajes jugadores")
    plt.xticks(numeros,usuarios)
    plt.show()


#########################################################################################################################

def main():
    menu1="\n\nMenú principal:\n1) General\n2) Jugar\n9) Salir\n\nEscriba el número de la opción que desea: "
    lista_opciones_1=[1,2,9]#Modificar para la opción salir

    menu2="\n1) ¿Cómo jugar? \n2) Preguntas frecuentes \n9) Salir \nElija el número de la opcion que desee: "
    lista_opciones_2=[1,2,9]

    menu3="\nIngrese el número del crucigrama que quiere\n1. Animales\n2. Comida\n3. Marvel\n4. Paises\n\nCrucigrama #: "
    lista_opciones_3=[1,2,3,4,9]

    #Bienvenida
    print ("\n --- CRUCIGRAMA --- \n")
    #Ingresa su nombre
    #Comprueba que el nombre de usuario sea de por lo menos 3 caracteres
    nom_usuario=compruebaNombreDeUsario()
    opcion = 1 # Para que a fuerzas entre al inicio
    #while opcion!=9:
        #le cambie el número a 9  por si qeuiree salir después del menu 3, porque ese ya tiene una opción 3
        #Muestra menu principal
    #while True and opcion!=9:
    while opcion != 9:
        bOpcionValida,opcion = mostrarmenuycapturaropcion(menu1,lista_opciones_1) 
        if bOpcionValida == True: #bOpciónValida comprueba que la respuesta ea valida en la lista
            if opcion==1:
                    bOpcionValida,opcion = mostrarmenuycapturaropcion(menu2,lista_opciones_2) 
                    if bOpcionValida == True:
                        if opcion!=9:
                            mostrarSelecciónDeMenu2(opcion)
                    # Error del menú 1
                    else:
                        print("Error: Opción inválida")
            
                #Hasta aqui ya se valido la opción de el segundo menu
                #Ahora que muestre la parte de preguntas frecuentes o ¿Cómo jugar?
                        
                #Se supone que aquí voamos a poner la opción de regresar al menu principal pero
                #Todavía no funciona #Se cambio para que estuviera en un ciclo

            ####JUGAR - Opción para mostrar tipos de crucigrama 
            elif opcion==2:
                while opcion !=9:
                    bOpcionValida,opcion = mostrarmenuycapturaropcion(menu3,lista_opciones_3) 
                    if bOpcionValida == True:
                        if opcion!=9:
                            matriz_pantalla = mostrarCrucigramaCapturarRespuesta(opcion)
                            InteraccionCrucigrama(opcion, matriz_pantalla,nom_usuario)
                    else: 
                        print("Error")
        else: 
            print("Error: Opción inválida... intenta nuevamente")

    finalDeCrucigrama(nom_usuario, puntaje_jugador)
        



#Final
if __name__ == "__main__":
    main()

