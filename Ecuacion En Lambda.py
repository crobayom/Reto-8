if __name__=="__main__":
    #Variable que recibe la x en la ecuacion
    x:int=int((input("Ingrese el valor de x en la ecuacion: ")))
    #Definicion de una variable que contenga una funcion (lamda) de x/(((x)**(1/3))-1) con argumento x tomado como a
    ecuacion:float= (lambda a: a/(((a)**(1/3))-1))(x)
    #Muestra de informacion con impresion en pantalla
    print(ecuacion)