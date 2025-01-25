def mayor (a:int, b:int, c:int=1) -> int:
    mayor:int=(a if a>b else b)
    menor:int=(a if a<b else b)
    if c==1: return mayor
    else: return menor

if __name__=="__main__":
    a:int=int(input("Ingrese el primer numero: "))
    b:int=int(input("Ingrese el segundo numero: "))
    c:int=int(input("Ingrese 0 para devolver el valor menor entre los anteriores, y 1 para el mayor: "))
    if a==b: print("Ambos numeros son iguales, intente con numeros distintos")
    elif c<0 or c>1: print("El numero ingresado para decidir el valor a devolver no es ni 1 ni 2, intentelo de nuevo")
    else:
        print("El ", end="")
        if c == 1: print("mayor ", end="")
        else:
            print("menor ", end="")
        print("numero entre "+str(a)+" y "+str(b)+" es: "+str(mayor(a,b)))
