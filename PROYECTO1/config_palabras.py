
    # Diccionario - para cada opción 1-4 habrá una palabra asignada con ese número y si es horiz o vertical
#config = {1:["perro","horizontal",0,2], 2:["pescado","vertical",0,2], 3:["vaca","horizontal",3,0], 4:["oveja","vertical,",2,0]}

# Lista de la configuración de las palabras de los crucigramas (llave = def_selec)(llave indica la definición seleccionada)
# Crucigrma Animales - 1 / Crucigrama Comida - 0 / Crucigrama Marvel - 2 / Crucigrama Países - 3
lista_config = [{1:["perro","horizontal",0,2], 2:["pescado","vertical",0,2], 3:["vaca","horizontal",3,0], 4:["oveja","vertical",2,0]},
                {1:["pasta","horizontal",0,0], 2:["pastel","vertical",0,0], 3:["salmon","vertical",0,2], 4:["tamales","horizontal",3,0]},
                {1:["vision","vertical",0,2], 2:["thor","horizontal",4,0], 3:["hulk","horizontal",7,0], 4:["rocket","vertical",4,3]},
                {1:["mexico","horizontal",0,0], 2:["china","vertical",0,4], 3:["italia","horizontal",2,0], 4:["tibet","vertical",2,1]}
                ]

palabras_animales = lista_config[0]
palabras_comida = lista_config[1]
palabras_marvel = lista_config[2]
palabras_paises = lista_config[3]




def MostrarDefiniciones(opcion):
    # = nombre del archivo - dsp hago el bloc de notas para cada crucigrama con sus definiciones
    # Entre corchetes va el nombre del archivo
    #dic_principal = {1:[""],2:[],3:[],4:[]}
    # Se mete a la llave que corresponde  a la opción seleccionada
    #crucigrama = dic_principal[opcion][0]
    # Abre el archivo según la opción seleccionada - en base al diccionario
    #a = open(crucigrama,encoding="utf-8")
    # Cada definición va a tener un número asignado (1-4)
    posibles_def_selec = (1,2,3,4)
    def_selec = int(input("Indique la definición que guste: "))
    #Validación de definición seleccionada (def_selec)
    while def_selec not in posibles_def_selec:
        def_selec = int(input("Indique la definición que guste: "))
    # a.close() - no sé si en algún punto tengamos que cerrar los archivos
    return def_selec


def main(matriz, matriz_pantalla, config): # en los parámetros le vamos a pasar la config del crucigrama selecionado & la matriz y matriz_pantalla de acuerdo al crucigrama
    #global matriz
    #global config
    opcion = 1
    def_selec = MostrarDefiniciones(opcion)
    # Pide al usuario la palabra y lo combierte a minúsculas para que dsp se pueda comparar correctamente
    palabra_usuario = input("Ingrese la palabra: ").lower()

    # Se asignó una variable para faciliar el ingreso a cada posición del diccionario
    # La variable indica qué está en esa posición del diccionario (configuración aplica para cualquier diccionario en el programa)
    palabra = config[def_selec][0]
    orientacion = config[def_selec][1]
    x_matriz = config[def_selec][2]
    y_posicion = config[def_selec][3]

    ImprimirMatriz(matriz_pantalla)
    
    # Comprueba si la palabra ingresada es correcta con la palabra correspondiente 
    if palabra_usuario == palabra:

    # Si es correcta entonces procederá a cambiar los números por la palabra
    # Los índices donde se encuentran los números de las palabras se irán modificando en base a la palabra y orientación correspondiente 
    # Selecciona la posición correspondiente = lo iguala a la letra de la palabra dada por "i" (letra 0, letra 1, ...)
        #HORIZONTAL
        if orientacion == "horizontal":
            for i in range (len(palabra)):
                matriz_pantalla[x_matriz][y_posicion+i] = matriz[x_matriz][y_posicion+i]
                # En caso de ser hosrizontal la matriz será fija, pero la posición sí irá cambiando
        
        # VERTICAL
        if orientacion == "vertical":
            for i in range (len(palabra)):
                matriz_pantalla[x_matriz+i][y_posicion] = matriz[x_matriz+i][y_posicion]
                # En caso de ser vertical la posición será fija, pero la matriz sí irá cambiando
    else:
        #error volver a escoger
        pass

    ImprimirMatriz(matriz_pantalla)

def ImprimirMatriz(matriz_pantalla): # se le pasa la matriz pantalla correspondiente
    print()
    for row in matriz_pantalla:
        for item in row:
            print ("{:4}".format(item),end="")
        print()
        




if __name__ == "__main__":
    main()
