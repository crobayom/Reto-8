#Importacion de time para hacer operaciones con el tiempo
import time
#Definicion de la funcion de fibonacci por iteracion
def fibonacci_iteracion(x)->int:
    #Variables bases de la sucesion de fibonacci
    f0:int=0
    f1:int=1
    #For que recorrera la cantidad de indices especificados por el usuario en la sucesion de fibonacci
    for i in range(x):
        #Transformaciones requeridas por la naturaleza de fibonacci, suma, igualacion de una variable a la siguiente, y la siguiente a la suma
        respuesta=f0+f1
        f0=f1
        f1=respuesta
    #Retorno del valor final
    return respuesta

#Definicion de la funcion fibonacci por recrusiva
def fibonacci_recursiva(x)->int:
    #Caso base de la recursion hasta el valor relevante (pues 0 no tiene relevancia en la suma)
    if x <= 1: return 1 
    #Regresion de la variable con autonombramiento por la definicion recurrente
    return fibonacci_recursiva(x-1)+fibonacci_recursiva(x-2)
        

if __name__=="__main__":
    #Variable que ingresa el usuario
    x:int=int(input("Ingrese el indice de la susecion de fibonacci deseada a calcular: "))
    #Comienzo de toma de tiempo
    start_time = time.time()
    #Muestra de informacion con llamado de la funcion de fibonacci por iteracion
    print("La susecion de fibonacci en el indice "+str(x)+" es: "+str(fibonacci_iteracion(x)))
    #Fin de la toma de tiempo
    end_time = time.time()
    #Calculo del tiempo tomado para hacer el proceso
    timer1 = end_time - start_time
    #Impresion de informacion sobre el tiempo tomado
    print("El tiempo tomado para el calculo de la susecion de fibonacci en el indice "+str(x)+" es: "+str(timer1))

    #Comienzo de toma de tiempo
    start_time = time.time()
    #Muestra de informacion con llamado de la funcion de fibonacci por recursion
    print("La susecion de fibonacci en el indice "+str(x)+" es: "+str(fibonacci_recursiva(x)))
    #Fin de toma de tiempo
    end_time = time.time()
    #Calculo del tiempo tomado para hacer el proceso
    timer2 = end_time - start_time
    #Muestra de informacion sobre el tiempo tomado
    print("El tiempo tomado para el calculo de la susecion de fibonacci en el indice "+str(x)+" es: "+str(timer2))
    print("La diferencia entre ambos metodos es de: "+str(timer1-timer2))