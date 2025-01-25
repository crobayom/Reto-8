
#* Elevar 2 a x, quinto ejercicio reto 7
#Definicion de la funcion que elevara 2, con varias "x's"
def elevar (*args) -> int:
    #for que recorreara los argumentos que se le den a la funcion
    for i in args:
        #Definicion de la variable que cargara el valor de 2 a la "x"
        elevado:int=1
        #for que recorrera los valores desde 0 hasta el argumento que sea pertinente revisar
        for j in range(i):
            #cambio a la variable elevado a razon de cuantas veces quieran elevar a 2
            elevado*=2
    #Muestra de resultados porque no encontre forma de regresar los valores sin que se salga de la funcion (ni siquiera usando recursiva, 
    # porque sino no dejaria usar los demas argumentos en una sola funcion cn la estructura dada y general)
        print("2 elevado a "+str(i)+" es : "+str(elevado))

if __name__=="__main__":
    #Declaracion de variables que ingresara el usuario y posteriormente elevaran a 2
    a:int=int(input("Ingrese el primer numero que elevara a 2: "))
    b:int=int(input("Ingrese el segundo numero que elevara a 2: "))
    c:int=int(input("Ingrese el tercer numero que elevara a 2: "))
    d:int=int(input("Ingrese el cuarto numero que elevara a 2: "))
    e:int=int(input("Ingrese el quinto numero que elevara a 2: "))
    #Varios llamados a la misma funcion con diferentes argumentos con contexto a travez de prints
    print("")
    elevar(a)
    print("")
    elevar(a, b)
    print("")
    elevar(a, b, c)
    print("")
    elevar(a, b, c, d)
    print("")
    elevar(a, b, c, d, e)