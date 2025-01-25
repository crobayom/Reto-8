from math import pi
if __name__=="__main__":
    #*Calculo de volumen y area, primer ejercicio reto 5
    #Definicion de variables constantes
    PI:float=pi
    #Definicion de variables ingresadas por el usuario
    r1:float=float(input("Ingrese el radio de la esfera: "))
    r2:float=float(input("Ingrese el radio de la base del cono: "))
    h:float=float(input("Ingrese la altura del cono: "))
    #Definicion de funcion de calculo de volumen en metodo lambda
    volumen1= (lambda PI,r1,r2,h:(4/3)*PI*r1**3+PI*r2**2*h*(1/3))(PI,r1,r2,h)
    #Definicion de funcion de calculo de area en metodo lambda
    area1= (lambda PI, r1, r2, h: 4*PI*r1**2+PI*r2**2+PI*r2*((r2**2+h**2)**0.5))(PI,r1,r2,h)
    
    #Muestra de resultados
    print("El volumen total de la figura es: "+str(volumen1))
    print("El area superficial de la figura es: "+str(area1))

    #*Calculo de area y perimetro, segundo ejercicio reto 5
    #Definicion de variables ingresadas por el usuario
    base:float=float(input("Ingrese la logitud de la base del rectangulo: "))
    altura:float=float(input("Ingrese la altura del rectangulo: "))
    r:float=float(input("Ingrese el radio del circulo: "))
    #Definicion de funcion de calculo de area en metodo lambda
    area2:float=(lambda base,altura,r,PI: base*altura+2*r**2*PI)(base,altura,r,PI)
    #Definicion de funcion de calculo de perimetro en metodo lambda
    perimetro2:float=(lambda base,altura,PI,r: 2*base+2*altura+2*(2*PI*r))(base,altura,PI,r)

    #Muestra de resultados
    print("El area de la figura es: "+str(area2))
    print("El perimetro de la figura es: "+str(perimetro2))

    #*Calculo de interes compuesto, cuarto ejercicio reto 5
    #Definicion de variables ingresadas por el usuario
    monto:float=float(input("Ingrese el monto inicial sobre el cual se hara el interes: "))
    interes:float=float(input("Ingrese el porcentaje de interes que se le aplicara mensualmente al monto 'sin incluir el signo de porcentaje': "))
    tiempo:float=float(input("Ingrese los meses que el monto se le aplicara el interes compuesto: "))
    #Definicion de funcio de calculo de interes compuesto en metodo lambda
    monto_final:float=(lambda a,b,c: a*(1+b/100)**c)(monto,interes,tiempo)

    #Muestra de resultados
    print("El monto al final del periodo de tiempo de "+str(tiempo)+" meses, teniendo un interes de "+str(interes)+"% es: "+str(monto_final))